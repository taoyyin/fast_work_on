# from datetime import datetime, timedelta, timezone
# from typing import Union
#
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status

from fastapi.middleware.cors import CORSMiddleware
from myapp import db_router
from toolsapp import toos_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(db_router.router)
app.include_router(toos_router.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == '__main__':
    uvicorn.run(app="fast_study:app",host="0.0.0.0",port=8080,debug=True,reload=True)