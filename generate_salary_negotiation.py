# generate_salary_negotiation.py
# Template for generating Salary Negotiation Letter in PDF

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
from reportlab.lib.units import mm
import unicodedata, datetime


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

# Offer data
HIRING_MANAGER_NAME = "Name Last Name"  # Manager/recruiter name
COMPANY_NAME = "Example Company"  # Company name
POSITION = "Senior Product Designer"  # Position title

# Offered compensation (specify what is offered)
OFFERED_SALARY = "$100,000"  # Offered salary
DESIRED_SALARY = "$115,000"  # Desired salary


# ========== LETTER TEXT: Edit for specific situation ==========

BODY = f"""

Dear {HIRING_MANAGER_NAME},

Thank you for extending the offer for the {POSITION} role at {COMPANY_NAME}. I'm very excited about this opportunity and the chance to contribute to your team.

After careful consideration, I'd like to discuss the compensation package. Based on my research of market rates for similar roles in [location/region] and my experience with [relevant experience], I believe a salary of {DESIRED_SALARY} would better reflect the value I can bring to {COMPANY_NAME}.

Here's what I bring to the table:
[Specific achievement or experience 1] - [how this helps the company]
[Specific achievement or experience 2] - [how this helps the company]
[Specific achievement or experience 3] - [how this helps the company]

I'm very enthusiastic about this role and {COMPANY_NAME}'s mission. I'm confident that my experience and skills will make a significant impact, and I believe this salary adjustment reflects that value.

I'm open to discussing this further and finding a package that works for both of us. Would you be available for a call this week to discuss?

Thank you again for this opportunity. I'm looking forward to joining the team.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Salary_Negotiation_Letter.pdf"):
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
