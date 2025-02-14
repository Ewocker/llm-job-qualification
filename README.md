# LLM Job Assistant

The LLM Job Assistant is a Python application that leverages local Large Language Models (LLMs) through Ollama to help streamline your job application process. It analyzes job descriptions and your resume to provide personalized insights and recommendations.

## Features

- **Resume Analysis**: Upload your resume to get detailed feedback and suggestions for improvement
- **Job Description Analysis**: Input job listings to extract key requirements and responsibilities
- **Skills Gap Analysis**: Compare your resume against job requirements to identify missing skills
- **Customized Application Tips**: Receive tailored advice on how to position yourself for specific roles

## Getting Started

### Prerequisites
- Python 3.8+
- Ollama installed and running locally
- Required Python packages (see requirements.txt)

### Installation
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run Ollama locally
4. Launch the application: `python main.py`

## Usage

1. Upload your resume in PDF format
2. Paste the job description or provide the job listing URL
3. Get instant analysis and recommendations

## Future Enhancements

- Web-based user interface for easier interaction
- Support for multiple resume formats
- Integration with job boards for direct listing access
- Enhanced resume improvement suggestions
- Automated cover letter generation

# React + Flask Project

This project consists of a React frontend and Flask backend.

## Setup Instructions

1. Install dependencies:
   ```bash
   # Create and activate conda environment
   conda env create -f environment.yml
   conda activate llm-job-qualification

   # Install frontend dependencies
   cd frontend
   npm install
   ```

2. Build the frontend:
   ```bash
   cd frontend
   npm run build
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Run the application:
   ```bash
   python app.py
   ```

The application will be available at http://localhost:5000

Would you like me to explain any part of the setup in more detail?