from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Starting the server
app = FastAPI()

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
