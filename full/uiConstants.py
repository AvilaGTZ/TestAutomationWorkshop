
# This file defines the Xpath (location in UI) of the
# automotive speedometer.

# URL -----------------------------------------------------------
# Define the url that will be opened with Selenium.
# This URL contains the automotive speedometer that will be
# used for testing purposes
automotiveSpeedometerUrl = "file:///C:/Users/avilagtz/Documents/Coding/Python/Automation_course/full/carSpeedometer/dist/index.html"

# This section defines the xptahs with the location
# of the different elements which are going to be tested
speedInputXpath = "/html/body/div[2]/input"
speedInputSubmitXpath = "/html/body/div[2]/button"

digitalSpeedXpath = "/html/body/div[1]/div/div[64]/div[1]"
gaugeSpeedAngleXpath = "/html/body/div[1]/div/div[62]"

# Report name
# Here is defined the Excel report with the results of the test cases
reportName = "speedometerTestResults"

# Gauge degrees -------------------------------------------------
'''gaugeDegrees = {
    '0': '-120deg',
    '30': '-105deg',
    '60': '-90deg',
    '90': '-75deg',
    '120': '-60deg',
    '150': '-45deg',
    '180': '-30deg',
    '210': '-15deg',
    '240': '-0deg'
}'''

