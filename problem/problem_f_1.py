import csv

with open('movie_details.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    revenue_percent = []
    for row in csv_reader:
        try:
            rev_per = int(row['revenue'])/int(row['budget']) * 100
        except ZeroDivisionError: 
            # budget이 0이라면 수익률도 0이라고 가정한다.
            rev_per = 0
        finally:
            revenue_percent.append((row['movie_id'], rev_per))
    # print(revenue_percent)


    # 가장 높은 수익률을 찾는다;
    max_revenue_movie = max(revenue_percent, key=lambda x:x[1])

    with open("movies.csv",'r') as movie :
        movie_reader = csv.DictReader(movie)
        for movie in movie_reader :
            if movie['id'] == max_revenue_movie[0] :
                print(f"가장 높은 수익률을 가진 영화는 {movie['title']}이고 수익률은 {max_revenue_movie[1]}% 입니다.")
                break