import csv

def get_list_csv(filename, column_index, ignore_header = True):
    tags =[]
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for i, row in enumerate(reader):
            tags.append(row[column_index])
        return tags
