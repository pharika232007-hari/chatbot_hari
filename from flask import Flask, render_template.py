from flask import Flask, render_template, request
import os

from resume_parser import parse_resume
from job_matcher import match_jobs

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # AI Processing
    resume_text = parse_resume(filepath)
    results = match_jobs(resume_text, jobs)

    return render_template("result.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)