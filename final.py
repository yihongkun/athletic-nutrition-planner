"""
==============================================================================
Athletic Nutrition Planner
Final Project - Iteration 2
Hongkun Yi
Date: December 2025

Description:
    A nutrition tracking program for athletes and fitness enthusiasts.
    Users can log meals, set fitness goals (bulking/cutting/maintain),
    and view daily progress reports.

Core Concepts Used:
    - Functions
    - File I/O (JSON)
    - Loops and Conditionals
    - Error Handling (try/except)
    - Lists and Dictionaries
==============================================================================
"""

import json
import os

# ==========================================
# Global Variables
# ==========================================
DATA_FILE = "nutrition_data.json"

# Default foods (per 100g)
DEFAULT_FOODS = [
    {"name": "Chicken Breast", "protein": 31, "carbs": 0, "fat": 3.6},
    {"name": "Brown Rice", "protein": 2.6, "carbs": 23, "fat": 0.9},
    {"name": "Broccoli", "protein": 2.8, "carbs": 7, "fat": 0.4},
    {"name": "Eggs", "protein": 13, "carbs": 1.1, "fat": 11},
    {"name": "Oatmeal", "protein": 13.5, "carbs": 68, "fat": 6.5},
]

DEFAULT_GOALS = {"calories": 2500, "protein": 200, "carbs": 250, "fat": 83, "mode": "maintain"}


# ==========================================
# Function 1: Load Data from File
# ==========================================
def load_data():
    """Load saved data from JSON file, or return defaults if file missing."""
    if os.path.exists(DATA_FILE):
        try:
            file = open(DATA_FILE, "r")
            data = json.load(file)
            file.close()
            return data
        except:
            print("Error loading file, using defaults.")
    
    # Return default data if no file
    return {"foods": DEFAULT_FOODS, "log": [], "goals": DEFAULT_GOALS}


# ==========================================
# Function 2: Save Data to File
# ==========================================
def save_data(data):
    """Save current data to JSON file."""
    try:
        file = open(DATA_FILE, "w")
        json.dump(data, file)
        file.close()
        print("Data saved.")
    except:
        print("Error: Could not save data.")


# ==========================================
# Function 3: Add New Food (addFood)
# ==========================================
def add_food(data):
    """Add a new food to the database."""
    print("\n--- Add New Food ---")
    
    name = input("Enter food name: ")
    if name == "":
        print("Error: Name cannot be empty.")
        return
    
    try:
        protein = float(input("Protein per 100g: "))
        carbs = float(input("Carbs per 100g: "))
        fat = float(input("Fat per 100g: "))
    except:
        print("Error: Please enter numbers only.")
        return
    
    if protein < 0 or carbs < 0 or fat < 0:
        print("Error: Values cannot be negative.")
        return
    
    # Create new food and add to list
    new_food = {"name": name, "protein": protein, "carbs": carbs, "fat": fat}
    data["foods"].append(new_food)
    save_data(data)
    print("Added " + name + " to database!")


# ==========================================
# Function 4: Log Meal (calculateCalories)
# ==========================================
def log_meal(data):
    """Record a meal and calculate its calories."""
    
    # Show available foods
    print("\n--- Available Foods ---")
    for i in range(len(data["foods"])):
        food = data["foods"][i]
        print(str(i + 1) + ". " + food["name"])
    
    # Get user choice
    try:
        choice = int(input("Select food number: "))
        portion = float(input("Enter portion in grams: "))
    except:
        print("Error: Please enter valid numbers.")
        return
    
    # Check if choice is valid
    if choice < 1 or choice > len(data["foods"]):
        print("Error: Invalid food number.")
        return
    
    if portion <= 0:
        print("Error: Portion must be greater than 0.")
        return
    
    # Get selected food
    selected = data["foods"][choice - 1]
    
    # Calculate nutrition based on portion
    # Formula: (value per 100g * portion) / 100
    ratio = portion / 100
    protein = selected["protein"] * ratio
    carbs = selected["carbs"] * ratio
    fat = selected["fat"] * ratio
    
    # Calculate calories
    # Protein: 4 cal/g, Carbs: 4 cal/g, Fat: 9 cal/g
    calories = (protein * 4) + (carbs * 4) + (fat * 9)
    
    # Create log entry
    entry = {
        "name": selected["name"],
        "portion": portion,
        "calories": round(calories),
        "protein": round(protein, 1),
        "carbs": round(carbs, 1),
        "fat": round(fat, 1)
    }
    
    data["log"].append(entry)
    save_data(data)
    print("Logged " + str(portion) + "g of " + selected["name"])


# ==========================================
# Function 5: Set Daily Goals (setDailyGoal)
# ==========================================
def set_goals(data):
    """Set nutrition goals based on fitness objective."""
    print("\n--- Set Daily Goals ---")
    print("1. Bulking  (30% protein, 50% carbs, 20% fat)")
    print("2. Cutting  (40% protein, 30% carbs, 30% fat)")
    print("3. Maintain (30% protein, 40% carbs, 30% fat)")
    
    mode_choice = input("Select mode (1-3): ")
    
    # Set ratios based on choice
    if mode_choice == "1":
        mode = "bulking"
        p_ratio = 0.30
        c_ratio = 0.50
        f_ratio = 0.20
    elif mode_choice == "2":
        mode = "cutting"
        p_ratio = 0.40
        c_ratio = 0.30
        f_ratio = 0.30
    elif mode_choice == "3":
        mode = "maintain"
        p_ratio = 0.30
        c_ratio = 0.40
        f_ratio = 0.30
    else:
        print("Error: Invalid choice.")
        return
    
    # Get calorie target
    try:
        calories = float(input("Enter daily calorie target: "))
    except:
        print("Error: Please enter a number.")
        return
    
    if calories <= 0:
        print("Error: Calories must be positive.")
        return
    
    # Calculate macro targets
    # Protein and carbs = 4 calories per gram
    # Fat = 9 calories per gram
    protein_g = int((calories * p_ratio) / 4)
    carbs_g = int((calories * c_ratio) / 4)
    fat_g = int((calories * f_ratio) / 9)
    
    # Save goals
    data["goals"]["calories"] = int(calories)
    data["goals"]["protein"] = protein_g
    data["goals"]["carbs"] = carbs_g
    data["goals"]["fat"] = fat_g
    data["goals"]["mode"] = mode
    
    save_data(data)
    
    print("\nGoals set for " + mode + ":")
    print("  Calories: " + str(int(calories)))
    print("  Protein: " + str(protein_g) + "g")
    print("  Carbs: " + str(carbs_g) + "g")
    print("  Fat: " + str(fat_g) + "g")


# ==========================================
# Function 6: View Report (generateReport + calculateDeficit)
# ==========================================
def view_report(data):
    """Show daily nutrition report with progress."""
    print("\n--- Daily Report ---")
    print("Mode: " + data["goals"]["mode"])
    
    # Check if any meals logged
    if len(data["log"]) == 0:
        print("No meals logged today.")
        return
    
    # Calculate totals using loop
    total_cal = 0
    total_p = 0
    total_c = 0
    total_f = 0
    
    for meal in data["log"]:
        total_cal = total_cal + meal["calories"]
        total_p = total_p + meal["protein"]
        total_c = total_c + meal["carbs"]
        total_f = total_f + meal["fat"]
    
    # Print each meal
    print("\nMeals logged:")
    for meal in data["log"]:
        print("  " + meal["name"] + " (" + str(meal["portion"]) + "g): " + str(meal["calories"]) + " cal")
    
    # Print totals
    print("\n--- Totals ---")
    print("Calories: " + str(total_cal) + " / " + str(data["goals"]["calories"]))
    print("Protein:  " + str(round(total_p, 1)) + "g / " + str(data["goals"]["protein"]) + "g")
    print("Carbs:    " + str(round(total_c, 1)) + "g / " + str(data["goals"]["carbs"]) + "g")
    print("Fat:      " + str(round(total_f, 1)) + "g / " + str(data["goals"]["fat"]) + "g")
    
    # Show progress bars
    print("\n--- Progress ---")
    show_progress("Calories", total_cal, data["goals"]["calories"])
    show_progress("Protein", total_p, data["goals"]["protein"])
    show_progress("Carbs", total_c, data["goals"]["carbs"])
    show_progress("Fat", total_f, data["goals"]["fat"])
    
    # Calculate deficit or surplus
    print("\n--- Status ---")
    diff = data["goals"]["calories"] - total_cal
    if diff > 0:
        print("Deficit: " + str(diff) + " calories remaining")
    else:
        print("Surplus: " + str(abs(diff)) + " calories over target")


def show_progress(label, current, goal):
    """Helper function to display a progress bar."""
    if goal <= 0:
        percent = 0
    else:
        percent = int((current / goal) * 100)
    
    if percent > 100:
        percent = 100
    
    # Build progress bar
    bar_length = 20
    filled = int(bar_length * percent / 100)
    empty = bar_length - filled
    
    bar = "[" + "#" * filled + "-" * empty + "]"
    print(label + ": " + bar + " " + str(percent) + "%")


# ==========================================
# Function 7: Reset Log
# ==========================================
def reset_log(data):
    """Clear the daily log."""
    confirm = input("Clear all logged meals? (y/n): ")
    if confirm == "y" or confirm == "Y":
        data["log"] = []
        save_data(data)
        print("Log cleared.")


# ==========================================
# Main Program
# ==========================================
def main():
    print("==============================================")
    print("       Athletic Nutrition Planner")
    print("  CS5001 Final Project - Hongkun Yi")
    print("==============================================")
    
    # Load data from file
    data = load_data()
    
    # Main menu loop
    running = True
    while running:
        print("\n=== Menu ===")
        print("1. View Foods")
        print("2. Add Food")
        print("3. Log Meal")
        print("4. Set Goals")
        print("5. View Report")
        print("6. Reset Log")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("\n--- Food Database ---")
            for i in range(len(data["foods"])):
                f = data["foods"][i]
                print(str(i+1) + ". " + f["name"] + " - P:" + str(f["protein"]) + " C:" + str(f["carbs"]) + " F:" + str(f["fat"]))
        
        elif choice == "2":
            add_food(data)
        
        elif choice == "3":
            log_meal(data)
        
        elif choice == "4":
            set_goals(data)
        
        elif choice == "5":
            view_report(data)
        
        elif choice == "6":
            reset_log(data)
        
        elif choice == "7":
            print("Goodbye!")
            running = False
        
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()