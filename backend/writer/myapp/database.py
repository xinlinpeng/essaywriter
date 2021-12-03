import pymysql
import json
from datetime import datetime, date
import time
import math
# from . import write_text
# db = pymysql.connect(host='localhost',port=3306,user='root',passwd='*Soa123456',db='soa',charset='utf8')
# cursor = db.cursor()
# sql = """CREATE TABLE IF NOT EXISTS cache (
#          topic  TEXT,
#          id  int(10) not null PRIMARY KEY auto_increment,
#          start_time TEXT, 
#          finish_time TEXT,
#          gene_type TEXT,
#          keywords TEXT,
#          para TEXT)"""
# cursor.execute(sql)

# sql = "INSERT INTO cache(topic, \
#                    start_time, finish_time, gene_type, keywords, para) \
#                    VALUES ('%s', '%s',  '%s',  '%s',  '%s',  '%s')" % \
#                   ("测试_topic2", "开始时间1", "结束时间", "类型", "关键词", "段落")
# cursor.execute(sql)
# db.commit()
# cursor.execute("select * from cache where topic='测试_topic1'")
# res = cursor.fetchall()
# print(res)
# for row in res:
#     print(row)
# cursor.close()
# db.close()

def save_cache(topic,start_time,finish_time,gene_type,keywords,para):
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='*Soa123456',db='soa',charset='utf8')
    cursor = db.cursor()
    sql = "INSERT INTO cache(topic, \
                   start_time, finish_time, gene_type, keywords, para) \
                   VALUES ('%s', '%s',  '%s',  '%s',  '%s',  '%s')" % \
                  (topic, start_time, finish_time, gene_type, keywords, para)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def search_topic(topic):
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='*Soa123456',db='soa',charset='utf8')
    cursor = db.cursor()
    sql = "select * from cache where topic = '%s'" % (topic)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    result = []
    for row in res:
        print(row)
        tmp = {}
        tmp["topic"] = row[0]
        tmp["id"] = row[1]
        tmp["start_time"] = row[2]
        tmp["finish_time"] = row[3]
        tmp["gene_type"] = row[4]
        tmp["keywords"] = row[5]
        tmp["para"] = row[6]
        result.append(tmp)
    db.close()
    return result

def search_by_id(id):
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='*Soa123456',db='soa',charset='utf8')
    cursor = db.cursor()
    sql = "select * from cache where id = %d" % (id)
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    result = []
    for row in res:
        print(row)
        tmp = {}
        tmp["topic"] = row[0]
        tmp["id"] = row[1]
        tmp["start_time"] = row[2]
        tmp["finish_time"] = row[3]
        tmp["gene_type"] = row[4]
        tmp["keywords"] = row[5]
        tmp["para"] = row[6]
        result.append(tmp)
    db.close()
    return result

def get_recent_time():
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='*Soa123456',db='soa',charset='utf8')
    cursor = db.cursor()
    sql = "select * from cache order by id desc limit 40"
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    time_list_sec = []
    for t in res:
        start_time = t[2]
        finish_time = t[3]
        print(start_time,finish_time)
        time_1_struct = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        time_2_struct = datetime.strptime(finish_time, "%Y-%m-%d %H:%M:%S")

        # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分，没有包含天数差，total_seconds包含天数差
        # 所以total_seconds两种情况都是可以用的
        total_seconds = (time_2_struct - time_1_struct).total_seconds()
        print('用时：')
        print(int(total_seconds))
        time_list_sec.append(int(total_seconds))
    sum = 0
    max = -1
    min = -1
    for num in time_list_sec:
        if max == -1 or max < num:
            max = num
        if min == -1 or min > num:
            min = num
        sum += num
    avg = sum / len(time_list_sec)
    print(math.ceil(min/60.0),math.ceil(max/60.0),math.ceil(avg/60.0))
    return {
        "min":math.ceil(min/60.0),
        "max":math.ceil(max/60.0),
        "avg":math.ceil(avg/60.0)
    }

    # result = []
    # for row in res:
    #     print(row)
    #     tmp = {}
    #     tmp["topic"] = row[0]
    #     tmp["id"] = row[1]
    #     tmp["start_time"] = row[2]
    #     tmp["finish_time"] = row[3]
    #     tmp["gene_type"] = row[4]
    #     tmp["keywords"] = row[5]
    #     tmp["para"] = row[6]
    #     result.append(tmp)
    # db.close()
    # return result

list = []

def keywords2str(keywords):
    res = ""
    for i in range(0,len(keywords)):
        if i == 0:
            res += keywords[i]
        else:
            res += " "+keywords[i]
    return res

def get_id_by_topic(topic):
    res = search_topic(topic)
    return [x["id"] for x in res]


# 生成自动填写配置文件
# _json = [] 
# print(len(list))  
# for i in range(0,37):
#     topic1 = list[3*i]["topic"]
#     topic2 = list[3*i+1]["topic"]
#     topic3 = list[3*i+2]["topic"]
#     keyword1 = list[3*i]["keyword"]
#     keyword2 = list[3*i+1]["keyword"]
#     keyword3 = list[3*i+2]["keyword"]
#     passage = {}
#     passage["title"] = ""
#     argument = [{
#         "topic":topic1,
#         "keyword":keyword1,
#         "id":get_id_by_topic(topic1)
#     },{
#         "topic":topic2,
#         "keyword":keyword2,
#         "id":get_id_by_topic(topic2)
#     },{
#         "topic":topic3,
#         "keyword":keyword3,
#         "id":get_id_by_topic(topic3)
#     }]
#     passage["argument"] = argument
#     _json.append(passage)
# print(_json)
# filename='cache.json'
# with open(filename,'w',encoding="utf-8") as file_obj:
#     json.dump(_json,file_obj,ensure_ascii=False, indent=4)

# 从文件读入缓存
# lines = []
# for line in open("mixed.txt"): 
#     line = line.strip()
#     if line != "":
#         lines.append(line)

# 存入数据库
# for i in range(0,len(list)):
#     time1 = lines[4*i]
#     time1 = time1[4:len(time1)]
#     para1 = lines[4*i+1]
#     type1 = "chat&qa"
#     topic = list[i]["topic"]
#     keywords = keywords2str(list[i]["keyword"])
#     save_cache(topic,time1,time1,type1,keywords,para1)
#     time2 = lines[4*i+2]
#     time2 = time2[4:len(time2)]
#     para2 = lines[4*i+3]
#     type2 = "chat"
#     save_cache(topic,time2,time2,type2,keywords,para2)

# 例子
# [
#     {
#         "title":"失败是成功之母"，
#         "argument":[
#             {
#                 "topic":"失败失败失败"，
#                 "keyword":"失败 成功"，
#                 "id"：[2,3]
#             }，
#             {
#                 "topic":"失败失败成功"，
#                 "keyword":"失败 成功"，
#                 "id"：[5,6]
#             }，
#         ]
#     }，
#     {
#         "title":"第二篇标题",
#         ...
#     }
# ]

# print(search_by_id(229))

# 生成新配置文件
# with open("cache.json",'r') as load_f:
#     load_dict = json.load(load_f)
#     # print(load_dict)

# for passage in load_dict:
#     for t in passage["argument"]:
#         para1 = search_by_id(t["id"][0])[0]["para"]
#         para2 = search_by_id(t["id"][1])[0]["para"]
#         t["para1"] = para1
#         t["para2"] = para2

# # print(load_dict)
# filename='cache_new.json'
# with open(filename,'w',encoding="utf-8") as file_obj:
#     json.dump(load_dict,file_obj,ensure_ascii=False, indent=4)

get_recent_time()


