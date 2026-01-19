# generate_networking_email.py
# Template for generating Networking Email in PDF

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

# Data for networking
CONTACT_NAME = "Name Last Name"  # Person name
COMPANY_NAME = "Example Company"  # Company where person works
NETWORKING_TYPE = "ADVICE"  # "ADVICE", "SHARED_INTEREST", "INDUSTRY_INSIGHT"


# ========== LETTER TEXT: Variants depending on networking type ==========

if NETWORKING_TYPE == "ADVICE":
    BODY = f"""

Hi {CONTACT_NAME},

I hope this email finds you well. I came across your profile and I'm really impressed by your work at {COMPANY_NAME} and your experience in [industry/field].

I'm currently [your situation - e.g., "exploring opportunities in product design" or "transitioning into UX design"] and I'd love to get your perspective and advice. Would you be open to a brief chat (15-20 minutes) or coffee? I'm particularly interested in learning about:
[Specific question 1]
[Specific question 2]

I completely understand if you're busy, and I'd be happy to work around your schedule. Even just a few minutes would be incredibly helpful.

Thank you so much for your time and consideration!

Best regards,

{NAME}

"""
elif NETWORKING_TYPE == "SHARED_INTEREST":
    BODY = f"""

Hi {CONTACT_NAME},

I hope this email finds you well. I noticed we both share an interest in [shared interest - e.g., "AI in product design" or "sustainable design practices"], and I'm really impressed by your work at {COMPANY_NAME}.

I'd love to connect and potentially exchange ideas or experiences. Would you be open to a brief chat or coffee? I think we could both benefit from sharing perspectives on [topic].

I completely understand if you're busy, but I'd love to stay in touch either way.

Best regards,

{NAME}

"""
else:  # INDUSTRY_INSIGHT
    BODY = f"""

Hi {CONTACT_NAME},

I hope this email finds you well. I came across your work at {COMPANY_NAME} and I'm really impressed by [specific reason - e.g., "your approach to design systems" or "the products you've built"].

I'm currently working in [field] and I'm always interested in learning from other professionals in the industry. Would you be open to a brief chat or coffee? I'd love to learn more about your experience and insights.

I completely understand if you're busy, but I'd love to connect either way.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Networking_Email.pdf"):
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
