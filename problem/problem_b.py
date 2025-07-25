# TMDB API 키 설정
import requests
import csv

# API 호출 함수

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}

# CSV 파일에서 영화 ID 읽기
id_list = []
with open('movies.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        id_list.append(row['id'])

# 영화 상세 데이터 처리 함수
# 데이터 수집 및 CSV 파일로 저장
with open('movie_details.csv', 'w') as file:
    # 요구사항인 예산, 수익, 시간, 장르를 탐색
    fieldnames = ['movie_id', 'budget', 'revenue', 'runtime', 'genres' ]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    # 상세 데이터는 id를 인자로 받으므로, id별로 검색을 할 수밖에 없음. 따라서 각 id별로 requests를 가져와서 처리 예정
    for id in id_list:
        temp_dict = {'movie_id': id}
        details = requests.get("https://api.themoviedb.org/3/movie/"+id, headers=headers).json()
        for field in fieldnames:
            # 장르 항목의 경우 dict의 list로 반환하므로, 이를 장르 이름을 합쳐서 전달
            if field == 'genres':
                genre_str = ''
                for i in details['genres']:
                    genre_str = genre_str + i['name'] + " "
                temp_dict['genres'] = genre_str
            elif field != 'movie_id':
                temp_dict[field] = details[field]
        csv_writer.writerow(temp_dict)
