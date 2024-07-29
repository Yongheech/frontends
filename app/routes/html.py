from fastapi import APIRouter, Request, Form
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

@html_router.get('/image', response_class=HTMLResponse)
async def image(req: Request):
    return templates.TemplateResponse('html/06image.html', {'request': req})

@html_router.get('/form', response_class=HTMLResponse)
async def form(req: Request):
    return templates.TemplateResponse('html/07form.html', {'request': req})

@html_router.post('/formproc')
async def formok(req: Request, userid:str = Form(...), passwd:str = Form(...)):
    print(f'회원가입 정보가 서버로 전송됨  : {userid} {passwd}')
    return templates.TemplateResponse('html/07form.html', {'request': req})

@html_router.get('/joinfrm')
async def joinfrm(req: Request):
    return templates.TemplateResponse('html/08joinfrm.html', {'request': req})

@html_router.get('/semantic')
async def semantic(req: Request):
    return templates.TemplateResponse('html/09semantic.html', {'request': req})

