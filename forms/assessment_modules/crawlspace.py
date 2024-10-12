# forms/assessment_modules/crawlspace.py

def process_crawlspace_assessment(data):
    """
    Processes crawlspace insulation-related information from the form data and generates recommendations.
    
    :param data: Dictionary containing form data
    :return: List of recommendations related to crawlspace insulation
    """
    recommendations = []
    if data.get('crawlspace_insulation') == 'none':
        recommendations.append("Consider adding insulation to your crawlspace to improve energy efficiency and reduce heat loss.")
    elif data.get('crawlspace_insulation') == 'poor':
        recommendations.append("Upgrading crawlspace insulation could significantly improve your home's energy efficiency.")
    return recommendations
