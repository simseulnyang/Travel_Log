# <span id="top">TRAVEL_LOG</span>
여행을 사랑하는 당신의 이야기를 남겨주세요. 누군가에게 당신의 이야기는 꿈을 꾸게 하고 곧 그것을 현실로 만들어 줄 거에요.

## 개요
- ESTsoft 백엔드 양성과정 오르미 1기 개인 프로젝트로 진행한 Travel_Log입니다.
- Travel_Log는 여행을 좋아하는 사람들이 모여 자신들의 여행이야기를 솔직담백하게 기록하고, 정보를 공유하며, 공감하는 사람들끼리 소통하는 블로그 서비스입니다.

## 목차
:link: 1. <a href="#goal">프로젝트 목표</a>
:link: 2. <a href="#dev">개발환경 및 배포 URL</a>
:link: 3. <a href="#ins">설치 및 실행</a>
:link: 4. <a href="#tree">프로젝트 구조</a>
:link: 5. <a href="#task">개발기간 및 작업관리</a>
:link: 6. <a href="#ui">UI</a>
:link: 7. <a href="#erd">데이터베이스 모델링(ERD)</a>
:link: 8. <a href="#pages">페이지 기능</a>
:link: 9. <a href="#issues">개발하며 겪은 이슈</a>
:link: 10. <a href="#realization">느낀점</a>
<p align="right"><a href="#top">(Top)</a></p>
<hr>

## <span id="goal">1. 프로젝트 목표</span>
- 1차 목표 (현재)
    - Django 강의에서 배운 내용들을 복습하며, 프로젝트의 핵심인 블로그 게시글의 CRUD 기능 구현에 익숙해진다.
    - 제공된 GitHub repo의 HTML+CSS를 기본으로 UI 커스터마이징하고, FBV보다는 CBV를 사용하여 개발한다.
    - ERD 작성 툴을 사용하여 데이터베이스 구조를 설계한다.
<p align="right"><a href="#top">(Top)</a></p>

## <span id="dev">2. 개발환경 및 배포 URL</span>
 ### 개발환경
    - Django 4.2.3 (Python 3.11.3)
    - HTML5
    - CSS
    - JavaScript
    - sqlite3

 ### 배포 URL
    - 현재 미정
<p align="right"><a href="#top">(Top)</a></p>

## <span id="ins">3. 설치 및 실행</span>
- terminal에 명령어를 입력하여 실행한다.
- 설치 및 실행을 위한 단계는 6번까지 이다.
- 서버 중지 및 가상환경 비활성화를 위해서는 7번과 8번 명령어를 입력하면 된다.
```
# 1. 가상환경 생성 
#     => 가상환경설정이름에 설정하고자 하는 가상환경이름을 넣는다.
python -m venv 가상환경설정이름

# 2. 가상환경 활성화 => 커맨드 라인 앞에 (venv)가 생성됨
    # macOS
        source venv/bin/activate
    # PowerShell
        venv/Scripts/Activate.ps1
    # CMD
        call venv/Scripts/activate.bat
    # Git Bash
        source venv/Scripts/activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 데이터베이스 마이그레이션
python manage.py migrate

# 5. 개발 서버 실행
python manage.py runserver

# 6. 실행 주소
http://127.0.0.1:8000/

# 7. 개발 서버 중지 (win에서는 ctrl + c)

# 8. 가상환경 비활성화 => 커맨드 라인 앞에 (venv)가 사라짐
deactivate
```
<p align="right"><a href="#top">(Top)</a></p>

## <span id="tree">4. 프로젝트 구조</span>
- app/ : Django 애플리케이션의 기본적인 세팅 디렉토리
- blog/ : Blog 기능을 담당하는 애플리케이션 디렉토리
- static/ : CSS, JavaScript 등 정적파일이 들어있는 디렉토리
- templates/ : HTML 템플릿 파일 디렉토리
- user/ : User 기능을 담당하는 애플리케이션 디렉토리

```
TRAVEL_LOG
│
├─app
├─blog
│  ├─templates
│  │  └─blog
│  └─templatetags
├─readme
├─static
│  ├─css
│  └─img
├─templates
└─user
   └─templates
      └─user

```
<p align="right"><a href="#top">(Top)</a></p>

## <span id="task">5. 개발기간 및 작업관리</span>
 ### 개발 기간
    - 1차 : 2023-07-17 ~ 2023-07-20

 ### 작업관리
    - 마인드 맵(Focus on 기능구현)
    ![img](readme/Travel_Log_function.mindmap.png)
<p align="right"><a href="#top">(Top)</a></p>


## <span id="ui">6. UI</span>

## <span id="erd">7. 데이터베이스 모델링(ERD)</span>
![img](readme/Travel_Log_ERD.png)

## <span id="pages">8. 페이지 기능</span>
 - 상세 기능 설명은 페이지별 링크 연결해서 보여주기
 1`)` 메인화면
    - 로그인
    - 회원가입

 2`)` 게시글
    - 게시글 작성 페이지

## <span id="issues">9. 개발하며 겪은 이슈</span>
    내용
    결론

## <span id="realization">10. 느낀점 및 다음 계획</span>

- 2차 목표 (오르미 1기 끝나기 전까지)
    - 블로그
        - HashTag, Category 기능을 추가하여 게시글을 조회, 검색, 정렬 할 수 있다.
        - like(좋아요) 기능을 추가하여 관심있는 블로그 게시글에 표현할 수 있다.
        - Pillow 이미지 처리 라이브러리를 사용하여 이미지 등의 정적파일을 저장할 수 있도록 한다.
        - 프로젝트에 Toast-ui-editor합쳐 Markdown 문서를 편집할 수 있도록 한다.
    - 유저
        - Profile 관련 Model을 설정하고, User가 직접 이미지를 포함한 자신의 프로필을 설정할 수 있고, 해당 내용을 DB에 저장하여 관리할 수 있다.
        - 유저 본인이 본인의 비밀번호를 직접 수정할 수 있다.
        - 회원탈퇴를 원하는 경우 본인의 비밀번호를 입력하여 회원탈퇴를 진행할 수 있다.

<p align="right"><a href="#top">(Top)</a></p>