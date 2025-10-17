# services/report_generator.py
import os
import json
from datetime import datetime
from jinja2 import Template

def generate_report(data, recommendations):
    """
    Generate an HTML report based on assessment data and recommendations
    
    :param data: Dictionary containing form data
    :param recommendations: List of recommendations
    :return: Path to generated report file
    """
    try:
        # Load template
        template_path = os.path.join('templates', 'report_template.html')
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        template = Template(template_content)
        
        # Prepare data for template
        report_data = {
            'assessment_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data': data,
            'recommendations': recommendations,
            'total_recommendations': len(recommendations)
        }
        
        # Generate report
        html_content = template.render(**report_data)
        
        # Save report
        os.makedirs('reports', exist_ok=True)
        report_filename = f"energy_assessment_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        report_path = os.path.join('reports', report_filename)
        
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        return report_path
        
    except Exception as e:
        print(f"Error generating report: {e}")
        return None

def generate_pdf_report(data, recommendations):
    """
    Generate a PDF report (future enhancement)
    
    :param data: Dictionary containing form data
    :param recommendations: List of recommendations
    :return: Path to generated PDF report
    """
    # TODO: Implement PDF generation using reportlab
    pass
