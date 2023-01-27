from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database import SessionLocal

from database import get_db
from domain.question import question_schema
from domain.question import question_crud
# 라우터 파일에 반드시 필요한 것은 APIRouter 클래스로 생성한 router 객체이다.
# router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작한다.
#라우팅? FastApi 가 요청받은 url 해석해서 그에 맞는 함수 실행,결과 리턴하는 행위
router=APIRouter(
    prefix="/api/question",
)

#/api/question/list 라는 URL 요청이 발생하면
# /api/question 이라는 prefix가 등록된 question_router.py 파일의
# /list로 등록된 함수 question_list가 실행되는 것이다.

#question_list 함수는 db 세션을 생성하고 해당 세션을 이용하여 질문 목록을 조회하여 리턴하는 함수
@router.get("/list",response_model=list[question_schema.Question])
def question_list(db:Session=Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list