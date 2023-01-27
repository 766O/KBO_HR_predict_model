from sqlalchemy import Column,Integer,String,Text,DateTime,ForeignKey

from sqlalchemy.orm import relationship

from database import Base

#모델틀래스는 database 에서 정의한 Base 클래스를 상속해서 만듬
class Question(Base):
    #모델에 의해 관리되는 테이블의 이름
    __tablename__ = "question"
    #테이블의 속성
    #게시글의 id,숫자 primary_key는 id 속성을 기본 키(Primary Key)로 만든다. 기본 키는 데이터베이스에서 중복된 값을 가질 수 없게 만드는 설정
    #데이터 타입이 Integer이고 기본키로 설정한 속성은 값이 자동으로 증가하는 특징도 있어서 데이터를 저장할 때 값을 세팅하지 않아도 1씩 자동으로 증가되어 저장
    #nullable => 속성에 null값 허용 X
    id=Column(Integer,primary_key=True)
    #게시글의 제목
    subject=Column(String,nullable=False)
    #게시글의 내용
    content=Column(Text,nullable=False)
    #게시글의 작성일자
    create_date=Column(DateTime,nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
