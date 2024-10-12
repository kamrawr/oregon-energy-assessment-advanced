# forms/assessment_modules/insulation.py

def process_insulation_assessment(data):
    recommendations = []
    if data.get('attic_insulation') == 'poor':
        recommendations.append("Consider adding or upgrading attic insulation to reduce heat loss.")
    elif data.get('attic_insulation') == 'fair':
        recommendations.append("Upgrading attic insulation could improve energy efficiency.")

    if data.get('wall_insulation') == 'none':
        recommendations.append("Installing wall insulation will significantly improve your home's energy efficiency.")
    return recommendations


