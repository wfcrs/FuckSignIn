import os
import requests
from bs4 import BeautifulSoup

if(os.path.exists("SignIn.txt")==True):
    f = open("SignIn.txt", "r",encoding="utf-8")
    ReadTemp = f.readlines()
    if(len(ReadTemp)!=0):
        ID = int(ReadTemp[-1].split()[0]) + 1
        f.close()
    else:
        ID=1440
else:
    ID=1440

f = open("SignIn.txt", "a+", encoding="utf-8")

session = requests.Session()
MainUrl = "http://weixin.buaa.edu.cn/w_checkin/actions/detail.html?id="
Login_Url = "http://weixin.buaa.edu.cn/wap/login/commit.html"
UserName = ""
PassWord = ""
Login_Data={"username":UserName,"password":PassWord}
r = session.post(url=Login_Url, data=Login_Data)

temp=""
while(1):
    URL=MainUrl+str(ID)
    q = session.get(url=URL)
    q.encoding = "utf-8"
    soup = BeautifulSoup(q.text, "lxml")
    Title = soup.title.string
    if(Title == "403"):
        break
    Description=soup.find("p", {"class": "flowexp", "style": "word-break:break-all;"})
    Time = soup.find_all("span", {"class": "font-time-color"})
    temp = str(ID) + "\t" + Title + "\t"
    if(Description.string!=None):
        temp += Description.string.replace("\n", " ")
    temp+=("\t" + Time[0].string + "-" + Time[1].string+"\n")
    f.write(temp)
    ID += 1