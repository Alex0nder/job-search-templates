# generate_thank_you_letter.py
# Template for generating Thank You Letter (after interview) in PDF (Academic Style)

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

# Interview data
INTERVIEWER_NAME = "Name Last Name"  # Interviewer name (or Hiring Manager)
COMPANY_NAME = "Example Company"  # Company name
POSITION = "Senior Product Designer"  # Position title
INTERVIEW_DATE = "yesterday"  # Interview date (e.g., "January 15, 2026" or "yesterday")


# ========== LETTER TEXT: Edit for specific situation ==========

BODY = f"""

Dear {INTERVIEWER_NAME},

Thank you for taking the time to meet with me {INTERVIEW_DATE} to discuss the {POSITION} role at {COMPANY_NAME}. I really enjoyed our conversation and learning more about the team, the product vision, and the challenges you're working on.

Our discussion about [specify specific topic from interview] reinforced my interest in this position. I'm particularly excited about the opportunity to [specify specific reason for interest]. Based on my experience with [relevant experience], I believe I can contribute to [specific result or project].

I also wanted to mention [additional thought or clarification, if any].

Thank you again for your time and consideration. I look forward to hearing from you about the next steps.

Best regards,

{NAME}

"""


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="Thank_You_Letter.pdf"):
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
    print(f"✅ Generated: {path}  (font={BASE_FONT}, academic style)")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
