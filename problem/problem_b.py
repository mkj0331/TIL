# TMDB API 키 설정
from pprint import pprint

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

import requests

#account_id = youngseok99
url = "https://api.themoviedb.org/3/movie/popular"

headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}

response = requests.get(url, headers=headers).json()

pprint(response)

# API 호출 함수

# 영화 상세 데이터 처리 함수

# CSV 파일에서 영화 ID 읽기

# 데이터 수집 및 CSV 파일로 저장
