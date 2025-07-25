import csv
import requests

# TMDB API 키 설정
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}

# movie 정보를 로드하는 함수 (problem_a.py의 결과 활용)
# 로드하여서 id를 수집한다.
movie_id = []
with open('movies.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        movie_id.append(row['id'])

# 리뷰 정보를 로드하는 함수 (problem_c.py의 결과 활용)

data = {k: {} for k in movie_id}
print(data)
with open('movie_reviews.csv', 'r') as file:
    csv_reader = csv.DictReader(file)


# API를 사용하여 영화 평점 정보 가져오기
average_rating = []
vote_count = []
for id in movie_id:
    response = requests.get('https://api.themoviedb.org/3/movie/'+id, headers=headers).json()
    average_rating.append(response['vote_average'])
    vote_count.append(response['vote_count'])
# 영화 평점 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장
with open('movie_ratings.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['id', 'average_rating', 'vote_count'])
    for i in range(len(movie_id)):
        csv_writer.writerow([movie_id[i], average_rating[i], vote_count[i]])