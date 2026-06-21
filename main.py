# Main file to run the Insurance Claim Management System
from customers import add_customer
from policies import add_policy
from claims import add_claim
from reports import generate_report
from charts import generate_chart

while True:

    print("\n1. Add Customer")
    print("2. Add Policy")
    print("3. Submit Claim")
    print("4. Dashboard Report")
    print("5. Generate Chart")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_customer()

    elif choice == "2":

        add_policy()

    elif choice == "3":

        add_claim()

    elif choice == "4":

        generate_report()

    elif choice == "5":

        generate_chart()

    elif choice == "6":

        print("Thank You")

        break

    else:

        print("Invalid Choice")