# generate_cv.py
# Template for generating CV/Resume in PDF

# pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

PAGE_W, PAGE_H = A4
MARGIN_X = 16 * mm
MARGIN_TOP = 16 * mm
MARGIN_BOTTOM = 16 * mm

FONT_MAIN = "Helvetica"
FONT_BOLD = "Helvetica-Bold"


def draw_wrapped_text(c: canvas.Canvas, text: str, x: float, y: float, max_width: float, font: str, size: int, leading: float):
    """Draws text with line breaks"""
    c.setFont(font, size)
    words = text.split()
    line = ""
    lines = []
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, font, size) <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)

    for ln in lines:
        c.drawString(x, y, ln)
        y -= leading
    return y

def draw_link(c: canvas.Canvas, text: str, url: str, x: float, y: float, font: str, size: int):
    """Draws text with link on canvas"""
    c.setFont(font, size)
    width = c.stringWidth(text, font, size)
    c.drawString(x, y, text)
    c.linkURL(url, (x, y - size * 0.7, x + width, y + size * 0.3), relative=1)
    return x + width

def section_title(c: canvas.Canvas, title: str, x: float, y: float):
    """Draws section title"""
    c.setFont(FONT_BOLD, 11)
    c.drawString(x, y, title.upper())
    return y - 6 * mm

def hr(c: canvas.Canvas, x: float, y: float, w: float):
    """Draws horizontal line"""
    c.setLineWidth(0.6)
    c.line(x, y, x + w, y)
    return y - 4 * mm

def ensure_space(c: canvas.Canvas, y: float, needed: float):
    """Checks space on page, adds new one if needed"""
    if y - needed < MARGIN_BOTTOM:
        c.showPage()
        return PAGE_H - MARGIN_TOP
    return y


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


def main():
    # Output file name
    out = "CV_Resume.pdf"
    c = canvas.Canvas(out, pagesize=A4)

    x = MARGIN_X
    w = PAGE_W - 2 * MARGIN_X
    y = PAGE_H - MARGIN_TOP

    # Header
    c.setFont(FONT_BOLD, 20)
    c.drawString(x, y, DATA["name"])
    y -= 8 * mm

    c.setFont(FONT_MAIN, 11)
    c.drawString(x, y, DATA["title"])
    y -= 5 * mm

    # Contacts with links
    contacts = DATA.get("contacts", {})
    current_x = x
    current_y = y
    separator = "  •  "
    c.setFont(FONT_MAIN, 9)
    separator_width = c.stringWidth(separator, FONT_MAIN, 9)
    line_height = 11
    
    c.setFillColorRGB(0, 0, 0)
    
    contact_items = []
    if contacts.get("email"):
        contact_items.append(("email", contacts["email"], f"mailto:{contacts['email']}"))
    if contacts.get("linkedin"):
        linkedin = contacts["linkedin"]
        linkedin_url = f"https://{linkedin}" if not linkedin.startswith(("http://", "https://")) else linkedin
        contact_items.append(("linkedin", linkedin, linkedin_url))
    if contacts.get("portfolio"):
        portfolio = contacts["portfolio"]
        portfolio_url = f"https://{portfolio}" if not portfolio.startswith(("http://", "https://")) else portfolio
        contact_items.append(("portfolio", portfolio, portfolio_url))
    
    first = True
    for item_type, text, url in contact_items:
        if not first:
            if current_x + separator_width > x + w:
                current_x = x
                current_y -= line_height
            c.setFillColorRGB(0, 0, 0)
            c.drawString(current_x, current_y, separator)
            current_x += separator_width
        
        text_width = c.stringWidth(text, FONT_MAIN, 9)
        if current_x + text_width > x + w:
            current_x = x
            current_y -= line_height
        
        c.setFillColor(blue)
        c.drawString(current_x, current_y, text)
        c.linkURL(url, (current_x, current_y - 9 * 0.7, current_x + text_width, current_y + 9 * 0.3), relative=1)
        c.setFillColorRGB(0, 0, 0)
        current_x += text_width
        first = False
    
    y = current_y - line_height
    y -= 2 * mm
    y = hr(c, x, y, w)

    # Summary
    y -= 1.4 * mm
    y = ensure_space(c, y, 40 * mm)
    y = section_title(c, "Summary", x, y)
    summary_text = DATA.get("summary", "")
    y = draw_wrapped_text(c, summary_text, x, y, w, FONT_MAIN, 10, leading=13)
    y -= 2 * mm

    # AI & Product Impact (can be renamed to "Key Achievements" or "Impact")
    y = ensure_space(c, y, 30 * mm)
    y = section_title(c, "AI & Product Impact", x, y)
    for line in DATA.get("ai_impact", []):
        y = draw_wrapped_text(c, f"• {line}", x, y, w, FONT_MAIN, 10, leading=13)
    y -= 2 * mm

    # Core Skills
    y = ensure_space(c, y, 30 * mm)
    y = section_title(c, "Core Skills", x, y)
    for s in DATA.get("core_skills", []):
        y = draw_wrapped_text(c, f"• {s}", x, y, w, FONT_MAIN, 10, leading=13)
    y -= 2 * mm

    # Experience
    y = ensure_space(c, y, 50 * mm)
    y = section_title(c, "Experience", x, y)
    for job in DATA.get("experience", []):
        y = ensure_space(c, y, 35 * mm)

        header = f'{job["company"]} — {job["role"]}'
        meta = f'{job.get("dates", "")} | {job.get("location", "")}'
        c.setFont(FONT_BOLD, 11)
        c.drawString(x, y, header)
        y -= 5 * mm

        c.setFont(FONT_MAIN, 9)
        c.drawString(x, y, meta)
        y -= 4 * mm

        for b in job.get("bullets", []):
            y = draw_wrapped_text(c, f"• {b}", x + 4 * mm, y, w - 4 * mm, FONT_MAIN, 10, leading=13)

        y -= 2 * mm

    # Education
    y = ensure_space(c, y, 25 * mm)
    y = section_title(c, "Education", x, y)
    for e in DATA.get("education", []):
        y = draw_wrapped_text(c, f"• {e}", x, y, w, FONT_MAIN, 10, leading=13)

    c.save()
    print(f"✅ Generated: {out}")


if __name__ == "__main__":
    main()
