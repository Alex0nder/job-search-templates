# generate_counter_offer_response.py
# Template for generating Counter-Offer Response (response to counter-offer) in PDF

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

# Counter-offer data
MANAGER_NAME = "Name Last Name"  # Your manager name
COMPANY_NAME = "Example Company"  # Current company
NEW_COMPANY = "New Company"  # Company that made the offer


# ========== LETTER TEXT: Edit for specific situation ==========
# Choose variant: ACCEPT (accept) or DECLINE (decline) counter-offer

RESPONSE_TYPE = "DECLINE"  # "ACCEPT" or "DECLINE"

if RESPONSE_TYPE == "ACCEPT":
    BODY = f"""

Dear {MANAGER_NAME},

Thank you so much for the counter-offer and for your efforts to keep me at {COMPANY_NAME}. I truly appreciate your support and the value you see in my contributions.

After careful consideration, I've decided to accept your counter-offer and stay with {COMPANY_NAME}. I'm excited about the opportunities ahead and look forward to continuing to contribute to the team's success.

I'm grateful for your flexibility and understanding throughout this process. I'm committed to delivering great work and helping {COMPANY_NAME} achieve its goals.

Thank you again for everything.

Best regards,

{NAME}

"""
else:  # DECLINE
    BODY = f"""

Dear {MANAGER_NAME},

Thank you so much for the counter-offer and for your efforts to keep me at {COMPANY_NAME}. I truly appreciate your support and the value you see in my contributions.

After careful consideration, I've decided to move forward with the opportunity at {NEW_COMPANY}. This was not an easy decision, as I have great respect for {COMPANY_NAME} and the team. However, I believe this new role aligns better with my long-term career goals and personal aspirations.

I want to express my gratitude for everything I've learned and experienced during my time here. I'm committed to ensuring a smooth transition and will do everything I can to help during this period.

Thank you again for your understanding and support.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Counter_Offer_Response.pdf"):
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
