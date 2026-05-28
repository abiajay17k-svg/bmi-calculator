
PROJECT: BMI Calculator
AUTHOR: Abinaya V
TECHNOLOGIES: Python
DESCRIPTION: 
    Calculates BMI using weight (kg) and height (m).
    Classifies health status and provides suggestions.

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_health_suggestion(bmi):
    if bmi < 18.5:
        return "Underweight – Consider gaining some weight through proper diet and exercise."
    elif 18.5 <= bmi < 25:
        return "Normal weight – Keep up the good work and maintain a healthy lifestyle."
    elif 25 <= bmi < 30:
        return "Overweight – Consider exercising regularly and monitoring your diet."
    else:
        return "Obesity – Consult a healthcare provider for proper guidance."

def main():
    print("Welcome to the BMI Calculator")
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        
        if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers.")
            return
        
        bmi = calculate_bmi(weight, height)
        suggestion = get_health_suggestion(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Health Suggestion: {suggestion}")
    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")

if __name__ == "__main__":
    main()