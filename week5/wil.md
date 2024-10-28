# 5주차에서 배운 것
## 장고 Model로 테이블 만들기
models.py에 클래스를 생성하면 장고가 클래스를 토대로 DB 테이블을 생성한다.

예시:

    from django.db import models

    class Question(models.Model):
        subject = models.CharField(max_length=200)
        content = models.TextField()
        created_date = models.DateTimeField()
또한 DB 테이블에서 값을 조회할 때 models.py에 만들어 놓은 객체에 값을 담아 반환해준다. 더 자세한 내용은 week4의 wil.md에 적혀있다.

## 장고 ORM 사용법
views.py에서, models에 만들어둔 클래스를 import하고, 변수에 [클래스 이름].objects를 이용해 DB에 저장된 값에 접근할 수 있다.

## objects의 메서드들
세 개의 메서드 중 두 개가 객체가 들어있는 리스트를 반환해주는 메서드이다. 따라서 html에서 이 리스트를 적극적으로 활용하기 위해선 <ol>, <ul>, <li>, {%for A in B%} ~~ {%endfor%}를 활용할 수 있다. 이것들에 대해서는 좀 나중에 기술할 예정이다.
### 리스트 형태 objects.all()
모든 테이블 정보를 객체로 만들어 **리스트**에 넣어 반환한다.

### 리스트 형태 objects.filter()
조건에 맞는 정보들을 객체로 만들어 **리스트**에 넣어 반환한다. get()과의 차이점은 여러 개의 객체가 리스트로 반환된다는 점이다.

예시:
    question = Question.objects.filter(id = question_id)

### objects.get()
조건에 맞는 데이터를 객체로 만들어 반환한다.

예시:
    question = Question.objects.get(id = question_id)
위 예시는 id값이 question_id인 데이터를 객체로 만들어 반환하는 메서드이다. 위의 filter()와의 차이점은 하나의 객체가 그대로 반환된다는 점이다.

## 동적 html 생성
views.py의 render함수에서, html 경로 뒤에는 **dictionary** 타입의 데이터를 넘겨줄 수 있다. 이 외의 타입은 안 된다.

### 넘겨받은 데이터를 html에서 사용하기
넘겨받은 데이터를 쓰고자 한다면 html 파일 내에서 {{[key]}}을 입력해서 사용할 수 있다. 이렇게 해서 html의 메세지를 상황에 따라 다르게 나오도록 할 수 있다.

### render함수의 인자
첫 번째 인자: HTTP Request 객체

두 번째 인자: 응답할 html 파일 이름

세 번째 인자: 동적 html에 사용할 dictionary

## 자주 쓰는 html 태그
### h1, h2, h3
제목을 생성해주는 태그, 숫자가 커질수록 글자 크기가 작아진다.

예:
    <h1>Hello World</h1>

### p
paragraph, 한 단락을 생성해주는 태그. 해당 태그의 위아래로 빈 줄이 생긴다.

예:
    <p>Hi</p>

### a
하이퍼링크를 걸어주는 태그로, href 속성 안에 지정된 링크로 하이퍼링크가 연결된다.

예:
    <a href='www.google.com'>구글 접속</a>
"구글 접속"이라는 글자가 파란 색으로 하이라이트되며, 해당 글자 클릭 시 지정된 링크로 이동한다.

### ul, ol, li
리스트를 만들어 주는 태그. ul 또는 ol 태그 안에 li 태그를 또 다시 넣어 리스트를 만든다.

**ol(ordered list)**는 순서가 있는 리스트이고, **ul(unordered list)**는 순서가 없는 리스트이다.

예시:
    <ul>
        <li>이혁</li>
        <li>김성훈</li>
        <li>홍길동</li>
    </ul>
    <ol>
        <li>이혁</li>
        <li>김성훈</li>
        <li>홍길동</li>
    </ol>

### div
그냥 레이아웃을 나눠주는 태그. CSS를 위해 자주 사용되는 태그다.

### form, input
form 태그를 통해 action 속성의 url을 목적지로 하여, form 태그 안 input 태그에서 입력받은 데이터를 전송한다.

예:
    <form action="localhost:8000/create">
        <input type="text"/>
        <input type="submit"/>
    </form>

## 장고 템플릿
html의 태그를 동적으로 하는 건 불가능하지만, 태그 안 내용을 동적으로 바꾸는 건 가능하다. 사용법은 위에 써있듯, dictionary 변수를 만들어 render함수에 해당 변수를 세 번째 인자로 준 후 html파일에서 {{[key]}}을 통해 사용 가능하다. [key]는 views.py에서 지정한 key다.

### {%for A in B%} ~~ {%endfor%}
html에 쓰는 문법으로, 파이썬의 for문과 매우 비슷하다. 중괄호 사이에 있는 내용들을 B에 남은 원소가 없을 때까지 반복적으로 실행한다.