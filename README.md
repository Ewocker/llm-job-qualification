# Resume Job Fit Analyzer

A Streamlit web application that analyzes resumes against job postings using AI to provide personalized insights and recommendations.

## Features

- **Resume Analysis**: Upload your resume in PDF format to get detailed feedback
- **Job Posting Analysis**: Enter a job posting URL to analyze requirements
- **AI-Powered Matching**: Uses OpenAI's GPT models to compare resume with job requirements
- **Real-time Analysis**: Streaming response shows analysis as it's being generated
- **Detailed Insights**:
  - Fit Score (0-100)
  - Strengths Analysis
  - Gap Analysis
  - Resume Improvement Suggestions

## Live Demo

Access the application at: [Streamlit Cloud URL]

## Local Development Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd resume-job-fit-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

The application will be available at http://localhost:8501

## Usage

1. Enter a job posting URL in the text input field
2. Upload your resume in PDF format
3. Click "Analyze" to get insights
4. Review the analysis which includes:
   - Overall fit score
   - Key strengths matching the job requirements
   - Potential gaps or areas for improvement
   - Specific suggestions to enhance your resume

## Technologies Used

- **Streamlit**: Web application framework
- **OpenAI API**: AI-powered analysis
- **PyPDF2**: PDF text extraction
- **BeautifulSoup4**: Web scraping for job postings
- **Selenium**: JavaScript-enabled web scraping

## Deployment

This application is deployed on Streamlit Cloud. To deploy your own instance:

1. Fork this repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Create a new app pointing to your fork
4. Add your OpenAI API key in Streamlit Cloud's secrets management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.