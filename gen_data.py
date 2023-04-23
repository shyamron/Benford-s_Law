import csv
import random

BENFORD_PERCENTAGES = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

data = []
for i in range(30000):
    first_digit = random.randint(1, 9)
    remaining_digits = random.randint(0, 999)
    number = int(str(first_digit) + str(remaining_digits).zfill(3))
    data.append(number)

with open('benford_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Number'])
    for number in data:
        writer.writerow([number])

