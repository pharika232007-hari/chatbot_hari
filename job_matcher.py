from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jobs(resume_text, jobs):

    results = []

    for job in jobs:
        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform([resume_text, job["skills"]])

        similarity = cosine_similarity(vectors[0:1], vectors[1:2])

        score = round(similarity[0][0] * 100, 2)

        results.append({
            "title": job["title"],
            "score": score
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)
