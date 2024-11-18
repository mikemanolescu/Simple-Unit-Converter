#Main Program
def main():
    print(“What are you converting? 1. Temperature or 2. Distance? Please choose a number corresponding to the conversion type.”)
    #Input conversion type from the user (1 for Temperature, 2 for Distance)
    conversion = int(input("Enter 1 or 2"))
    #Validate input:
    while conversion not in [1, 2]:
        print(“This input is not recognized, please enter 1 for Temperature or 2 for Distance”)
        #Ask user for valid input
        conversion = int(input("Enter 1 or 2"))
       
    if conversion == 1:
        convert_temperature()
    elif conversion == 2:
        convert_distance()

#Restart or Exit Loop
while True:
    print(“Do you wish to perform another conversion? (yes/no)”)
    again = input().lower()
    if again == "yes":
        main()
    elif again == "no":
        print("Bye!")
        break
    else:
        print ("Invalid input. Please enter 'yes' or 'no'.")


#Conversion Formulas
def to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9 
  return celsius
  
def to_fahrenheit(celsius): 
  fahrenheit = celsius * 9/5 + 32 
  return fahrenheit
  
#Function convert_temperature-
def convert_temperature():
    print("What would you like to convert? 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius")
    #Get input
    tempunit = int(input("Enter 1 or 2"))
    #Validate input
    while tempunit not in [1, 2]:
        print(“This input is not recognized, please enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius”)
        #Ask user for valid input
        tempunit = int(input("Enter 1 or 2"))
    #Ask for Value to Convert
    if tempunit == 1:
        print("Please input degrees Celsius)
        celsius = int(input("Enter a value"))

    elif tempunit == 2:
        print("Please input degrees Fahrenheit")
        fahrenheit = int(input("Enter a value"))




    #If choice is 1:
        #Convert using formula: (value x 9/5) + 32
        #Set result as converted value with Fahrenheit unit
    #Else if choice is 2:
        #Convert using formula: (value - 32) x 9/5
        #Set result as converted value with Celsius unit

    #Print result: original value with unit = converted value with unit

#Function convert_distance-
#Def convert_distance():
    #Print distance conversion choices:
        #1 for Miles to Kilometers
        #2 for Kilometers to Miles
    #Input distance conversion choice
    #While input is invalid:
        #Print error message “This input is not recognized, please enter 1 for Miles to Kilometers or 2 for Kilometers to Miles”
        #Ask user for valid input

    #Input value to convert
    #If input contains units, like 20 miles:
        #Print error message: “This input is not recognized, please enter a number only without units”
        #Ask user for valid input

    #If choice is 1:
        #Convert using formula: value x 1.60934
        #Set result as converted value with kilometers as unit
    #Else if choice is 2:
        #Convert using formula: value / 1.60934
        #Set result as converted value with miles as unit

    #Print result: original value with unit = converted value with unit
