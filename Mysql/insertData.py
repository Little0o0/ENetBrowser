import pandas as pd
df = pd.read_excel("traindata.xlsx")
import pymysql
db = pymysql.connect("localhost","root","#password","ENetDB")
cursor = db.cursor()

for index, row in df.iterrows():
    ID = row["Unnamed: 0"]
    Q = pymysql.escape_string(row["question"])
    A = pymysql.escape_string(row["answer"])
    sql = f"""
        INSERT INTO dataTable(
         id, question, answer)
         VALUES ({int(ID)}, '{Q}', '{A}')"""
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except Exception as e:
       # 如果发生错误则回滚
       print(e)
       db.rollback()

db.close()
