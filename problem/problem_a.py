# TMDB API 키 설정
from pprint import pprint

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

import requests, csv

#account_id = youngseok99
url = "https://api.themoviedb.org/3/movie/popular"

headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}

response = requests.get(url, headers=headers).json()
response = response['results']



# API 호출 함수

# 영화 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

# 인기 영화 목록에서 id, title, release_date, popularity를 추출하여 CSV로 저장

problem_a = []
fields = ['id', 'title', 'release_date', 'popularity']
for item in response:
    temp_item = {}
    for key in fields:
        temp_item[key] = item[key]
    problem_a.append(temp_item)

with open('movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(problem_a)


