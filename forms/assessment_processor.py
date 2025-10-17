# forms/assessment_processor.py
"""
Processing logic for energy assessments, replacing the tkinter form manager
"""

from forms.assessment_modules import insulation, hvac, crawlspace, ductwork, windows, doors

def process_assessment(data):
    """
    Process assessment data and generate recommendations
    
    :param data: Dictionary containing form data
    :return: List of recommendations
    """
    recommendations = []
    
    try:
        # Run specific assessment modules
        recommendations.extend(insulation.process_insulation_assessment(data))
        recommendations.extend(hvac.process_hvac_assessment(data))
        recommendations.extend(crawlspace.process_crawlspace_assessment(data))
        recommendations.extend(ductwork.process_ductwork_assessment(data))
        recommendations.extend(windows.process_windows_assessment(data))
        recommendations.extend(doors.process_doors_assessment(data))
        
        # Add general recommendations based on overall assessment
        recommendations.extend(generate_general_recommendations(data))
        
    except Exception as e:
        recommendations.append(f"Error processing assessment: {str(e)}")
    
    # Remove duplicates and return
    return list(set(recommendations)) if recommendations else ["Your home appears to be in good shape!"]

def generate_general_recommendations(data):
    """
    Generate general energy efficiency recommendations
    
    :param data: Dictionary containing form data
    :return: List of general recommendations
    """
    recommendations = []
    
    # Count the number of issues
    issues_found = 0
    
    # Check for multiple poor conditions
    poor_conditions = [
        data.get('attic_insulation') in ['none', 'poor'],
        data.get('wall_insulation') == 'none',
        data.get('crawlspace_insulation') in ['none', 'poor'],
        data.get('window_type') == 'single_pane',
        data.get('door_sealing') == 'poor',
        data.get('ductwork_condition') == 'poor'
    ]
    
    issues_found = sum(poor_conditions)
    
    if issues_found >= 3:
        recommendations.append("Your home has multiple energy efficiency issues. Consider a comprehensive energy audit for prioritized improvements.")
    
    # Add seasonal recommendations
    recommendations.append("Consider programmable thermostats to optimize heating and cooling schedules.")
    recommendations.append("Regular maintenance of HVAC systems improves efficiency and extends equipment life.")
    
    return recommendations