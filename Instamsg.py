from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://instagram.com/')
time.sleep(4) 
#Automating the login
def login():#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input
    Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    Username.send_keys("username")
    time.sleep(4)
    password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("password")
    password.submit()
    time.sleep(5)
#Automate the notifications
def notification():
    Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    Notnow.click()  
    time.sleep(3)
    Noti=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    Noti.click()
    time.sleep(7)
#click the message
def message():
    msgclick=browser.find_element_by_class_name('xWeGp')
    msgclick.click()
    time.sleep(7)
#Final part of automation
def  final():
    chat=browser.find_element_by_class_name('QBdPU')
    chat.click()
    time.sleep(7)
    typename=browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
    typename.send_keys('arun.codes')
    time.sleep(7)
    name=browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div')
    name.click()
    time.sleep(7)
    next=browser.find_element_by_class_name('rIacr').click()
    time.sleep(7)
    mbox = browser.find_element_by_tag_name('textarea')
    mbox.send_keys('This is an automated message')
    send=browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
login()
notification()
message()
final()

