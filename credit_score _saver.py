import csv


def credit_score_saver(score):
    f = open('Credit_score_saver.csv', 'r')

    with f:

        reader = csv.DictReader(f)

        for row in reader:
            print(row['min'], row['avg'], row['max'])

credit_score_saver(23)
