# forms/assessment_modules/hvac.py

def process_hvac_assessment(data):
    """
    Processes HVAC-related information from the form data and generates recommendations.
    
    :param data: Dictionary containing form data
    :return: List of recommendations related to HVAC
    """
    recommendations = []
    if data.get('heating_system_age'):
        try:
            heating_system_age = int(data.get('heating_system_age').split('-')[-1].replace('+', ''))
            if heating_system_age > 15:
                recommendations.append("Your heating system is over 15 years old. Consider replacing it with an energy-efficient model.")
        except ValueError:
            recommendations.append("Heating system age information is incomplete.")

    if data.get('cooling_system_age'):
        try:
            cooling_system_age = int(data.get('cooling_system_age').split('-')[-1].replace('+', ''))
            if cooling_system_age > 15:
                recommendations.append("Your cooling system is over 15 years old. Replacing it with an efficient model could lower your 
energy bills.")
        except ValueError:
            recommendations.append("Cooling system age information is incomplete.")
    return recommendations
