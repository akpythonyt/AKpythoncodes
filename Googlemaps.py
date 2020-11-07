from selenium import webdriver 
from time import sleep 

driver = webdriver.Chrome("/home/arun/Downloads/chromedriver") 
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z") 
sleep(2) 

def searchplace():
	   Place=driver.find_element_by_class_name("tactile-searchbox-input")
	   Place.send_keys("Tiruchirappalli")
	   Submit=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	   Submit.click()
searchplace()

def directions():
	   sleep(10)	
	   directions=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div/button")
	   directions.click()
directions()

def find():
         sleep(6)
         find=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
         find.send_keys("Tirunelveli")
         sleep(2)
         search=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
         search.click()
find()

def kilometers():
               sleep(5)
               Totalkilometers=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
               print("Total Kilometers:",Totalkilometers.text)
               sleep(5)
               Bus=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
               print("Bus Travel:",Bus.text)
               sleep(7)
               Train=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div")
               print("Train Travel:",Train.text)
               sleep(7)

kilometers()

def available():
               print("*COVID-19 Special Trains*")
               sleep(7)
               trainone=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[2]/span[1]/span[1]/span")
               print("Train No:1",trainone.text)
               
def availableone():           
	   trainsec=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[8]/span[1]/span[1]/span") 
	   print("Train No:2",trainsec.text)
available()
availableone()
	               
               
               
               
               
               
               
               
               
               
               
               
               
               
                   
