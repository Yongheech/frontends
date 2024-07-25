from fastapi import APIRouter
from starlette.templating import Jinja2Templates

# 라우터 생성
jscript_router = APIRouter()
# 탬플릿 지정
templetes = Jinja2Templates(directory='views/templates')

# 라우트 설정