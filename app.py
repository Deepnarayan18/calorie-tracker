import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from dataclasses import dataclass
from tkinter import StringVar, IntVar, messagebox
import matplotlib.pyplot as plt

# Define the Food dataclass
@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

# Initialize the food list and goals
today = []
calorie_goal = 3000
protein_goal = 180
fat_goal = 80
carbs_goal = 300

# Function to add food
def add_food():
    name = name_var.get()
    calories = calories_var.get()
    protein = protein_var.get()
    fat = fat_var.get()
    carbs = carbs_var.get()

    if not name or not calories or not protein or not fat or not carbs:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return
    
    try:
        food = Food(name, int(calories), int(protein), int(fat), int(carbs))
        today.append(food)
        messagebox.showinfo("Success", "Food added successfully!")
        clear_inputs()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for calories, protein, fat, and carbs.")

# Function to clear input fields
def clear_inputs():
    name_var.set("")
    calories_var.set(0)
    protein_var.set(0)
    fat_var.set(0)
    carbs_var.set(0)

# Function to visualize progress
def visualize_progress():
    calorie_sum = sum(food.calories for food in today)
    protein_sum = sum(food.protein for food in today)
    fat_sum = sum(food.fat for food in today)
    carb_sum = sum(food.carbs for food in today)

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Pie chart for macronutrient distribution
    axs[0, 0].pie([protein_sum, fat_sum, carb_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
    axs[0, 0].set_title("Macronutrients Distribution")

    # Bar chart for progress towards goals
    axs[0, 1].bar(["Calories", "Protein", "Fat", "Carbs"], 
                  [calorie_sum, protein_sum, fat_sum, carb_sum],
                  color=['blue', 'green', 'red', 'purple'])
    axs[0, 1].axhline(y=calorie_goal, color='blue', linestyle='--', label="Calorie Goal")
    axs[0, 1].axhline(y=protein_goal, color='green', linestyle='--', label="Protein Goal")
    axs[0, 1].axhline(y=fat_goal, color='red', linestyle='--', label="Fat Goal")
    axs[0, 1].axhline(y=carbs_goal, color='purple', linestyle='--', label="Carbs Goal")
    axs[0, 1].legend()
    axs[0, 1].set_title("Progress Towards Goals")

    # Histogram of calorie distribution per food item
    calories_list = [food.calories for food in today]
    axs[1, 0].hist(calories_list, bins=10, color='orange', edgecolor='black')
    axs[1, 0].set_title("Calorie Distribution")
    axs[1, 0].set_xlabel("Calories")
    axs[1, 0].set_ylabel("Frequency")

    # Scatter plot of protein vs carbs for each food item
    proteins_list = [food.protein for food in today]
    carbs_list = [food.carbs for food in today]
    axs[1, 1].scatter(proteins_list, carbs_list, color='green')
    for i, food in enumerate(today):
        axs[1, 1].annotate(food.name, (proteins_list[i], carbs_list[i]))
    axs[1, 1].set_title("Protein vs Carbs")
    axs[1, 1].set_xlabel("Protein (g)")
    axs[1, 1].set_ylabel("Carbs (g)")

    fig.tight_layout()
    plt.show()

# Create the main application window
app = ttk.Window(themename="superhero")
app.title("Food Tracker")
app.geometry("500x400")

# Create a frame to act as a card
card = ttk.Frame(app, padding=20, bootstyle="dark")
card.place(relx=0.5, rely=0.5, anchor=CENTER)

# Define variables for input fields
name_var = StringVar()
calories_var = IntVar()
protein_var = IntVar()
fat_var = IntVar()
carbs_var = IntVar()

# Create input fields and labels inside the card
ttk.Label(card, text="Name:").pack(pady=5)
ttk.Entry(card, textvariable=name_var).pack(pady=5)

ttk.Label(card, text="Calories:").pack(pady=5)
ttk.Entry(card, textvariable=calories_var).pack(pady=5)

ttk.Label(card, text="Protein (g):").pack(pady=5)
ttk.Entry(card, textvariable=protein_var).pack(pady=5)

ttk.Label(card, text="Fat (g):").pack(pady=5)
ttk.Entry(card, textvariable=fat_var).pack(pady=5)

ttk.Label(card, text="Carbs (g):").pack(pady=5)
ttk.Entry(card, textvariable=carbs_var).pack(pady=5)

# Create buttons for adding food and visualizing progress
ttk.Button(card, text="Add Food", command=add_food, bootstyle=SUCCESS).pack(pady=10)
ttk.Button(card, text="Visualize Progress", command=visualize_progress, bootstyle=INFO).pack(pady=10)

# Run the application
app.mainloop()
