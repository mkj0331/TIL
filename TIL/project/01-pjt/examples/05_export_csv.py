'''
    외부 라이브러리나 모듈 등을 import 해야 할 때, 파일 열자마자 우다다닥 import 받지 말고,
    그 import가 반드시 필요한 경우에 받기
'''

# 요청을 보내야 한다.
import requests, csv
response = requests.get('https://jsonplaceholder.typicode.com/todos').json()

completed_todos = [] # 최종 결과물을 담을 리스트
fields = ['id', 'title']
for item in response:
    if item.get('completed'):
        temp_item = {}        
        for key in fields: 
            temp_item[key] = item[key]
        completed_todos.append(temp_item)

with open('completed_todos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(completed_todos)        
      