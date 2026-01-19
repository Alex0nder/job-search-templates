# generate_application_withdrawal.py
# Template for generating Application Withdrawal (application withdrawal) in PDF

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

# Data for application withdrawal
CONTACT_NAME = "Name Last Name"  # Recruiter/HR name
COMPANY_NAME = "Example Company"  # Company name
POSITION = "Senior Product Designer"  # Position title


# ========== LETTER TEXT: Edit for specific situation ==========
# Reason for withdrawal can be specified briefly (optional) or removed entirely

BODY = f"""

Hi {CONTACT_NAME},

I hope this email finds you well. I'm writing to withdraw my application for the {POSITION} position at {COMPANY_NAME}.

[Optional: brief reason - e.g., "I've accepted another opportunity that better aligns with my career goals" or "My circumstances have changed and I'm no longer actively seeking this position" or simply remove this paragraph]

I want to thank you and the team at {COMPANY_NAME} for your time and consideration throughout this process. I have great respect for {COMPANY_NAME} and I wish you the best in finding the right candidate for this role.

Thank you again for the opportunity.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Application_Withdrawal.pdf"):
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
