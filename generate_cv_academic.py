# generate_cv_academic.py
# Template for generating CV/Resume in academic style (scientific publications)

# pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
import unicodedata

# Import academic styles
from academic_styles import (
    get_academic_styles,
    get_academic_margins,
    format_academic_email_link,
    format_academic_url_link,
    BASE_FONT,
    BOLD_FONT,
    TEXT_COLOR,
    META_COLOR
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

DATA = {
    "name": "John Doe",
    "title": "Senior Product Designer",
    "contacts": {
        "email": "john.doe@example.com",
        "linkedin": "linkedin.com/in/johndoe",
        "portfolio": "johndoe.dev",
    },
    "summary": "Product designer with 8+ years of experience designing complex software products. Focus on data-driven platforms, conversion flows, and scalable design systems. Experience with fintech, AI-driven tools, and B2B interfaces.",
    "ai_impact": [
        "Improved task efficiency in AI-assisted flows by ~25-30%",
        "Increased onboarding activation by ~30% through user research and A/B testing",
        "Reduced design-to-dev inconsistencies by ~20% via unified design systems",
    ],
    "core_skills": [
        "Product Design & UX Strategy",
        "Design Systems & Component Libraries",
        "User Research & Usability Testing",
        "Prototyping & Interaction Design",
        "Figma, Sketch, Principle",
    ],
    "experience": [
        {
            "company": "Example Company",
            "role": "Senior Product Designer",
            "dates": "2022 - Present",
            "location": "Remote",
            "bullets": [
                "Designed AI-powered internal service integrated into product workflows",
                "Built scalable design system used across multiple tools and teams",
                "Improved user efficiency by ~25% through workflow optimization",
            ],
        },
        {
            "company": "Another Company",
            "role": "Product Designer",
            "dates": "2020 - 2022",
            "location": "New York",
            "bullets": [
                "Redesigned trading experiences and onboarding flows",
                "Improved activation by ~30% through iterative UX research",
                "Collaborated with growth teams on A/B testing and conversion optimization",
            ],
        },
    ],
    "education": [
        "Bachelor's Degree in Design, Example University (2015-2019)",
    ],
}


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="CV_Resume.pdf"):
    """Generates CV in academic style"""
    margins = get_academic_margins()
    
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        **margins
    )
    
    s = get_academic_styles()
    
    story = []
    
    # Header
    story.append(Paragraph(nz(DATA["name"]), s["title"]))
    story.append(Paragraph(nz(DATA["title"]), s["subsection"]))
    story.append(Spacer(1, 2*mm))
    
    # Contacts
    contacts = DATA.get("contacts", {})
    contact_parts = []
    if contacts.get("email"):
        contact_parts.append(format_academic_email_link(contacts["email"]))
    if contacts.get("linkedin"):
        contact_parts.append(format_academic_url_link("LinkedIn", contacts["linkedin"]))
    if contacts.get("portfolio"):
        contact_parts.append(format_academic_url_link("Portfolio", contacts["portfolio"]))
    
    if contact_parts:
        story.append(Paragraph(" · ".join(contact_parts), s["meta"]))
        story.append(Spacer(1, 6*mm))
    
    # Summary
    story.append(Paragraph(nz("<b>SUMMARY</b>"), s["section"]))
    story.append(Paragraph(nz(DATA.get("summary", "")), s["body"]))
    
    # AI & Product Impact
    story.append(Paragraph(nz("<b>AI & PRODUCT IMPACT</b>"), s["section"]))
    for line in DATA.get("ai_impact", []):
        story.append(Paragraph(nz(line), s["body_left"]))
    
    # Core Skills
    story.append(Paragraph(nz("<b>CORE SKILLS</b>"), s["section"]))
    skills_text = " · ".join(DATA.get("core_skills", []))
    story.append(Paragraph(nz(skills_text), s["body_left"]))
    
    # Experience
    story.append(Paragraph(nz("<b>EXPERIENCE</b>"), s["section"]))
    for job in DATA.get("experience", []):
        header = f'{job["company"]} — {job["role"]}'
        meta = f'{job.get("dates", "")} | {job.get("location", "")}'
        
        story.append(Paragraph(nz(header), s["subsection"]))
        story.append(Paragraph(nz(meta), s["meta_text"]))
        
        # Bullets as paragraphs (no bullet points in academic style)
        for b in job.get("bullets", []):
            story.append(Paragraph(nz(b), s["body_left"]))
        
        story.append(Spacer(1, 2*mm))
    
    # Education
    story.append(Paragraph(nz("<b>EDUCATION</b>"), s["section"]))
    for e in DATA.get("education", []):
        story.append(Paragraph(nz(e), s["body_left"]))
    
    doc.build(story)
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
