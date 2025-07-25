# 다작 배우 목록 수집  : 수집된 출연진 정보에서 2편 이상의 영화에 출연한 배우 목록을 추출하는 기능 

import csv, requests
from pprint import pprint

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'

with open('movie_cast.csv', 'r', encoding='utf-8') as file:
    movie_cast = []
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        movie_cast.append({
            'movie_id': row['movie_id'],
            'name': row['name']
        })

name_count = {}     # 이름별 등장 횟수 저장
duplicates = []     # 2번 이상 등장한 이름 저장

for item in movie_cast:
    name = item['name']
    
    # 이름이 이미 등장했으면 count 증가
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

# 2회 이상 등장한 name만 결과 리스트에 추가
for name in name_count:
    if name_count[name] >= 2:
        duplicates.append(name)

# 출력
print(duplicates)