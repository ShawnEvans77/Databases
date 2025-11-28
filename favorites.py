import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    next(reader) # skip first line of this file

    for row in reader:
        favorite = row[1]
        print(favorite)