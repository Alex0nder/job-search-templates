# generate_career_break.py
# Template for generating Career Break Explanation in PDF

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

# Data about career break
BREAK_START = "January 2023"  # When break started
BREAK_END = "January 2024"  # When break ended (or "Present")
BREAK_DURATION = "1 year"  # Break duration
BREAK_REASON = "PERSONAL_DEVELOPMENT"  # "PERSONAL_DEVELOPMENT", "FAMILY", "TRAVEL", "STUDY", "HEALTH", "OTHER"


# ========== LETTER TEXT: Variants depending on break reason ==========

REASON_TEXTS = {
    "PERSONAL_DEVELOPMENT": "I took time off to focus on personal development and skill-building. During this period, I [specific actions - e.g., 'completed online courses in UX design, worked on personal projects, and attended industry conferences'].",
    "FAMILY": "I took a career break to focus on family responsibilities. During this time, I [specific actions - e.g., 'maintained my skills through freelance projects and continued learning'].",
    "TRAVEL": "I took time to travel and explore different cultures, which has given me valuable perspective and new insights that I'm excited to bring to my work.",
    "STUDY": "I took time off to pursue further education. I [specific actions - e.g., 'completed a certification program in Product Design and worked on several portfolio projects'].",
    "HEALTH": "I took time off to focus on my health and well-being. I'm now fully recovered and ready to return to work with renewed energy and focus.",
    "OTHER": "[Describe break reason positively, focusing on what you did and what you learned]"
}

BODY = f"""

I wanted to address the gap in my employment history from {BREAK_START} to {BREAK_END}.

{REASON_TEXTS.get(BREAK_REASON, REASON_TEXTS["OTHER"])}

During this {BREAK_DURATION} break, I remained engaged with the industry through [specific actions - e.g., 'freelance projects, online learning, attending webinars, or working on personal projects']. I'm now ready to return to full-time work and I'm excited about the opportunity to bring fresh perspectives and renewed energy to [position/company name].

I'm confident that the skills and experiences I've gained during this time, combined with my previous professional background, make me a strong candidate for this role.

Thank you for your understanding and consideration.

Best regards,

{NAME}

"""


# ---------- Build PDF ----------

def build_pdf(path="Career_Break_Explanation.pdf"):
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
