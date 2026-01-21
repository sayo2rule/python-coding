# BMI Calculator
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index (BMI)."""
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return bmi

if __name__ == "__main__":
    print("Welcome to the BMI Calculator.")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.") 

