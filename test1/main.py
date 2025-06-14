#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from pyfiglet import Figlet
from termcolor import colored
from modules.input_handler import get_student_input
from modules.swot_analyzer import perform_swot_analysis
from modules.program_matcher import load_programs, match_programs
from modules.llm_adviser import llm_advice as generate_llm_advice

def display_banner():
    """Display the application banner"""
    f = Figlet(font='slant')
    print(colored(f.renderText('AI  Counselor'), 'cyan'))
    print(colored("College Admissions Assistant\n", 'blue'))

def main():
    try:
        load_dotenv()
        display_banner()
        
        # Step 1: Get student input
        student_profile = get_student_input()
        
        # Step 2: Perform SWOT analysis
        swot_analysis = perform_swot_analysis(student_profile)
        
        # Step 3: Load and match programs
        programs = load_programs()
        recommended_programs = match_programs(student_profile, programs)
        
        if not recommended_programs:
            print(colored("\nNo matching programs found based on your profile.", 'yellow'))
            return
        
        # Step 4: Generate LLM advice
        advice = generate_llm_advice(student_profile, swot_analysis, recommended_programs)
        
        # Display results
        print(colored("\n=== ADMISSIONS RECOMMENDATIONS ===", 'green', attrs=['bold']))
        print(advice)
        
    except Exception as e:
        print(colored(f"\nAn error occurred: {str(e)}", 'red'))

if __name__ == "__main__":
    main()