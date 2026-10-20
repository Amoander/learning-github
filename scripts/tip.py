# Tip calculator, with error handling and a testable math function


def calculate_tip(bill, tip_percent, people):
    """Return (tip, total, per_person) for a bill split among people."""
    if people < 1:
        raise ValueError("people must be at least 1")
    tip = bill * tip_percent / 100
    total = bill + tip
    per_person = total / people
    return tip, total, per_person


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, like 47.83")


def ask_people(prompt):
    while True:
        try:
            people = int(input(prompt))
            if people >= 1:
                return people
            print("At least 1 person has to pay!")
        except ValueError:
            print("Please enter a whole number, like 3")


def main():
    bill = ask_float("Bill total: $")
    tip_percent = ask_float("Tip percent (e.g. 18): ")
    people = ask_people("Number of people splitting: ")

    tip, total, per_person = calculate_tip(bill, tip_percent, people)

    print()
    print(f"Tip:        ${tip:.2f}")
    print(f"Total:      ${total:.2f}")
    print(f"Per person: ${per_person:.2f}")


if __name__ == "__main__":
    main()