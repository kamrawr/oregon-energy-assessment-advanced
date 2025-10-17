# 🏠 Oregon Energy Assessment Tool (Advanced Version)

**Advanced home energy assessment tool with detailed sizing calculations, dynamic form fields, and precise Energy Trust of Oregon incentive calculations.**

> 📋 **Need a simpler tool?** Check out our [**Standalone Assessment Tool**](https://github.com/kamrawr/dynamic-energy-assessment-tool) for basic assessments without sizing requirements.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

## ✨ Advanced Features

- 📏 **Detailed Sizing Inputs** - Square footage inputs for accurate calculations
- 📈 **Dynamic Form Fields** - Inputs appear/hide based on your responses
- 💵 **Precise Incentive Calculations** - Accurate Energy Trust of Oregon incentive amounts
- 📏 **HVAC Load Calculations** - Conditioned space sizing for heat pump requirements
- 📊 **Professional Reports** - Detailed cost analysis with net costs and payback periods
- 🏗️ **Comprehensive Assessment** - Housing type, foundation, envelope, HVAC, health & safety
- 🎯 **Smart Recommendations** - Heat pump suggestions with specific incentive amounts
- 📱 **Mobile Responsive** - Works on desktop, tablet, and mobile
- ⚡ **Real-time Updates** - Form adapts as you fill it out
- 🔧 **Multi-Select Options** - Choose multiple health & safety factors

## 🚀 Quick Start

### Option 1: Use Online (Recommended)
**[Open the Assessment Tool →](https://kamrawr.github.io/dynamic-energy-assessment-tool/standalone_assessment.html)**

### Option 2: Download and Use Locally
1. **Download**: Right-click [standalone_assessment.html](./standalone_assessment.html) → "Save As"
2. **Open**: Double-click the downloaded file to open in your web browser
3. **Assess**: Fill out the form and get instant recommendations

### Option 3: Clone Repository
```bash
git clone https://github.com/kamrawr/oregon-energy-assessment-advanced.git
cd oregon-energy-assessment-advanced
open standalone_assessment.html
```

## 🔬 What Makes This Advanced?

### 📏 Detailed Sizing Calculations
- **Home Square Footage** - Total home size for comprehensive analysis
- **Conditioned Space** - Specific area for HVAC load calculations
- **Attic Square Footage** - Precise insulation area calculations
- **Wall Square Footage** - Accurate wall insulation sizing
- **Heat Pump Units** - Number of units needed for proper heating/cooling

### 📈 Dynamic Form Intelligence
- Form fields appear based on your selections
- Attic sizing inputs show when attic insulation needs work
- Wall sizing inputs appear for poor/missing wall insulation
- Heat pump sizing appears for electric resistance heating or no cooling

### 💵 Precise Energy Trust Incentives
- **Attic Insulation**: $0.15 per square foot
- **Wall Insulation**: $0.10 per square foot  
- **Heat Pump Systems**: $500 per unit
- Real-time calculation of total available incentives
- Net cost analysis after incentives

## 🎯 How to Use

1. **📋 Fill Assessment Form**
   - Property basics (housing type, foundation, roof condition)
   - Envelope systems (insulation, windows, doors)
   - HVAC equipment (heating/cooling type and age)
   - Health & safety factors (select multiple if applicable)
   - Use "N/A" for unknown items—the tool will guide you!

2. **🔍 Analyze**
   - Click "Analyze" for instant results
   - View real-time KPIs (issues found, recommendations, form completeness)
   - See color-coded status overview

3. **📄 Get Report**
   - Review personalized recommendations
   - Download professional HTML report
   - Print or save as PDF

## 🏗️ Assessment Categories

### Property Basics
- Housing type (single-family, multi-family, townhome, manufactured, condo)
- Foundation type (slab, crawlspace, basement)
- Roof condition assessment
- Health & safety factors (multi-select)

### Building Envelope
- Attic insulation condition
- Wall insulation assessment
- Crawlspace/basement insulation
- Window types and efficiency
- Door sealing condition

### HVAC Systems
- Primary heating type and age
- Cooling system type and age
- Ductwork condition (including "no ducts" option)
- Smart heat pump recommendations

### Smart Logic Features
- **Heat Pump Recommendations**: Suggests heat pumps when adding cooling or replacing old systems
- **Ductless Options**: Recommends mini-splits when no ductwork exists
- **N/A Handling**: Provides targeted recommendations for missing information
- **Cross-System Analysis**: Considers heating + cooling combinations for optimal upgrades

## 📊 Report Features

### Visual Dashboard
- **Potential Issues** - Count of systems needing attention
- **Recommendations** - Number of actionable suggestions
- **Form Completeness** - Percentage of fields completed

### Status Overview
- **Envelope Status** - Color-coded assessment of insulation, windows, doors
- **Systems Status** - HVAC equipment condition and age
- **Health & Safety** - Multi-factor safety considerations

### Smart Badges
- 🔍 "Comprehensive Audit Recommended" - For homes with multiple issues
- ⚠️ "Health & Safety First" - When safety factors are present
- 💡 "Heat Pump Opportunity" - When heat pump upgrades make sense

## 🎨 Perfect For

- **🏠 Homeowners** - DIY energy assessments and upgrade planning
- **🔧 Energy Auditors** - Professional assessment tool
- **🌡️ HVAC Contractors** - Customer education and sales support
- **🏢 Utility Programs** - Energy efficiency program delivery
- **🏘️ Property Managers** - Building efficiency evaluations
- **🏡 Real Estate** - Property energy assessments

## 🛠️ Technical Details

- **File Size**: ~28KB (incredibly lightweight)
- **Dependencies**: None (vanilla HTML/CSS/JavaScript)
- **Browser Support**: All modern browsers (Chrome, Safari, Firefox, Edge)
- **Offline Capable**: Works without internet connection
- **Mobile Optimized**: Responsive design for all screen sizes

## 📚 Advanced Features

For developers and power users interested in the full Flask web application version with server-side processing, database integration, and advanced features, see the [`flask-version`](../../tree/flask-version) branch.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter issues:
1. Check that JavaScript is enabled in your browser
2. Try opening the file directly (not through a file server)
3. For technical issues, [create an issue](../../issues) on GitHub

---

**Built with ❤️ for energy efficiency and sustainability**

*Making home energy assessments accessible to everyone, everywhere.*
