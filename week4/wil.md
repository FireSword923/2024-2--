# 4주차에서 배운 것
## 데이터베이스(DataBase, DB)
일련의 데이터들을 모아놓고, 분류 및 관리하는 공간을 **데이터베이스**(DB)로, 그냥 메모장에 양식대로 기록한 것 역시 DB라고 할 수 있다.

### 데이터베이스 관리 시스템(DataBase Management System, DBMS)
**양식에 맞는 정보만 읽어들이고. DB에서 특정 정보를 꺼내주는 소프트웨어.**

데이터를 메모리에 저장할지 디스크에 저장할지, 딕셔너리로 저장할지 스트링으로 저장할지 등등이 **DBMS** 종류에 따라 다르다.

## 관계형 데이터베이스(Relational DBMS. RDBMS)
데이터를 **table** 형식으로 정리해놓는 DBMS이다. 가로줄과 세로줄을 각각 **row, column**라고 표현한다.

장점으로는

    1. 데이터 구조화
    2. 중복 데이터 최소화
이 있다.

사용할 수 있는 명령어는
    
    SELECT [정보] from [DB] where [variable]=[value]
    
    insert into [DB] [value]

    delete from [DB] where [variable]=[value]

등등이 있다. 이를 **SQL**(Structured Query Language)이라고 한다.

장고를 이용하여 웹을 만들경우, models에서 알아서 DB를 관리하므로 위 명령어를 쓸 일은 없다.

### 기본 키(Primary Key, PK)
각각의 row들을 구분해주는 데이터가 있어야한다. 그러한 데이터의 특징은

    1. 고유한 값
    2. 잘 변경 안됨
    3. 모든 로우가 가져야 함
등이 있다.

이러한 데이터를 **기본 키(Primary Key, PK)**라고 한다.

#### 자작 PK인 ID
DB에 추가되는 순서에 따라 할당되는 데이터. PK로 쓸만한 데이터가 없을 때의 대안 중 하나다.

#### 다른 Table의 Pk, 즉 외래 키(Foregin Key, FK) 사용
ID를 사용하는 것에는 한계가 있기 때문에, 여러 Table **a, b**를 만들고, **b**에 있는 PK를 **a**에 저장해놓는 방법 역시 대안이 될 수 있다. 이 때 **a**는 외부 Table인 **b**의 **PK**를 사용하므로, 이 Key를 **외래 키**(Foregin Key, FK)라고 한다.

## 파이썬 파일의 from 명령문의 시작지점
저번 주차에서는 manage.py를 시작점으로 한다고 했으나, 사실 manage.py보다 먼저 살펴보는 곳이 있다.

    1. 일단 가상환경 내에서 파일을 찾아봄
    2. 없으면 manage.py를 기준으로 파일을 찾음
이러한 방식이다.

## 동적 html 생성
사용자에 따라 다른 데이터를 포함하는 html을 만들고자 할 때는, views파일에 적혀있는

    return render([이 함수의 매개변수], [html 파일])
이 부분에서 인수를 하나 더 주면 된다. 예를 들어,

    name = 'kim'
    context = {'name' : name}
같이 딕셔너리를 만들어서 이 딕셔너리를 html에 넘겨주고 싶다면, return문을

    return render([이 함수의 매개변수], [html 파일], context)
로 바꿔주면(인수를 하나 더 써주면) html이 이 정보를 받을 수 있다.

html파일에서 이 정보를 이용하려면 {{[받은 딕셔너리의 key]}} 를 태그 안에 넣으면 된다.

## DB 만들기
models 파일에 dango.db의 models를 import 한 후, models.Model을 상속하는 클래스를 만들어서 Table의 각 데이터 이름의 변수를 할당하고 그 변수에다 그 데이터의 형식 (ex: models.CharField(max_length=200))을 할당한다.

그 이후 터미널에 
    
    python manage.py makemigrations
를 입력한 후

    python manage.py migrate
를 입력해 데이터베이스 파일을 생성할 수 있다.

## 어드민 계정 생성
터미널에

    python manage.py createsuperuser
를 입력하면 관리자 이름, 이메일 주소(선택), 비밀번호를 입력하도록 한다. 모두 입력하면 어드민 계정이 생성된다.

## 어드민 등록
admin파일에 DB 관련 클래스가 있는 models 파일에 있는 그 클래스를 import한 후, 
    
    admin.site.regoster([DB 관련 클래스 이름])
을 추가해준다.

그 이후 사이트 url의 경로를 admin으로 지정해서 접속해보면 