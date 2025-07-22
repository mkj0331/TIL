# 아래에 코드를 작성하시오.
movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]


# 문제
# 다음 요구사항을 만족하는 파이썬 코드를 작성하시오.
# 요구사항
# movies리스트를 순회하며 영화 제목과 평점을 가진 딕셔너리 객체로 만들고 
# 새로운 리스트에 담는다.
movie_rating = []
for i in range(len(movies)):
    movie_rating.append({'title': movies[i], 'rating': ratings[i]}) 
print(movie_rating)
# get_high_rated_movies 함수를 정의하여, threshold 매개변수를 받아서
# 평점이 threshold 이상인 영화를 리스트로 반환한다.
def get_high_rated_movies(threshold):
    good_movies = []
    for i in movie_rating:
        if i['rating'] >= threshold:
            good_movies.append(i['title'])    
    return good_movies        

# 사용자로부터 평점 기준을 입력받아, get_high_rated_movies 함수를 
# 호출하여 해당 평점 이상인 영화를 출력한다.
threshold = int(input("Enter the rating threshold: "))
ans = get_high_rated_movies(threshold)
print(f"Movies with a rating of {threshold:.1f} or higher: ")
for mv in ans:
    print(mv)