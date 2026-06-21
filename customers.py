# Customer registration functions
import csv

def add_customer():

    customer_id = input("Enter Customer ID: ")

    customer_name = input("Enter Customer Name: ")

    email = input("Enter Email: ")

    phone = input("Enter Phone Number: ")

    policy_number = input("Enter Policy Number: ")

    with open("data/customers.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            customer_id,
            customer_name,
            email,
            phone,
            policy_number
        ])

    print("Customer added successfully")