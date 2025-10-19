def weight_converter():
    print("Welcome to the Weight Converter!")
    print("Choose the conversion type:")
    print("1: Kilograms to Pounds")
    print("2: Pounds to Kilograms")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms is equal to {pounds:.2f} pounds.")
    elif choice == '2':
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kg:.2f} kilograms.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    weight_converter()

