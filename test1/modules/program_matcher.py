import json
from pathlib import Path

def load_programs():
    """Load program data from JSON file"""
    data_path = Path(__file__).parent / 'data' / 'programs.json'
    with open(data_path, 'r') as f:
        return json.load(f)

def match_programs(student_profile, programs):
    """
    Match programs based on student interests and strengths.
    Returns a list of matched programs with relevance scores.
    """
    matched = []
    interests = [i.lower() for i in student_profile['interests']]
    strengths = [s.lower() for s in student_profile['strengths']]
    preferences = student_profile['preferences'].lower() if student_profile['preferences'] else None
    
    for program in programs:
        score = 0
        
        # Check program fields for interest matches
        program_text = (
            program['name'] + ' ' + 
            program['description'] + ' ' + 
            ' '.join(program['keywords'])
        ).lower()
        
        for interest in interests:
            if interest in program_text:
                score += 2
        
        # Check requirements for strength matches
        requirements = program['requirements'].lower()
        for strength in strengths:
            if strength in requirements:
                score += 1.5
        
        # Check extracurricular alignment
        if student_profile['extracurriculars']:
            for activity in student_profile['extracurriculars']:
                if activity.lower() in program_text:
                    score += 0.5
        
        # Check location preference
        if preferences and preferences in program['location'].lower():
            score += 1
        
        # GPA filter (if provided)
        if student_profile['gpa']:
            min_gpa = program.get('min_gpa', 0)
            if float(student_profile['gpa']) >= min_gpa:
                score += 1
            else:
                continue  # Skip programs where GPA is below minimum
        
        if score > 0:
            matched.append((program, score))
    
    # Sort by match score
    matched.sort(key=lambda x: x[1], reverse=True)
    
    return [m[0] for m in matched[:5]]  # Return top 5 matches