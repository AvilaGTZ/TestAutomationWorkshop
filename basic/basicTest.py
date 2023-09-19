
from selenium import webdriver
from time import sleep

# URL
automotiveSpeedometerUrl = "file:///C:/Users/avilagtz/Documents/Coding/Python/Automation_course/basic/carSpeedometer/dist/index.html"

# XPATHS
speedInputXpath = "/html/body/div[2]/input"
speedInputSubmitXpath = "/html/body/div[2]/button"

digitalSpeedXpath = "/html/body/div[1]/div/div[64]/div[1]"
gaugeSpeedAngleXpath = "/html/body/div[1]/div/div[62]"

driver = webdriver.Chrome()
driver.get(automotiveSpeedometerUrl)
sleep(10)

speedInput = driver.find_element("xpath", speedInputXpath)
speedInput.send_keys("100")

speedInputSubmit = driver.find_element("xpath", speedInputSubmitXpath)
speedInputSubmit.click()

sleep(5)

digitalSpeed = driver.find_element("xpath", digitalSpeedXpath)
print("Digital speed:", digitalSpeed.text)

gaugeSpeedDeg = driver.find_element("xpath", gaugeSpeedAngleXpath)
print("Gauge angle:", gaugeSpeedDeg.get_attribute('style'))

print("All good!")