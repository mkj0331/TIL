import csv

with open('movie_details.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    revenue_percent = []
    for row in csv_reader:
        try:
            rev_per = int(row['revenue'])/int(row['budget']) * 100
        except ZeroDivisionError:
            rev_per = int(row['revenue'])
        finally:
            revenue_percent.append((row['movie_id'], rev_per))
    print(revenue_percent)