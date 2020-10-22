from selenium import webdriver
import time
browser = webdriver.Chrome('D:\chromedriver.exe')
browser.get('https://instagram.com/')
time.sleep(4)
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys("Username")
time.sleep(4)
password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("Password")
password.submit()
time.sleep(5)
Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
Notnow.click()
time.sleep(3)
Noti=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(7)

def firstpic():
                    
	time.sleep(5)
	
	pic = browser.find_element_by_class_name("_9AhH0") 
	pic.click() 
def likepic(): 
	time.sleep(7) 
	like = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button")
	like.click()
first()
likepic()




