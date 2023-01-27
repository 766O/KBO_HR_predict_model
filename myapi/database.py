
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLCHEMY_DATABASE_URL='sqlite:///./myapi.db'
#데이터베이스 접속주소=데이터베이스의 파일,프로젯트 루트 디렉토리에 저장한다는 의미

#커넥션 풀 생성
#커넥션 풀? > 데이터베이스에 접속하는 객체 일정만큼 만들어 놓고 돌려가며 사용하는것
engine=create_engine(

    SQLCHEMY_DATABASE_URL,connect_args={'check_same_thread':False}
)

#데이터베이스 접속하기 위해 필요한 클래스
#데이터확인하고 수정하기 위해 autocommit False 설정
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#데이터베이스 모델 구성위한 클래스
Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()