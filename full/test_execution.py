
# Test automation project with python
# This project uses selenium web driver to execute tests
# on an Automotive speedometer embedded in a WEB / HTML UI.

# Additionally, as part of the automation an Excel report will
# be generated with the results of the tests.

# Author: Carlos Avila

from uiConstants import *
from selenium import webdriver
from time import sleep
import re
import json
import pytest
from reportGenerator import *

# Crete an instance of selenium web driver and open the 'automotiveSpeedometerUrl'
driver = webdriver.Chrome()
driver.get(automotiveSpeedometerUrl)
sleep(10)

def getDegFromGaugeStyle(gaugeStyle):
    # TO RESEARCH: REGULAR EXPRESSIONS
    #'transform: rotate(-70deg); transition: none 0s ease 0s;'
    pattern = r'-?\d+deg'
    deg = re.findall(pattern, gaugeStyle)
    return deg

def setSpeed(speed):
    speedInput = driver.find_element("xpath", speedInputXpath)
    speedInput.clear()
    speedInput.send_keys(speed)

    speedInputSubmit = driver.find_element("xpath", speedInputSubmitXpath)
    speedInputSubmit.click()
    sleep(5)

# This function will get the test cases from the json file
def loadTestsFromJson(jsonFile):
    with open(jsonFile, 'r') as archivo:
        testCases = json.load(archivo)
    return testCases

# Load the json file and store it in the variable 'testCases'
testCases = loadTestsFromJson("testCases.json")


# TO RESEARCH: PYTEST MARKERS
# This marker receives the 'testCases' defined in the jsonfile
@pytest.mark.parametrize("testCase", testCases)
def test_all(testCase):
    # Each test case contains the keys 'testName', 'speed', 'expectedDeg' and 'result'
    testName = testCase["testName"]
    speedToSet = testCase["speed"]
    expectedDeg = testCase["expectedDeg"]
    print("Executing test:", testName)
    print("Speed to set:", speedToSet)
    print("Expected deg:", expectedDeg)

    # Set the speed defined by the test case
    setSpeed(speedToSet)

    digitalSpeed = driver.find_element("xpath", digitalSpeedXpath)
    assert digitalSpeed.text == speedToSet
    print("Digital speed was the expected")

    initialGaugeDegData = driver.find_element("xpath", gaugeSpeedAngleXpath)
    degInfo = initialGaugeDegData.get_attribute('style')
    initialGaugeDeg = getDegFromGaugeStyle(degInfo)
    assert len(initialGaugeDeg) == 1
    assert expectedDeg == initialGaugeDeg[0]
    print("Gauge deg correct")

    # As no assetion failed, then change the test result to PASS
    testCase["result"] = "PASS"

    setSpeed("0")

# This test will generate the report
def test_print_data():
    reportStatus = generateReport(testCases, reportName)
    assert reportStatus == True
