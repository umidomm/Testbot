import os
from PyPDF2 import PdfReader

def analyze_pdfs(directory):
    usages = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            reader = PdfReader(os.path.join(directory, file))
            for page in reader.pages:
                text = page.extract_text()
                if "total usage" in text.lower():
                    usages.append((file, text.strip()))
    return usages
