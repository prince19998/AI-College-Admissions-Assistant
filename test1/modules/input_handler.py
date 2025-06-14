def get_student_input():
    """Collect and validate student information from command line input."""
    print("Please provide the following information (press Enter to skip optional fields):")
    
    # Collect required inputs
    while True:
        interests = input("Academic interests (comma-separated, e.g. 'Computer Science, AI'): ").strip()
        if interests:
            break
        print("Academic interests are required.")
    
    while True:
        strengths = input("Personal strengths (comma-separated, e.g. 'math, research'): ").strip()
        if strengths:
            break
        print("Personal strengths are required.")
    
    # Collect optional inputs
    preferences = input("Preferences (location, program type, etc.): ").strip()
    test_scores = input("Standardized test scores (if any): ").strip()
    gpa = input("Current GPA (if known): ").strip()
    extracurriculars = input("Extracurricular activities (comma-separated): ").strip()
    
    # Clean and process inputs
    interests = [i.strip() for i in interests.split(',') if i.strip()]
    strengths = [s.strip() for s in strengths.split(',') if s.strip()]
    extracurriculars = [e.strip() for e in extracurriculars.split(',')] if extracurriculars else []
    
    return {
        'interests': interests,
        'strengths': strengths,
        'preferences': preferences,
        'test_scores': test_scores,
        'gpa': gpa,
        'extracurriculars': extracurriculars
    }