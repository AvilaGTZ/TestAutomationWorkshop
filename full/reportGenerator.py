import openpyxl
from openpyxl.styles import Font, Color
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

# Define the initial row to be written
initWritableRow = 4

# Define the location of the columns
testNameCol = "C"
speedToTestCol = "D"
expectedDegCol = "E"
resultCol = "F"

def generateReport(data, reportName):
    writableRow = initWritableRow
    excelWorkbook = openpyxl.load_workbook("template.xlsx")
    testResultsSheet = excelWorkbook["TestsResults"]
    stylesSheet = excelWorkbook["Styles"]

    # Get the styles to be used
    yellowStyle = stylesSheet["A1"]
    redStyle = stylesSheet["A2"]
    greenStyle = stylesSheet["A3"]
    emptyStyle = stylesSheet["A4"]

    for test in data:
        # Create the coordinates of the columns to be written
        testNameColWritable = testNameCol + str(writableRow)
        speedToTestColWritable = speedToTestCol + str(writableRow)
        expectedDegColWritable = expectedDegCol + str(writableRow)
        resultColWritable = resultCol + str(writableRow)

        # Apply the style to the coordinate to be written and then add the required information.
        testResultsSheet[testNameColWritable]._style = emptyStyle._style
        testResultsSheet[testNameColWritable].value = test["testName"]

        # Apply the style to the coordinate to be written and then add the required information.
        testResultsSheet[speedToTestColWritable]._style = emptyStyle._style
        testResultsSheet[speedToTestColWritable].value = test["speed"]

        # Apply the style to the coordinate to be written and then add the required information.
        testResultsSheet[expectedDegColWritable]._style = emptyStyle._style
        testResultsSheet[expectedDegColWritable].value = test["expectedDeg"]

        # Apply the style to the coordinate based on the test result then add the required information.
        if test["result"] == "PASS":
            testResultsSheet[resultColWritable]._style = greenStyle._style
        else:
            testResultsSheet[resultColWritable]._style = redStyle._style
        testResultsSheet[resultColWritable].value = test["result"]

        # Increase the row to write
        writableRow += 1

    #Save the report
    excelWorkbook.save(reportName + ".xlsx")
    return True

