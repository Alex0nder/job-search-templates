# generate_informational_interview.py
# Template for generating Informational Interview Request in PDF

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

    return f'<a href="{full_url}" color="blue">{url}</a>'


# ========== CONFIGURATION: Replace with your data ==========

NAME    = "John Doe"  # Your name
EMAIL   = "john.doe@example.com"  # Your email
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/johndoe")} · {format_academic_url_link("Portfolio", "johndoe.dev")}'

# Data for informational interview
CONTACT_NAME = "Name Last Name"  # Person name, you want to meet with
COMPANY_NAME = "Example Company"  # Company where person works
THEIR_ROLE = "Senior Product Designer"  # This person role
CONNECTION = "LinkedIn"  # How you are connected (LinkedIn, mutual connection, conference, etc.)


# ========== LETTER TEXT: Edit for specific situation ==========

BODY = f"""

Hi {CONTACT_NAME},

I hope this message finds you well. I came across your profile on {CONNECTION} and I'm really impressed by your work as {THEIR_ROLE} at {COMPANY_NAME}.

I'm currently exploring opportunities in [industry/field] and I'd love to learn more about your experience at {COMPANY_NAME} and in the industry. Would you be open to a brief informational chat (15-20 minutes) over coffee or a video call? I'm particularly interested in learning about:
[Specific question 1 - e.g., "the product design process at {COMPANY_NAME}"]
[Specific question 2 - e.g., "challenges in the industry"]
[Specific question 3 - e.g., "career growth paths"]

I completely understand if you're busy, and I'd be happy to work around your schedule. Even just a few minutes would be incredibly helpful.

Thank you so much for your time and consideration!

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Informational_Interview_Request.pdf"):
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
