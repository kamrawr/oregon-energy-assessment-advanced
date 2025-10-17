#!/usr/bin/env python3
"""
Flask Web Application for Dynamic Energy Assessment Tool
"""

import os
from flask import Flask, render_template, request, jsonify, send_file
from services.github_connector import load_form_config
from services.report_generator import generate_report
from forms.assessment_processor import process_assessment

app = Flask(__name__, template_folder='templates')

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def index():
    """Main page with energy assessment form"""
    # Load form configuration (try local first, then remote)
    config = load_local_config() or load_remote_config()
    if not config:
        return "Error: Could not load form configuration", 500
    
    return render_template('assessment_form.html', config=config)

@app.route('/submit_assessment', methods=['POST'])
def submit_assessment():
    """Process submitted assessment form"""
    try:
        data = request.get_json()
        recommendations = process_assessment(data)
        
        # Generate report
        report_path = generate_report(data, recommendations)
        
        return jsonify({
            'success': True,
            'recommendations': recommendations,
            'report_path': report_path
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/download_report')
def download_report():
    """Download the generated report"""
    report_path = request.args.get('path', 'reports/energy_assessment_report.html')
    if os.path.exists(report_path):
        return send_file(report_path, as_attachment=True)
    return "Report not found", 404

def load_local_config():
    """Load configuration from local JSON file"""
    try:
        import json
        config_path = os.path.join('assessments', 'energy_assessment.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading local config: {e}")
    return None

def load_remote_config():
    """Load configuration from GitHub"""
    config_url = "https://raw.githubusercontent.com/kamrawr/dynamic-energy-assessment-tool/main/assessments/energy_assessment.json"
    return load_form_config(config_url)

if __name__ == '__main__':
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=8080)
