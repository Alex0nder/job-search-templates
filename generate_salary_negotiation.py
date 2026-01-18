# generate_salary_negotiation.py
# Шаблон для генерации Salary Negotiation Letter в PDF

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

# Данные оффера
HIRING_MANAGER_NAME = "Имя Фамилия"  # Имя менеджера/рекрутера
COMPANY_NAME = "Пример Компания"  # Название компании
POSITION = "Senior Product Designer"  # Название позиции

# Предложенная компенсация (указать что предлагают)
OFFERED_SALARY = "$100,000"  # Предложенная зарплата
DESIRED_SALARY = "$115,000"  # Желаемая зарплата


# ========== ТЕКСТ ПИСЬМА: Отредактируйте под конкретную ситуацию ==========

BODY = f"""

Dear {HIRING_MANAGER_NAME},

Thank you for extending the offer for the {POSITION} role at {COMPANY_NAME}. I'm very excited about this opportunity and the chance to contribute to your team.

After careful consideration, I'd like to discuss the compensation package. Based on my research of market rates for similar roles in [локация/регион] and my experience with [релевантный опыт], I believe a salary of {DESIRED_SALARY} would better reflect the value I can bring to {COMPANY_NAME}.

Here's what I bring to the table:
• [Конкретное достижение или опыт 1] - [как это помогает компании]
• [Конкретное достижение или опыт 2] - [как это помогает компании]
• [Конкретное достижение или опыт 3] - [как это помогает компании]

I'm very enthusiastic about this role and {COMPANY_NAME}'s mission. I'm confident that my experience and skills will make a significant impact, and I believe this salary adjustment reflects that value.

I'm open to discussing this further and finding a package that works for both of us. Would you be available for a call this week to discuss?

Thank you again for this opportunity. I'm looking forward to joining the team.

Best regards,

{NAME}

{EMAIL}

{LINKS}

"""


# ---------- Build PDF ----------

def build_pdf(path="Salary_Negotiation_Letter.pdf"):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = styles()
    
    story = [
        Paragraph(nz(NAME), s["hdr"]),
        Spacer(1, 3*mm),
        Paragraph(nz(LINKS), s["meta"]),
        Spacer(1, 8*mm),
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>").replace("\n• ", "<br/>• "), s["p"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT in ("Times-Roman", "Helvetica"):
        print("⚠️ Font fallback in use. For best results add fonts/DejaVuSans.ttf and DejaVuSans-Bold.ttf in ./fonts/")
    build_pdf()
