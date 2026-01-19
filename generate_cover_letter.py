# generate_cover_letter.py
# Template for generating Cover Letter in PDF (Academic Style)

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
CITY    = "New York, USA"  # Your city
PHONE   = "+1 234 567 8900"  # Your phone
EMAIL   = "john.doe@example.com"  # Your email

# Format contacts with clickable links (academic style)
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/johndoe")} · {format_academic_url_link("Portfolio", "johndoe.dev")}'

COMPANY = "Example Company"  # Company name (optional, if not used in text)
ROLE    = "Senior Product Designer"  # Desired position

TODAY   = datetime.date.today().strftime("%B %d, %Y")  # Date (can be removed from story)


# ========== LETTER TEXT: Edit for your company and situation ==========

BODY = f"""

Hi,

I'm reaching out because I'm currently open to new opportunities after a recent company-wide layoff.

For the past 8+ years, I've been working as a product designer in fintech and AI-driven products, focusing on areas where design decisions have a direct impact on metrics — activation, retention, efficiency, and revenue. I usually work end to end: from research and UX strategy to hands-on execution and close collaboration with engineering and product.

In my recent roles, I've designed AI-assisted flows, trading tools, onboarding experiences, and scalable design systems. The work resulted in outcomes like improved efficiency, higher conversion during onboarding, reduced support load, and stronger early retention. I care less about "polished screens" and more about making complex systems feel clear, predictable, and useful in real product contexts.

Alongside my professional work, I actively build and maintain my personal project, where I explore AI-assisted UX, product thinking, and practical execution. It reflects how I approach problems and how I think about product design beyond a single role or company.
Portfolio & case studies: {format_academic_simple_url("https://example.com")}

I'm looking for a team where design is treated as part of product decision-making — not just delivery — and where clarity, ownership, and outcomes matter. If that sounds aligned, I'd be glad to talk.

Best regards,

{NAME}

"""


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="Cover_Letter.pdf"):
    """Generates PDF in academic style"""
    margins = get_academic_margins()
    
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        **margins
    )
    
    s = get_academic_styles()
    
    story = [
        Paragraph(nz(NAME), s["title"]),
        Spacer(1, 3*mm),
        Paragraph(nz(LINKS), s["meta"]),
        Spacer(1, 8*mm),
        # Uncomment next line if date is needed:
        # Paragraph(nz(TODAY), s["date"]),
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>"), s["body"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT}, academic style)")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
