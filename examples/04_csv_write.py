import csv

with open('data_1.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['이름', '나이', '직업'])
    csv_writer.writerow(['홍길동', 21, '의적'])
    csv_writer.writerow(['김철수', 25, '과학자'])
    csv_writer.writerow(['이영희', 23, '달리기선수'])

with open('data_2.csv', 'w') as file:
    fieldnames = ['이름', '나이', '직업']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow({'이름': '이세돌', '나이': 40, '직업':'바둑기사'})
    csv_writer.writerow({'이름': '정지훈', '직업': '프로게이머', '나이': 25})
