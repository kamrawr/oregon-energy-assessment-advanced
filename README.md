# Dynamic Energy Assessment Tool

## Overview

This repository contains a dynamic tool for conducting home energy assessments, providing recommendations based on user inputs. The 
application is designed to be highly modular and configurable, with JSON-driven forms that allow easy updates and expansion of assessments.

## Project Structure

```plaintext
dynamic-energy-assessment-tool/
├── main.py                  # Main entry point of the application.
├── forms/
│   ├── form_manager.py      # Logic to dynamically generate forms from JSON.
│   └── assessment_modules/  # Separate files for each assessment type.
│       ├── insulation.py    # Module for insulation-related assessments.
│       ├── hvac.py          # Module for HVAC-related assessments.
├── assessments/
│   ├── energy_assessment.json  # Configuration for energy assessment form.
│   ├── hvac_assessment.json    # Configuration for HVAC assessment form.
├── services/
│   ├── report_generator.py  # Utility to generate HTML or PDF reports.
│   └── github_connector.py  # Logic to connect to GitHub and pull configuration files.
├── templates/               # HTML templates for reports.
│   ├── report_template.html # Template for generating reports.
└── README.md                # Documentation on how to use the repository.
```

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/username/dynamic-energy-assessment-tool.git
   cd dynamic-energy-assessment-tool
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```sh
   python main.py
   ```

## Usage

- The tool dynamically generates forms based on JSON configurations located in the `assessments/` folder.
- You can add new forms or modify existing ones by updating the JSON files.

## Modules Overview

### Main Application (`main.py`)
- The main entry point that loads configuration and triggers the form generation.

### Form Management (`forms/form_manager.py`)
- Dynamically generates forms using Tkinter based on the JSON configuration.
- Handles user inputs and manages the submission process.

### Assessment Modules (`forms/assessment_modules/`)
- Separate modules for processing different parts of the assessment.
- **insulation.py**: Processes insulation data and provides related recommendations.
- **hvac.py**: Processes HVAC-related information and provides recommendations.

### Assessment Configurations (`assessments/`)
- JSON files defining the form structure, including labels, field types, and options.
- **energy_assessment.json**: Configuration for the overall energy assessment.
- **hvac_assessment.json**: Configuration for HVAC-specific assessment.

### Report Generator (`services/report_generator.py`)
- Generates HTML reports based on the data and recommendations collected.
- Saves the report to a file (`energy_assessment_report.html`).

### GitHub Connector (`services/github_connector.py`)
- Loads the form configuration from a remote GitHub repository.

### Report Template (`templates/report_template.html`)
- HTML template used to format the report.

## Adding a New Assessment
1. Create a new JSON file in the `assessments/` directory with the form structure.
2. Add a new module in `forms/assessment_modules/` to process the data from the new assessment.
3. Update `main.py` to include your new configuration if needed.

## License

This project is licensed under the MIT License.
