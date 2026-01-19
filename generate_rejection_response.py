# generate_rejection_response.py
# Template for generating Rejection Response (rejection of offer) in PDF

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

# Offer data
HIRING_MANAGER_NAME = "Name Last Name"  # Manager/recruiter name
COMPANY_NAME = "Example Company"  # Company name
POSITION = "Senior Product Designer"  # Position title


# ========== LETTER TEXT: Edit for specific situation ==========
# Rejection reason can be specified briefly (optional) or removed entirely

BODY = f"""

Dear {HIRING_MANAGER_NAME},

Thank you so much for extending the offer for the {POSITION} role at {COMPANY_NAME}. I truly appreciate the time you and the team took throughout the interview process.

After careful consideration, I've decided to decline the offer. This was not an easy decision, as I was very impressed with {COMPANY_NAME}'s mission, culture, and the team I met.

[Optional: brief reason - e.g., "I've accepted another opportunity that better aligns with my current career goals" or "The timing isn't quite right for me at this moment" or simply remove this paragraph]

I have a great deal of respect for {COMPANY_NAME} and would love to stay in touch for potential future opportunities. I wish you and the team all the best.

Thank you again for your consideration and the opportunity to learn more about {COMPANY_NAME}.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Rejection_Response.pdf"):
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
