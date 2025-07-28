### 변수데이터 타입

- 식별자(변수명) 작성 규칙
    - 반드시 문자, 달러(’$’), 또는 밑줄(’_’)로 시작
    - 대소문자 구분
    - 예약어 사용 불가 (for, if, function,..)
- 변수 선언 키워드
    - let - **재할당이 필요하다면** 그때 const가 아닌 let으로 변경해서 사용
        - block scope를 갖는 지역 변수를 선언
        - 재할당은 가능하지만, 재선언은 불가능
            
            
            - let number = 10
            number = 20 → 가능
            
            - let number = 10
            let number = 20  → 불가능
    - **const - 기본적으로 const 사용을 권장(자료형은 못바꾸지만 객체 안의 값은 조작 가능하므로)**
        - block scope를 갖는 지역 변수를 선언
        - 재할당과 재선언 모두 불가능 → 최초로 변수 선언 시 **반드시 초기값 설정 필요**!
    - ~~var~~
- block scope
    - if, for, 함수 등의 중괄호 내부를 가리킴 ( 블록 바깥에서 접근 불가능)
        
        ```html
        let x = 1
        
        if (x===1) {
        	let x = 2
        	console.log(x) // 2
        }
        
        console.log(x) // 1
        ```
        
    
- 데이터 타입
    - 원시 자료형
        - 변수에 값이 직접 저장되는 자료형(불변, 값이 복사됨)
            - Number, String, Boolean, null, undefined
            
            ![image.png](attachment:d86923a7-ba61-4f5a-be35-536b7f82036e:image.png)
            
    - 참조 자료형
        - 객체의 주소가 저장되는 자료형(가변, 주소가 복사됨)
            - Objects (Object, Array, Function)
            
            ![image.png](attachment:9d82cf6e-fbe2-4c27-a3a2-84f27a97dcaa:image.png)
            

- 원시 자료형( Number, String, null, undefined, Boolean)
    - `typeof null` —> “object”
    - 템플릿 리터럴(python에서 f-string)
        
        ```html
        const age = 100
        const message = `홍길동은 ${age}세입니다.` // 백틱임
        console.log(message) // 홍길동은 100세입니다
        ```
        
    - null - 변수의 값이 없음을 의도적으로 표현할 때 사용
        
        ```html
        let a = null
        console.log(a) // null
        ```
        
    - undefined - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
        
        ```html
        let b
        console.log(b) // undefined
        ```
        
    - 자동 형변환
        
        ![image.png](attachment:df71f3b0-11a8-47b7-8b04-fb8dc7f661a0:image.png)
        

### 연산자

- 증가 연산자(’++’), 감소연산자(’- -’)
    - 피연산자를 증가 혹은 감소 시키고, 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
    - +=나 -=를 더 권장
- 비교연산자 - 기존과 동일
- 동등 연산자
    - == : 암묵적 타입 변환을 통해 **타입을 일치시킨 후** 같은 값인지 비교
    - === : 두 피연산자의 **값과 타입이 모두 같은** 경우 true
- 논리 연산자
    - and : &&, or: ||, not: !, 단축 평가 지원

### 제어문

- if
    - if - else if - else
    
    ```jsx
    const name = 'customer'
    
    if (name === 'admin') {
    	console.log('관리자님 환영해요')
    } else if (name === 'customer') {
    	console.log('고객님 환영해요')
    } else {
    	console.log(`반갑습니다, ${name}님`)
    }
    ```
    
- 삼항 연산자
    - condition ? expression1 : expression2
    - ?이 맞으면 expression1, 아니면 expression2
- while → 기존과 동일
    
    ```jsx
    let i = 0
    
    while (i<6) {
    	console.log(i)
    	i += 1
    }
    ```
    
- for - 특정한 조건이 거짓으로 판별될 때까지 반복
    - 여기서는 재할당이 사용되기 때문에 const가 아닌 let 사용!
    
    ```jsx
    for (let i=0; i<6; i++) {
    	console.log(i)
    }
    //1. 반복문 진입 및 변수 i 선언
    //2. 조건문 평가 후 코드 블럭 실행
    //3. 코드 블록 실행 이후 i 값 증가
    ```
    
- for … in - 객체의 열거 가능한 속성에 대해 반복(배열이 아닌 object 순회할 때만 사용)
    - 인덱스의 순서가 중요한 **배열에서는 사용하지 않음 → 배열은 for문 또는 for…of 사용**
    
    ```jsx
    const fruits = {a:'apple', b:'banana'}
    
    for (const property in fruits) {
    	console.log(property) // a,b
    	console.log(fruits[property]) // apple, banana
    }
    ```
    
- for … of - 반복 가능한 객체(배열,문자열 등)에 대해 반복
    
    ```jsx
    const numbers = [0,1,2,3]
    
    for (const number of numbers) {
    	console.log(number) //0,1,2,3
    }
    ```
    
    ![image.png](attachment:b8a42877-13ad-4a83-ad87-6be53e5309f9:image.png)
    

### DOM

- 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공하는 API → 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함
- 브라우저는 HTML 문서를 해석하여 DOM tree 라는 객체 트리로 구조화(객체 간 상속 구조가 존재)
    
    ![image.png](attachment:fd583652-168b-4348-a7fc-4c4e82536e12:image.png)
    

### DOM 선택

- 선택 메서드
    - document.querySelector(selector)
        - 제공한 선택자와 일치하는 element 한 개 선택
        - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
    - document.querySelectorALL(selector)
        - 요소 여러 개 선택
        - 제공한 CSS selector를 만족하는 NodeList를 반환
        
        ![image.png](attachment:ac7087cb-1497-4ca4-8da4-79deac35c28e:image.png)
        

### DOM 조작 → 과목평가에 안나옴

- 클래스 속성 조작 메서드
    - `element.classList.add()`
    - `element.classList.remove()`
    - `element.classList.toggle()`
        - 클래스가 존재한다면 제거하고 false를 반환
        - 클래스가 존재하지 않으면 클래스를 추가하고 true를 반환
- **일반 속성 조작 메서드 - 보통 이거 씀**
    - `Element.getAttribute()`
        - 해당 요소에 지정된 값을 반환(조회)
    - `Element.setAttribute(name, value)`
        - 지정된 요소의 속성 값을 설정
        - 속성이 이미 있으면 기존 값을 갱신, 없으면 지정된 이름과 값으로 새 속성이 추가
    - `Element.removeAttribute()`
        - 요소에서 지정된 이름을 가진 속성 제거
        
        ```jsx
        const aTag = document.querySelector('a')
        console.log(aTag.getAttribute('href')) // https://www.google.co.kr/
        
        aTag.setAttribute('href', 'https://www.naver.com/')
        console.log(aTag.getAttribute('href')) // https://www.naver.com
        
        aTag.removeAttribute('href')
        console.log(aTag.getAttribute('href')) // null
        ```
        
- DOM 요소 조작 메서드
    
    ![image.png](attachment:51df60ae-1120-4f43-abd5-9c76977e6a6a:image.png)
    
- ~~style 조작~~ → 저번주에 배운 css로 지정하는게 더 편함

### 함수

```jsx
# 선언식
function add (num1, num2) {
	return num1 + num2
}
add(1,2) // 3

# 표현식 -> 사용 권장(익명 함수 사용 가능, 호이스팅 없음)
const sub = function (num1, num2) {
	return num1 - num2
}
sub(2,1) // 1
```

 python과 다르게 return값이 없다면 undefined 반환

- 매개변수 정의 방법
    - 기본 함수 매개변수
        
        ```jsx
        const greeting = function (name = 'Anonymous') {
        	return `Hi ${name}`
        }
        greeting() // Hi Anonymous
        ```
        
    - 나머지 매개변수
        
        ```jsx
        const myFunc = function (param1, param2, ...restParams) {
        	return [param1, param2, restparams]
        }
        myFunc(1,2,3,4,5) // [1,2,[3,4,5]]
        myFunc(1,2) // [1,2,[]]
        ```
        
    - 매개변수와 인자 개수가 불일치 할 때 오류 발생 안하고 알아서 undefined 혹은 생략으로 처리함

- Spread syntax - ‘…’ ↔ python에서 패킹(’*’)

- 화살표 함수 - 함수 표현식의 간결한 표현법
    
    ![image.png](attachment:167afa44-33b0-418d-8c69-622913d81da4:image.png)
    
    1. function 키워드 삭제 후 화살표 작성

### 이벤트

- 무언가 일어났다는 신호, 사건 → 모든 DOM 요소는 이러한 event를 만들어 냄
- DOM 요소는 event를 받고 받은 evenet를 ‘처리’할 수 있음
- event handler - 이벤트가 발생했을 때 실행되는 함수
    - 사용자의 행동에 어떻게 반응할지를 JS 코드로 표현한 것
    
    ![image.png](attachment:b892b778-083d-4d76-9cf2-3d164a72d940:image.png)
    
    - 대상(EventTarget)에 특정 Event(type)가 발생하면, 지정한 이벤트를 받아 할 일(handler)을 등록
    
    ```jsx
    const btn = document.querySelector('#btn')
    
    const detectClick = function (event) {
    	console.log(event)
    	console.log(event.currentTarget)
    	console.log(this)
    }
    
    btn.addEventListener('click', detectClick)
    ```
    
- 버블링
    - 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
    - 가장 최상단의 조상 요소를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작
    - currentTarget → 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
    - target → 이벤트가 발생한 가장 안쪽의 요소를 참조하는 속성

- **이벤트의 기본 동작 취소하기**
    - `.preventDefault()`
    - 예: form 요소의 제출 이벤트를 취소하여 페이지 새로고침을 막을 수 있음
        
        ```jsx
        const formTag = document.querySelector('#my-form')
        
        const handleSubmit = function (event) {
        	event.preventDefault()
        	alert('새로고침 X')
        }
        
        formTag.addEventListener('submit', handleSubmit)
        ```