# generate_follow_up.py
# Template for generating Follow-up after silence in PDF

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

# Data for follow-up
CONTACT_NAME = "Name Last Name"  # Contact name (recruiter, manager, etc.)
COMPANY_NAME = "Example Company"  # Company name
FOLLOW_UP_TYPE = "AFTER_APPLICATION"  # "AFTER_APPLICATION" or "AFTER_INTERVIEW"
TIME_PASSED = "2 weeks"  # How much time has passed


# ========== LETTER TEXT: Variants depending on follow-up type ==========

if FOLLOW_UP_TYPE == "AFTER_APPLICATION":
    BODY = f"""

Hi {CONTACT_NAME},

I hope this email finds you well. I wanted to follow up on my application for [position title] at {COMPANY_NAME}, which I submitted about {TIME_PASSED} ago.

I'm still very interested in this opportunity and would love to learn more about the next steps in the process. I understand you're likely busy, so I appreciate any update you can provide.

If the position has been filled, I'd still be interested in future opportunities at {COMPANY_NAME}. Thank you for your time and consideration!

Best regards,

{NAME}

"""
else:  # AFTER_INTERVIEW
    BODY = f"""

Hi {CONTACT_NAME},

I hope you're doing well. I wanted to follow up on our interview for [position title] at {COMPANY_NAME}, which took place about {TIME_PASSED} ago.

I'm still very enthusiastic about this opportunity and would love to hear about the next steps. I understand the hiring process can take time, so I wanted to check in and see if there's any update.

Thank you again for your time during the interview process. I'm looking forward to hearing from you!

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Follow_Up_Letter.pdf"):
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
