
from selenium import webdriver
from time import sleep

# URL
automotiveSpeedometerUrl = "file:///C:/Users/avilagtz/Documents/Coding/Python/Automation_course/basic/carSpeedometer/dist/index.html"

# XPATHS are the location of the elements in the UI
speedInputXpath = "/html/body/div[2]/input"
speedInputSubmitXpath = "/html/body/div[2]/button"

digitalSpeedXpath = "/html/body/div[1]/div/div[64]/div[1]"
gaugeSpeedAngleXpath = "/html/body/div[1]/div/div[62]"

# Launch the chrome browser and open the UI
driver = webdriver.Chrome()
driver.get(automotiveSpeedometerUrl)
sleep(10)

# Find the speed input in the UI
speedInput = driver.find_element("xpath", speedInputXpath)
speedInput.send_keys("100")

# Find the speed send button in the UI
speedInputSubmit = driver.find_element("xpath", speedInputSubmitXpath)
speedInputSubmit.click()

# Wait for the UI to update the requested value
sleep(5)

# Find the digital speed in the UI and get the value
digitalSpeed = driver.find_element("xpath", digitalSpeedXpath)
print("Digital speed:", digitalSpeed.text)

# Find the gauge angle and get the value
gaugeSpeedDeg = driver.find_element("xpath", gaugeSpeedAngleXpath)
print("Gauge angle:", gaugeSpeedDeg.get_attribute('style'))

print("All good!")