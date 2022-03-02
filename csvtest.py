import csv

filename = "b4b csv 12_10_21.csv"

fields = []
rows = []
title = set()

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
        title.add(row[0])

    print("total number of rows %d"%(csvreader.line_num))

    print(title)
    
