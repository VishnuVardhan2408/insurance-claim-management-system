# Policy management functions
import csv

def add_policy():

    policy_id = input("Enter Policy ID: ")

    customer_id = input("Enter Customer ID: ")

    print("\nInsurance Types")

    print("1. Health Insurance")

    print("2. Vehicle Insurance")

    print("3. Life Insurance")

    print("4. Travel Insurance")

    insurance_choice = input("Choose Insurance Type: ")

    if insurance_choice == "1":

        insurance_type = "Health Insurance"

    elif insurance_choice == "2":

        insurance_type = "Vehicle Insurance"

    elif insurance_choice == "3":

        insurance_type = "Life Insurance"

    elif insurance_choice == "4":

        insurance_type = "Travel Insurance"

    else:

        insurance_type = "Unknown"

    premium_amount = input("Enter Premium Amount: ")

    with open("data/policies.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            policy_id,
            customer_id,
            insurance_type,
            premium_amount
        ])

    print("Policy added successfully")