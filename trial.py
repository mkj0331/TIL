import pandas as pd

a = pd.read_csv('movie_reviews.csv')
print(a)
author = a['author']
content = a['content']
print(author)
print(content)