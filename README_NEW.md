# 🏠 Dynamic Energy Assessment Tool

A comprehensive web-based tool for conducting home energy assessments and generating personalized energy efficiency recommendations.

## ✨ Features

- 🌐 **Web-Based Interface** - Modern, responsive design that works on desktop and mobile
- 📊 **Comprehensive Assessment** - Evaluates insulation, HVAC, windows, doors, and ductwork
- 🎯 **Smart Recommendations** - AI-powered suggestions based on your home's specific conditions
- 📄 **Professional Reports** - Generate beautiful HTML reports with actionable insights
- ⚡ **Real-Time Processing** - Instant analysis and recommendations
- 🔧 **Modular Architecture** - Easy to extend with new assessment modules

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kamrawr/dynamic-energy-assessment-tool.git
   cd dynamic-energy-assessment-tool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** to: http://localhost:8080

## 🎯 How to Use

1. **Fill out the assessment form** with details about your home's current conditions
2. **Submit the form** to get instant analysis
3. **Review personalized recommendations** tailored to your home
4. **Download a comprehensive report** with detailed next steps

## 🏗️ Architecture

### Project Structure

```
dynamic-energy-assessment-tool/
├── app.py                          # Flask web application (main entry)
├── main.py                         # Legacy entry point with instructions
├── requirements.txt                # Python dependencies
├── assessments/
│   ├── energy_assessment.json      # Form configuration
│   └── hvac_assessment.json        # HVAC-specific configuration
├── forms/
│   ├── assessment_processor.py     # Main assessment logic
│   ├── form_manager.py            # Legacy tkinter form (deprecated)
│   └── assessment_modules/         # Individual assessment modules
│       ├── insulation.py          # Insulation analysis
│       ├── hvac.py                 # HVAC system analysis
│       ├── crawlspace.py           # Crawlspace assessment
│       ├── ductwork.py             # Ductwork evaluation
│       ├── windows.py              # Window efficiency check
│       └── doors.py                # Door sealing assessment
├── services/
│   ├── github_connector.py        # Configuration loading from GitHub
│   └── report_generator.py        # HTML report generation
├── templates/
│   ├── assessment_form.html        # Main web interface
│   └── report_template.html        # Report template
└── reports/                        # Generated reports (created at runtime)
```

### Key Components

- **Web Interface** (`app.py`): Flask-based web application with modern UI
- **Assessment Engine** (`forms/assessment_processor.py`): Core logic for analyzing home conditions
- **Assessment Modules** (`forms/assessment_modules/`): Specialized analysis for different home systems
- **Report Generator** (`services/report_generator.py`): Creates beautiful, downloadable reports
- **Configuration System** (`assessments/`): JSON-driven form definitions for easy customization

## 🔧 Customization

### Adding New Assessment Categories

1. Create a new module in `forms/assessment_modules/`:
   ```python
   # forms/assessment_modules/your_module.py
   def process_your_assessment(data):
       recommendations = []
       # Your assessment logic here
       return recommendations
   ```

2. Update `forms/assessment_processor.py` to include your module:
   ```python
   from forms.assessment_modules import your_module
   # Add to process_assessment function
   recommendations.extend(your_module.process_your_assessment(data))
   ```

3. Add corresponding fields to `assessments/energy_assessment.json`

### Modifying the Web Interface

- Edit `templates/assessment_form.html` for form changes
- Update `templates/report_template.html` for report styling
- Modify CSS in the template files for visual customization

## 💻 Development

### Running in Development Mode

```bash
export FLASK_ENV=development
python app.py
```

### Testing

The application includes comprehensive error handling and validation. Test by:

1. Running the app locally
2. Filling out forms with various data combinations
3. Checking generated reports in the `reports/` directory

## 🔄 Recent Improvements

### Version 2.0 Features

✅ **Web-Based Interface** - Replaced tkinter with modern Flask web app
✅ **Missing Modules** - Added ductwork, windows, and doors assessment modules
✅ **Enhanced Styling** - Professional, mobile-responsive design
✅ **Better Error Handling** - Comprehensive error management and user feedback
✅ **Improved Reports** - Beautiful HTML reports with modern styling
✅ **Smart Recommendations** - Enhanced logic for generating targeted suggestions
✅ **Easy Deployment** - Simple setup with requirements.txt and clear instructions

### Bug Fixes

- ❌ Fixed tkinter dependency issues
- ❌ Resolved missing assessment modules (ductwork, windows, doors)
- ❌ Corrected GitHub URL references
- ❌ Added proper error handling for network requests
- ❌ Fixed report generation and styling issues

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter issues:

1. Check the console output for error messages
2. Ensure all dependencies are properly installed
3. Verify Python version compatibility (3.8+)
4. Create an issue on GitHub with details about your problem

## 🎉 What's Next?

- 📱 Mobile app version
- 🔌 Integration with smart home devices
- 📈 Energy usage tracking and analytics
- 🌍 Integration with local utility rebate programs
- 🔐 User accounts and assessment history
- 📊 Advanced analytics and benchmarking

---

**Built with ❤️ for energy efficiency and sustainability**