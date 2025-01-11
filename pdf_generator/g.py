import os
import re
from PyPDF2 import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
import arabic_reshaper
from bidi.algorithm import get_display

# مسیر لوگو و فونت
current_dir = os.path.dirname(__file__)
logo_path = os.path.join(current_dir, "assets", "logo.png")
font_path = os.path.join(current_dir, "assets", "Vazir.ttf")

# ثبت فونت
pdfmetrics.registerFont(TTFont('Vazir', font_path))

# فرمت‌دهی متن فارسی
def format_persian_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

# تحلیل PDFها
def analyze_pdfs(directory):
    total_usages = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            file_path = os.path.join(directory, file)
            reader = PdfReader(file_path)
            for page in reader.pages:
                text = page.extract_text()
                match = re.search(r"([\d.]+)\s*total usage", text, re.IGNORECASE)
                if match:
                    total_usages.append((file, float(match.group(1))))
                    break
    return total_usages

# تولید PDF خروجی
def create_pdf(total_usages, output_file):
    pdf = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []

    # لوگو
    logo = Image(logo_path)
    logo.drawHeight = 2 * inch
    logo.drawWidth = 4 * inch
    elements.append(logo)
    elements.append(Spacer(1, 12))

    # جدول
    table_data = [['File Name', 'Total Usage']]
    for file, usage in total_usages:
        table_data.append([
            Paragraph(format_persian_text(file), ParagraphStyle('DataStyle', fontName='Vazir')),
            Paragraph(format_persian_text(str(usage)), ParagraphStyle('DataStyle', fontName='Vazir')),
        ])

    table = Table(table_data, colWidths=[4 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Vazir'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    pdf.build(elements)
