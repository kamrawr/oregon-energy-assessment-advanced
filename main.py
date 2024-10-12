# main.py
from forms.form_manager import generate_form
from services.github_connector import load_form_config

# Entry point of the application
def main():
    config_url = "https://raw.githubusercontent.com/username/dynamic-energy-assessment-tool/main/assessments/energy_assessment.json"
    form_config = load_form_config(config_url)
    generate_form(form_config)

if __name__ == "__main__":
    main()
