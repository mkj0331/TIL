# 아래에 코드를 작성하시오.

# numbers 리스트에 1부터 10까지의 정수를 할당한다.
numbers = list(range(1,11))

# numbers 리스트의 각 요소를 순회하며, 짝수일 경우 해당 숫자를 출력한다.
for num in numbers:
    if num%2 == 0:
        print(num)
# numbers 리스트의 각 요소를 순회하며, 홀수일 경우 해당 숫자를 '홀수'로 출력한다.
    else:
        print(f"{num}은(는) 홀수")
# numbers 리스트의 각 요소를 순회하며, 숫자가 5일 경우 반복을 종료한다.
    if num == 4:
        break