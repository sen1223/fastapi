from concurrent.futures.thread import _worker
import uvicorn
from fastapi import FastAPI

from tutorial import app03, app04, app05, app06, app07, app08

app = FastAPI()

app.include_router(app03, prefix='/chapter03', tags=['chapter03'])
app.include_router(app04, prefix='/chapter04', tags=['chapter04'])
app.include_router(app05, prefix='/chapter05', tags=['chapter05'])
app.include_router(app06, prefix='/chapter06', tags=['chapter06'])
app.include_router(app07, prefix='/chapter07', tags=['chapter07'])
app.include_router(app08, prefix='/chapter08', tags=['chapter08'])

# uvicorn run:app --reload

if __name__ == '__main__':
    uvicorn.run('run:app', host= '0.0.0.0', port=8000, reload=True,
    debug=True, workers=1)

