# forms/assessment_modules/doors.py

def process_doors_assessment(data):
    """
    Processes doors-related information from the form data and generates recommendations.
    
    :param data: Dictionary containing form data
    :return: List of recommendations related to doors
    """
    recommendations = []
    
    if data.get('door_type') == 'hollow_core':
        recommendations.append("Hollow core doors provide poor insulation. Consider upgrading to solid core or insulated doors.")
    
    if data.get('door_sealing') == 'poor':
        recommendations.append("Poor door sealing allows air leaks. Install weather stripping and door sweeps.")
    
    if data.get('storm_doors') == 'none':
        recommendations.append("Storm doors can significantly improve energy efficiency, especially for older exterior doors.")
        
    if data.get('door_condition') == 'poor':
        recommendations.append("Doors in poor condition should be repaired or replaced to maintain energy efficiency.")
        
    return recommendations