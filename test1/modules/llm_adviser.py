import os
import requests
from dotenv import load_dotenv

load_dotenv()

def llm_advice(student_profile, swot_analysis, recommended_programs):
    """
    Generate personalized advice using OpenRouter's LLM API.
    """
    # Prepare program descriptions for the prompt
    program_descriptions = "\n".join(
        f"{idx+1}. {prog['name']} at {prog['university']}\n"
        f"   Location: {prog['location']}\n"
        f"   Description: {prog['description']}\n"
        f"   Key Features: {', '.join(prog['keywords'])}\n"
        for idx, prog in enumerate(recommended_programs)
    )
    
    # Construct the prompt
    prompt = f"""
    You are an experienced college admissions counselor. Provide detailed, personalized advice 
    for a student based on their profile and recommended programs.

    Student Profile:
    - Academic Interests: {', '.join(student_profile['interests'])}
    - Strengths: {', '.join(student_profile['strengths'])}
    - Extracurriculars: {', '.join(student_profile['extracurriculars']) if student_profile['extracurriculars'] else 'None listed'}
    - GPA: {student_profile['gpa'] or 'Not provided'}
    - Test Scores: {student_profile['test_scores'] or 'Not provided'}
    - Preferences: {student_profile['preferences'] or 'None specified'}

    SWOT Analysis:
    - Strengths: {', '.join(swot_analysis['strengths'])}
    - Weaknesses: {', '.join(swot_analysis['weaknesses'])}
    - Opportunities: {', '.join(swot_analysis['opportunities'])}
    - Threats: {', '.join(swot_analysis['threats'])}

    Recommended Programs:
    {program_descriptions}

    Provide:
    1. A brief analysis of how the student's profile aligns with each recommended program
    2. Specific advice on how to strengthen their application for these programs
    3. Suggestions for highlighting their strengths in application materials
    4. Any potential weaknesses to address
    5. Additional recommendations based on their profile
    """
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
                "HTTP-Referer": "YOUR_SITE_URL",  # Optional but recommended
                "X-Title": "College Counselor"     # Optional but recommended
            },
            json={
                "model": "mistralai/mistral-7b-instruct:free",  # Free model
                # "model": "anthropic/claude-3-opus",  # Paid model (better quality)
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 2000
            }
        )
        
        # Check for API errors
        if response.status_code != 200:
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            return f"API Error: {error_msg}"
        
        return response.json()['choices'][0]['message']['content']
    
    except Exception as e:
        return f"Could not generate LLM advice. Error: {str(e)}"