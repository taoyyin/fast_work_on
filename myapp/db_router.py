import datetime
import time
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from pydantic import BaseModel
from myapp.db import get_db
from myapp.sql_enum import ISql
from pymysql.connections import Connection
from myapp.db_depends import  virify_date
router = APIRouter(prefix="/user",
                   tags=['db_router'],
                   responses={404:{"decription":"not found"}},
                   )

expire_time_delay = 60 * 60 * 24 * 30

class User_Model(BaseModel):
    user_name:str
    platform:str


@router.post("/save/userinfo",status_code=200)
async def save_userinfo(user_info:User_Model,db:Connection=Depends(get_db)):
    """
        aditor:tyy,
        function:save_user
        time:2024-3-18
    """
    save_user_sql = ISql.SAVEUSERINFO.value
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    create_time_stamp = int(time.time())
    expiration_date = create_time_stamp + int(expire_time_delay)
    try:
        with db.cursor() as cursor:
            cursor.execute(save_user_sql,(user_info.user_name,create_time,create_time_stamp,user_info.platform,expiration_date))
            cursor.connection.commit()
        return {"message":"success"}
    except Exception as e:
        if str(e).find("Duplicate entry") != -1:
            raise HTTPException(status_code=200,detail="user name already exists")
        else:
            raise HTTPException(status_code=201,detail=str(e))



@router.get("/is_active/",status_code=200)
async def get_users(user_info:User_Model ,db:Connection=Depends(get_db), dependcy:None=Depends(virify_date)):
    """
    :aditor:tyy
    :param user_name:
    :param db:
    :return:
    function:check user is_on_active
    """
    select_sql = ISql.SELECTBYUSER.value
    result={}
    try:
        with db.cursor() as cursor:
            cursor.execute(select_sql,(user_info.user_name,user_info.platform))
            result = cursor.fetchone()
    except Exception as e:
        raise HTTPException(status_code=201,detail=str(e))
    if result:
        if result.get("expiration_date",0) > int(time.time()):
            return {"is_active":True}
        else:
            return {"is_active":False}
    else:
       raise HTTPException(status_code=200,detail="user is not exists")
