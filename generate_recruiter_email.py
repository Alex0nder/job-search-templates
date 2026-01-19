# generate_recruiter_email.py
# Template for generating Email request to recruiter/HR in PDF (Academic Style)

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

# Data for request
RECRUITER_NAME = "Name Last Name"  # Recruiter name (can be left empty or "Hiring Team")
COMPANY_NAME = "Example Company"  # Company name
POSITION = "Senior Product Designer"  # Position title


# ========== LETTER TEXT: Edit for specific situation ==========

BODY = f"""

Hi {RECRUITER_NAME if RECRUITER_NAME else "there"},

I hope this email finds you well. I'm reaching out because I'm interested in exploring opportunities at {COMPANY_NAME}. I've been following {COMPANY_NAME}'s work in [industry/field] and I'm impressed by [specific reason interest].

With [X] years of experience as a [position] focusing on [specialization field], I've worked on [examples of projects or achievements]. I'm particularly drawn to {COMPANY_NAME} because of [specific reason - mission, product, team].

I've attached my CV for your review. I'd love to learn more about open positions or discuss how my experience could contribute to your team. Would you be available for a brief call or coffee chat?

Portfolio & case studies: {format_academic_simple_url("https://example.com")}

Thank you for your time and consideration. Looking forward to hearing from you!

Best regards,

{NAME}

"""


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="Recruiter_Email.pdf"):
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
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>"), s["body"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
