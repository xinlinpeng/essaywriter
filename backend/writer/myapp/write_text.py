# -*- coding:utf-8 -*-
import json
import requests
import time
import re
import traceback
# import synonyms

masked_words = [" ", "本书", "本册", "编者", "作者", "甄嬛", "出版", "简介", "小说", "本名",
                "祖籍", "现居", "作家", "丛书", "主编", "，男，", "，女，", "《", "》", "全书", "该书", "书中", "文库", "章节",
                "发表", "论文", "本文","从事","毕业","作文","论文","主人公","就读","著作","学家","出生"]
end_punc = "。!！?？"
punc = ".。!！?？‘’“”—：；"
min_para_len = 200

def divide_sentence(para):
    sent_list = []
    sent_start = 0    # 这句话开始的位置
    into_func = False
    for i in range(len(para)):
        if punc.find(para[i]) != -1:    # 结尾标点符号
            if end_punc.find(para[i]) != -1:
                into_func = True
        else:
            if into_func:
                into_func = False
                sent_list.append(para[sent_start:i])
                sent_start = i
    for s in sent_list:
        print(s)
    return sent_list

def merge_sentence(sent_list):
    para = ""
    for s in sent_list:
        para += s
    return para

def del_unfinished(para):
    sent_list = divide_sentence(para)
    last_sent = sent_list[len(sent_list)-1]
    if punc.find(last_sent[len(last_sent)-1]) == -1:
        sent_list.remove(len(sent_list)-1)
    result = merge_sentence(sent_list)
    return result 

def getMaxSubStr(s1, s2):
    maxL, count = 0, 0
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > maxL:
                    maxL = m[i + 1][j + 1]
                    count = i + 1
    return s1[count - maxL:count], maxL


def is_similar(s1,s2):
    if s1=="" or s2 == "":
        return False
    _,substr_len = getMaxSubStr(s1,s2)
    min_len = min(len(s1),len(s2))
    if 1.0*substr_len/min_len > 0.8:
        return True
    else:
        return False


def is_repeat(pre_sent,str):
    for s in pre_sent:
        if is_similar(s,str):
            return True
    return False


def is_masked(str):
    for word in masked_words:
        if str.find(word)!=-1:
            return True
    return False



def get_data(app,content):
    req_url = f"http://lab.aminer.cn/isoa-2021/gpt"
    if app == "chat":
        token = "0f5668dcccaaecfb88826bfdb3499e1f"
    else:
        token = "0f5668dcccaaecfb88826bfdb3499e1f"
    pre_data = {
        "token": token,
        "app": app,
        "content": content
    }
    headers = {"content-type": "application/json"}
    param = json.dumps(pre_data)
    try:
        resp = requests.post(req_url, data=param, headers=headers)
        resp.raise_for_status()
        print(resp.json())

        return resp.json()
    except Exception as Error:
        print(Error)


def get_num():
    req_url = f"http://lab.aminer.cn/isoa-2021/user"
    pre_data = {"token": "0f5668dcccaaecfb88826bfdb3499e1f"}
    headers = {"content-type": "application/json"}
    param = json.dumps(pre_data)
    try:
        resp = requests.post(req_url, data=param, headers=headers)
        resp.raise_for_status()
        # print(resp.status_code)

        return resp.json()
    except Exception as Error:
        print(Error)

def chat_list(list, num):
    filename = 'C:\\Users\\15790\\Desktop\\chat_essay.txt'
    for content in list:
        print(content)
        for i in range(num):
            print(i)
            with open(filename, 'a+') as file_object:
                file_object.write("【")
                file_object.write(str(i))
                file_object.write("】 " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")
                data = get_data("chat",content)
                try:
                    file_object.write(data["result"]+"\n\n")
                except Exception as Error:
                    print(Error)

def qa_list(list, num):
    filename = 'C:\\Users\\15790\\Desktop\\qa_essay.txt'
    for content in list:
        print(content)
        for i in range(num):
            print(i)
            with open(filename, 'a+') as file_object:
                file_object.write("【")
                file_object.write(str(i))
                file_object.write("】 " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")
                data = get_data("qa",content)
                try:
                    file_object.write(data["result"]["content"]+"\n\n")
                except Exception as Error:
                    print(Error)
                    print(data["result"]["content"]+"\n\n")

def qa_cyc(list,num):
    filename = 'C:\\Users\\15790\\Desktop\\qa_cyc.txt'
    for content in list:
        print(content)
        for i in range(num):
            print(i)
            with open(filename, 'a+') as file_object:
                file_object.write("【")
                file_object.write(str(i))
                file_object.write("】 " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")
                tmp = content
                for i in range(10):
                    data = get_data("qa",content)
                    result = data["result"]["content"]
                    if result.find(" ")==-1 and result.find("本书")==-1 and result.find("编者")==-1 and result.find("作者")==-1 and result.find("甄嬛")==-1:
                        content = content + result
                try:
                    file_object.write(content + "\n\n")
                    # file_object.write(data["result"]["content"]+"\n\n")

                except Exception as Error:
                    print(Error)


# TODO:最后一句如果没完，去掉
def chat_para(topic):
    sent_list = []
    data = get_data("chat", "问题：如何以“" + topic + "”开头，写一篇议论文?问题描述：回答用户：共青团中央 回答：" + topic)
    # data = get_data("chat", topic)
    result = data["result"]
    result = result[len("问题：如何以“" + topic + "”开头，写一篇议论文?问题描述：回答用户：共青团中央 回答："):len(result)]
    result.replace("收藏 查看我的收藏 0 有用+1 已投票 0 ", "")
    result.replace("<n>","")
    tmp_list = divide_sentence(result)
    for s in tmp_list:
        s = s.strip()
        if len(sent_list) == 0:
            sent_list.append(s)
        else:
            if is_masked(s):
                continue
            elif is_repeat(sent_list, s):
                continue
            else:
                sent_list.append(s)
    return sent_list

def chat_para_direct(topic):
    sent_list = []
    data = get_data("chat", topic)
    # data = get_data("chat", topic)
    result = data["result"]
    # result = result[len("问题：如何以“" + topic + "”开头，写一篇议论文?问题描述：回答用户：共青团中央 回答："):len(result)]
    result.replace("收藏 查看我的收藏 0 有用+1 已投票 0 ", "")
    result.replace("<n>","")
    tmp_list = divide_sentence(result)
    for s in tmp_list:
        s = s.strip()
        if len(sent_list) == 0:
            sent_list.append(s)
        else:
            if is_masked(s):
                continue
            elif is_repeat(sent_list, s):
                continue
            else:
                sent_list.append(s)
    return sent_list


def write_para(topic,keywords,min_len):
    if punc.find(topic[len(topic)-1]) == -1:
        topic += "。"
    sent_list = chat_para(topic)
    para = merge_sentence(sent_list)
    keyword_fail_times = {}
    for k in keywords:
        keyword_fail_times[k] = 0
    if len(para) < min_len:
        tmp_list = chat_para(topic)
        para_tmp = merge_sentence(tmp_list)
        if len(para_tmp) > len(para):
            para = para_tmp
            sent_list = tmp_list
    next_keyword = ""
    print("!!!para:"+para)
    if len(para) > min_len:
        last_part = para[max(0,len(para)-80): len(para)]
        for keyword in keywords:
            if last_part.find(keyword) == -1:
                next_keyword = keyword
                break
        if next_keyword == "":
            return para
        else:
            for i in range(3):
                data = get_data("qa", para + next_keyword)
                try:
                    result = data["result"]["content"]
                except Exception as e:
                    result = ""
                    e = traceback.format_exc()
                    e_msg = "data1:"+str(data)
                if not is_masked(result):
                    return para + next_keyword + result
                else:
                    keyword_fail_times[next_keyword]+=1
            return para
    else:
        for i in range(10):
            last_part = para[max(0, len(para) - 80): len(para)]
            print("last part:"+last_part)
            next_keyword = ""
            for keyword in keywords:
                if last_part.find(keyword) == -1 and keyword_fail_times[keyword]<3:
                    next_keyword = keyword
                    break
            print("now para:"+para)
            print("now keyword:"+next_keyword)
            data = get_data("qa", para+next_keyword)
            try:
                result = data["result"]["content"]
            except  Exception as e:
                result = ""
                e = traceback.format_exc()
                e_msg = "data2:"+str(data)

            if is_masked(result) or is_repeat(sent_list,result):
                if next_keyword != "":
                    keyword_fail_times[next_keyword] += 1
            else:
                sent_list.append(next_keyword+result)
                para += next_keyword+result
    para = para.replace("<n>","")
    para = del_unfinished(para)
    return para

def write_para_chat(topic,keywords,min_len):
    e = ""
    e_msg = "chat"
    if punc.find(topic[len(topic)-1]) == -1:
        topic += "。"
    sent_list = chat_para_direct(topic)
    para = merge_sentence(sent_list)
    print("!!!para:" + para)
    keyword_fail_times = {}
    for k in keywords:
        keyword_fail_times[k] = 0
    if len(para) < min_len:
        if len(keywords)>0:
            para = para + keywords[0]
        tmp_list = chat_para_direct(para)
        para = merge_sentence(tmp_list)
        print("!!!para:" + para)
    if len(para) < min_len:
        if len(keywords)>0:
            if len(keywords)>1:
                para = para + keywords[1]
            else:
                para = para + keywords[0]
        tmp_list = chat_para_direct(para)
        para = merge_sentence(tmp_list)
        print("!!!para:" + para)
    para = para.replace("<n>","")
    para = del_unfinished(para)
    return para


content = "拥有自制力的人，才能实现个人发展和进步。"
con0 = "只有做到自主，才能够自强。"
con1 = "没有自主，便会受制于人。"
con2 = "自主更是守护国家安全的基础。"
con3 = "以北斗为代表的国之重器，必自主才能守护国家安全。"
con4 = "朴素之中蕴含着文化与精神之光华。"
con5 = "不了解中华文化的人，就无法看到传承于朴素中的光华。"
con6 = "我们需要更多愿意传承传统文化、传统技艺的人。"
con7 = "幸福是奋斗出来的。"
con8 = "只有向着一个目标不懈奋斗，不断前进，才能体会到这种无与伦比的满足感与幸福感。"
con9 = "没有经过奋斗的收获，往往也不能带来幸福。"
con10 = "一个国家的幸福，需要所有人民齐心协力的奋斗。"
con11 = "纽带可以拉近两端事物或人之间的距离。"
con12 = "如果没有纽带，封闭﹑孤立就会产生。"
con13 = "在如今以“共享”为名的新时代，纽带在我们的生活中显得更为重要。"
con14 = "许多生命中平凡的点滴，在日日夜夜的坚守中，都会成就伟大。"
con15 = "所有的伟大都离不开对平凡的坚守。"
list = [con0,con1,con2,con4,con5,con6,con7,con9,con10,con11,con12,con13,con14,con15]
# qa_cyc(list,2)
# qa_list(list,8)
# chat_list(list,5)
# print(get_data("chat",content))
# da ta = get_data("qa",content)
# print(data)
print(get_num())
# filename = 'test_text.txt'
# with open(filename, 'a') as file_object:
#     file_object.write("lalala\n")
#     file_object.write("hahaha\n")
# str1 = "不了解中华文化的人，无法看到传承于朴素中的光华。来来来"
# str2 = "不了解中华文化的人，就无法看到传承于朴素中的光华。姑姑"
# print(str1.split())
# str, _ = getMaxSubStr(str1, str2)
# print(is_similar(str1,str2))
# p = "幸福是奋斗出来的。幸福是伴随着生活的挑战和高难的，世界在进步，人类要不断向前。幸福不仅是给自己，也在给他人。生动地诠释着生活永远是奋斗出来的。幸福是完整的，一个不完整的人是没有生命的。我们需要完成身体、心智和精神上三个层次的幸福。使自己成为一个完整的人，使自己的家庭、事业和社会更幸福。常言说:“人无癖不可与交，以其无深情也;人无疵不可与交，以其无真气也。王介甫言:‘癖者，情之疾也;疵者，心之贼也。’”幸福来源于对生活的热爱，是自己对世界的感受。我们知道没有痛苦就不会有幸福，幸福是人生的一种境界。"
# divide_sentence(p)
# synlst = synonyms.display('良师益友')
# print(synlst)

# print(write_para(content,["自制力","个人发展"],200))