# forms/assessment_modules/windows.py

def process_windows_assessment(data):
    """
    Processes windows-related information from the form data and generates recommendations.
    
    :param data: Dictionary containing form data
    :return: List of recommendations related to windows
    """
    recommendations = []
    
    if data.get('window_type') == 'single_pane':
        recommendations.append("Single-pane windows lose significant energy. Consider upgrading to double or triple-pane windows.")
    elif data.get('window_type') == 'double_pane_old':
        recommendations.append("Older double-pane windows may benefit from storm windows or replacement with modern efficient units.")
    
    if data.get('window_sealing') == 'poor':
        recommendations.append("Poor window sealing allows air leaks. Consider caulking and weather stripping around windows.")
    
    if data.get('window_coverings') == 'none':
        recommendations.append("Window coverings like blinds or curtains can help regulate temperature and reduce energy loss.")
        
    return recommendations