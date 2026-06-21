# Reports and analytics functions
import csv

def generate_report():

    total_customers = 0
    total_policies = 0
    total_claims = 0
    approved_claims = 0
    under_review_claims = 0

    try:

        with open("data/customers.csv", "r") as file:

            total_customers = sum(1 for row in file)

    except:

        pass

    try:

        with open("data/policies.csv", "r") as file:

            total_policies = sum(1 for row in file)

    except:

        pass

    try:

        with open("data/claims.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                total_claims += 1

                if row[4] == "Approved":

                    approved_claims += 1

                elif row[4] == "Under Review":

                    under_review_claims += 1

    except:

        pass

    print("\n===== DASHBOARD REPORT =====")

    print("Total Customers:", total_customers)

    print("Total Policies:", total_policies)

    print("Total Claims:", total_claims)

    print("Approved Claims:", approved_claims)

    print("Under Review Claims:", under_review_claims)