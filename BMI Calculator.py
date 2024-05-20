import tkinter as tk
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers and greater than 0.")
        
        bmi = weight / (height ** 2)
        bmi_result_label.config(text=f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        bmi_category_label.config(text=f"You are classified as: {category}")
    except ValueError as e:
        bmi_result_label.config(text="Error: " + str(e))
        bmi_category_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create widgets
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

bmi_result_label = tk.Label(root, text="")
bmi_result_label.grid(row=3, column=0, columnspan=2)

bmi_category_label = tk.Label(root, text="")
bmi_category_label.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()