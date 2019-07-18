import csv

with open("examples.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)
