### 웹

- Web page 구성 요소
    - HTML(Structure)
    - CSS(Styling)
    - Javascript(Behavior)

### 웹 구조화

- HTML(**H**yper**T**ext **M**arkup **L**anguage)
    - 웹 페이지의 의미와 구조를 정의하는 언어
    - HyperText
        - 웹 페이지를 다른 페이지로 연결하는 링크(하이퍼링크랑 비슷)
    - Markup Language
        - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어(ex - HTML, Markdown)
            - <h1>HTML</h1>
            - <p>HTML이란 …</p>
- HTML 구조
    
    
    - <!DOCTYPE html>
        - 해당 문서가 html로 문서라는 것을 나타냄
    - <html></html>
        - 전체 페이지의 콘텐츠를 포함
    - <title></title>
        - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
    - <head></head>
        - HTML문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터를 작성
        - 사용자에게 보이지 않음
    - <body></body>
        - HTML문서의 내용을 나타냄
        - 페이지에 표시되는 모든 콘텐츠를 작성
        - **한 문서에 하나**의 body 요소만 존재
    
    ![image.png](attachment:081083e8-2ff5-4628-8828-7b9686cd794e:image.png)
    

- HTML 요소
    
    ![image.png](attachment:f35375d8-cdc5-41ea-b3ee-1b44172e8c1a:image.png)
    

- HTML 속성
    
    ![image.png](attachment:c9bacfa3-71a0-4219-864f-28a77a572561:image.png)
    
    - 대소문자 구분 못함. **소문자로 통일!**
    - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
    - 속성 값은 열고 닫는 따옴표로 감싸야 함
- Text Structure
    - HTML의 주요 목적 중 하나는 **텍스트 구조와 의미**를 제공하는 것
    - Heading & Paragraphs
        - h1~6, p
    - Lists
        - ol, ul, li
    - Emphasis & Importance
        - em, strong
        

### 웹 스타일링

- CSS(Cascading Style Sheet)
    - 웹 페이지의 디자인과 레이아웃을 구성하는 언어
    - CSS를 적용하지 않은 웹 사이트 모습
        
        ![image.png](attachment:8ffd7233-31ce-4c62-829d-f49cac7a1d2a:image.png)
        
    - CSS 구문
        
        ```html
        h1 {
        	color : red;
        	font-size: 30px;
        }
        # **h1 : 선택자**, font-size: 속성, 30px: 값
        ```
        
    - CSS 적용 방법
        - ~~인라인 스타일~~
        - 내부 스타일 시트
            - head 태그 안에 style 태그에 작성
        - 외부 스타일 시트
            - 별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

- **CSS Selectors**
    - HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
    - 기본 선택자
        - 전체 - ‘*’
            - HTML 모든 요소를 선택
        - 요소(tag)
            - 지정한 모든 태그를 선택
        - **클래스(class) - ‘.’**
            - 주어진 클래스 속성을 가진 모든 요소를 선택
        - 아이디(id) - ‘#’
            - 주어진 아이디 속성을 가진 요소 선택
            - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
        - 속성(attr)
    - 결합자
        - 자손 결합자(” “ (space) )
            - 첫 번째 요소의 자손 요소들 선택
                - p span은 <P> 안에 있는 모든 <span>를 선택 (**하위 레벨 상관 없이**)
        - 자식 결합자 (”>”)
            - 첫 번째 요소의 직계 자식만 선택
                - ul > li은 <ul> 안에 있는 모든 <li>를 선택 (**한 단계 아래 자식들만**)

- **명시도**
    - 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
        - CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
        - 동일한 요소를 가리키는 2개 이상의 CSS규칙이 있는 경우, 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨
            - VScode 상에서 마우스 올려놓으면 명시도 보임
    - 명시도 높은 순
        - **Importance(!important)** > Inline 스타일 > 선택자(id > class > 요소) > 소스 코드 선언 순서

- 상속
    - 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
    - 상속되는 속성
        - Text 관련 요소(font, color, text_align), opacity, visibility 등
    - 상속되지 않는 속성
        - Box model 관련 요소(width, height, border, ..)
        - position 관련 요소(position, top/right/bottom/left. ..)

### CSS Box Model

- 웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델
    
    ![image.png](attachment:f7976f3f-5e2b-46fa-ac0a-5fe8d97761c6:image.png)
    
    원은 네모박스를 깎은 것
    
- 박스 타입
    - Block box
    - Inline box
    - 박스 표시 타입
        - Outer display type
            - `display: block`
                - **항상 새로운 행으로** 나뉨
                - width와 height 속성 사용 가능
                - padding, margin, border로 인해 **다른 요소를 상자로부터 밀어냄(block)**
                - width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
                    - 한 row에 두 개의 box를 만들 수 없음
                    - h1 ~ h6, p, div
            - `display: inline`
                - **새로운 행으로 넘어가지 않음**
                - width와 height 속성을 사용할 수 없음(display가 block인 부모 요소의 height를 따라감 - 불변형) ( 앞 쪽의 content에 따라 바뀜 - 가변형)
                    - 수직 방향으로는 padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
                    - 수평 방향으로는 padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음(CSS is Awesome)
                    - a, img, span, strong, em
        
        - Normal flow - 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식
            
            ![image.png](attachment:9f80777e-b504-4523-b0f1-8d8a9222001a:image.png)
            

---

### 참고

- 그림으로 보는 명시도
    
    ![image.png](attachment:80aab414-eb60-48d0-a7fd-9b15033a9caf:image.png)
    

- HTML 스타일 가이드
    - 소문자 사용 강력히 권장
    - 속성 값에는 큰 따옴표를 사용하는 것을 권장
    - 일관된 들여쓰기 사용 (보통 2칸 공백)
    - 각 요소는 한 줄에 하나씩 작성
    - 중첩된 요소는 한 단계 더 들여쓰기
    - HTML은 연속된 공백을 하나의 공백으로 처리
    - HTML은 문법 오류가 있어도 별도의 **에러 메시지를 출력하지 않음**

- CSS 스타일 가이드
    - 마지막 속성 뒤에는 세미콜론(;) 넣기
    - 선택자 사용
        - class 선택자를 우선적으로 사용
        - id, 요소 선택자 등은 가능한 피할 것