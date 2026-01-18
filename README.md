# Job Search Templates

Python templates for generating professional PDF Cover Letters and CV/Resume for job applications.

## Features

- 📄 **Cover Letter Generator** - Create customizable cover letters in PDF format
- 📋 **CV/Resume Generator** - Generate professional resumes with standard sections
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

1. Edit `generate_cover_letter.py` and `generate_cv.py` with your information
2. Run the scripts:
```bash
python generate_cover_letter.py
python generate_cv.py
```

PDF files will be generated in the same directory.

## Project Structure

```
job-search-templates/
├── generate_cover_letter.py  # Cover Letter generator script
├── generate_cv.py            # CV/Resume generator script
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
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
