# Job Search Templates

Python templates for generating professional PDF documents for job applications in scientific publication style.

## Features

- 📄 **Professional Style** - Beautiful, strict formatting like scientific publications (Times New Roman, justified text, professional margins)
- 📝 **17 Professional Templates** - Cover letters, CV, thank you letters, and more
- 🎨 **Customizable** - Easy to modify templates with your own data
- 🔗 **Clickable Links** - Email, LinkedIn, and portfolio links are clickable in PDF
- 🚀 **Ready to Use** - Simple Python scripts, no complex setup needed
- 🌍 **English Only** - All templates and documentation in English

## Examples

See example PDF files in the [`examples/`](examples/) folder:

- [Cover Letter](examples/Cover_Letter.pdf) - Professional cover letter template
- [CV/Resume](examples/CV_Resume.pdf) - One-page resume in scientific publication style
- [Thank You Letter](examples/Thank_You_Letter.pdf) - Post-interview follow-up
- [Salary Negotiation](examples/Salary_Negotiation_Letter.pdf) - Compensation negotiation

All 17 templates have example PDFs available in the `examples/` folder.

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Alex0nder/job-search-templates.git
cd job-search-templates
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Edit the template script you need with your information
2. Run the script:
```bash
# Cover Letter
python generate_cover_letter.py

# CV/Resume
python generate_cv_academic.py

# Thank You Letter (after interview)
python generate_thank_you_letter.py

# Recruiter Email
python generate_recruiter_email.py

# Salary Negotiation
python generate_salary_negotiation.py

# Rejection Response
python generate_rejection_response.py

# Recommendation Request
python generate_recommendation_request.py
```

PDF files will be generated in the same directory.

**Note:** Example PDF files are available in the `examples/` folder to see the output format.

## Professional Style

All templates use a professional scientific publication style:

- **Font**: Times New Roman (serif font)
- **Text Alignment**: Justified (for body text)
- **Margins**: 25-30mm (larger margins like scientific papers)
- **Colors**: Dark gray (#1a1a1a) instead of pure black for softer appearance
- **Typography**: No bullet points, clean paragraph-based lists
- **Line Spacing**: Tight, professional leading (13pt)

The `academic_styles.py` module provides consistent styling across all templates.

## Project Structure

```
job-search-templates/
├── academic_styles.py                  # Academic style definitions (shared module)
├── generate_cover_letter.py            # Cover Letter generator
├── generate_cv_academic.py             # CV/Resume generator (academic style)
├── generate_cv.py                      # CV/Resume generator (standard style)
├── generate_thank_you_letter.py       # Thank You Letter (after interview)
├── generate_recruiter_email.py        # Recruiter/HR email template
├── generate_salary_negotiation.py     # Salary negotiation letter
├── generate_rejection_response.py     # Decline job offer template
├── generate_recommendation_request.py # Request recommendations
├── generate_resignation_letter.py     # Resignation letter
├── generate_counter_offer_response.py # Response to counter-offer
├── generate_informational_interview.py # Informational interview request
├── generate_linkedin_connection.py    # LinkedIn connection request
├── generate_follow_up.py              # Follow-up after silence
├── generate_application_withdrawal.py # Application withdrawal
├── generate_career_break.py           # Career break explanation
├── generate_networking_email.py       # Networking email
├── generate_reference_check_prep.py   # Reference check preparation
├── generate_portfolio_project.py      # Portfolio project description
├── generate_academic_style.py         # Academic style example
├── examples/                          # Example PDF files (generated samples)
│   ├── Cover_Letter.pdf
│   ├── CV_Resume.pdf
│   ├── Thank_You_Letter.pdf
│   └── ... (all 17 templates)
├── requirements.txt                    # Python dependencies
├── .gitignore                         # Git ignore rules
└── README.md                          # This file
```

## Available Templates

### Core Templates

1. **Cover Letter** (`generate_cover_letter.py`)
   - Standard cover letter template for job applications
   - Customize greeting and body text for each company

2. **CV/Resume** (`generate_cv_academic.py`)
   - Professional resume in scientific publication style
   - Sections: Summary, AI & Product Impact, Core Skills, Experience, Education

3. **Thank You Letter** (`generate_thank_you_letter.py`)
   - Follow-up email after an interview
   - Includes gratitude, reminder of key points, and enthusiasm

### Communication Templates

4. **Recruiter Email** (`generate_recruiter_email.py`)
   - Initial contact email to recruiters or HR
   - Use for cold outreach or exploring opportunities

5. **Networking Email** (`generate_networking_email.py`)
   - Professional networking emails
   - Multiple variants for different scenarios

6. **LinkedIn Connection Request** (`generate_linkedin_connection.py`)
   - LinkedIn connection request messages
   - Variants: cold outreach, after interview, after meeting, mutual connection

7. **Follow-up Letter** (`generate_follow_up.py`)
   - Follow-up after application or interview silence
   - Professional reminder without being pushy

### Negotiation & Response Templates

8. **Salary Negotiation** (`generate_salary_negotiation.py`)
   - Professional letter to negotiate salary/compensation
   - Includes reasoning and value proposition

9. **Rejection Response** (`generate_rejection_response.py`)
   - Polite decline of a job offer
   - Maintains professional relationship for future opportunities

10. **Counter-Offer Response** (`generate_counter_offer_response.py`)
    - Response to counter-offer from current employer
    - Variants: accept or decline

### Career Management Templates

11. **Resignation Letter** (`generate_resignation_letter.py`)
    - Professional resignation letter
    - Maintains positive relationship with employer

12. **Application Withdrawal** (`generate_application_withdrawal.py`)
    - Withdraw job application politely
    - Useful when accepting another offer

13. **Career Break Explanation** (`generate_career_break.py`)
    - Explain career gaps positively
    - Multiple variants for different reasons

### Reference & Recommendation Templates

14. **Recommendation Request** (`generate_recommendation_request.py`)
    - Request recommendations from former colleagues or managers
    - Useful for LinkedIn recommendations or references

15. **Reference Check Preparation** (`generate_reference_check_prep.py`)
    - Prepare your references for reference checks
    - Helps them highlight your strengths

### Interview Templates

16. **Informational Interview Request** (`generate_informational_interview.py`)
    - Request informational interviews
    - Learn about company, role, or industry

### Portfolio Templates

17. **Portfolio Project Description** (`generate_portfolio_project.py`)
    - Professional project case study format
    - Structure: Challenge, Solution, Process, Results, Role, Tools

## Configuration

### Cover Letter Setup

Edit the following variables in `generate_cover_letter.py`:

```python
NAME    = "Your Name"
LINKS   = f'{format_academic_url_link("LinkedIn", "linkedin.com/in/yourprofile")} · {format_academic_url_link("Portfolio", "yourportfolio.com")}'
COMPANY = "Example Company"
ROLE    = "Senior Product Designer"
```

Edit the `BODY` variable to customize your cover letter text.

### CV/Resume Setup

Edit the `DATA` dictionary in `generate_cv_academic.py`:

```python
DATA = {
    "name": "Your Name",
    "title": "Your Job Title",
    "contacts": {
        "email": "your.email@example.com",
        "linkedin": "linkedin.com/in/yourprofile",
        "portfolio": "yourportfolio.com",
    },
    "summary": "Your professional summary...",
    "ai_impact": ["Achievement 1", "Achievement 2"],
    "core_skills": ["Skill 1", "Skill 2"],
    "experience": [...],
    "education": [...],
}
```

## Customization

### Fonts (Optional)

For best results with Times New Roman:

1. On macOS: Times New Roman is available by default
2. On Linux: Add DejaVuSerif fonts to `fonts/` directory:
   - `DejaVuSerif.ttf`
   - `DejaVuSerif-Bold.ttf`
   - `DejaVuSerif-Italic.ttf`
   - `DejaVuSerif-BoldItalic.ttf`
3. Download from [DejaVu Fonts](https://dejavu-fonts.github.io/)

If fonts are not specified, system default fonts will be used.

### Output File Names

Default output files:
- Cover Letter: `Cover_Letter.pdf`
- CV: `CV_Resume_Academic.pdf`

You can change these in the `build_pdf()` function in each script.

### Adding Date to Cover Letter

Uncomment the date line in `generate_cover_letter.py`:

```python
Paragraph(nz(TODAY), s["date"]),
```

## Style Module

The `academic_styles.py` module provides:

- **Font Registration**: Times New Roman with fallbacks
- **Style Definitions**: Consistent paragraph styles
- **Margins**: Scientific paper margins (25-30mm)
- **Link Formatting**: Professional links with underlines
- **Color Scheme**: Professional dark gray colors

All templates import and use this module for consistent styling.

## Requirements

- Python 3.6+
- reportlab (install via `pip install -r requirements.txt`)

## Troubleshooting

If you encounter issues:

1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Verify data in scripts is correct (no syntax errors)
3. Check font paths if using custom fonts
4. Ensure `academic_styles.py` is in the same directory as templates

## Contributing

Feel free to fork, modify, and use these templates for your job search needs.

## License

This project is free and open source. You are free to use, modify, and distribute these templates for any purpose, including commercial use.

## Author

**Alexander Young**

Created for simplifying the job search process. Feel free to customize to your needs!

- GitHub: [@Alex0nder](https://github.com/Alex0nder)
