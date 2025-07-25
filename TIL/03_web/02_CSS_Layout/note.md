### CSS Box Model

- 웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델
    - 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되어 요소의 크기와 배치를 결정
    
    ![image.png](attachment:c4f46077-50ab-4aa8-98ba-5173dc941147:image.png)
    
    - margin: 25px auto; → 상하 25px, 좌우 auto(페이지 크기에 따라 자동으로 좌우 정렬)
    
- shorthand 속성
    - border
        - border-width, border-style, border-color를 **한번에** 설정하기 위한 속성(순서 무관)
            - border: 2px solid black;
    - margin & padding
        - 네 가지 방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성
        - 4개 - 상/우/하/좌(시계방향)
            - margin: 10px 20px 30px 40px;
        - 3개 - 상/좌우/하 (응)
            - padding: 10px 20px 30px;
        - 2개 - 상하/좌우
            - margin: 10px 20px;
        - 1개 - 공통
            - padding: 10px;

- box-sizing 속성
    - 표준 상자 모델에서 width와 height 속성 값을 설정하면 이 값은 content box의 크기를 조정하게 됨, 디폴트 값은 content-box
    - 하지만 border-box에서는 width와 height로 실제 상자의 너비와 높이 지정
        
        ![image.png](attachment:c66cde12-127d-488b-9cee-7f00646496d1:image.png)
        
    - `box-sizing: border-box` 고정!! (`* {box-sizing: border-box}`)

- 기타 display 속성
    - `display: inline-block`
        - inline과 block 요소 사이의 중간 지점을 제공하는 display 값
        - width 및 height 속성 사용 가능
        - padding, margin, border로 인해 다른 요소가 상자에서 밀려남
            - but 새로운 행으로 넘어가지 않음
        - —> **요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용**
    - `display: none`
        - 요소를 화면에 표시하지 않고 공간조차 부여되지 않음
        
        ![image.png](attachment:bd7ac63a-ba1e-4dd4-82d1-80c789c71d88:image.png)
        

### CSS position

- 주 목적: 전체 페이지에 대한 레이아웃을 구성하는 것 보다는 **페이지 특정 항목의 위치를 조정**하는 것

- CSS Layout
    - 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
        - Display, Position, Flexbox
- CSS Position
    - 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
        - 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등
    - Position 유형
        - static
            - 원래 디폴트 값
        - relative
            - 원래 본인의 공간을 **삭제하지 않고**, 원래 본인 공간을 기준으로 요소만 이동
        - absolute
            - 원래 본인에 공간을 **삭제해버리고**, 화면 공간을 기준으로 요소를 이동
                - but 부모가 존재하면, 만약 부모들 중에 relative가 있으면 그 부모의 공간을 기준으로 요소 이동. 없으면 그냥 화면 공간을 기준으로 요소를 이동
        - fixed
            - 마우스 휠을 올리든 내리든 화면 상에서 지정한 위치에 고정
        - sticky
            - relative + fixed
        - 위 전부 top, right, bottom, left 속성으로 위치를 조정
        
- z-index
    
    ![image.png](attachment:4b376482-eadb-4fe4-9d4f-4b4d22f883d7:image.png)
    
    - 요소의 쌓임 순서(z축 순서)를 정의하는 속성
    - 값이 클수록 요소가 위에 쌓이게 됨
    - static이 아닌 요소에만 적용됨
    - 기본 값은 auto
    - 부모 요소의 z-index 값에 영향을 받음
        - 같은 부모 내에서만 z-index 값을 비교

### **!!CSS Flexbox!!**

![image.png](attachment:80d78f6d-320a-4898-ab19-d38ff10e1dc3:image.png)

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
    - → 공간 배열 & 정렬
- 박스 Display 타입 - Inner display type
    - 박스 내부의 요소들이 어떻게 배치될 지를 결정
    
    ![image.png](attachment:d3377ea0-e23d-4e63-8088-f1517d8a142d:image.png)
    

- 배치
    - flex-direction
        - flex item이 나열되는 방향(축)을 지정(`flex-direction: column`)
            - 기본값이 row
    - flex-wrap
        - flex item 목록이 flex container의 한 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정 ( `flex-wrap: wrap` )
- 공간 분배
    - justify-content
        - 주 축을 기준으로 flex item과 주위에 공간을 분배( `justify-content: center` / flex-start / flex-end )
    - align-content
        - 교차 축을 기준으로  flex item과 주위에 공간을 분배( `align-content: center` / flex-start / flex-end )
        - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
            - 적용 대상: 여러 줄
- 정렬
    - align-items
        - 교차 축을 기준으로 flex item 행을 정렬 (`align-items : center` )
            - 적용 대상: 개별 항목(요소 하나 하나)
    - align-self
        - 교차 축을 기준으록 개별로 flex item을 정렬
- justify-items 및 justify-self 속성은 margin auto로 가능하므로 필요 없음
- 속성명 tip
    - justify : 주 축
    - align : 교차 축

### 참고

- block 요소의 수평 정렬 - `margin: auto`
- Inline 요소의 수평 정렬 - `text-align: center`
- 내부 자식의 수직 정렬 → flex로 관리 추천

![image.png](attachment:643051fd-828e-4637-aebe-88d845770810:image.png)

![image.png](attachment:ec549a3d-db68-44a8-ad01-d257dacc6f3f:image.png)

![image.png](attachment:761db407-bc0c-4b46-b19e-b8cefec876c9:image.png)

![image.png](attachment:fdd9b1f2-3340-4eda-9f62-e37e9fe08677:image.png)

![image.png](attachment:72b1d591-16a6-4fdb-8caf-b32434c0ef9d:image.png)

![image.png](attachment:42d5a748-dca7-4122-ab92-13df17d15542:image.png)