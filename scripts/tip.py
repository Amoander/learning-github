# Tip calculator, with error handling

def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number, like 47.83")
def ask_people(prompt):
    while True:
        try:
            people = int(input(prompt))
            if people >= 1:
                return people
            print("At least 1 person has to pay!")
        except ValueError:
            print("Please enter a valid number, like 3")

bill = ask_float("Bill total: $")
tip_percent = ask_float("Tip percentage (e.g. 18): ")
people = ask_people("Number of people splitting: ")

tip = bill * (tip_percent / 100)
total= bill + tip
per_person = total / people

print()
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Per person: ${per_person:.2f}")
