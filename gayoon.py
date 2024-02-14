'''
from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://www.google.com")


driver2=webdriver.Chrome()
driver2.get("https://www.youtube.com")




driver.maximize_window()

driver.set_window_size(0.0)



u=["https://youtube.com","https://naver.com","https://goole.com"]
d=[]
import time
for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    time.sleep(1)


for i in range (len(u)):
    d[i].get(u[i])


input("엔터치면 창이 닫침니다. 종료할까요?")

w=1920/2
h=1080/2

scf=[]


pos=[(0,0),(w,0),(0,h),(w,h)]
for i in range(4):
    d=webdriver.Chrome()
    f.append(d)
    d.get("https://www.youtube.com")
    d.set_window_size(w,h)
    d.set_window_position(pos[i][0],pos[i][1])
'''
#테스트 웹크롤링 (햄버거 아저씨)
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")

p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element("xpath",p)
e.click()

p='//*[@id="id_firstName"]'
e=driver.find_element("xpath",p)
e.send_keys("GaYun")

p='//*[@id="id_lastName"]'
e=driver.find_element("xpath",p)
e.send_keys("Ko")

p='//*[@id="id_gender_0"]'
e=driver.find_element("xpath",p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element("xpath",p)
e.send_keys("Ko GaYun")

p='//*[@id="id_password"]'
e=driver.find_element("xpath",p)
e.send_keys("123456789")


p='//*[@id="id_state"]/option[2]'
e=driver.find_element("xpath",p)
e.click()


p='//*[@id="id_fee"]/option[4]'
e=driver.find_element("xpath",p)
e.click()

p='//*[@id="id_date"]'
e=driver.find_element("xpath",p)
e.send_keys("11/08/2023")


p='/html/body/form/div/input'
e=driver.find_element("xpath",p)
e.click()


#세종 늘봄초등학교 공식 홈피

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
driver.get("https://neulbom.sjedues.kr/neulbom-e/main.do?sso=ok")

p='//*[@id="container"]/div[1]/div[2]/div[1]/div/a'
e=driver.find_element("xpath",p)
e.click()

p='//*[@id="detailForm"]/div/table/tbody/tr/td[5]/div/p[1]'
e=driver.find_element("xpath",p)
e.click()
'''
#엔터치기
'''
from selenium.webdriver.common.keys import Keys
e.send_keys (Keys.RETURN)




import time
time.sleep()
'''
#유튜브에서 검색하기
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://www.youtube.com/results?search_query=%ED%81%AC%EB%A0%88%EC%8A%A4%ED%8B%B0%EB%93%9C%EA%B2%8C%EC%BD%94")
time.sleep(2)


#p='//input[@id="search"]'
#e=driver.find_element("xpath",p)
#e.send_keys("크레스티드게코")

time.sleep(2)
from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)

time.sleep(2)


p1='//a[@id="thumbnail"]'
es=driver.find_elements("xpath",p1)
print(es[3].get_attribute("href"))
driver.get(es[3].get_attribute("href"))
'''


#텍스트 파일로 저장하기
'''
text="안녕사세욧"
file=open ('테스트.txt','w')
file.write(text)
file. close()
'''


#학교 종이
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get('https://v4.schoolbell-e.com/ko/gate/home?return_uri=https:%2F%2Fschoolbell-e.com%2Fko%2Fmain%2Fhome')
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div[1]/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.click()
e.send_keys('01080258066')
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div[1]/input'
e=driver.find_element('xpath',p)
e.click()
e.send_keys('iams9801@@') #비번 입력
time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)

p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[2]/div/div[1]/div/div[1]'
e=driver.find_element('xpath',p)
e.click()
time.sleep(3)

#학교종이_안내문 출력하기(f, formatting 이용)
file=open('학교종이.txt','w')
for i in range(10):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div[3]/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    file.write(e.text+'\n')
file. close()
'''

#네이버 뉴스 검색창 스크립 캡처 하기


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)



driver.maximize_window()


u=["aa","bb","cc"]
for i in range(3):
    driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+u[i])
    driver.save_screenshot(u[i]+".png")









































          
          










