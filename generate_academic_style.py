# generate_academic_style.py
# Template for generating documents in academic/scientific style
# Strict, beautiful style as in scientific publications

# pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import mm
import unicodedata, datetime

# Import academic styles
from academic_styles import (
    get_academic_styles,
    get_academic_margins,
    format_academic_url_link,
    format_academic_simple_url,
    format_academic_email_link,
    BASE_FONT
)


# ---------- Helpers ----------

def nz(s: str) -> str:
    """Unicode normalization and character replacements (academic style)"""
    if not s: return ""
    s = unicodedata.normalize("NFC", s)
    return (s.replace("\u00A0"," ")
             .replace("\u2009"," ")
             .replace("\u2013","–")  # en-dash for academic style
             .replace("\u2014","—")  # em-dash
             .replace("\u2212","−"))


# ========== CONFIGURATION: Replace with your data ==========

NAME    = "John Doe"  # Your name
EMAIL   = "john.doe@example.com"  # Your email
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/johndoe")} · {format_academic_url_link("Portfolio", "johndoe.dev")}'

TODAY   = datetime.date.today().strftime("%B %d, %Y")  # Date (can be removed from story)


# ========== LETTER TEXT ==========

BODY = f"""

This is an example document in academic style. The text is justified, uses Times New Roman font, and follows the strict formatting conventions of scientific publications.

Academic papers typically use:
- Justified text alignment
- Times New Roman or similar serif fonts
- Larger margins (25-30mm)
- Tight line spacing (leading 13)
- Dark gray colors instead of pure black
- No bullet points in lists
- En-dashes (–) instead of hyphens (-)

This style creates a professional, scholarly appearance that is commonly used in academic journals, research papers, and formal publications.

The formatting emphasizes readability and follows established typographic conventions that have been refined over decades of academic publishing.

Thank you for your time and consideration.

Sincerely,

{NAME}

"""


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="Academic_Style_Document.pdf"):
    """Generates PDF in academic style"""
    
    margins = get_academic_margins()
    
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        **margins
    )
    
    s = get_academic_styles()
    
    story = [
        # Title
        Paragraph(nz(NAME), s["title"]),
        
        # Metadata
        Paragraph(nz(LINKS), s["meta"]),
        
        # Date (optional, uncomment if needed)
        # Paragraph(nz(TODAY), s["date"]),
        
        # Main text
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>"), s["body"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT}, academic style)")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
