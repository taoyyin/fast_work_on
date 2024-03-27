from enum import Enum


class ISql(Enum):
    SELECTBYUSER =  """ select expiration_date from user_info where user_name= %s and plateform=%s"""#根据用户名查询信息
    SAVEUSERINFO = '''insert into user_info (user_name,create_time,create_time_stamp,plateform,expiration_date) values (%s,%s,%s,%s,%s)'''#插入用户信息
