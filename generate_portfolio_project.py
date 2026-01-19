# generate_portfolio_project.py
# Template for generating Portfolio Project Description in PDF (Academic Style)

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

# Project data
PROJECT_NAME = "Project Name"  # Project name
PROJECT_TYPE = "Product Design"  # Project type (Product Design, UX Research, etc.)
COMPANY = "Example Company"  # Company/client (or "Personal Project")
TIMELINE = "Q1 2024"  # Project timeline
TEAM_SIZE = "3 people"  # Team size (or "Solo project")


# ========== PROJECT DESCRIPTION TEXT ==========

BODY = f"""

{PROJECT_NAME}

{PROJECT_TYPE} • {COMPANY} • {TIMELINE} • Team: {TEAM_SIZE}

---

Challenge

[Describe problem or challenge, that the project solved. What was wrong? What were the pain points users or business?]

Solution

[Describe your solution. What approach did you use? What key decisions were made?]

Key Features:
[Key feature 1]
[Key feature 2]
[Key feature 3]

Process

[Describe work process: research, iterations, testing, etc.]

Research: [What you learned from research]

Design: [How you approached to design and prototyping]

Testing: [How you tested and iterated]

Results

[Describe results and metrics. What changed? What were the achievements?]

[Result 1 - e.g., "Increased user engagement by 30%"]
[Result 2 - e.g., "Reduced support tickets by 25%"]
[Result 3 - e.g., "Improved conversion rate by 15%"]

My Role

[Describe your role in project. What specifically did you do? What were you responsible for?]

Tools & Technologies

[List of tools and technologies used]

"""


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="Portfolio_Project_Description.pdf"):
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
        Spacer(1, 2*mm),
        Paragraph(nz(LINKS), s["meta"]),
        Spacer(1, 8*mm),
        Paragraph(nz(BODY).replace("\n\n", "<br/><br/>").replace("\n---", "<br/><br/>---"), s["body"]),
    ]
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
