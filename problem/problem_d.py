import csv, requests
from pprint import pprint
# 각 영화의 출연진 정보를 조건에 맞게 필터링하고 처리하여 CSV로 저장

# TMDB API 키 설정
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
with open('movies.csv', 'r', encoding='utf-8') as file:
    movies = []
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        movies.append(row)

popular_movie_id=[]
for movie in movies:
    temp_movie = {}
    temp_movie['id'] = movie['id']
    popular_movie_id.append(temp_movie)

popular_movie_id = [int(x['id']) for x in popular_movie_id]


# API 호출 함수 + # 배우 데이터 처리 함수
headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}


# 출연 순서(order)가 10 이하인 배우들 선택
#   cast_id, movie_id, 
ans = []
def problem_d(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits" 
    headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
    }
    response = requests.get(url, headers=headers).json()
    
    cast_response = response['cast']
    cast_response_order_filterd = [x for x in cast_response if x['order'] <= 10]
    
    for item in cast_response_order_filterd:
        temp_item = {
            'cast_id': item['cast_id'],
            'movie_id': movie_id,
            'name': item['name'],
            'character': item['character'],
            'order': item['order']
        }
    ans.append(temp_item)

for movie_id in popular_movie_id:
    problem_d(movie_id)

pprint(ans)
  

# pprint(response['id']) # movie_id


# 데이터 수집 및 CSV 파일로 저장



    