# This is a Python script to fill an online form.

# Press Shift+F10 to execute it

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from path import *
from selenium.webdriver.common.keys import Keys

chromedriver = "/Users/Lpaulose/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html')

brandList = ("Ford", "Ford")
modelList = ("Taurus", "F150")
modelYearList = ("2018", "2015")
trimList = ("SEL", "XLT")
carColorList = ("Black", "Red")
licenseList = ("TEST-0001", "Test-0002")

employeeData = "Isabel Britt"
summaryData = "This is a test Employee Summary."
departmentData = "Management"
salaryData = "$50,000.00"
addressLatData = "34.833850°"
addressLongData = "106.748580°"
workLocationData = "Headquarters"
dateData = '06042018'
lengthData = "47"
lengthUnitData = "in"
widthData = "21"
widthUnitData = "in"
colorData = "Brown"

employeeField = driver.find_element_by_xpath(employeeName)
summaryField = driver.find_element_by_xpath(summary)
departmentField = driver.find_element_by_xpath(department)
salaryField = driver.find_element_by_xpath(salary)
addressLatField = driver.find_element_by_xpath(addressLat)
addressLongField = driver.find_element_by_xpath(addressLong)
workLocationField = driver.find_element_by_xpath(workLocation)
dateField = driver.find_element_by_xpath(date)
activeField = driver.find_element_by_xpath(active)
lengthField = driver.find_element_by_xpath(length)
lengthUnitField = driver.find_element_by_xpath(lengthUnit)
widthField = driver.find_element_by_xpath(width)
widthUnitField = driver.find_element_by_xpath(widthUnit)
colorField = driver.find_element_by_xpath(color)
brand1Field = driver.find_element_by_xpath(brand1)
brand2Field = driver.find_element_by_xpath(brand2)
model1Field = driver.find_element_by_xpath(model1)
model2Field = driver.find_element_by_xpath(model2)
modelYear1Field = driver.find_element_by_xpath(modelYear1)
modelYear2Field = driver.find_element_by_xpath(modelYear2)
trim1Field = driver.find_element_by_xpath(trim1)
trim2Field = driver.find_element_by_xpath(trim2)
carColor1Field = driver.find_element_by_xpath(carColor1)
carColor2Field = driver.find_element_by_xpath(carColor2)
license1Field = driver.find_element_by_xpath(license1)
license2Field = driver.find_element_by_xpath(license2)
submitButton = driver.find_element_by_xpath(submit)

# Filling the form
employeeField.send_keys(employeeData)
summaryField.send_keys(summaryData)
Select(departmentField).select_by_visible_text(departmentData)
salaryField.send_keys(salaryData)
addressLatField.send_keys(addressLatData)
addressLongField.send_keys(addressLongData)
Select(workLocationField).select_by_visible_text(workLocationData)
dateField.click()
time.sleep(2)
dateField.send_keys(Keys.LEFT)
dateField.send_keys(Keys.LEFT)
dateField.send_keys(dateData)
activeField.click()
lengthField.send_keys(lengthData)
Select(lengthUnitField).select_by_visible_text(lengthUnitData)
widthField.send_keys(widthData)
Select(widthUnitField).select_by_visible_text(widthUnitData)
colorField.send_keys(colorData)

brand1Field.send_keys(brandList[0])
model1Field.send_keys(modelList[0])
modelYear1Field.send_keys(modelYearList[0])
trim1Field.send_keys(trimList[0])
carColor1Field.send_keys(carColorList[0])
license1Field.send_keys(licenseList[0])

brand2Field.send_keys(brandList[1])
model2Field.send_keys(modelList[1])
modelYear2Field.send_keys(modelYearList[1])
trim2Field.send_keys(trimList[1])
carColor2Field.send_keys(carColorList[1])
license2Field.send_keys(licenseList[1])
submitButton.click()
time.sleep(2)



