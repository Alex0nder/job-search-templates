# academic_styles.py
# Module with academic styles for use in other templates

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_config import TTFSearchPath
import os


# ---------- Fonts Setup ----------

TIMES_REG = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
TIMES_BOLD = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
TIMES_ITALIC = "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf"
TIMES_BOLD_ITALIC = "/System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf"

FONT_CANDIDATES = [
    ("TimesCustom", TIMES_REG, TIMES_BOLD, TIMES_ITALIC, TIMES_BOLD_ITALIC),
    ("DejaVuSerif", "fonts/DejaVuSerif.ttf", "fonts/DejaVuSerif-Bold.ttf", 
     "fonts/DejaVuSerif-Italic.ttf", "fonts/DejaVuSerif-BoldItalic.ttf"),
]

def register_academic_fonts():
    """Registers fonts for academic style"""
    TTFSearchPath.append(os.path.abspath("fonts"))
    for fam, reg, bld, it, bi in FONT_CANDIDATES:
        if os.path.exists(reg):
            try:
                pdfmetrics.registerFont(TTFont(fam, reg))
                if os.path.exists(bld):
                    pdfmetrics.registerFont(TTFont(fam+"-Bold", bld))
                if os.path.exists(it):
                    pdfmetrics.registerFont(TTFont(fam+"-Italic", it))
                if os.path.exists(bi):
                    pdfmetrics.registerFont(TTFont(fam+"-BoldItalic", bi))
                return fam
            except Exception:
                continue
    return "Times-Roman"  # fallback

BASE_FONT = register_academic_fonts()
BOLD_FONT = BASE_FONT + "-Bold" if BASE_FONT != "Times-Roman" else "Times-Bold"
ITALIC_FONT = BASE_FONT + "-Italic" if BASE_FONT != "Times-Roman" else "Times-Italic"


# ---------- Academic Style Colors ----------

TEXT_COLOR = HexColor("#1a1a1a")      # Almost black for main text
META_COLOR = HexColor("#4a4a4a")      # Dark gray for metadata
LINK_COLOR = HexColor("#1a1a1a")      # For links (with underline)


# ---------- Academic Style Definitions ----------

def get_academic_styles():
    """Returns dictionary of styles in academic format"""
    base = getSampleStyleSheet()
    
    return {
        # Document title (academic style)
        "title": ParagraphStyle(
            "title",
            parent=base["Normal"],
            fontName=BOLD_FONT,
            fontSize=13,
            leading=16,
            textColor=TEXT_COLOR,
            spaceAfter=4*mm,
            alignment=0,  # left
        ),
        
        # Metadata (contacts)
        "meta": ParagraphStyle(
            "meta",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=9.5,
            leading=12,
            textColor=META_COLOR,
            spaceAfter=8*mm,
            alignment=0,
        ),
        
        # Date
        "date": ParagraphStyle(
            "date",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=10,
            leading=13,
            textColor=TEXT_COLOR,
            spaceAfter=10*mm,
            alignment=0,
        ),
        
        # Main text (justified for academic style - strict scientific format)
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=10.5,
            leading=13,  # Tight leading for academic papers
            textColor=TEXT_COLOR,
            spaceAfter=3*mm,
            alignment=4,  # justify for academic style
            firstLineIndent=0,
            wordWrap='CJK',  # Better word wrapping
        ),
        
        # Body text left-aligned (for lists without bullets - academic style)
        "body_left": ParagraphStyle(
            "body_left",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=10.5,
            leading=13,
            textColor=TEXT_COLOR,
            spaceAfter=1.5*mm,
            alignment=0,  # left
            leftIndent=0,
            wordWrap='CJK',
        ),
        
        # Signature
        "signature": ParagraphStyle(
            "signature",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=11,
            leading=16,
            textColor=TEXT_COLOR,
            spaceBefore=8*mm,
            alignment=0,
        ),
        
        # Name in signature
        "signature_name": ParagraphStyle(
            "signature_name",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=11,
            leading=16,
            textColor=TEXT_COLOR,
            spaceBefore=4*mm,
            alignment=0,
        ),
        
        # Section title (academic style - strict format)
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName=BOLD_FONT,
            fontSize=10.5,
            leading=13,
            textColor=TEXT_COLOR,
            spaceBefore=6*mm,
            spaceAfter=2.5*mm,
            alignment=0,
            letterSpacing=0.3,
        ),
        
        # Subsection (for job titles, company names)
        "subsection": ParagraphStyle(
            "subsection",
            parent=base["Normal"],
            fontName=BOLD_FONT,
            fontSize=10.5,
            leading=13,
            textColor=TEXT_COLOR,
            spaceAfter=1*mm,
            alignment=0,
        ),
        
        # Metadata text (dates, locations)
        "meta_text": ParagraphStyle(
            "meta_text",
            parent=base["Normal"],
            fontName=BASE_FONT,
            fontSize=9.5,
            leading=12,
            textColor=META_COLOR,
            spaceAfter=2*mm,
            alignment=0,
        ),
    }


# ---------- Academic Margins ----------

def get_academic_margins():
    """Returns margins in academic style (strict scientific format)"""
    return {
        "leftMargin": 25*mm,      # Larger margins for academic papers
        "rightMargin": 25*mm,
        "topMargin": 30*mm,
        "bottomMargin": 30*mm,
    }


# ---------- Helper Functions for Academic Style ----------

def format_academic_email_link(email):
    """Formats email in academic style (with underline)"""
    return f'<a href="mailto:{email}" color="#1a1a1a"><u>{email}</u></a>'

def format_academic_url_link(name, url):
    """Formats URL in academic style (with underline)"""
    if not url.startswith(("http://", "https://")):
        full_url = f"https://{url}"
    else:
        full_url = url
    return f'<a href="{full_url}" color="#1a1a1a"><u>{name}</u></a>'

def format_academic_simple_url(url):
    """Formats URL without name in academic style"""
    if not url.startswith(("http://", "https://")):
        full_url = f"https://{url}"
    else:
        full_url = url
    return f'<a href="{full_url}" color="#1a1a1a"><u>{url}</u></a>'
