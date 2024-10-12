# services/report_generator.py

def generate_html_report(report_content):
    """
    Generates an HTML report from the given report content.
    
    :param report_content: Dictionary containing form data and recommendations
    """
    html_content = f"""
    <html>
    <head>
        <title>Energy Assessment Report</title>
    </head>
    <body>
        <h1>Energy Assessment Report for {report_content['data'].get('address')}</h1>
        <h2>General Information</h2>
        <p>Date: {report_content['data'].get('sited_date')}</p>
        <h2>Recommendations</h2>
        <ul>
    """
    for recommendation in report_content['recommendations']:
        html_content += f"<li>{recommendation}</li>\n"

    html_content += """
        </ul>
    </body>
    </html>
    """
    with open('energy_assessment_report.html', 'w') as report_file:
        report_file.write(html_content)
    print("Report generated and saved as 'energy_assessment_report.html'")
