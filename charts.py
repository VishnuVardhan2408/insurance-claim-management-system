# Data visualization charts
import csv
import matplotlib.pyplot as plt

def generate_chart():

    approved = 0

    under_review = 0

    try:

        with open("data/claims.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) >= 5:

                    if row[4] == "Approved":

                        approved += 1

                    elif row[4] == "Under Review":

                        under_review += 1

    except:

        print("No claim data found")

        return

    labels = ["Approved", "Under Review"]

    values = [approved, under_review]

    plt.figure(figsize=(7,5))

    plt.bar(labels, values)

    plt.title("Insurance Claim Status Report")

    plt.xlabel("Claim Status")

    plt.ylabel("Number of Claims")

    plt.show()