import csv

def extract():
    # csv file name
    filename = "uscities.csv"

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            bow = str(row[1]) + ", " + str(row[2])
            rows.append(bow)
    return rows

def issues():
    lis = ["Single Car Accident", "Bike & Car Accident", "Multiple Car Accident", "Auto Theft", "Hit and Run"]
    return lis