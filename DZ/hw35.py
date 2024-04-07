import csv

with open("data2.csv") as f:
    file_reader = csv.reader(f, delimiter=";")
    for row in file_reader:
        print(row)
