import requests
from pprint import pprint
import csv


# TMDB API 키 설정
API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjEyOTVjNTc2M2U1OTE3NzVmNzJhM2RmZDVlOTQwMCIsIm5iZiI6MTc1MzQxMDA1MC43MDIwMDAxLCJzdWIiOiI2ODgyZWEwMjI2ODM0Mzk1Njg1NWUyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.p8dXSMvDJxL3o7HTjoNYaGx0vIUzvdv5HuB7MTMtc-c'
BASE_URL = ''

# url = "https://api.themoviedb.org/3/movie/popular"

headers = {
    "accept": "application/json",
    "Authorization": "bearer " + API_KEY
}

# CSV 파일에서 영화 ID 읽기
movies_id = []

# 영화 id를 movies.csv로부터 받아온다.
with open('movies.csv','r',encoding='utf-8') as file :
    csv_reader = csv.DictReader(file)
    # print(csv_reader.fieldnames)
    for row in csv_reader :
        movies_id.append(row['id'])


# TMDB 사이트에서 리뷰 결과를 가져와서 정제한다.
with open('movie_reviews.csv','w',newline='',encoding='utf-8') as file :
    fields = ['review_id','movie_id','author','content','rating']
    writer=csv.DictWriter(file,fields,quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writeheader()

    # 각 영화 id를 넣어 리뷰 페이지에서 가져오기
    for id in movies_id :
        temp_dict = {}
        review_details = requests.get("https://api.themoviedb.org/3/movie/"+id+"/reviews",headers=headers).json()

        # pprint(review_details)

        for review in review_details.get('results',[]) :
            author_details = review.get('author_details',{})
            rating = author_details.get('rating')

            if rating is not None and rating >= 5:
                content = review.get('content')
                if not content :
                    content = "내용 없음"
                else :
                    content = content.replace("\n",' ').replace("\r",'').strip()
                    content = content.replace(",", ";")
                writer.writerow({
                    'review_id' : review.get('id'),
                    'movie_id' : id,
                    'author' : review.get('author'),
                    'content' : content,
                    'rating' : author_details.get('rating')
                })





# 영화 ID 리스트를 movies.csv 파일에서 읽어옴

# API 호출 함수

# 리뷰 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

