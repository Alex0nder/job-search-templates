# generate_cover_letter.py
# Шаблон для генерации Cover Letter в PDF

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

def format_phone_link(phone):
    """Форматирует телефон в кликабельную ссылку на WhatsApp"""
    phone_clean = phone.replace(" ", "").replace("+", "")
    return f'<a href="https://wa.me/{phone_clean}" color="blue">{phone}</a>'

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
        "date": ParagraphStyle("date", parent=base["Normal"], fontName=BASE_FONT, fontSize=10.5, leading=14, spaceAfter=10),
        "p": ParagraphStyle("p", parent=base["Normal"], fontName=BASE_FONT, fontSize=11, leading=15),
        "sig": ParagraphStyle("sig", parent=base["Normal"], fontName=BOLD_FONT, fontSize=11, leading=14, spaceBefore=10),
    }


# ========== НАСТРОЙКИ: Замените на свои данные ==========

NAME    = "Иван Иванов"  # Ваше имя
CITY    = "Москва, Россия"  # Ваш город
PHONE   = "+7 900 123 45 67"  # Ваш телефон
EMAIL   = "ivan.ivanov@example.com"  # Ваш email

# Форматируем контакты с кликабельными ссылками
CONTACT = f'{CITY} · {format_phone_link(PHONE)} · {format_email_link(EMAIL)}'
LINKS   = f'{format_url_link("LinkedIn", "linkedin.com/in/ivanov")} · {format_url_link("Portfolio", "ivanov.dev")}'

COMPANY = "Пример Компания"  # Название компании (необязательно, если не используется в тексте)
ROLE    = "Senior Product Designer"  # Желаемая позиция

TODAY   = datetime.date.today().strftime("%B %d, %Y")  # Дата (можно удалить из story)


# ========== ТЕКСТ ПИСЬМА: Отредактируйте под свою компанию и ситуацию ==========

BODY = f"""

Hi,

I'm reaching out because I'm currently open to new opportunities after a recent company-wide layoff.

For the past 8+ years, I've been working as a product designer in fintech and AI-driven products, focusing on areas where design decisions have a direct impact on metrics — activation, retention, efficiency, and revenue. I usually work end to end: from research and UX strategy to hands-on execution and close collaboration with engineering and product.

In my recent roles, I've designed AI-assisted flows, trading tools, onboarding experiences, and scalable design systems. The work resulted in outcomes like improved efficiency, higher conversion during onboarding, reduced support load, and stronger early retention. I care less about "polished screens" and more about making complex systems feel clear, predictable, and useful in real product contexts.

Alongside my professional work, I actively build and maintain my personal project, where I explore AI-assisted UX, product thinking, and practical execution. It reflects how I approach problems and how I think about product design beyond a single role or company.
Portfolio & case studies: {format_simple_url("https://example.com")}

I'm looking for a team where design is treated as part of product decision-making — not just delivery — and where clarity, ownership, and outcomes matter. If that sounds aligned, I'd be glad to talk.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Cover_Letter.pdf"):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=18*mm, rightMargin=18*mm,
                            topMargin=16*mm, bottomMargin=16*mm)
    s = styles()
    
    story = [
        Paragraph(nz(NAME), s["hdr"]),
        Spacer(1, 3*mm),
        Paragraph(nz(LINKS), s["meta"]),
        Spacer(1, 8*mm),
        # Раскомментируйте следующую строку, если нужна дата:
        # Paragraph(nz(TODAY), s["date"]),
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>"), s["p"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT in ("Times-Roman", "Helvetica"):
        print("⚠️ Font fallback in use. For best results add fonts/DejaVuSans.ttf and DejaVuSans-Bold.ttf in ./fonts/")
    build_pdf()
