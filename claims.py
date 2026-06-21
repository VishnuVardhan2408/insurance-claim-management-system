# Claim processing functions
import csv
from datetime import datetime

def add_claim():

    claim_id = input("Enter Claim ID: ")

    policy_id = input("Enter Policy ID: ")

    claim_amount = int(input("Enter Claim Amount: "))

    reason = input("Enter Claim Reason: ")

    if claim_amount <= 50000:

        status = "Approved"

    else:

        status = "Under Review"

    date = datetime.now().strftime("%d-%m-%Y")

    with open("data/claims.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            claim_id,
            policy_id,
            claim_amount,
            reason,
            status,
            date
        ])

    print("\nClaim submitted successfully")

    print("Claim Status:", status)