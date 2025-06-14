# AI College Admissions Assistant

An interactive command-line tool that helps students explore and match with college programs based on their academic interests, strengths, and preferences. The assistant performs a SWOT analysis and generates personalized admissions advice using a large language model (LLM).

## Features
- **Interactive CLI**: Collects student profile information via prompts.
- **SWOT Analysis**: Analyzes strengths, weaknesses, opportunities, and threats based on the profile.
- **Program Matching**: Recommends top programs from a dataset using a scoring algorithm.
- **LLM-Powered Advice**: Generates detailed, personalized application advice using an LLM API.

## Installation
1. **Clone the repository**
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv yahvenv
   source yahvenv/bin/activate  # On Windows: yahvenv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script from the `test1` directory:
```bash
python main.py
```
You will be prompted to enter:
- Academic interests (required)
- Personal strengths (required)
- Preferences (optional)
- Standardized test scores (optional)
- Current GPA (optional)
- Extracurricular activities (optional)

### Example Input
```
Academic interests: Computer Science, Artificial Intelligence
Personal strengths: programming, math, research experience
Preferences: Urban campus with strong AI research
Standardized test scores: SAT 1480
Current GPA: 3.8
Extracurricular activities: robotics team president, AI research internship
```

## Configuration
- **API Keys**: The app uses environment variables for LLM API access. Create a `.env` file in the root directory with the following (replace with your keys):
  ```env
  OPENROUTER_API_KEY=your_openrouter_api_key
  # GROQ_API_KEY=your_groq_api_key (if using Groq)
  ```

## Data
- **Program Data**: The program matcher uses a JSON file at `test1/modules/data/programs.json`.
- **Sample Format:**
```json
[
  {
    "name": "Computer Science",
    "university": "Tech Institute",
    "description": "Comprehensive program covering algorithms, systems, and AI with strong industry connections.",
    "location": "Urban",
    "keywords": ["programming", "algorithms", "software engineering", "AI"],
    "requirements": "Strong math background, programming experience preferred",
    "min_gpa": 3.2
  },
  ...
]
```

## File Structure
- `test1/main.py` — Main entry point
- `test1/modules/input_handler.py` — Handles user input
- `test1/modules/swot_analyzer.py` — Performs SWOT analysis
- `test1/modules/program_matcher.py` — Loads and matches programs
- `test1/modules/llm_adviser.py` — Generates LLM-based advice
- `test1/modules/data/programs.json` — Sample program data
- `requirements.txt` — Python dependencies

## License
MIT License (or specify your license here) 