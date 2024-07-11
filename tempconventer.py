# temp_converter.py

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

if __name__ == "__main__":
    while True:
        print("Options:")
        print("Enter '1' to convert Celsius to Fahrenheit")
        print("Enter '2' to convert Fahrenheit to Celsius")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
        elif user_input == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
        else:
            print("Unknown input, please try again")
