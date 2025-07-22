- Vs Code에서 우측 상단에 Run 버튼 봉인
    - CLI 환경에 익숙해지기 위함
    - 복잡한 경로 헷갈리지 않기 위함

---

- 메서드
    - 객체에 속한 **함수**
    - 객체의 상태를 조작하거나 동작을 수행
    - 데이터 타입 객체.메서드() → `‘hello’.capitalize()`
- 객체
    - 파이썬에 있는 모든 것(?)
    - 객체는 타입으로 분류됨

---

Sequence Types

- 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형
- str, list, tuple, range
    - 특징
        1. 순서 존재
        2. 각 값에 고유한 인덱스를 가지고 있음
            1. abs(네거티브 인덱스) + 인덱스 = len()
        3. 슬라이싱 가능
        4. 길이 추출 가능
        5. 반복문을 사용하여 저장된 값들을 반복적으로 처리 가능

- str
    - 문자들의 순서가 있어, **순서 혹은 값 변경 불가능**한 시퀀스 자료형
    - f-string
        - 문자열에 파이썬 표현식의 값을 삽입할 수 있음
        - `print(f"Debugging {bugs} {counts} {area}')`
            - tip : {expression} 내에 복잡한 연산 결과를 넣는 건 비추
    - 문자열 조작 메서드 ( 새 문자열 반환 )
        
        ![image.png](attachment:08d54d40-1370-4a45-9872-2b96dd8f1242:image.png)
        
    
- list
    - 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형
    - 리스트 값 추가 및 삭제 메서드
        
        ![image.png](attachment:05bc4ef2-2316-4c1f-9d2c-46b0ef094439:image.png)
        
        - pop(i)에 인덱스를 넣어서 해당 인덱스 값을 뺄 수는 있지만, 쓸 일 없음!
    - 리스트 탐색 및 정렬 메서드
        - L.reverse() - 리스트의 순서를 역순으로 변경
        - L.sort() - 리스트를 정렬

- tuple
    - 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형
    - **개발자가 직접 사용하기 보다** ‘파이썬 내부 동작’에서 주로 사용됨

- range
    - 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

- dict
    - key - value 쌍으로 이루어진, 순서와 중복이 없는 **변경 가능한** 자료형
    - key는 **변경 불가능한** 자료형(str, int, float, tuple, range, …)만 사용 가능
    - value는 모든 자료형 사용 가능
    - 딕셔너리 메서드
        
        ![image.png](attachment:bb806514-a5aa-4036-bf12-fc2dc8a3cd20:image.png)
        
        - D.get(k) 와 D[’k’] 둘 다 해당 키의 value를 반환하지만, 후자는 value가 없을 때 **오류**(KeyError)를 발생시키지만, 전자는 **오류가 아닌 None** 반환

- set(:= 수학에서의 집합)
    - **순서와 중복이 없는** 변경 가능한 자료형
    - 세트의 집합 연산
        - 합집합(|), 차집합(-), 교집합(&)
    - 세트 메서드
        - s.add(x) - 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
        - s.remove(x) - 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 key Error
    
    ---
    

Other Types

- None
    - 파이썬에서 값이 없음을 표현하는 자료형
- Boolean
    - 참(True)와 거짓(False)를 표현하는 자료형

---

- 복사
    - 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
        - ‘변경 가능한 데이터 타입’과 ‘변경 불가능한 데이터 타입’
        
        ```python
        # 변경 가능한 데이터 타입
        a = [1, 2, 3, 4]
        b = a
        b[0] = 100
        print(a)  # [100, 2, 3, 4]
        print(b)  # [100, 2, 3, 4]
        
        # 변경 불가능한 데이터 타입
        a = 20
        b = a
        b = 10
        print(a)  # 20
        print(b)  # 10
        ```
        
    1. **할당**
        1. 할당 연산자(=)를 통한 복사는 해당 객체에 대한 **객체 참조를 복사**
        
        ```python
        # 할당
        original_list = [1, 2, 3]
        copy_list = original_list
        print(original_list, copy_list)  # [1, 2, 3] [1, 2, 3]
        
        copy_list[0] = 'hi'
        print(original_list, copy_list)  # ['hi', 2, 3] ['hi', 2, 3]
        ```
        
    2. **얕은 복사**
        1. 슬라이싱으로 생성된 객체는 원본 객체와 **독립적으로 존재**
        2. but 한계 : 2차원 리스트와 같이 변경 가능한 객체 **안에 또** 변경 가능한 객체가 있는 경우에 대해서는 독립적으로 존재하지 않아서 참조가 됨
        
        ```python
        # 얕은 복사
        a = [1, 2, 3]
        b = a[:]
        print(a, b)  # [1, 2, 3] [1, 2, 3]
        b[0] = 100
        print(a, b)  # [1, 2, 3] [100, 2, 3]
        
        # 얕은 복사의 한계 
        a = [1, 2, [1, 2]]
        b = a[:]
        print(a, b)  # [1, 2, [1, 2]] [1, 2, [1, 2]]
        b[2][0] = 100
        print(a, b)  # [1, 2, [100, 2]] [1, 2, [100, 2]]
        ```
        
    3. **깊은 복사**
        1. 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
        
        ```python
        # 깊은 복사
        import copy
        
        original_list = [1, 2, [1, 2]]
        deep_copied_list = copy.deepcopy(original_list)
        
        deep_copied_list[2][0] = 100
        
        print(original_list)  # [1, 2, [1, 2]]
        print(deep_copied_list)  # [1, 2, [100, 2]]
        ```
        

---

Type Conversion

- 암시적 형변환 - 파이썬이 자동으로 형변환을 하는 것(Boolean과 Numeric Type에서만 가능)
    - `print(3 + 5.0)` → 8.0
- 명시적 형변환 - 개발자가 직접 형변환을 하는 것
    - `print(int(’1’)` → 1
    
    ![image.png](attachment:46e99877-7a35-486c-bcc6-242361029504:image.png)
    

---

Operator

- 비교 연산자
    - ‘==’와 ‘is’  / ‘≠’와 ‘not is’ 중에 둘 다 일단 전자를 사용하자
- 단축평가
    - 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
    - 즉, 두번째 인자까지 확인하지 않아도 결과를 낼 수 있으면 확인하지 않고 첫번째 인자를 기준으로 결과를 반환하는 것
        
        ```python
        vowels = 'aeiou'
        print(('a' and 'b') in vowels)  # False ('a' and 'b') -> 'b'
        print(('b' and 'a') in vowels)  # True ('b' and 'a') -> 'a'
        print(3 and 5)  # 5
        print(3 and 0)  # 0
        print(0 and 3)  # 0
        print(0 and 0)  # 0
        print(5 or 3)  # 5
        print(3 or 0)  # 3
        print(0 or 3)  # 3
        print(0 or 0)  # 0
        ```
        

---

제어문

- 코드의 실행 흐름을 제어하는 데 사용되는 구분
- 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행
- 조건문
    - if / elif / else
- 반복문
    - for
        - 임의의 시퀀스 항목들을 그 시퀀스에 들어있는 순서대로 반복(시퀀스 뿐 아니라 dict, set 등 iterable 모두 순회 가능)
        
        ```python
        numbers = [4, 6, 10, -8, 5]
        for i in range(len(numbers)):
            numbers[i] = numbers[i] * 2 # 리스트는 변경 가능하므로
        print(numbers)  # [8, 12, 20, -16, 10]
        ```
        
    - while
        - 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행 ↔ 조건식이 거짓(False) 될 때까지 반복
        - for ↔ while 문 바꾸는 연습 중요
    - 적절한 반복문 활용하기
        - for
            - 반복 횟수가 명확하게 정해져 있는 경우에 유용
            - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때
        - while
            - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
            - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우
- 반복문 제어
    - break - 반복을 즉시 중지
    - continue - 아래 코드를 적용하지 않고 다음 반복으로 건너뜀
    - pass - 아무런 동작도 수행하지 않고 넘어감
    
    ```python
    # break
    for i in range(10):
        if i == 5:
            break
        print(i)  # 0 1 2 3 4
    
    # continue
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)  # 1 3 5 7 9
    
    # pass
    for i in range(10):
        pass  # 아무 작업도 안함
    ```
    

---

List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]

data1 = [[0] * (10) for _ in range(10)]
# 또는
data2 = [[0 for _ in range(10)] for _ in range(10)
```

---

매개변수와 인자

- 매개변수
    - 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
- 인자
    - 함수를 호출할 때, 실제로 전달되는 값
    
    ```python
    def add_nums(x,y): # x와 y는 매개변수
    	res = x+y
    	return result
    	
    a = 2
    b = 3
    sum_res = add_nums(a, b) # a와 b는 인자
    print(sum_res)
    ```
    
- 다양한 인자 종류
    - 위치 인자
        - 함수 호출 시 인자의 위치에 따라 전달되는 인자
        - 위치 인자는 함수 호출 시 반드시 값을 전달해야 함
    - 기본 인자 값
        - 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 키워드 인자
        - 함수 호출 시 name=’Dave’ 이런 식으로 인자의 이름과 함께 값을 전달하는 인자
        - 키워드 인자는 반드시 위치 인자 뒤에 위치해야 함
    - 임의의 인자 목록
        - 함수 정의 시 매개변수 앞에 ‘*’를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
    - 임의의 키워드 인자 목록
        - 정해지지 않은 개수의 키워드 인자를 처리하는 인자(**)
    
    ```python
    # Positional Arguments 
    def make_sum(pram1, pram2):
        """이것은 두 수를 받아
        두 수의 합을 반환하는 함수입니다.
        >>> make_sum(1, 2)
        3
        """
        return pram1 + pram2
    
    # Default Argument Values 
    def greet(name, age=30):
        print(f'안녕하세요, {name}님! {age}살이시군요.')
    greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
    greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.
    
    # Keyword Arguments
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')
    greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
    
    # Arbitrary Argument Lists 
    def calculate_sum(*args):
        print(args)
        total = sum(args)
        print(f'합계: {total}')
    calculate_sum(1, 2, 3)
    
    # Arbitrary Keyword Argument Lists 
    def print_info(**kwargs):
        print(kwargs)
    print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30}
    
    # 함수 인자 권장 작성순서 : 위치 -> 기본 -> 가변 -> 가변 키워드
    # 인자의 모든 종류를 적용한 예시
    def func(pos1, pos2, default_arg='default', *args, **kwargs):
        print('pos1:', pos1)
        print('pos2:', pos2)
        print('default_arg:', default_arg)
        print('args:', args)
        print('kwargs:', kwargs)
    func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
    ```
    

---

- Packing
    - 여러 개의 값을 하나의 변수에 묶어서 담는 것(튜플 형태로 묶임)
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    a, *b, c = numbers
    print(a)  # 1
    print(b)  # [2, 3, 4]
    print(c)  # 5
    ```
    
- Unpacking
    - 리스트, 튜플, 딕셔너리와 같이 시퀀스나 반복 가능한 객체로 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
    
    ```python
    def my_function(x, y, z):
        print(x, y, z)
    
    names = ['alice', 'jane', 'peter']
    my_function(*names) # alice jane peter
    
    def my_function(x, y, z):
        print(x, y, z)
    my_dict = {'x': 1, 'y': 2, 'z': 3}
    my_function(**my_dict)  # 1 2 3
    # **는 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달
    ```
    

---

- 내장 함수
    - 파이썬이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)
        - map(function, iterable)
            - iterable의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
        - zip(*iterables)
            - 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
            
            ```python
            girls = ['jane', 'ashley']
            boys = ['peter', 'jay']
            pair = zip(girls, boys)
            
            print(pair) # <zip object at 0x000..>
            print(list(pair)) # [('jane','peter'), ('ashley','jay')]
            ```
            
- 람다 표현식
    - 한 줄로 간단한 함수를 정의
    - `lambda 매개변수: 표현식`

---

Style Guide - 코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음

- 변수명은 직관적인 이름으로
- 공백(spaces) 4칸을 기준으로 코드 블록 들여쓰기
- 한 줄의 길이는 79자로 제한. 길어지면 줄 바꿈(\n)
- 문자와 밑줄로 함수, 변수, 속성의 이름을 작성
- 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가

---

![image.png](attachment:6ca05b22-d6b9-4356-90be-cf121fa0917f:image.png)

---

**LEGB Rule**

![image.png](attachment:339b68a1-7654-48b8-95d1-d07aef97e2f7:image.png)

- 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 **수정은 할 수 없음**

[예시]

```python
print(sum) # Built-in Scope
print(sum(range(3))) # 3

sum = 5 # Global Scope

print(sum) # 5
print(sum(range(3))) # TypeError : 'int' object is not callable
# -> sum 변수 객체 삭제를 위해 del sum을 입력 후 진행
```

```python
a = 1; b = 2

def enclosed():
	a = 10
	c = 3
	
	def local(c):
		print(a, b, c) 
	
	local(500) # 10 2 500
	print(a, b, c) # 10 2 3
		
enclosed()
print(a, b) # 1 2
```

---

참고

- 과제 제출 방법
    1. SSAFY GIT에서 과제>상세보기 이동 (1차, 2차, …제출만 필수)
    2. 우측 하단 실습하기
        1. 실습하기 옆에 문제뷰어에서 문제 복붙해서 이후 clone 받아오는 파일에 붙여놓고 풀면 편함
    3. 좌측 상단 My GitLab 주소 복사 후 새 창에서 열기
    4. 코드 url 복사해서 TIL아래에 clone 받아오기
    5. 해당 파일에서 문제 풀기
    6. add commit push
    7. 문제풀이 창(실습하기)에서 새로고침 하면 push한 내용으로 고쳐짐 → 좌측 상단 > 실습 제출하기
    8. hw파일의 git 삭제(gitlab과 github 충돌 방지)
    9. git 파일에서 내 github TIL에 add commit push