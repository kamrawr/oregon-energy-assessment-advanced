# forms/assessment_modules/ductwork.py

def process_ductwork_assessment(data):
    """
    Processes ductwork-related information from the form data and generates recommendations.
    
    :param data: Dictionary containing form data
    :return: List of recommendations related to ductwork
    """
    recommendations = []
    
    if data.get('ductwork_condition') == 'poor':
        recommendations.append("Your ductwork is in poor condition. Consider sealing and insulating ducts to improve efficiency.")
    elif data.get('ductwork_condition') == 'fair':
        recommendations.append("Sealing ductwork gaps could improve your HVAC system's efficiency.")
    
    if data.get('ductwork_location') == 'unconditioned_space':
        recommendations.append("Ducts in unconditioned spaces lose significant energy. Consider moving or insulating them.")
        
    return recommendations