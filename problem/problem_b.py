# TMDB API 키 설정
import requests
import csv
from tqdm import tqdm

# API 호출 함수

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}

# 영화 상세 데이터 처리 함수

popular_movies = requests.get("https://api.themoviedb.org/3/movie/popular", headers=headers).json()
id_list = []
for item in tqdm(popular_movies['results']):
    id_list.append(item['id'])

with open('details.csv', 'w') as file:
    fieldnames = ['budget','revenue', 'runtime', 'genres' ]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    #for id in tqdm(id_list):
    #temp_dict = {}
    details = requests.get("https://api.themoviedb.org/3/tv/968171", headers=headers).json()
    print(details)

# CSV 파일에서 영화 ID 읽기

# 데이터 수집 및 CSV 파일로 저장