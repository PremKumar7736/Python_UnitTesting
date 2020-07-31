import csv
import json

def csvToJson(csvFilePath, jsonFilePath):

    data = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            data.append(rows)

    bikedict = {"Bike": data}
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(bikedict, indent=4))


def jsonToCSV(jsonFilePath, csvFilePath):

    with open(jsonFilePath) as json_file:
        data = json.load(json_file)

    bike_data = data['Bike']
    data_file = open(csvFilePath, 'w')
    csv_writer = csv.writer(data_file)

    count = 0

    for rows in bike_data:
        if count == 0:
            header = rows.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(rows.values())

    data_file.close()

