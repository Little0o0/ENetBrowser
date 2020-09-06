from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
import pymysql
import json
import time
import pandas as pd


def ENet(request):
    return render(request, "ENet.html", {})

@csrf_exempt
def loadData(request):
    returnData = {}
    db = pymysql.connect("localhost","root","#password","ENetDB")
    cursor = db.cursor()
    data = {}
    if request.POST:
        data = dict(request.POST)
        ID = int(data['page'][0])
        dataTableSql = f"SELECT * FROM dataTable where id = {ID}"
        try:
           # 执行SQL语句
           cursor.execute(dataTableSql)
           # 获取所有记录列表
           result = cursor.fetchone()
           returnData["question"] = result[1]
           returnData["answer"] = result[2]
           returnData["Nowpage"] = ID
        except:
            print ("Error: unable to fetch data")

        ENetTableSql = f"SELECT * FROM ENetTable where dataId = {ID}"
        try:
            cursor.execute(ENetTableSql)
            results = cursor.fetchall()
            tmp = []
            for row in results:
                tmp.append([row[3],row[2],row[4]])
            returnData["ENet"] = tmp
        except:
            print ("Error: unable to fetch data")

    db.close()
    return HttpResponse(json.dumps(returnData))

@csrf_exempt
def saveData(request):
    db = pymysql.connect("localhost","root","#password","ENetDB" )
    cursor = db.cursor()
    data = {}
    if request.POST:
        data = dict(request.POST)
        page = int(data["page"][0])
        deleteSQL = f"DELETE FROM ENetTable WHERE dataId = {page}"
        try:
           cursor.execute(deleteSQL)
           db.commit()
        except:
           # 发生错误时回滚
           db.rollback()

        with open("tmp.log", "w") as f:
            f.write(str(data))

        for i in range(1, 13):
            d = [x.strip(" ") for x in data[f'data[{i}][]']]
            if d != ["","",""]:
                event = pymysql.escape_string(d[0])
                relation = pymysql.escape_string(d[1])
                inference = pymysql.escape_string(d[2])
                insertSQL = f"""
                    insert into ENetTable 
                    (dataId, event, relation,inference,submission_date)
                    values
                    ({page},'{event}','{relation}','{inference}',NOW())
                """
                try:
                   cursor.execute(insertSQL)
                   db.commit()
                except:
                   db.rollback()
    db.close()

    return HttpResponse("OK")