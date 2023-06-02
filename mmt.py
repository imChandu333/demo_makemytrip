from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from time import sleep

driver.get("https://www.makemytrip.com")
driver.maximize_window()
sleep(6)
iframe = driver.find_element("id","webklipper-publisher-widget-container-notification-frame")
driver.switch_to.frame(iframe)
sleep(5)
driver.find_element("xpath","//a[@id='webklipper-publisher-widget-container-notification-close-div']/i").click()
sleep(5)
driver.switch_to.default_content()
sleep(5)
driver.find_element("xpath","//span[@class='ic_circularclose_grey']").click()
sleep(5)
driver.find_element("xpath","//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']").click()
sleep(5)
driver.find_element("xpath","//button[text()='OKAY, GOT IT!']").click()
sleep(5)
airline_name = driver.find_elements("xpath", "//p[@class='boldFont blackText airlineName']")
sleep(5)
airline_code = driver.find_elements("xpath", "//p[@class='fliCode']")
sleep(5)
dep_place = driver.find_elements("xpath","//div[@class='flexOne timeInfoLeft']/p[@class='blackText']/font")
sleep(5)
dep_time = driver.find_elements("xpath","//div[@class='flexOne timeInfoLeft']/p/span")
sleep(5)
dest_place = driver.find_elements("xpath","//div[@class='flexOne timeInfoRight']/p[@class='blackText']/font")
sleep(5)
dest_time = driver.find_elements("xpath","//div[@class='flexOne timeInfoRight']/p/span")
sleep(5)
fare_prices  = driver.find_elements("xpath","//div[@class='blackText fontSize18 blackFont white-space-no-wrap']")



print("Getting flight names")
names = [name.text for name in airline_name]

print("Getting flight codes")
codes = ["Flight code "+code.text for code in airline_code]

print("Getting flight timings")
times = [("From "+deploc.text+" at "+deptime.text+" To "+destloc.text+" at "+desttime.text) for deploc,deptime,destloc,desttime in zip(dep_place, dep_time, dest_place, dest_time)]

print("Getting flight Fare")
prices = [("Fare Price "+price.text) for price in fare_prices]

flight = { name : (code, time, price) for name,code,time,price in zip(names,codes,times,prices)}

print("----------------------------------------------Flight info-----------------------------------------------------")

print(f"-------------------------------------you got {len(names)} flights---------------------------------------------")

for i in range(1,len(names)+1):
    print(f"{i})",names[i]+"==>>>")
    print(f">>>>>>>>>>{flight[names[i]]}")

driver.quit()