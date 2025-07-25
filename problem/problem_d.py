import csv, requests
from pprint import pprint
# 각 영화의 출연진 정보를 조건에 맞게 필터링하고 처리하여 CSV로 저장

# TMDB API 키 설정
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

## 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
# movies.csv를 movies로 가져오기
with open('movies.csv', 'r', encoding='utf-8') as file:
    movies = []
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        movies.append(row)

# movies에서 movie_id만 추출
popular_movie_id=[]
for movie in movies:
    temp_movie = {}
    temp_movie['id'] = movie['id']
    popular_movie_id.append(temp_movie)

# 이후 함수에 사용하기 위해 id만 정수형으로 변환
popular_movie_id = [int(x['id']) for x in popular_movie_id]


## API 호출 함수 + # 배우 데이터 처리 함수
# 헤더 설정
headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}


## 출연 순서(order)가 10 이하인 배우들 선택
ans = [] # 최종 답안 리스트
def problem_d(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits" 
    headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
    }
    response = requests.get(url, headers=headers).json()
    
    # response에서 배우 정보가 저장돼있는 cast 데이터만 필터링
    cast_response = response['cast']

    # 출연 순서(order)가 10 이하인 배우들 필터링
    cast_response_order_filterd = [x for x in cast_response if x['order'] <= 10]
    
    # 필터링한 데이터에서 필요한 데이터만 추출
    for item in cast_response_order_filterd:
        temp_item = {
            'cast_id': item['cast_id'],
            'movie_id': movie_id,
            'name': item['name'],
            'character': item['character'],
            'order': item['order']
        }
    ans.append(temp_item)

# 함수 실행
for movie_id in popular_movie_id:
    problem_d(movie_id)

# csv로 export
fields = ['cast_id', 'character', 'movie_id', 'name', 'order']
with open('movie_cast.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(ans)




    