import openpyxl
from openpyxl.styles import Font, Color
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

# Datos
data = [
    {"testName": "test_initial_speed", "speed": "0", "expectedDeg": "-120deg", "result": "FAIL"},
    {"testName": "test_30_speed", "speed": "30", "expectedDeg": "-105deg", "result": "FAIL"},
    {"testName": "test_60_speed", "speed": "60", "expectedDeg": "-90deg", "result": "PASS"},
    {"testName": "test_90_speed", "speed": "90", "expectedDeg": "-75deg", "result": "FAIL"},
    {"testName": "test_120_speed", "speed": "120", "expectedDeg": "-60deg", "result": "FAIL"},
    {"testName": "test_130_speed", "speed": "500", "expectedDeg": "-130deg", "result": "FAIL"},
]

initWritableRow = 4
testNameCol = "C"
speedToTestCol = "D"
expectedDegCol = "E"
resultCol = "F"

def generateReport(data, reportName):
    writableRow = initWritableRow
    excelWorkbook = openpyxl.load_workbook("template.xlsx")
    testResultsSheet = excelWorkbook["TestsResults"]
    stylesSheet = excelWorkbook["Styles"]

    yellowStyle = stylesSheet["A1"]
    redStyle = stylesSheet["A2"]
    greenStyle = stylesSheet["A3"]
    emptyStyle = stylesSheet["A4"]

    for test in data:
        testNameColWritable = testNameCol + str(writableRow)
        speedToTestColWritable = speedToTestCol + str(writableRow)
        expectedDegColWritable = expectedDegCol + str(writableRow)
        resultColWritable = resultCol + str(writableRow)

        testResultsSheet[testNameColWritable]._style = emptyStyle._style
        testResultsSheet[testNameColWritable].value = test["testName"]

        testResultsSheet[speedToTestColWritable]._style = emptyStyle._style
        testResultsSheet[speedToTestColWritable].value = test["speed"]

        testResultsSheet[expectedDegColWritable]._style = emptyStyle._style
        testResultsSheet[expectedDegColWritable].value = test["expectedDeg"]

        if test["result"] == "PASS":
            testResultsSheet[resultColWritable]._style = greenStyle._style
        else:
            testResultsSheet[resultColWritable]._style = redStyle._style
        testResultsSheet[resultColWritable].value = test["result"]

        writableRow += 1


    excelWorkbook.save(reportName + ".xlsx")
    return True

generateReport(data,"testReport")
