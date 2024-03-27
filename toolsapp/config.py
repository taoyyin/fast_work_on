import pymongo

client = pymongo.MongoClient("mongodb://root:tyy2750709@localhost:27017/?authSource=admin")
# 选择要使用的数据库
db = client["tools"]
# 选择要使用的集合（表）
tools_info_collection = db["toolsinfo"]
tools_info_collection_cal = db["toolsinfo_cal"]
