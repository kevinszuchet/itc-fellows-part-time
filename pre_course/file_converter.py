import csv
import json
import pickle

# You should run this script in a directory with a files directory who has all the required files:
# - comments.json
# - hw_25000.csv
# - mlb_players.pkl


def write_csv(filename, data):
    with open('./files/' + filename + '.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i, elem in enumerate(data):
            if i == 0:
                csv_writer.writerow(elem.keys())

            csv_writer.writerow(elem.values())


def write_json(filename, data):
    with open('./files/' + filename + '.json', 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))


def json_to_csv(file):
    filename = file.split('.')[0]
    with open('./files/' + filename + '.json') as json_file:
        data = json.load(json_file)

    write_csv(filename, data)


def csv_to_json(file):
    filename = file.split('.')[0]
    data = []
    with open('./files/' + filename + '.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    write_json(filename, data)


def plk_to_csv_and_json(file):
    filename = file.split('.')[0]
    data = []
    with open('./files/' + filename + '.pkl', 'rb') as plk_file:
        data = pickle.load(plk_file)

    for fn in [write_csv, write_json]:
        fn(filename, data)


# json_to_csv('comments')
# csv_to_json('hw_25000')
# plk_to_csv_and_json('mlb_players')
