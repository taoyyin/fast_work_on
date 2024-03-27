from fastapi import Header, Cookie, HTTPException


async def virify_date(Host:str=Header()):
    print(Host)
    if not Host:
        raise HTTPException(status_code=203,detail="csrftoken is invalid")
