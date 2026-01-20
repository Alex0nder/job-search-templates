# generate_portfolio_case.py
# Template for generating Portfolio Case Study in PDF (Academic Style with Images)

# pip install reportlab pillow

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
import unicodedata, datetime, os, random

# Import academic styles
from academic_styles import (
    get_academic_styles,
    get_academic_margins,
    format_academic_url_link,
    format_academic_simple_url,
    format_academic_email_link,
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


def create_placeholder_image(width, height, base_path=None):
    """Creates a placeholder image using PIL/Pillow"""
    try:
        from PIL import Image as PILImage, ImageDraw, ImageFont
        import tempfile
        
        if base_path is None:
            # Create temporary file with absolute path
            fd, path = tempfile.mkstemp(suffix='.png', prefix='placeholder_')
            os.close(fd)
        else:
            path = os.path.abspath(base_path)
        
        img = PILImage.new('RGB', (int(width), int(height)), color='#f5f5f5')
        draw = ImageDraw.Draw(img)
        
        # Draw border
        draw.rectangle([0, 0, width-1, height-1], outline='#cccccc', width=2)
        
        # Draw text
        text = f"{int(width)}×{int(height)}"
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        draw.text(
            ((width - text_width) / 2, (height - text_height) / 2),
            text,
            fill='#999999',
            font=font
        )
        
        img.save(path)
        return path
    except ImportError:
        # If PIL not available, return None (image will be skipped)
        return None
    except Exception as e:
        print(f"Warning: Could not create placeholder image: {e}")
        return None


def add_image_with_caption(story, image_path, caption, styles, max_width=160*mm, placeholder_files=None):
    """Adds image with caption in academic style"""
    if image_path and os.path.exists(image_path):
        # Load image and scale proportionally
        try:
            from PIL import Image as PILImage
            pil_img = PILImage.open(image_path)
            img_width, img_height = pil_img.size
            aspect_ratio = img_height / img_width
            scaled_height = max_width * aspect_ratio
            
            img = Image(image_path, width=max_width, height=scaled_height)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 4*mm))
            story.append(img)
            story.append(Spacer(1, 2*mm))
            
            # Caption in italic, centered, smaller font
            caption_para = Paragraph(
                f'<i>{nz(caption)}</i>',
                styles["caption"]
            )
            story.append(caption_para)
            story.append(Spacer(1, 4*mm))
        except Exception as e:
            print(f"Warning: Could not load image {image_path}: {e}")
    else:
        # Create placeholder if image doesn't exist
        placeholder_height = max_width * 0.6
        placeholder_path = create_placeholder_image(max_width, placeholder_height)
        if placeholder_path:
            img = Image(placeholder_path, width=max_width, height=placeholder_height)
            img.hAlign = 'CENTER'
            story.append(Spacer(1, 4*mm))
            story.append(img)
            story.append(Spacer(1, 2*mm))
            caption_para = Paragraph(
                f'<i>{nz(caption)}</i>',
                styles["caption"]
            )
            story.append(caption_para)
            story.append(Spacer(1, 4*mm))
            # Track placeholder files for cleanup
            if placeholder_files is not None:
                placeholder_files.append(placeholder_path)


# ========== CONFIGURATION: Replace with your data ==========

NAME    = "John Doe"  # Your name
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/johndoe")} · {format_academic_url_link("Portfolio", "johndoe.dev")}'

# Case study data
CASE_TITLE = "AI-Powered Trading Assistant: Improving User Efficiency by 40%"
CASE_SUBTITLE = "Product Design Case Study"
COMPANY = "Example Company"
TIMELINE = "March 2023 – December 2024"
ROLE = "Senior Product Designer"


# ========== CASE STUDY CONTENT ==========

ABSTRACT = """
This case study presents the design process and outcomes of an AI-powered trading assistant feature that improved user trading efficiency by 40% and reduced support requests by 35%. The project involved end-to-end product design, from user research and problem definition to iterative prototyping and data-driven validation.
"""

INTRODUCTION = """
Trading platforms face a common challenge: users struggle to make informed decisions quickly, leading to missed opportunities and increased support workload. This case study documents the design and implementation of an AI-powered trading assistant that addresses these pain points through intelligent automation and contextual guidance.
"""

METHODS = """
The design process followed a structured approach combining quantitative analysis, qualitative research, and iterative prototyping. User interviews with 15 active traders revealed key pain points: decision paralysis, lack of contextual information, and time-consuming manual research. Competitive analysis of 8 leading trading platforms informed the initial feature set.

Prototyping was conducted in three phases: low-fidelity wireframes for concept validation, high-fidelity interactive prototypes for usability testing, and a limited beta release for real-world validation. A/B testing was used to compare different interaction patterns and information architectures.
"""

RESULTS = """
The final design resulted in measurable improvements across key metrics:

• Trading efficiency increased by 40% (measured by time-to-decision)
• Support ticket volume decreased by 35%
• User activation rate improved by 22% in the first month
• 78% of beta users reported increased confidence in trading decisions

Qualitative feedback highlighted the value of contextual AI suggestions and the streamlined interface that reduced cognitive load during decision-making.
"""

DISCUSSION = """
The success of this feature demonstrates the importance of combining AI capabilities with thoughtful UX design. Key learnings include the need for transparent AI decision-making, the value of progressive disclosure for complex information, and the critical role of user trust in AI-assisted features.

Future iterations will focus on personalization, expanding the AI's contextual understanding, and exploring voice-based interactions for mobile users.
"""

# Image configurations (use actual image paths or leave empty for placeholders)
IMAGES = [
    {
        "path": "",  # Leave empty for placeholder
        "caption": "Figure 1. Initial user flow diagram showing the AI assistant integration points."
    },
    {
        "path": "",
        "caption": "Figure 2. High-fidelity prototype of the trading assistant interface with contextual suggestions."
    },
    {
        "path": "",
        "caption": "Figure 3. A/B test results comparing different interaction patterns (n=1,247 users)."
    },
]


# ---------- Build PDF with Academic Style ----------

def build_pdf(path="Portfolio_Case_Study.pdf"):
    """Generates PDF in academic style with images"""
    margins = get_academic_margins()
    
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        **margins
    )
    
    s = get_academic_styles()
    
    # Add caption style for images
    from reportlab.lib.styles import getSampleStyleSheet
    base = getSampleStyleSheet()
    s["caption"] = ParagraphStyle(
        "caption",
        parent=base["Normal"],
        fontName=BASE_FONT,
        fontSize=9,
        leading=11,
        textColor=META_COLOR,
        spaceAfter=2*mm,
        alignment=TA_CENTER,
        fontStyle='Italic'
    )
    
    story = []
    placeholder_files = []  # Track placeholder files for cleanup
    
    # Title
    story.append(Paragraph(nz(CASE_TITLE), s["title"]))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(nz(CASE_SUBTITLE), s["subsection"]))
    story.append(Spacer(1, 4*mm))
    
    # Author and metadata
    story.append(Paragraph(nz(NAME), s["meta"]))
    story.append(Paragraph(nz(f"{COMPANY} • {TIMELINE} • {ROLE}"), s["meta"]))
    story.append(Paragraph(nz(LINKS), s["meta"]))
    story.append(Spacer(1, 8*mm))
    
    # Abstract
    story.append(Paragraph(nz("<b>Abstract</b>"), s["section"]))
    story.append(Paragraph(nz(ABSTRACT), s["body"]))
    story.append(Spacer(1, 6*mm))
    
    # Introduction
    story.append(Paragraph(nz("<b>1. Introduction</b>"), s["section"]))
    story.append(Paragraph(nz(INTRODUCTION), s["body"]))
    story.append(Spacer(1, 4*mm))
    
    # Add first image
    if IMAGES:
        add_image_with_caption(story, IMAGES[0]["path"], IMAGES[0]["caption"], s, placeholder_files=placeholder_files)
    
    # Methods
    story.append(Paragraph(nz("<b>2. Methods</b>"), s["section"]))
    story.append(Paragraph(nz(METHODS), s["body"]))
    story.append(Spacer(1, 4*mm))
    
    # Add second image
    if len(IMAGES) > 1:
        add_image_with_caption(story, IMAGES[1]["path"], IMAGES[1]["caption"], s, placeholder_files=placeholder_files)
    
    # Results
    story.append(Paragraph(nz("<b>3. Results</b>"), s["section"]))
    story.append(Paragraph(nz(RESULTS), s["body"]))
    story.append(Spacer(1, 4*mm))
    
    # Add third image
    if len(IMAGES) > 2:
        add_image_with_caption(story, IMAGES[2]["path"], IMAGES[2]["caption"], s, placeholder_files=placeholder_files)
    
    # Discussion
    story.append(Paragraph(nz("<b>4. Discussion</b>"), s["section"]))
    story.append(Paragraph(nz(DISCUSSION), s["body"]))
    
    doc.build(story)
    
    # Clean up placeholder files
    for placeholder_file in placeholder_files:
        try:
            if os.path.exists(placeholder_file):
                os.remove(placeholder_file)
        except Exception as e:
            print(f"Warning: Could not remove placeholder file {placeholder_file}: {e}")
    
    print(f"✅ Generated: {path}  (font={BASE_FONT})")


if __name__ == "__main__":
    if BASE_FONT == "Times-Roman":
        print("⚠️ Using system Times-Roman. For best results, ensure Times New Roman fonts are available or add DejaVuSerif fonts to ./fonts/")
    build_pdf()
