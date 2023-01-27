from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.question import question_router
app=FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)

#http://localhost:5173/ 그냥 이용하면됨 버전차이 였음
#코드 저장해주고 웹페이지 새로고침해줘야 적용됨