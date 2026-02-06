from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from src.config.db import db

templates=Jinja2Templates(directory="templates")

router=APIRouter()

@router.get('/ftn')
def show_welcome_page(request: Request):
    return templates.TemplateResponse("welcome.html",{'request':request})


@router.get('/signup')
def show_signup(request: Request):
    if request.cookies.get('user_session'):
        return templates.TemplateResponse("dashboard.html", {'request':request})
    return templates.TemplateResponse("signup.html",{'request':request})

@router.post('/signup')
def get_signup(request: Request,email=Form(...),password=Form(...)):
    result=db.auth.sign_up({
        "email": email,
        "password": password
    })
    response=templates.TemplateResponse("dashboard.html", {'request':request})
    response.set_cookie(key="user_session",value=result.session.access_token,max_age=3600)
    return response

@router.get('/signin')
def show_login_page(request: Request):
    #if request.cookies.get('user_session'):
    return templates.TemplateResponse("signin.html", {'request':request})
    #return templates.TemplateResponse("signup.html",{'request':request})

@router.post('/signin')
def get_login_page(request: Request,email=Form(...),password=Form(...)):
    result=db.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    response=templates.TemplateResponse("dashboard.html", {'request':request})
    #response.set_cookie(key="user_session",value=result.session.access_token,max_age=3600)
    return response
