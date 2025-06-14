def perform_swot_analysis(student_profile):
    """
    Perform a basic SWOT analysis based on student profile.
    Returns a dictionary with strengths, weaknesses, opportunities, threats.
    """
    swot = {
        'strengths': [],
        'weaknesses': [],
        'opportunities': [],
        'threats': []
    }
    
    # Extract profile data
    strengths = student_profile['strengths']
    interests = student_profile['interests']
    gpa = student_profile['gpa']
    test_scores = student_profile['test_scores']
    extracurriculars = student_profile['extracurriculars']
    
    # Analyze strengths
    for strength in strengths:
        strength_lower = strength.lower()
        if any(word in strength_lower for word in ['math', 'quantitative', 'analytical']):
            swot['strengths'].append("Strong quantitative skills")
        elif any(word in strength_lower for word in ['communicat', 'write', 'speak']):
            swot['strengths'].append("Strong communication skills")
        elif any(word in strength_lower for word in ['research', 'publish', 'experiment']):
            swot['strengths'].append("Research experience")
        elif any(word in strength_lower for word in ['leader', 'team', 'organiz']):
            swot['strengths'].append("Leadership skills")
        else:
            swot['strengths'].append(strength.capitalize())
    
    # Analyze weaknesses
    if gpa:
        if float(gpa) < 3.0:
            swot['weaknesses'].append("GPA below competitive threshold")
    else:
        swot['weaknesses'].append("GPA not provided - may limit options")
    
    if not test_scores:
        swot['weaknesses'].append("Standardized test scores not provided")
    
    if not any('math' in s.lower() for s in strengths) and \
       any(i.lower() in ['computer science', 'engineering', 'physics', 'math'] for i in interests):
        swot['weaknesses'].append("Math skills not highlighted for technical field interest")
    
    # Analyze opportunities
    if extracurriculars:
        swot['opportunities'].append("Strong extracurricular profile")
    
    if any(s.lower() in ['research', 'publication', 'internship'] for s in strengths):
        swot['opportunities'].append("Relevant experience for competitive programs")
    
    # Analyze threats (simplified for prototype)
    if not extracurriculars and float(gpa or 0) < 3.5:
        swot['threats'].append("Profile may not stand out at highly selective schools")
    
    return swot