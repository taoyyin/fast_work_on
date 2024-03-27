import datetime

from fastapi import APIRouter
from pydantic import BaseModel
from toolsapp.config import *
router = APIRouter(prefix="/tools",
                   tags=['tools'],
                   responses={404:{"decription":"not found"}},
                   )

class InputItem_model(BaseModel):
    search_plateform:str
    search_type:str
    date:str
    page:int
    page_size:int



@router.post("/tools/info")
async def get_tools_info(item:InputItem_model):

    data = list(tools_info_collection_cal.find({'search_plateform':item.search_plateform,'second_type':item.search_type,'date':item.date},
                                           {'_id':0,'date':0,'time':0,'first_type':0,'second_type':0,'search_plateform':0}).skip((item.page-1)*item.page_size).limit(item.page_size))

    return data