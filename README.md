# Job Search Templates

Python templates for generating professional PDF Cover Letters and CV/Resume for job applications.

## Features

- 📄 **Cover Letter Generator** - Create customizable cover letters in PDF format
- 📋 **CV/Resume Generator** - Generate professional resumes with standard sections
- 🙏 **Thank You Letter** - Follow-up after interviews
- 💼 **Recruiter Email** - Initial contact with companies and recruiters
- 💰 **Salary Negotiation** - Professional salary negotiation letters
- ❌ **Rejection Response** - Polite decline of job offers
- 📝 **Recommendation Request** - Ask former colleagues for recommendations
- 🎨 **Customizable** - Easy to modify templates with your own data
- 🔗 **Clickable Links** - Email, LinkedIn, and portfolio links are clickable in PDF
- 🚀 **Ready to Use** - Simple Python scripts, no complex setup needed

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
python generate_cv.py

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

## Project Structure

```
job-search-templates/
├── generate_cover_letter.py         # Cover Letter generator
├── generate_cv.py                   # CV/Resume generator
├── generate_thank_you_letter.py     # Thank You Letter (after interview)
├── generate_recruiter_email.py      # Recruiter/HR email template
├── generate_salary_negotiation.py   # Salary negotiation letter
├── generate_rejection_response.py   # Decline job offer template
├── generate_recommendation_request.py # Request recommendations
├── requirements.txt                 # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## Configuration

### Cover Letter Setup

Edit the following variables in `generate_cover_letter.py`:

```python
NAME    = "Your Name"
CITY    = "Your City"
PHONE   = "+1 234 567 8900"
EMAIL   = "your.email@example.com"
LINKS   = f'{format_url_link("LinkedIn", "linkedin.com/in/yourprofile")} · {format_url_link("Portfolio", "yourportfolio.com")}'
```

Edit the `BODY` variable to customize your cover letter text.

### CV/Resume Setup

Edit the `DATA` dictionary in `generate_cv.py`:

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

For better cross-platform support and special characters:

1. Create a `fonts/` directory in the project root
2. Add font files:
   - `DejaVuSans.ttf`
   - `DejaVuSans-Bold.ttf`
3. Download from [DejaVu Fonts](https://dejavu-fonts.github.io/)

If fonts are not specified, system default fonts will be used.

### Output File Names

Default output files:
- Cover Letter: `Cover_Letter.pdf`
- CV: `CV_Resume.pdf`

You can change these in the `build_pdf()` function in each script.

### Adding Date to Cover Letter

Uncomment the date line in `generate_cover_letter.py`:

```python
Paragraph(nz(TODAY), s["date"]),
```

## Customizing for Specific Companies

### Cover Letter

Create a separate version for each company:

1. Copy `generate_cover_letter.py` with a new name (e.g., `cover_letter_company_name.py`)
2. Edit:
   - Greeting (Hi, Hello [Company Name]!, etc.)
   - `BODY` content for the specific company and role
   - Output filename in `build_pdf()`

### CV

Typically one CV works for all positions, but you can:
- Adjust `summary` for specific industries
- Add/remove sections (e.g., projects, publications)
- Change the filename

## CV Structure

Standard sections:
- **Summary** - Brief description (1-2 sentences)
- **AI & Product Impact** - Key achievements and results
- **Core Skills** - List of skills
- **Experience** - Work experience with descriptions
- **Education** - Educational background

You can modify section names, add new sections, or remove unnecessary ones in the `main()` function of `generate_cv.py`.

## Available Templates

### 1. Cover Letter (`generate_cover_letter.py`)
Standard cover letter template for job applications. Customize greeting and body text for each company.

### 2. CV/Resume (`generate_cv.py`)
Professional resume with standard sections: Summary, Impact, Skills, Experience, and Education.

### 3. Thank You Letter (`generate_thank_you_letter.py`)
Follow-up email after an interview. Includes gratitude, reminder of key points discussed, and enthusiasm for the role.

### 4. Recruiter Email (`generate_recruiter_email.py`)
Initial contact email to recruiters or HR. Use for cold outreach or when exploring opportunities at a company.

### 5. Salary Negotiation (`generate_salary_negotiation.py`)
Professional letter to negotiate salary/compensation package. Includes reasoning and value proposition.

### 6. Rejection Response (`generate_rejection_response.py`)
Polite decline of a job offer. Maintains professional relationship for future opportunities.

### 7. Recommendation Request (`generate_recommendation_request.py`)
Request recommendations from former colleagues or managers. Useful for LinkedIn recommendations or references.

## Requirements

- Python 3.6+
- reportlab (install via `pip install -r requirements.txt`)

## Troubleshooting

If you encounter issues:

1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Verify data in scripts is correct (no syntax errors)
3. Check font paths format if using custom fonts

## Contributing

Feel free to fork, modify, and use these templates for your job search needs.

## License

Free to use and modify for your personal use.

## Author

Created for simplifying the job search process. Feel free to customize to your needs!
