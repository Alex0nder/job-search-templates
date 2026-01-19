# generate_reference_check_prep.py
# Template for generating Reference Check Preparation (preparation for reference check) in PDF

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

# Data for reference check preparation
REFEREE_NAME = "Name Last Name"  # Referee name
COMPANY = "Example Company"  # Company where you worked together
ROLE = "Senior Product Designer"  # Your role there
NEW_COMPANY = "New Company"  # Company checking references
NEW_POSITION = "Senior Product Designer"  # Position you are applying for


# ========== LETTER TEXT: Edit for specific situation ==========

BODY = f"""

Hi {REFEREE_NAME},

I hope you're doing well! I wanted to reach out because {NEW_COMPANY} is conducting reference checks as part of their hiring process for the {NEW_POSITION} position I'm applying for.

They may be contacting you in the coming days, and I wanted to give you a heads up. I've listed you as a reference because of our work together at {COMPANY}, where I worked as {ROLE}.

If they reach out, here are some key points you might want to mention:
[Specific achievement 1 - e.g., "My work on [project] that resulted in [result]"]
[Specific achievement 2 - e.g., "My collaboration skills and ability to work with cross-functional teams"]
[Specific achievement 3 - e.g., "My problem-solving approach and attention to detail"]

I've also attached my current resume for your reference, in case it's helpful.

Thank you so much for your support! I really appreciate you taking the time to speak with them. If you have any questions or need additional information, please don't hesitate to reach out.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Reference_Check_Preparation.pdf"):
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
