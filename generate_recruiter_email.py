# generate_recruiter_email.py
# Шаблон для генерации Email-запроса к рекрутеру/HR в PDF

# pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_config import TTFSearchPath
import os, unicodedata, datetime


# ---------- Fonts (macOS Arial → DejaVu fallback) ----------

ARIAL_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_CANDIDATES = [
    ("ArialCustom", ARIAL_REG, ARIAL_BLD),
    ("DejaVuSans", "fonts/DejaVuSans.ttf", "fonts/DejaVuSans-Bold.ttf"),
]

def register_fonts():
    TTFSearchPath.append(os.path.abspath("fonts"))
    for fam, reg, bld in FONT_CANDIDATES:
        if os.path.exists(reg):
            try:
                pdfmetrics.registerFont(TTFont(fam, reg))
                bold = fam
                if os.path.exists(bld):
                    pdfmetrics.registerFont(TTFont(fam+"-Bold", bld))
                    bold = fam+"-Bold"
                return fam, bold
            except Exception:
                continue
    return "Times-Roman", "Times-Bold"

BASE_FONT, BOLD_FONT = register_fonts()


# ---------- Helpers ----------

def nz(s: str) -> str:
    """Нормализация unicode и замены символов"""
    if not s: return ""
    s = unicodedata.normalize("NFC", s)
    return (s.replace("\u00A0"," ")
             .replace("\u2009"," ")
             .replace("\u2013","-")
             .replace("\u2014","--")
             .replace("\u2212","-"))

def format_email_link(email):
    """Форматирует email в кликабельную ссылку mailto"""
    return f'<a href="mailto:{email}" color="blue">{email}</a>'

def format_url_link(name, url):
    """Форматирует URL в кликабельную ссылку"""
    if not url.startswith(("http://", "https://")):
        full_url = f"https://{url}"
    else:
        full_url = url
    return f'<a href="{full_url}" color="blue">{name}: {url}</a>'

def format_simple_url(url):
    """Форматирует URL в кликабельную ссылку без названия"""
    if not url.startswith(("http://", "https://")):
        full_url = f"https://{url}"
    else:
        full_url = url
    return f'<a href="{full_url}" color="blue">{url}</a>'

def styles():
    base = getSampleStyleSheet()
    return {
        "hdr": ParagraphStyle("hdr", parent=base["Normal"], fontName=BOLD_FONT, fontSize=12, leading=15),
        "meta": ParagraphStyle("meta", parent=base["Normal"], fontName=BASE_FONT, fontSize=10, leading=13, textColor="#444444"),
        "p": ParagraphStyle("p", parent=base["Normal"], fontName=BASE_FONT, fontSize=11, leading=15),
        "sig": ParagraphStyle("sig", parent=base["Normal"], fontName=BOLD_FONT, fontSize=11, leading=14, spaceBefore=10),
    }


# ========== НАСТРОЙКИ: Замените на свои данные ==========

NAME    = "Иван Иванов"  # Ваше имя
EMAIL   = "ivan.ivanov@example.com"  # Ваш email
LINKS   = f'{format_url_link("LinkedIn", "linkedin.com/in/ivanov")} · {format_url_link("Portfolio", "ivanov.dev")}'

# Данные для запроса
RECRUITER_NAME = "Имя Фамилия"  # Имя рекрутера (можно оставить пустым или "Hiring Team")
COMPANY_NAME = "Пример Компания"  # Название компании
POSITION = "Senior Product Designer"  # Название позиции


# ========== ТЕКСТ ПИСЬМА: Отредактируйте под конкретную ситуацию ==========

BODY = f"""

Hi {RECRUITER_NAME if RECRUITER_NAME else "there"},

I hope this email finds you well. I'm reaching out because I'm interested in exploring opportunities at {COMPANY_NAME}. I've been following {COMPANY_NAME}'s work in [индустрия/область] and I'm impressed by [конкретная причина интереса].

With [X] years of experience as a [должность] focusing on [область специализации], I've worked on [примеры проектов или достижений]. I'm particularly drawn to {COMPANY_NAME} because of [конкретная причина - миссия, продукт, команда].

I've attached my CV for your review. I'd love to learn more about open positions or discuss how my experience could contribute to your team. Would you be available for a brief call or coffee chat?

Portfolio & case studies: {format_simple_url("https://example.com")}

Thank you for your time and consideration. Looking forward to hearing from you!

Best regards,

{NAME}

{EMAIL}

{LINKS}

"""


# ---------- Build PDF ----------

def build_pdf(path="Recruiter_Email.pdf"):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = styles()
    
    story = [
        Paragraph(nz(NAME), s["hdr"]),
        Spacer(1, 3*mm),
        Paragraph(nz(LINKS), s["meta"]),
        Spacer(1, 8*mm),
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>"), s["p"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT in ("Times-Roman", "Helvetica"):
        print("⚠️ Font fallback in use. For best results add fonts/DejaVuSans.ttf and DejaVuSans-Bold.ttf in ./fonts/")
    build_pdf()
