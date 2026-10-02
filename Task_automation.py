# ============================================
# Automated Transaction Report Generator
# CodeAlpha Internship - Task 3
# ============================================

import csv


INPUT_FILE = "transactions.csv"
OUTPUT_FILE = "transaction_report.txt"


# Read transactions from CSV
def read_transactions():
    transactions = []

    try:
        with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                transactions.append(row)

        return transactions

    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} was not found.")
        return []


# Calculate transaction statistics
def calculate_statistics(transactions):

    total_transactions = len(transactions)
    successful_transactions = 0
    failed_transactions = 0

    total_amount = 0
    successful_amount = 0
    failed_amount = 0

    for transaction in transactions:

        amount = float(transaction["Amount"])
        status = transaction["Status"].strip().lower()

        total_amount += amount

        if status == "success":
            successful_transactions += 1
            successful_amount += amount

        elif status == "failed":
            failed_transactions += 1
            failed_amount += amount

    if total_transactions > 0:
        success_rate = (
            successful_transactions / total_transactions
        ) * 100
    else:
        success_rate = 0

    statistics = {
        "total_transactions": total_transactions,
        "successful_transactions": successful_transactions,
        "failed_transactions": failed_transactions,
        "total_amount": total_amount,
        "successful_amount": successful_amount,
        "failed_amount": failed_amount,
        "success_rate": success_rate
    }

    return statistics


# Display transaction details
def display_transactions(transactions):

    print("\n" + "=" * 75)
    print("                    TRANSACTION DETAILS")
    print("=" * 75)

    print(
        f"{'ID':<12}"
        f"{'Date':<15}"
        f"{'Type':<12}"
        f"{'Amount':<15}"
        f"{'Status':<12}"
    )

    print("-" * 75)

    for transaction in transactions:

        print(
            f"{transaction['Transaction_ID']:<12}"
            f"{transaction['Date']:<15}"
            f"{transaction['Type']:<12}"
            f"₹{float(transaction['Amount']):<14.2f}"
            f"{transaction['Status']:<12}"
        )

    print("=" * 75)


# Display statistics
def display_statistics(statistics):

    print("\n" + "=" * 50)
    print("              TRANSACTION REPORT")
    print("=" * 50)

    print(
        f"Total Transactions     : "
        f"{statistics['total_transactions']}"
    )

    print(
        f"Successful Transactions: "
        f"{statistics['successful_transactions']}"
    )

    print(
        f"Failed Transactions    : "
        f"{statistics['failed_transactions']}"
    )

    print(
        f"Total Amount           : "
        f"₹{statistics['total_amount']:.2f}"
    )

    print(
        f"Successful Amount      : "
        f"₹{statistics['successful_amount']:.2f}"
    )

    print(
        f"Failed Amount          : "
        f"₹{statistics['failed_amount']:.2f}"
    )

    print(
        f"Success Rate           : "
        f"{statistics['success_rate']:.2f}%"
    )

    print("=" * 50)


# Generate text report
def generate_report(statistics):

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write("       AUTOMATED TRANSACTION REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(
            f"Total Transactions     : "
            f"{statistics['total_transactions']}\n"
        )

        file.write(
            f"Successful Transactions: "
            f"{statistics['successful_transactions']}\n"
        )

        file.write(
            f"Failed Transactions    : "
            f"{statistics['failed_transactions']}\n"
        )

        file.write(
            f"Total Amount           : "
            f"₹{statistics['total_amount']:.2f}\n"
        )

        file.write(
            f"Successful Amount      : "
            f"₹{statistics['successful_amount']:.2f}\n"
        )

        file.write(
            f"Failed Amount          : "
            f"₹{statistics['failed_amount']:.2f}\n"
        )

        file.write(
            f"Success Rate           : "
            f"{statistics['success_rate']:.2f}%\n"
        )

        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write("Report generated automatically using Python.\n")
        file.write("=" * 50 + "\n")

    print(
        f"\nReport saved successfully to {OUTPUT_FILE}"
    )


# Main program
def main():

    print("=" * 50)
    print("     AUTOMATED TRANSACTION PROCESSOR")
    print("=" * 50)

    transactions = read_transactions()

    if not transactions:
        print("\nNo transaction data found.")
        return

    display_transactions(transactions)

    statistics = calculate_statistics(transactions)

    display_statistics(statistics)

    generate_report(statistics)

    print("\nAutomation completed successfully!")


# Program entry point
if __name__ == "__main__":
    main()