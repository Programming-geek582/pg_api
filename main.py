import fastapi, helpers
from fastapi import staticfiles, templating

# initialise a fastapi instance
app = fastapi.FastAPI(docs_url="/api/v2/docs", title="PG Api", description="A modular rest api for basic api intergrations in your bot.", version="2.0", redoc_url="/api/v2/redoc")
app.mount('/static', staticfiles.StaticFiles(directory="static"), "static")
templates = templating.Jinja2Templates(directory="templates")

@app.route('/')
async def home(request : fastapi.Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.route('/docs')
async def documentation(request : fastapi.Request):
    return templates.TemplateResponse('docs.html', context={"request" : request})

@app.route('/developer')
async def credits(request : fastapi.Request):
    return templates.TemplateResponse('dev.html', context={"request" : request})

@app.get('/api/v2/joke/programming', tags=['fun'])
async def get_programming_joke(request : fastapi.Request):
    # get a programming joke
    joke = helpers.get_programming_joke()

    # return the json response containing the joke
    return {
        "joke" : joke
    }

@app.get('/api/v2/kill', tags=['fun'])
async def kill(request : fastapi.Request, user_name : str, your_name : str):
    statement = helpers.kill(user_name, your_name)
    return {
        "message" : statement
    }

@app.get('/api/v2/eightball', tags=['fun'])
async def eightball(request : fastapi.Request, *, question : str):
    answer = helpers.eightball(question=question)
    return {
        "question" : question,
        "answer" : answer
    }

@app.get('/api/v2/pickup_line')
async def pickup_line(request : fastapi.Request):
    return {
        "pickup_line" : helpers.get_pickup_line()
    }