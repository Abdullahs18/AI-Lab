import csv

with open("data.csv", "r") as file:
    data = list(csv.reader(file))

print(data)