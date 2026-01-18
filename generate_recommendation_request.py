# generate_recommendation_request.py
# Шаблон для генерации Request for Recommendation (запрос рекомендаций) в PDF

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

# Данные для запроса рекомендации
REFEREE_NAME = "Имя Фамилия"  # Имя человека, у которого просите рекомендацию
COMPANY = "Пример Компания"  # Компания, где вы работали вместе
ROLE = "Senior Product Designer"  # Ваша роль там
START_DATE = "January 2020"  # Когда начали работать вместе
END_DATE = "March 2023"  # Когда закончили работать вместе (или "Present")
CURRENT_POSITION = "Senior Product Designer"  # Позиция, на которую вы претендуете


# ========== ТЕКСТ ПИСЬМА: Отредактируйте под конкретную ситуацию ==========

BODY = f"""

Hi {REFEREE_NAME},

I hope you're doing well! I wanted to reach out because I'm exploring new opportunities and I'd love to ask for your support.

I'm currently applying for {CURRENT_POSITION} positions and I'd be honored if you'd be willing to write a recommendation or serve as a reference for me. We worked together at {COMPANY} from {START_DATE} to {END_DATE}, where I worked as {ROLE}. Your perspective on my work during that time would be invaluable.

Specifically, if you could speak to [конкретные аспекты - например, "my design process, collaboration with cross-functional teams, and ability to deliver results"], that would be particularly helpful.

I've attached my current resume for your reference. The recommendation can be brief — even just a few sentences about our work together would be very helpful.

Of course, I completely understand if you're unable to do this, and I appreciate your time either way. If you have any questions or need additional information, please don't hesitate to reach out.

Thank you so much for your consideration, and I hope we can catch up soon!

Best regards,

{NAME}

{EMAIL}

{LINKS}

"""


# ---------- Build PDF ----------

def build_pdf(path="Recommendation_Request.pdf"):
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
