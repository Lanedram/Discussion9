def main():
    intro()

    try:
        gals_needed = int(input("Enter the number of gallons: "))

        gals_to_liters(gals_needed)

    except:
        print("An exception occurred, try again by entering only an number")
        print()
        main()

def intro():
        print("This program converts measurements")
        print("in gallons to liters. For your")
        print("reference the formula is:")
        print(" 1 gal = 3.78541 fluid ounces")
        print()

def gals_to_liters(gals):
     liters = gals * 3.78541
     print("That converts to ", liters, " liters.")

main()