from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from .request_validations import Token, CreateUserRequest
from typing import Annotated
from sqlalchemy.orm import Session
from .utils import (
    get_db,
    authenticate_user,
    create_access_token,
    bcrypt_context,
    get_current_user,
    redirect_to_login
)
from starlette import status
from datetime import timedelta
from .models import Users

# Starting the server
app = FastAPI()

# Initializing the DB
Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]

# Importing the static css and js files
static_folder_path = "/Users/leventeharsanyi/Desktop/Herman_Support/static"
app.mount("/static", StaticFiles(directory=static_folder_path), name="static")

# Importing html templates files
templates_path = "/Users/leventeharsanyi/Desktop/Herman_Support/templates"
templates = Jinja2Templates(directory=templates_path)

###################################
############ MAIN PAGE ############
###################################
@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})


########################################
############ AUTHENTICATION ############
########################################
@app.get("/auth/login-page")
def render_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request":request})

@app.get("/auth/register-page")
def render_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request":request})

@app.post("/auth", status_code=status.HTTP_201_CREATED)
def create_user(db: db_dependency,
                create_user_request: CreateUserRequest):
    create_user_model = Users(
        email = create_user_request.email,
        username = create_user_request.username,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        role = "client",
        hashed_password = bcrypt_context.hash(create_user_request.password),
        is_active = True,
    )
    db.add(create_user_model)
    db.commit()

@app.post("/auth/token", response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                           db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user')
    token = create_access_token(user.username, user.id, user.role, user.first_name, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}


##############################
############ USER ############
##############################
@app.get("/user/home-page")
def render_todo_page(request: Request):
    try:
        user = get_current_user(request.cookies.get('access_token'))
        if user is None:
            return redirect_to_login()
        return templates.TemplateResponse("user.html", {
            "request":request,
            "user": user
        })
    except:
        return redirect_to_login()
