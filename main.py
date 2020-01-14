import telebot
import requests
import json
from mysql_config import insert_db
from mysql_config import select_db
botid="Notification Bot id" #
chatid="chatid" #
success=False
url1='https://dekt.bupt.edu.cn/SecondClass/user/web_login'
logindata={
    'userid':"BUPT username", #
    'password':"password" #
}
r1=requests.post(url1, headers={'Content-Type':'application/json'},json=logindata)
c=r1.cookies
#print(c)
url='https://dekt.bupt.edu.cn/SecondClass/activity/list'
data={
    "limit": 100,
    "state": "已发布",
    "userid": "BUPT username" #
}
r=requests.post(url, headers={'Content-Type':'application/json'},json=data ,cookies=c)
bot = telebot.TeleBot(botid)
jsondata = json.loads(r.text)
result = [(item.get('title', 'NA'), item.get('beginTime', 'NA'),item.get('needCheckin', 'NA'),item.get('signupBeginTime', 'NA'),item.get('actId','NA'),item.get('location','NA'),item.get('cateName','NA')) for item in jsondata['page']['activities']]
#print(result)
for item in result:
    #print(item)
    title=item[0]+'\n\n'
    begin_time='📅'+item[1][5:16]+'\n'
    if(item[2]==True):
        checkin='✅需要签到        '
    else:
        checkin='❎无需签到        '
    if(item[3]!='1970-01-01 08:00:00'):
        signup='需要报名 ⏰%s\n'%item[3][5:16]
    else:
        signup='无需报名 ❌\n'
    localtion='📍'+item[5]+'\n'
    category='📒'+item[6]+'        '
    if(select_db(item[4])!=1):
        continue #数据库中已有情况去重
    else:
        botdata=title+category+begin_time+localtion+checkin+signup
        try:
            bot.send_message(chatid,botdata)
            success=True
        except:
            print("Fail to send message")
            success=False
        if(success):
            insert_db((item[4]))
