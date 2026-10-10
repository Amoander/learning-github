# Tip calculator
bill = float(input("Bill total: $"))
tip_percent = float(input("Tip percent (e.g. 18): "))
people = int(input("Number of people splitting: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print()
print(f"Tip:        ${tip:.2f}")
print(f"Total:      ${total:.2f}")
print(f"Per person: ${per_person:.2f}")