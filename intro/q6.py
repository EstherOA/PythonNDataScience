years = 23
accumulator = 0

while years > 0:
    accumulator += years
    years -= 1

print("Total years:", accumulator)
months = accumulator*12
print("Months:", months)
days = months * 30
print("Days:", days)
hours = days * 24
print("Hours", hours)
