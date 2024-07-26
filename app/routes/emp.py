from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.schema.emp import Employee
# 라우터 생성
emp_router = APIRouter()
# 템플릿지정
templetes = Jinja2Templates(directory='views/templates')

# 라우트 설정
@emp_router.get('/', response_class=HTMLResponse)
async def emp(req: Request):
    return templetes.TemplateResponse('emp/emp.html', {'request': req})

@emp_router.post('/', response_class=HTMLResponse)
async def empok(req: Request,
              empid : int = Form(...), fname : str = Form(...),
              lname : str = Form(...), email : str = Form(...),
              phone : str = Form(...), hdate : str = Form(...),
              jobid : str = Form(...), sal: int = Form(...),
              comm : float = Form(...), mgrid: int = Form(...),
              deptid : int = Form(...)):
     print(empid,fname,lname,email,phone,hdate,jobid,sal,
           comm,mgrid,deptid)

     comm = float(comm) if comm != '0' else None
     mgrid = int (mgrid) if mgrid != '0' else None
     deptid = int(deptid) if deptid != '0' else None

     emp = Employee(empid =empid, fname =fname, lname = lname,
            email =email, phone= phone, hdate =hdate,
            jobid = jobid, sal= sal, comm =comm, mgrid= mgrid,
            deptid = deptid)


     return templetes.TemplateResponse('emp/result.html',
           {'emp':emp , 'request': req})

