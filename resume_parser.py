from pdfminer.high_level import extract_text
def parse_resume(file_path):
    try:
        text = extract_text(file_path)
        return text.lower()
    except:
        return ""