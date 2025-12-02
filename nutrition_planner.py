"""
Iteration 1: Project Proposal & Initial Development
Athletic Nutrition Planner
Hongkun Yi
10/23/2025
This program helps athletes and fitness amateur track their daily nutrition intake,
calculate macronutrients (protein, carbohydrates, and fat), to help them achieve their fitness goals.
"""

# ===== Function 1: Add Food to Database =====
def addFood():
    """Add a new food item to the database"""
    print("\n--- Add New Food to Database ---")
    
    # Get user input
    food_name = input("Food name: ").strip().lower()
    
    # Input validation - using try-except error handling
    try:
        protein = float(input("Protein per 100g: "))
        carbs = float(input("Carbohydrates per 100g: "))
        fat = float(input("Fat per 100g: "))
        
        # Check if values are negative
        if protein < 0 or carbs < 0 or fat < 0:
            print("Error: Nutritional values cannot be negative!")
            return
    except:
        print("Error: Please enter valid numbers!")
        return
    
    # Open file and add new food - using append mode
    file = open("food_database.txt", "a")
    file.write(f"{food_name},{protein},{carbs},{fat}\n")
    file.close()
    
    print(f"Success: '{food_name}' has been added to the database!")


# ===== Function 2: Calculate Calories =====
def calculateCalories(food_name, portion_grams):
    """
    Calculate calories and macronutrients for a specific food portion
    Formula: Calories = (protein × 4) + (carbs × 4) + (fat × 9)
    """
    # Validate portion size
    if portion_grams <= 0:
        print("Error: Portion size must be greater than 0!")
        return None
    
    # Read food database
    try:
        file = open("food_database.txt", "r")
        lines = file.readlines()
        file.close()
    except:
        print("Error: Database file not found!")
        return None
    
    # Search for food in database
    found = False
    for line in lines:
        # Split each line: name,protein,carbs,fat
        parts = line.strip().split(",")
        name = parts[0]
        
        if name == food_name.lower():
            found = True
            # Get nutritional values per 100g
            protein_per_100 = float(parts[1])
            carbs_per_100 = float(parts[2])
            fat_per_100 = float(parts[3])
            
            # Calculate actual nutritional values based on portion
            protein = (protein_per_100 * portion_grams) / 100
            carbs = (carbs_per_100 * portion_grams) / 100
            fat = (fat_per_100 * portion_grams) / 100
            
            # Calculate total calories
            calories = (protein * 4) + (carbs * 4) + (fat * 9)
            
            # Log to daily log file
            log_file = open("daily_log.txt", "a")
            log_file.write(f"{food_name},{portion_grams},{calories:.1f},{protein:.1f},{carbs:.1f},{fat:.1f}\n")
            log_file.close()
            
            # Return results
            return {
                'calories': calories,
                'protein': protein,
                'carbs': carbs,
                'fat': fat
            }
    
    if not found:
        print(f"Error: '{food_name}' not found in database!")
        return None


# ===== Function 3: Set Daily Goal =====
def setDailyGoal():
    """Set daily nutrition goals based on fitness objective"""
    print("\n--- Set Daily Nutrition Goals ---")
    print("1. Bulking (Muscle Gain) - 30% protein, 50% carbs, 20% fat")
    print("2. Cutting (Fat Loss) - 40% protein, 30% carbs, 30% fat")
    print("3. Maintaining (Maintenance) - 30% protein, 40% carbs, 30% fat")
    
    choice = input("Choose goal type (1-3): ")
    
    # Set macro ratios based on goal type
    if choice == "1":
        goal_type = "Bulking"
        protein_percent = 30
        carbs_percent = 50
        fat_percent = 20
    elif choice == "2":
        goal_type = "Cutting"
        protein_percent = 40
        carbs_percent = 30
        fat_percent = 30
    elif choice == "3":
        goal_type = "Maintaining"
        protein_percent = 30
        carbs_percent = 40
        fat_percent = 30
    else:
        print("Error: Invalid selection!")
        return
    
    # Get daily calorie target
    try:
        daily_calories = float(input("Daily calorie target: "))
        if daily_calories <= 0:
            print("Error: Calorie target must be greater than 0!")
            return
    except:
        print("Error: Please enter a valid number!")
        return
    
    # Calculate macro targets in grams
    protein_grams = (daily_calories * protein_percent / 100) / 4
    carbs_grams = (daily_calories * carbs_percent / 100) / 4
    fat_grams = (daily_calories * fat_percent / 100) / 9
    
    # Save to file
    file = open("daily_goals.txt", "w")
    file.write(f"{goal_type}\n")
    file.write(f"{daily_calories}\n")
    file.write(f"{protein_grams},{carbs_grams},{fat_grams}\n")
    file.close()
    
    print(f"\nSuccess: Daily goals have been set!")
    print(f"Goal Type: {goal_type}")
    print(f"Daily Calories: {daily_calories:.0f} kcal")
    print(f"Protein: {protein_grams:.1f}g")
    print(f"Carbohydrates: {carbs_grams:.1f}g")
    print(f"Fat: {fat_grams:.1f}g")


# ===== Function 4: Calculate Daily Nutrition =====
def calculateDailyNutrition():
    """Display all meals logged for today"""
    print("\n--- Daily Nutrition Summary ---")
    
    try:
        file = open("daily_log.txt", "r")
        lines = file.readlines()
        file.close()
    except:
        print("No meals have been logged today")
        return
    
    if len(lines) == 0:
        print("No meals have been logged today")
        return
    
    # Initialize totals
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    print("\nToday's Food Log:")
    print("-" * 70)
    
    # Iterate through each line
    for line in lines:
        parts = line.strip().split(",")
        food = parts[0]
        grams = parts[1]
        calories = float(parts[2])
        protein = float(parts[3])
        carbs = float(parts[4])
        fat = float(parts[5])
        
        print(f"{food} ({grams}g): {calories:.0f} cal | P: {protein:.1f}g C: {carbs:.1f}g F: {fat:.1f}g")
        
        # Accumulate totals
        total_calories += calories
        total_protein += protein
        total_carbs += carbs
        total_fat += fat
    
    print("-" * 70)
    print(f"TOTAL: {total_calories:.0f} cal | P: {total_protein:.1f}g C: {total_carbs:.1f}g F: {total_fat:.1f}g")


# ===== Function 5: Calculate Deficit/Surplus =====
def calculateDeficit():
    """Compare actual intake against daily goals"""
    print("\n--- Calorie Deficit/Surplus Analysis ---")
    
    # Read goals
    try:
        file = open("daily_goals.txt", "r")
        lines = file.readlines()
        file.close()
        
        goal_type = lines[0].strip()
        goal_calories = float(lines[1].strip())
        macros = lines[2].strip().split(",")
        goal_protein = float(macros[0])
        goal_carbs = float(macros[1])
        goal_fat = float(macros[2])
    except:
        print("Error: Please set your daily goals first!")
        return
    
    # Read today's intake
    try:
        file = open("daily_log.txt", "r")
        lines = file.readlines()
        file.close()
        
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        
        for line in lines:
            parts = line.strip().split(",")
            total_calories += float(parts[2])
            total_protein += float(parts[3])
            total_carbs += float(parts[4])
            total_fat += float(parts[5])
    except:
        print("No meals have been logged today")
        return
    
    # Calculate differences
    cal_diff = total_calories - goal_calories
    protein_diff = total_protein - goal_protein
    carbs_diff = total_carbs - goal_carbs
    fat_diff = total_fat - goal_fat
    
    print(f"\nGoal Type: {goal_type}")
    print("-" * 60)
    print(f"Calories: {total_calories:.0f} / {goal_calories:.0f} (Difference: {cal_diff:+.0f})")
    print(f"Protein: {total_protein:.1f}g / {goal_protein:.1f}g (Difference: {protein_diff:+.1f}g)")
    print(f"Carbs: {total_carbs:.1f}g / {goal_carbs:.1f}g (Difference: {carbs_diff:+.1f}g)")
    print(f"Fat: {total_fat:.1f}g / {goal_fat:.1f}g (Difference: {fat_diff:+.1f}g)")
    print("-" * 60)
    
    # Provide recommendations
    if cal_diff > 100:
        print("Warning: You are over your calorie target today")
    elif cal_diff < -100:
        print("Notice: You are under your calorie target today")
    else:
        print("Success: You are on track with your calorie goals!")


# ===== Function 6: Generate Report =====
def generateReport():
    """Generate detailed report with progress bars"""
    print("\n" + "=" * 70)
    print("              DAILY NUTRITION REPORT")
    print("=" * 70)
    
    # Read goals
    try:
        file = open("daily_goals.txt", "r")
        lines = file.readlines()
        file.close()
        
        goal_type = lines[0].strip()
        goal_calories = float(lines[1].strip())
        macros = lines[2].strip().split(",")
        goal_protein = float(macros[0])
        goal_carbs = float(macros[1])
        goal_fat = float(macros[2])
    except:
        print("Error: Please set your daily goals first!")
        return
    
    # Read today's intake
    try:
        file = open("daily_log.txt", "r")
        lines = file.readlines()
        file.close()
        
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        meal_count = len(lines)
        
        for line in lines:
            parts = line.strip().split(",")
            total_calories += float(parts[2])
            total_protein += float(parts[3])
            total_carbs += float(parts[4])
            total_fat += float(parts[5])
    except:
        print("No meals have been logged today")
        return
    
    # Calculate percentages
    cal_percent = (total_calories / goal_calories) * 100
    protein_percent = (total_protein / goal_protein) * 100
    carbs_percent = (total_carbs / goal_carbs) * 100
    fat_percent = (total_fat / goal_fat) * 100
    
    print(f"\nGoal Type: {goal_type}")
    print(f"Meals Logged: {meal_count}")
    print()
    
    # Display progress bars
    def show_progress(name, current, goal, percent):
        # Create progress bar (40 characters wide)
        filled = int((percent / 100) * 40)
        if filled > 40:
            filled = 40
        bar = "#" * filled + "-" * (40 - filled)
        print(f"{name}")
        print(f"{current:.1f} / {goal:.1f} ({percent:.1f}%)")
        print(f"[{bar}]")
        print()
    
    show_progress("CALORIES", total_calories, goal_calories, cal_percent)
    show_progress("PROTEIN", total_protein, goal_protein, protein_percent)
    show_progress("CARBOHYDRATES", total_carbs, goal_carbs, carbs_percent)
    show_progress("FAT", total_fat, goal_fat, fat_percent)
    
    print("=" * 70)


# ===== Initialize Files =====
def initialize_files():
    """Create default files if they don't exist"""
    # Create food database
    try:
        file = open("food_database.txt", "r")
        file.close()
    except:
        file = open("food_database.txt", "w")
        # Add some default foods
        file.write("chicken_breast,31.0,0.0,3.6\n")
        file.write("brown_rice,2.6,23.0,0.9\n")
        file.write("broccoli,2.8,7.0,0.4\n")
        file.write("salmon,20.0,0.0,13.0\n")
        file.write("oatmeal,13.2,67.7,6.7\n")
        file.write("banana,1.1,22.8,0.3\n")
        file.write("eggs,13.0,1.1,11.0\n")
        file.close()
        print("Success: Food database has been created with default foods")
    
    # Create daily log file
    try:
        file = open("daily_log.txt", "r")
        file.close()
    except:
        file = open("daily_log.txt", "w")
        file.close()


# ===== Main Menu =====
def print_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("         ATHLETIC NUTRITION PLANNER")
    print("=" * 60)
    print("1. Add Food to Database")
    print("2. Log a Meal")
    print("3. Set Daily Goal")
    print("4. View Daily Nutrition Summary")
    print("5. Calculate Calorie Deficit/Surplus")
    print("6. Generate Detailed Report")
    print("7. Clear Today's Log")
    print("8. Exit")
    print("=" * 60)


# ===== Main Program =====
def main():
    """Main program loop"""
    initialize_files()
    
    print("\nWelcome to Athletic Nutrition Planner!")
    print("Track your nutrition and achieve your fitness goals.")
    
    # Main loop
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            addFood()
            
        elif choice == "2":
            food_name = input("Food name: ").strip().lower()
            try:
                portion = float(input("Portion size (grams): "))
                result = calculateCalories(food_name, portion)
                if result:
                    print(f"\nSuccess: Meal logged successfully!")
                    print(f"Calories: {result['calories']:.1f} kcal")
                    print(f"Protein: {result['protein']:.1f}g")
                    print(f"Carbohydrates: {result['carbs']:.1f}g")
                    print(f"Fat: {result['fat']:.1f}g")
            except:
                print("Error: Please enter a valid number for portion size!")
                
        elif choice == "3":
            setDailyGoal()
            
        elif choice == "4":
            calculateDailyNutrition()
            
        elif choice == "5":
            calculateDeficit()
            
        elif choice == "6":
            generateReport()
            
        elif choice == "7":
            # Clear today's log
            file = open("daily_log.txt", "w")
            file.close()
            print("Success: Today's log has been cleared")
            
        elif choice == "8":
            print("\nThank you for using Athletic Nutrition Planner!")
            print("Stay healthy and keep training!\n")
            break
            
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 8.")


# Run the program
if __name__ == "__main__":
    main()