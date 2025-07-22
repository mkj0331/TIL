### 객체

- 객체
    - 클래스에서 정의한 것을 토대로 메모리에 할당된 것
    - **속성**과 **행동**으로 구성된 모든 것(객체 = 속성 + 기능(Method))
- 인스턴스 - 클래스로 만든 객체
    - 가수(클래스) → 아이유는 객체(O), 인스턴스(△), 가수의 인스턴스(O)
- `[1,2,3].sort()` → 리스트.정렬() → **객체**.행동() → **인스턴스**.메서드()
    - `name = Alice` 에서 name의 타입은 **str 클래스**이고, 변수 name은 **str클래스의 인스턴스**이다.

---

### 클래스

- 클래스
    - 파이썬에서 **타입을 표현**하는 방법( 클래스를 만든다 ↔ 타입을 만든다)
    - 객체를 생성하기 위한 설계도 / 데이터와 기능을 함께 묶는 방법을 제공
- 클래스 이름은 파스칼 케이스 방식으로 작성(MyClass처럼 공백을 기준으로 첫 문자를 대문자로 작성)
- 클래스 구성요소
    - 생성자 함수
        - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
        - `__init__` 메서드로 정의되며, 객체 초기화를 담당
        - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
    
    ```python
    def __init__(self,name):
    	self.name = name
    ```
    
    - 인스턴스 변수
        - 인스턴스마다 별도로 유지되는 변수
        - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
            - `self.name = name`
    - 클래스 변수
        - 클래스 내부에 선언된 변수
        - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
        
        ```python
        class Person:
        	``blood_color = 'red'`
        ```
        
    - 인스턴스 메서드
        - 각 인스턴스에서 호출할 수 있는 메서드(함수)
    - 인스턴스가 클래스 변수를 변경할 수는 없음(`c1.pi = 1.15` 를 인스턴스 내에서 설정하면 인스턴스 내에서는 바뀌지만, 클래스 변수는 바뀌지 않음 → `Circle.pi = 1.15` 로 선언해야 클래스 변수가 바뀜)

---

### 메서드

- 인스턴스 메서드(클래스 내에서 정의하는 함수)
    - 반드시 첫 번째 매개변수로 **인스턴스 자신(self)**를 전달받음
- 클래스 메서드
    - 클래스가 호출하는 메서드(클래스 변수 조작 or 클래스 레벨의 동작 수행)
    - `@classmethod`  데코레이터를 사용하여 정의
    - 호출 시, 첫 번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
    
    ```python
    class Dog:
        species = "강아지"  # 클래스 변수
    
        def __init__(self, name):
            self.name = name  # 인스턴스 변수
    
        def say_hi(self):  # 인스턴스 메서드
            print(f"안녕! 나는 {self.name}야.")  # self로 인스턴스 변수 접근
    
        @classmethod
        def what_species(cls):  # 클래스 메서드
            print(f"우리는 모두 {cls.species}입니다.")  # cls로 클래스 변수 접근
    
    d = Dog("초코")
    d.say_hi()        # 👉 안녕! 나는 초코야.
    Dog.what_species()  # 👉 우리는 모두 강아지입니다.
    ```
    
- 정적 메서드
    - 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
        - 주로 클래스와 관련이 있지만 **인스턴스와 상호작용이 필요하지 않은 경우**에 사용
    - `@staticmethod`  데코레이터를 사용하여 정의
    
    ```python
    # 정적 메서드
    class StringUtils:
        @staticmethod
        def reverse_string(string):
            return string[::-1]
        @staticmethod
        def capitalize_string(string):
            return string.capitalize()
    
    text = 'hello, world'
    reversed_text = StringUtils.reverse_string(text)
    print(reversed_text)  # dlrow ,olleh
    capitalized_text = StringUtils.capitalize_string(text)
    print(capitalized_text)  # Hello, world
    ```
    
- 인스턴스와 클래스 간의 이름 공간
    - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
    - 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인 이름 공간 생성**
    - 인스턴스에서 특정 속성에 접근하면, **인스턴스→클래스 순으로 탐색**

---

### 상속

- 클래스 상속
    - 동일한 메서드를 중복으로 정의할 필요 없이 상속을 통해 생략
    
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def talk(self):  # 메서드 재사용
            print(f'반갑습니다. {self.name}입니다.')
    class Professor(Person):
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
    class Student(Person):
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa
    
    p1 = Professor('박교수', 49, '컴퓨터공학과')
    s1 = Student('김학생', 20, 3.5)
    # 부모 Person 클래스의 talk 메서드를 활용
    p1.talk()  # 반갑습니다. 박교수입니다.
    # 부모 Person 클래스의 talk 메서드를 활용
    s1.talk()  # 반갑습니다. 김학생입니다.
    ```
    
- 다중 상속
    - 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
    - **중복된** 속성이나 메서드가 있는 경우, **상속 순서(MRO)에 의해 결정됨**
    
    ```python
    O = object
    class D(O): pass
    class E(O): pass
    class F(O): pass
    class B(D, E): pass
    class C(F, D): pass
    class A(B, C): pass
    
    # A 클래스의 상속 탐색 순서를 출력
    print(A.__mro__) # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.F'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>)
    # C3 선형화 규칙 -> 머리를 기준으로 다른 라인에 해당 머리가 머리가 아닌 곳에 있으면 건너 뜀!
    ```
    
- super()
    - 부모 클래스의 메서드를 편하게 호출하기 위해 사용하는 내장 함수
        - 단일 상속 구조
            - 명시적으로 이름을 지정하지 않고 부모 클래스 참조 가능하므로 편리
            - 클래스 이름이 변경되거나 부모 클래스가 교체돼도 super()사용하면 됨
        - 다중 상속 구조
            - MRO를 따른 메서드 호출
            - 복잡한 다중 상속 구조에서 발생할 수 있는 문제 방지
    
    ![image.png](attachment:7d98ce65-f74f-4335-a443-f0076e040735:image.png)
    
    ![image.png](attachment:399e06d5-eebd-400f-af93-af3abccbc6bd:image.png)
    

---

### 클래스 참고

- 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드
- 인스턴스가 사용해야 할 것
    - 인스턴스 메서드
    
- 매직 매서드
    - 특정 상황에서 **자동으로** 호출되는 메서드
    
    ```python
    class Circle:
    	def __init__(self, r):
    		self.r = r
    		
    	def __str__(self): # 숫자 r을 str로 변경해줌
    		return f'원의 반지름: {self.r}'
    print(Circle(10)) # -> 원의 반지름: 10
    
    # __str__안했으면 <__main__.Circle object at 0x00000203163C3690>
    ```
    

- 데코레이터
    - 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수
    
    ```python
    def my_decorator(func):
        def wrapper():
            # 함수 실행 전에 수행할 작업
            print('함수 실행 전')
            # 원본 함수 호출
            result = func()
            # 함수 실행 후에 수행할 작업
            print('함수 실행 후')
            return result
        return wrapper
    
    @my_decorator
    def my_function():
        print('원본 함수 실행')
    my_function()
    """
    함수 실행 전
    원본 함수 실행
    함수 실행 후
    """
    ```
    

---

### 제너레이터

- Iterator : 반복 가능한 객체의 요소를 하나씩 반환하는 객체

```python
my_str = 'abc'
my_iter = iter(my_str)

print(next(my_iter)) # a
print(next(my_iter)) # b
print(next(my_iter)) # c
print(next(my_iter)) # StopIteration
```

- Generator : 이터레이터를 간단하게 만드는 함수
    - 메모리 효율성 Good - return과 다르게 한 번에 한 개의 값만 생성 → 대용량 데이터 처리에 유용
    - 무한 시퀀스 처리 - 무한 루프를 통해 무한 시퀀스 생성 가능
    - 지연 평가 - 필요할 때만 값 생성 → 불필요한 계산 피하고 성능 최적화 가능
    - 클래스 기반의 이터레이터 만들 필요 없이 `__iter__()`, `__next__()` 메서드가 저절로 만들어짐
    
    ```python
    # 제너레이터 구조
    def generate_numbers():
    	for i in range(3):
    		yield i
    
    for number in generate_numbers():
    	print(number) # 0 1 2
    	
    
    # 제너레이터 활용1
    def infinite_sequence():
    	num = 0
    	while True:
    		yield num
    		num += 1
    
    gen = infinite_sequence()
    print(next(gen)) # 0
    print(next(gen)) # 1
    print(next(gen)) # 2		
    
    # 제너레이터 활용2
    nums = (i for i in range(int(1e6)))
    ```
    

---

### 에러와 예외 처리

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
# 0으로 나눌 수 없습니다.
```

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
```

---

### 모듈

- 한 파일로 묶인 변수와 함수의 모음
- 모듈 가져오는 방법
    - `import math
    print(math.sqrt(4))`
    - `from math import sqrt
    print(sqrt(4))`

---

### 패키지

- 연결된 모듈들을 하나의 디렉토리에 모아 놓은 것
- 내부 패키지
    - 바로 import
- 외부 패키지
    - pip로 설치 후 import

---

### 파일 읽고 쓰기

- 파일 열기와 닫기
    - open 함수로 파일을 열어서 파일 객체를 반환
    - wirte 메서드를 사용하여 파일을 쓰고
    - close 메서드를 사용하여 파일을 닫음
        - with 키워드를 사용해 파일을 사용한 뒤 close 메서드 없이자동으로 파일 객체를 닫을 수 있음
- 파일 쓰기 읽기
    
    ```python
    # 쓰기
    with open('example.txt', 'w', encoding='utf-8') as file:
        file.write('Hello, World!')
    
    # 읽기
    with open('example.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)
    ```
    
    ![image.png](attachment:f6fcd9d7-09bb-4db2-87a3-68f3cacce8c8:image.png)
    

- CSV 파일 처리
    
    ```
    import csv
    
    # CSV 파일 쓰기
    with open('example.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', 30, 'New York'])
        writer.writerow(['Bob', 25, 'Los Angeles'])
    
    # CSV 파일 읽기
    with open('example.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    ```
    
- JSON 파일 처리
    
    ```python
    import json
    
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    
    # JSON 파일 쓰기
    with open('example.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
    
    # JSON 파일 읽기
    with open('example.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
        print(type(data))  # <class 'dict'>
    ```
    

---

### 정규표현식

- 예시

```python
import re

pattern = r'\d+' # 숫자가 하나 이상인 패턴
text = 'There are 24 apples and 42 oranges.'

matches = re.findall(pattern, text)
print(matches) # ['24', '42']
```

![image.png](attachment:3703bb7b-e566-4e0a-8e96-ea836bc4466c:image.png)

![image.png](attachment:f8602a4d-fcb4-48ae-ac1a-f61a495f0141:image.png)

![image.png](attachment:bf8ccac1-6f62-4b1f-a7dd-1b75386295e6:image.png)