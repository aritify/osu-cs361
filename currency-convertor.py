# from simple_term_menu import TerminalMenu
import time

# For floating number validation when entering currency amount
def check_user_input(input):
    try:
        val = float(input)
        return True
    except ValueError:
        print("You did not enter a number")
        return False

class CurrencyConvertor():
    # Currency Rates
    # USD
    usd_usd = 1.00
    usd_eur = 0.92
    usd_cad = 1.38
    big_mac_us = 5.69

    # EUR
    eur_eur = 1.00
    eur_usd = 1.09
    eur_cad = 1.50
    big_mac_eu = 5.87

    # CAD
    cad_cad = 1.00
    cad_usd = 0.72
    cad_eur = 0.67
    big_mac_ca = 5.56

    while True:

        # Welcome Message
        print("Welcome to the Currency Convertor Program!\n")
        print("Please enter the number or select the option of the currency you want to convert:")

        #options = ["1. USD", "2. EUR", "3. CAD"]
        #terminal_menu = TerminalMenu(options)
        #menu_entry_index = terminal_menu.show()
        #print(f"You have selected {options[menu_entry_index]}!")

        # Starting Currencies
        print("1. USD (United States Dollar)")
        print("2. EUR (European Dollar)")
        print("3. CAD (Canadian Dollar) *---New Option---*")

        # Initialize user input
        user_input = 0

        # Getting user input: currently user enters option number. Eventually will add option selection.
        while user_input != "1" or user_input != "2" or user_input != "3":
            user_input = input("Select your currency (enter 1, 2, or 3): ")
            if user_input == "1":
                print("You chose to start with USD.\n")
                current_currency = "USD"
                break
            elif user_input == "2":
                print("You chose to start with EUR.\n")
                current_currency = "EUR"
                break
            elif user_input == "3":
                print("You chose to start with CAD.\n")
                current_currency = "CAD"
                break
            else:
                print("You didn't choose a valid option")

        # Foreign Currency
        print("Now, select the currency you would like to convert into: ")
        print("1. USD (United States Dollar)")
        print("2. EUR (European Dollar)")
        print("3. CAD (Canadian Dollar) *---New Option---*")

        # Reset user input
        user_input = 0

        # user input for foreign currency
        while user_input != "1" or user_input != "2" or user_input != "3":
            user_input = input("Select the currency you want to convert to (enter 1, 2, 3): ")
            if user_input == "1":
                print("You chose to convert to USD.\n")
                converted_currency = "USD"
                break
            elif user_input == "2":
                print("You chose to convert to EUR.\n")
                converted_currency = "EUR"
                break
            elif user_input == "3":
                print("You chose to convert to CAD. * New Option *\n")
                converted_currency = "CAD"
                break
            else:
                print("You didn't choose a valid option")

        # Currency exchange amount
        print("Now, choose how much " + current_currency + " you want to convert into " + converted_currency + ": ")

        user_input = 0

        while True:
            # Number validation
            user_input = input("Enter a number amount: ")
            if check_user_input(user_input) == True:
                break

        print("")
        if current_currency == "USD":
            if converted_currency == "USD":
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + user_input + " " + converted_currency)
            elif converted_currency == "EUR":
                money = float(user_input) * usd_eur
                money = "{:.2f}".format(money)
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + money + " " + converted_currency)
            elif converted_currency == "CAD":
                money = float(user_input) * usd_cad
                money = "{:.2f}".format(money)
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + money + " " + converted_currency)
        elif current_currency == "EUR":
            if converted_currency == "EUR":
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + user_input + " " + converted_currency)
            elif converted_currency == "USD":
                money = float(user_input) * eur_usd
                money = "{:.2f}".format(money)
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + money + " " + converted_currency)
            elif converted_currency == "CAD":
                money = float(user_input) * eur_cad
                money = "{:.2f}".format(money)
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + money + " " + converted_currency)
        elif current_currency == "CAD":
            if converted_currency == "CAD":
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + user_input + " " + converted_currency)
            elif converted_currency == "USD":
                money = float(user_input) * cad_usd
                money = "{:.2f}".format(money)
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + money + " " + converted_currency)
            elif converted_currency == "EUR":
                money = float(user_input) * cad_eur
                money = "{:.2f}".format(money)
                print(user_input + " " + current_currency + " converted into " + converted_currency + " is " + money + " " + converted_currency)

        time.sleep(5)

        print("")
        print("Do you want to see item equivalency value of your money, restart, or quit?")
        print("0. Quit")
        print("1. Restart !---You will lose your previous inputs and start from the beginning--!")
        print("2. Item Equivalency *---This shows the value of one item and how many you can buy of that item with your money---*")

        user_input = input("Option 1, 2 or 0: ")
        if user_input == "0":
            print("\nThank you for using Currency Convertor! Goodbye!\n")
            break
        if user_input == "1":
            print("\n...Restarting...\n")
            continue
        elif user_input == "2":
            if converted_currency == "USD":
                big_macs = float(money) / big_mac_us
                big_macs = "{:.2f}".format(big_macs)
                big_mac_us = "{:.2f}".format(big_mac_us)
                print("\nAt " + big_mac_us + " per Big Mac in July 2024, you would be able to buy " + big_macs + " Big Macs.")
            elif converted_currency == "EUR":
                big_macs = float(money) / big_mac_eu
                big_macs = "{:.2f}".format(big_macs)
                big_mac_eu = "{:.2f}".format(big_mac_eu)
                print("\nAt " + big_mac_eu + " per Big Mac in July 2024, you would be able to buy " + big_macs + " Big Macs.")
            elif converted_currency == "CAD":
                big_macs = float(money) / big_mac_ca
                big_macs = "{:.2f}".format(big_macs)
                big_mac_ca = "{:.2f}".format(big_mac_ca)
                print("\nAt " + big_mac_ca + " per Big Mac in July 2024, you would be able to buy " + big_macs + " Big Macs.")

        print("")
        print("Do you want to restart, or quit?")
        print("0. Quit")
        print("1. Restart !---You will lose your previous inputs and start from the beginning--!")

        user_input = input("Option 1 or 0: ")
        if user_input == "0":
            print("\nThank you for using Currency Convertor! Goodbye!\n")
            break
        else:
            print("\n...Restarting...\n")
            time.sleep(5)
