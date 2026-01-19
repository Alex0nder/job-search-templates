# generate_resignation_letter.py
# Template for generating Resignation Letter (resignation letter) in PDF

# pip install reportlab

from reportlab.lib.pagesizes import A4

# Import academic styles
from academic_styles import (
    get_academic_styles,
    get_academic_margins,
    format_academic_url_link,
    format_academic_simple_url,
    format_academic_email_link,
    BASE_FONT
)

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
import unicodedata, datetime



# ---------- Helpers ----------

def nz(s: str) -> str:
    """Unicode normalization and character replacements"""
    if not s: return ""
    s = unicodedata.normalize("NFC", s)
    return (s.replace("\u00A0"," ")
             .replace("\u2009"," ")
             .replace("\u2013","–")
             .replace("\u2014","—")
             .replace("\u2212","-"))

    return f'<a href="{full_url}" color="blue">{name}: {url}</a>'


# ========== CONFIGURATION: Replace with your data ==========

NAME    = "John Doe"  # Your name
EMAIL   = "john.doe@example.com"  # Your email
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/johndoe")} · {format_academic_url_link("Portfolio", "johndoe.dev")}'

# Data about resignation
MANAGER_NAME = "Name Last Name"  # Your manager name
COMPANY_NAME = "Example Company"  # Company name
POSITION = "Senior Product Designer"  # Your current position
LAST_DAY = "February 15, 2026"  # Last working day (usually 2 weeks or per contract)
NOTICE_PERIOD = "2 weeks"  # Notice period


# ========== LETTER TEXT: Edit for specific situation ==========
# Resignation reason can be specified briefly (optional) or removed entirely

BODY = f"""

Dear {MANAGER_NAME},

Please accept this letter as formal notification that I am resigning from my position as {POSITION} at {COMPANY_NAME}. My last day of work will be {LAST_DAY}, which provides {NOTICE_PERIOD} notice as required.

I want to express my gratitude for the opportunities I've had during my time at {COMPANY_NAME}. I've learned a great deal and truly appreciate the support and guidance I've received from you and the team.

[Optional: brief reason - e.g., "I've accepted a new opportunity that aligns with my long-term career goals" or "I'm taking time to focus on personal development" or simply remove this paragraph]

I'm committed to ensuring a smooth transition. I'm happy to help train my replacement, document my current projects, and assist in any way possible during this transition period.

Thank you again for everything. I wish {COMPANY_NAME} and the team continued success.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Resignation_Letter.pdf"):
    """Generates PDF in academic style"""
    margins = get_academic_margins()
    doc = SimpleDocTemplate(path, pagesize=A4, **margins)
    s = get_academic_styles()
    
    story = [
        Paragraph(nz(NAME), s["title"]),
        Spacer(1, 3*mm),
        Paragraph(nz(LINKS), s["meta"]),
        Spacer(1, 8*mm),
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>"), s["body"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
