# generate_linkedin_connection.py
# Template for generating LinkedIn Connection Request in PDF (Academic Style)

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
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/johndoe")} · {format_academic_url_link("Portfolio", "johndoe.dev")}'

# Data for LinkedIn request
CONTACT_NAME = "Name Last Name"  # Person name
COMPANY_NAME = "Example Company"  # Company where person works
CONNECTION_TYPE = "AFTER_INTERVIEW"  # "COLD", "AFTER_INTERVIEW", "AFTER_MEETING", "MUTUAL_CONNECTION"


# ========== LETTER TEXT: Variants depending on connection type ==========

if CONNECTION_TYPE == "COLD":
    BODY = f"""

Hi {CONTACT_NAME},

I came across your profile and I'm impressed by your work at {COMPANY_NAME}. I'm also in [industry/field] and would love to connect and learn from your experience.

Looking forward to connecting!

Best,
{NAME}

"""
elif CONNECTION_TYPE == "AFTER_INTERVIEW":
    BODY = f"""

Hi {CONTACT_NAME},

Great meeting you during the interview process at {COMPANY_NAME}! I really enjoyed our conversation about [topic from interview].

I'd love to stay connected on LinkedIn. Looking forward to keeping in touch!

Best,
{NAME}

"""
elif CONNECTION_TYPE == "AFTER_MEETING":
    BODY = f"""

Hi {CONTACT_NAME},

It was great meeting you at [event/conference/meeting]! I really enjoyed our conversation about [topic].

I'd love to connect on LinkedIn and continue the conversation. Looking forward to staying in touch!

Best,
{NAME}

"""
else:  # MUTUAL_CONNECTION
    BODY = f"""

Hi {CONTACT_NAME},

I noticed we have [Name] in common, and I'm impressed by your work at {COMPANY_NAME}. I'm also in [industry/field] and would love to connect.

Looking forward to connecting!

Best,
{NAME}

"""


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="LinkedIn_Connection_Request.pdf"):
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
