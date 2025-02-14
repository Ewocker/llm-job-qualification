import streamlit as st
import os
import requests
import io
from openai import OpenAI
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
openai = OpenAI()

# Constants
SYSTEM_PROMPT = """You are an AI assistant designed to evaluate an applicant's resume against a given job posting to determine their fit for the role. Your response should:
1. Provide a structured analysis
   - List 3 reasons why the applicant is a good fit for the job.
   - List 3 reasons why the applicant may not be a good fit for the job.
2. Ignore irrelevant content
   - Exclude navigation-related or non-informative text from both the job posting and the resume.
3. Score the applicant's fit
   - Assign a fit score between 0 and 100, where:
     - 100 = Perfect fit
     - 0 = No match
   - The score should be based on skills, experience, and qualifications relative to the job description.
   - Consider years of experience as a factor but not as a strict requirement.
   - Be very strict about if applicants have the required skills or relevant experience.
   - A score of 40 or below indicates a poor fit.
   - A score of 60 or above indicates a acceptable fit.
   - A score of 80 or above indicates a strong fit.
4. Provide Resume Improvement Suggestions
   - Offer 3 specific and actionable suggestions to improve the applicant's resume.
5. Format the response in Markdown"""

class JSWebsite:
    def __init__(self, url):
        self.url = url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup([["script", "style", "img", "input", "nav", "footer", "header"]]):
            irrelevant.decompose()
        self.text = soup.get_text(separator="\n", strip=True)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text, job_post_url):
    try:
        job_post = JSWebsite(job_post_url)
        user_prompt = f"Given the applicant profile and job post;\n"
        user_prompt += f"Job Post: {job_post.text}\n"
        user_prompt += f"Resume: {resume_text}\n"
        
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
        
        # Create a placeholder for the streaming output
        analysis_placeholder = st.empty()
        full_response = ""
        
        # Stream the response
        stream = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                # Update the placeholder with the accumulated response
                analysis_placeholder.markdown(full_response + "▌")
        
        # Final update without the cursor
        analysis_placeholder.markdown(full_response)
        return full_response
    except Exception as e:
        return f"Error analyzing resume: {str(e)}"

def main():
    st.title("Resume Job Fit Analyzer")
    st.write("Upload your resume and enter a job posting URL to analyze your fit for the position.")
    
    # Job posting URL input
    job_url = st.text_input("Job Posting URL", 
                           placeholder="Enter the job posting URL here...")
    
    # Resume file upload
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    
    # Single analyze button with conditions
    if st.button("Analyze", key="analyze_button"):
        if not uploaded_file or not job_url:
            if not uploaded_file:
                st.warning("Please upload your resume.")
            if not job_url:
                st.warning("Please enter a job posting URL.")
        else:
            with st.spinner("Analyzing your resume..."):
                try:
                    # Extract text from PDF
                    resume_text = extract_text_from_pdf(uploaded_file)
                    
                    # Get analysis with streaming
                    analyze_resume(resume_text, job_url)
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 