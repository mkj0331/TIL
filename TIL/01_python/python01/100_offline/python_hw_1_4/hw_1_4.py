'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.

# 1. 학생들의 이름과 점수를 딕셔너리에 저장하시오.
print("1. 학생들의 이름과 점수를 딕셔너리에 저장")
students = {"Alice" : 85, "Bob" : 78, "Charlie" : 92, "David" : 88, "Eve" : 95}
print(f"students type: {type(students)}")
print(f"학생들의 이름과 점수: {students}")


# 2. 모든 학생의 평균 점수
summ = 0
for score in students.values():
    summ += score
avg = summ / len(students)
print(f"2. 모든 학생의 평균 점수: {avg:.2f}")    


# 3. 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
students_80 = [name for name in students if students[name] >= 80]
print(f"3. 기준 점수(80점) 이상을 받은 학생 수: {students_80}")
    

# 4. 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
sorted_scores = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
print("4. 점수 순으로 정렬:")
for name, score in sorted_scores.items():
    print(f"{name}: {score}")


# 5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
ans = max(students.values()) - min(students.values())
print(f"5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: {ans}")


# 6. 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.
print("6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")
for name, score in students.items():
    if score < avg:
       print(f"{name} 학생의 점수({score})는 평균 이하입니다.")
    else:
        print(f"{name} 학생의 점수({score})는 평균 이상입니다.")
        
   