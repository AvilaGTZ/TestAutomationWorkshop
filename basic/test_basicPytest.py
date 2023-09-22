
from selenium import webdriver
from time import sleep

automotiveSpeedometerUrl = "file:///C:/Users/avilagtz/Documents/Coding/Python/Automation_course/basic/carSpeedometer/dist/index.html"

speedInputXpath = "/html/body/div[2]/input"
speedInputSubmitXpath = "/html/body/div[2]/button"

digitalSpeedXpath = "/html/body/div[1]/div/div[64]/div[1]"
gaugeSpeedAngleXpath = "/html/body/div[1]/div/div[62]"

driver = webdriver.Chrome()
driver.get(automotiveSpeedometerUrl)
sleep(2)

def test_Speed():
    speedInput = driver.find_element("xpath", speedInputXpath)
    speedInput.clear()
    speedInput.send_keys("30")

    speedInputSubmit = driver.find_element("xpath", speedInputSubmitXpath)
    speedInputSubmit.click()
    sleep(5)

    initialDigitalSpeed = driver.find_element("xpath", digitalSpeedXpath)
    assert initialDigitalSpeed.text == "30"

    initialGaugeDegData = driver.find_element("xpath", gaugeSpeedAngleXpath)
    degInfo = initialGaugeDegData.get_attribute('style')

    deg = False
    if degInfo.find("-105deg") > -1:
        deg = True

    assert deg == True