import requests
import csv


response = requests.request('get', 'https://jsonplaceholder.typicode.com/todos').json()
with open('todos.csv', 'w') as file:
    header = ['id', 'userId', 'title']
    csv_writer = csv.DictWriter(file, fieldnames=header)
    csv_writer.writeheader()
    for item in response:
        if item.get('completed'):
            item.pop('completed', None)
            csv_writer.writerow(item)
