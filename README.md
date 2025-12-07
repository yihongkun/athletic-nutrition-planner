# Athletic Nutrition Planner

A command-line nutrition tracking application designed for athletes and fitness enthusiasts. Track meals, set macro goals based on your fitness phase (bulking/cutting/maintain), and monitor daily progress.

**Author:** Hongkun Yi  
**Course:** CS5001 - Northeastern University  
**Date:** December 2025

---

## Features

- **Food Database**: Pre-loaded with common fitness foods, add custom foods anytime
- **Meal Logging**: Log meals with portion sizes, automatic calorie calculation
- **Goal Setting**: Set daily targets based on bulking, cutting, or maintenance phases
- **Progress Tracking**: Visual progress bars and deficit/surplus calculations
- **Data Persistence**: All data saved to JSON file automatically

---

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only `json` and `os`)

---

## How to Run

1. **Download** the file `final.py` to your computer

2. **Open Terminal/Command Prompt** and navigate to the file location:
   ```
   cd path/to/your/folder
   ```

3. **Run the program**:
   ```
   python final.py
   ```
   Or on some systems:
   ```
   python3 final.py
   ```

4. **Follow the menu** to use the application

---

## Usage Guide

### Menu Options

| Option | Function | Description |
|--------|----------|-------------|
| 1 | View Foods | Display all foods in database with macros |
| 2 | Add Food | Add a custom food with protein/carbs/fat per 100g |
| 3 | Log Meal | Record a meal with portion size |
| 4 | Set Goals | Choose fitness mode and calorie target |
| 5 | View Report | See daily progress with visual bars |
| 6 | Reset Log | Clear all logged meals for the day |
| 7 | Exit | Save and close the program |

### Example Workflow

```
1. Set your goals (Option 4)
   - Select "Cutting" mode
   - Enter 2000 calories

2. Log your meals throughout the day (Option 3)
   - Select "Chicken Breast"
   - Enter 200 grams

3. Check your progress (Option 5)
   - View calories remaining
   - See macro breakdown
```

---

## File Structure

```
project/
├── final.py           # Main program file
├── nutrition_data.json # Auto-generated data file (created on first run)
└── README.md          # This file
```

---

## Notes

- Data is automatically saved after each action
- The `nutrition_data.json` file stores your foods, logs, and goals
- Delete `nutrition_data.json` to reset all data to defaults
