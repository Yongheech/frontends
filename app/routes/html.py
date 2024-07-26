from fastapi import APIRouter ,Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
html_router = APIRouter()
# 탬플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@html_router.get('/', response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('html/index.html', {'request': req})

@html_router.get('/layout', response_class=HTMLResponse)
async def layout(req: Request):
    return templates.TemplateResponse('html/01layout.html', {'request': req})

@html_router.get('/text', response_class=HTMLResponse)
async def text(req: Request):
    return templates.TemplateResponse('html/02text.html', {'request': req})

@html_router.get('/link', response_class=HTMLResponse)
async def link(req: Request):
    return templates.TemplateResponse('html/03link.html', {'request': req})

@html_router.get('/list', response_class=HTMLResponse)
async def list(req: Request):
    return templates.TemplateResponse('html/04list.html', {'request': req})

@html_router.get('/table', response_class=HTMLResponse)
async def table(req: Request):
    return templates.TemplateResponse('html/05table.html', {'request': req})
