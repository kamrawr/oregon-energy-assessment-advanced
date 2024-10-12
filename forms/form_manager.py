# forms/form_manager.py
import tkinter as tk
from tkinter import messagebox
from forms.assessment_modules import insulation, hvac, crawlspace, ductwork, windows, doors

# Function to dynamically generate the form from JSON config
def generate_form(config):
    root = tk.Tk()
    root.title(config["form_title"])
    variables = {}

    row = 0
    for field in config["fields"]:
        tk.Label(root, text=field["label"]).grid(row=row, column=0, sticky='w')
        if field["type"] == "text":
            variables[field["variable_name"]] = tk.StringVar()
            tk.Entry(root, textvariable=variables[field["variable_name"]]).grid(row=row, column=1)
        elif field["type"] == "dropdown":
            variables[field["variable_name"]] = tk.StringVar()
            tk.OptionMenu(root, variables[field["variable_name"]], *field["options"]).grid(row=row, column=1)
        row += 1

    # Submit button
    tk.Button(root, text="Submit", command=lambda: process_form(variables)).grid(row=row, column=1, pady=10)
    root.mainloop()
    
    return variables

# Function to process form submission and assess different areas
def process_form(variables):
    data = {key: var.get() for key, var in variables.items()}
    print(f"Data collected: {data}")
    recommendations = []

    # Run specific assessment modules
    recommendations.extend(insulation.process_insulation_assessment(data))
    recommendations.extend(hvac.process_hvac_assessment(data))
    recommendations.extend(crawlspace.process_crawlspace_assessment(data))
    recommendations.extend(ductwork.process_ductwork_assessment(data))
    recommendations.extend(windows.process_windows_assessment(data))
    recommendations.extend(doors.process_doors_assessment(data))

    # Display the recommendations
    if recommendations:
        messagebox.showinfo("Recommendations", "\n".join(recommendations))
    else:
        messagebox.showinfo("Recommendations", "Your home is in good shape!")
