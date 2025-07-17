# Git - 분산 버전 관리 시스템
## 버전 관리
- 변화를 기록하고 추적하는 것

## 분산
- 중앙 집중식
  - 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드
- 분산식
  - 버전을 여러 개의 복제된 저장소에 저장 및 관리
--> 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구

## Git의 영역
1. Working Directory
    - 실제 작업 중인 파일들이 위치하는 영역
2. Staging Area
    - Working Directory에서 **변경된** 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
3. Repository
    - 버전 이력과 파일들이 영구적으로 저장되는 영역 
    - 모든 버전과 변경 이력이 기록됨
- commit : 변경된 파일들을 저장하는 행위

## Git의 동작
- `git init` : 로컬 저장소 설정/초기화 (git의 버전 관리를 시작할 디렉토리에서 진행)
    - git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것.
    - 즉, 이미 git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것. (밖의 git의 내부 git의 변경 사항 추적 불가능)
        - `rm -rf ~/Desktop/.git` -> git init 취소 코드?
- `git add` : 변경 사항이 있는 파일을 staging area에 추가
    - 잘못 수정했으면 다시 add로 해당 파일을 staging area에 추가하면 원상 복구 됨
- `git status` : 현재 git 상태
- `git commit -m '파일명'` : staging area에 있는 파일들을 저장소에 기록
    - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
    - commit을 생성하기 위해서는 작성자 정보 필요 ↓
    - `git config --global user.email "메일주소"` -> 이메일 설정
    - `git config --global user.name "유저이름"` -> 이름 설정
    - `code ~/.gitconfig` -> 설정한 코드 내용 창 열기
        - `git config --global -l` -> git global 설정 정보 보기
    - `git log` -> commit한 내용 확인
        - log가 너무 많아서 터미널 창이 안넘어가면 `q`
        - `git log --oneline` -> commit 목록 한 줄로 보기

## Remote Repository
- 원격 저장소 : 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간
    - GitLab(ssafy 과제 제출), GitHub(개인 포트폴리오 및 공부), Bitbucket
- `git remote add origin [url]` -> origin이라는 별칭을 사용해서 추가하는 원격 저장소의 url을 로컬 저장소에 추가

### GitHub
- Branch 생성 시, 이미 컴퓨터에서 local 작업 하고 있으면 Add a README file 체크 X
- GitHub에 이미 push한 상태에서 이 파일을 수정했으면, 다시 add, commit, push하면 됨
    - `git add .` : 현재 작업 디렉토리에서 변경된 파일 모두 add
    - `git commit -m "파일명"` : staging area에 있는 파일들을 repository에 저장
        - 여기서 '파일명'은, 웬만하면 이전 버전에서 수정한 내용으로 정하면 좋음
    - `git push origin master` : repository에 저장된 내용들을 github에 저장(반영)
        - 위 코드로 한 번 push 했으면 다음에는 `git push`만 해도 push 됨
    - 집에서는 Git Bash에서 `git clone [url]` 입력하면 github에 push된 내용 복제됨
        - [url] : 내 github의 TIL의 https 주소
- `git clone`은 아예 해당 파일이 없을 때 내려받을 때 사용 
    - 일부 변경된 것만 최신화 하고 싶으면, `git pull`하면 됨
        - 어제 집에서 따로 작업해서 push했으면, 오늘 강의장에서 `git pull` 하면 강의장 컴퓨터에도 집에서 작업한 내용이 최신화 되는 것        


*잘못 입력해서 터미널에 문제가 생겨서 exit하는 명령어 : Ctrl + C*
    