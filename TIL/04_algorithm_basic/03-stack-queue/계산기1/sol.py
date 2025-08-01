import sys

sys.stdin = open('input (1).txt')

def infix_to_postfix(expression): # 후위표기식 변환 함수
    stack = []
    postfix = []

    for char in expression: # 매개변수 expression 순회
        if char.isnumeric():    # char가 숫자라면
            postfix.append(char)    # 후위표기식에 추가
        elif char == '+':   # 연산자라면
            while stack:  # 스택이 비지 않았으면
                postfix.append(stack.pop()) # 연산자 꺼내서 후위표기식에 추기
            stack.append(char)  # 현재 연산자 스택에 넣음

    while stack:  # 남은 연산자 꺼내서 후위표기식에 추가
        postfix.append(stack.pop())

    return postfix

for t in range(10):
    length = int(input()) # 문자열 길이
    postfix = infix_to_postfix(input()) # 받은 문자열 후위표기식으로 변환

    todo_calc = [] # 계산할 것들 넣어놓을 리스트
    ans = 0
    for i in postfix:
        if i.isdigit(): # 숫자면
            todo_calc.append(int(i)) # 계산할 리스트에 추가
        else:
            ans += sum(todo_calc) # 계산할 리스트에 있는 거 합을 ans에 더해주기
            todo_calc.clear() # 계산한거는 clear로 초기화
    print(f"#{t+1} {ans}")







