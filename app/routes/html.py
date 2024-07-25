from fastapi import APIRouter ,Request
from starlette.templating import Jinja2Templates

# 라우터 생성
html_router = APIRouter()
# 탬플릿 지정
templetes = Jinja2Templates(directory='views/templates')

# 라우트 설정
@html_router.get('/')
async def layout(req: Request):
    return templetes.TemplateResponse('html/index.html', {'request': req})

@html_router.get('/layout')
async def layout(req: Request):
    return templetes.TemplateResponse('html/01layout.html', {'request': req})