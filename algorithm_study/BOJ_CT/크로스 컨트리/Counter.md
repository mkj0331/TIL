## Counter
데이터의 개수를 셀 때 매우 유용한 파이썬의 collections 모듈의 Counter 클래스

`from collections import Counter`

Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
-> Counter({'blue': 3, 'red': 2, 'green': 1})

Counter("hello world")
-> Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

counter = Counter("hello world")
counter["o"], counter["l"]
-> (2, 3)

counter["l"] += 100 가능

o in counter -> True


가장 흔한 데이터 찾기
    데이터의 개수가 많은 순으로 정렬된 배열을 리턴
Counter('hello world').most_common()

Counter('hello world').most_common(2) -> 가장 개수가 많은 2개의 데이터 반환

