from fastapi import Depends

import pymysql

# def get_db_connection():
#     connection = pymysql.connect(
#         host='localhost',
#         port=3306,
#         user="root",
#         password="tyy2750709",
#         database="online",
#     )
#     return connection
#
# def get_db():
#     connection = get_db_connection()
#     db = connection.cursor(pymysql.cursors.DictCursor)
#     try:
#         yield db
#     finally:
#         db.close()
#         connection.close()

# class MySQLHelper:
#     def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
#         self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
#
#     def execute_query(self, query, params=None):
#         try:
#             self.cursor.execute(query, params)
#             return self.cursor.fetchall()
#         except Exception as e:
#             print(f"Error executing query: {e}")
#
#     def execute_insert(self, query, params=None):
#         try:
#             self.cursor.execute(query, params)
#             self.connection.commit()
#             return self.cursor.lastrowid
#         except Exception as e:
#             self.connection.rollback()
#             print(f"Error executing insert query: {e}")
#
#     def execute_update(self, query, params=None):
#         try:
#             self.cursor.execute(query, params)
#             self.connection.commit()
#         except Exception as e:
#             self.connection.rollback()
#             print(f"Error executing update query: {e}")
#
#     def execute_delete(self, query, params=None):
#         try:
#             self.cursor.execute(query, params)
#             self.connection.commit()
#         except Exception as e:
#             self.connection.rollback()
#             print(f"Error executing delete query: {e}")
#
#     def __del__(self):
#         self.cursor.close()
#         self.connection.close()
db_config = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"tyy2750709",
    "database":"xhs",
    "port":3306,
    "cursorclass": pymysql.cursors.DictCursor

}

async def get_db():
    connection = pymysql.connect(**db_config)
    try:
        yield connection
    finally:
        connection.close()

