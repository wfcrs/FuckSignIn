from selenium import webdriver
import os

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
f=open("SignIn.txt", "a+",encoding="utf-8")

browser = webdriver.Chrome()
MainUrl="http://weixin.buaa.edu.cn/w_checkin/actions/detail.html?id="

# 直接模拟登陆
browser.implicitly_wait(3)
browser.get(MainUrl + str(ID))
InputBlank = browser.find_element_by_name("username")
InputBlank.send_keys("")# 统一认证账号
InputBlank = browser.find_element_by_name("password")
InputBlank.send_keys("") # 统一认证密码
Btn = browser.find_element_by_tag_name("button")
webdriver.ActionChains(browser).click(Btn).perform()

TimeTemp = []
StrTemp=""
while(1):
    try:
        browser.find_element_by_class_name("error-infor")
        break
    except Exception as e:
        StrTemp = (str(ID) + "\t" + browser.find_element_by_class_name("create-tag-top").text + "\t" + browser.find_element_by_class_name("flowexp").text + "\t")
        TimeTemp = browser.find_elements_by_class_name("font-time-color")
        StrTemp += (TimeTemp[0].text + "-" + TimeTemp[-1].text)
        print(StrTemp)
        f.write(StrTemp + "\n")
        ID += 1
        browser.get(MainUrl + str(ID))
browser.close()
os.system("pause")