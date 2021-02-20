# This is a Python script to verify an online form.

# Press Shift+F10 to execute it
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Author : Riyamoll Paulose
# Date : 19/02/2021

import time
from requests import *
from bs4 import BeautifulSoup
import datetime
import form

# Assert all data displayed in the redirected page is as in the form
def verify_form():
    redirect_url = "https://rpmsoftware.com/hiring/2020/integration-test/form.html#"
    current_url = form.driver.current_url
    if (current_url != redirect_url):
        print("Failed to load the redirected page "+redirect_url)
    form.driver.get(redirect_url)    # getting the redirect_url as the submit button doesn't work just for testing purposes
    testName = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/span[2]').text
    assert testName == form.employeeData

    testSummary = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[4]/span[2]').text
    testSummary = testSummary.split('Employee Summary:\n\n')[1]
    assert testSummary == form.summaryData

    testDepartment = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[6]/span[2]').text
    assert testDepartment == form.departmentData

    testSalary = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[7]/span[2]').text
    assert testSalary == form.salaryData

    testAddress = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[8]/span[2]').text
    testAddressLat = testAddress.split(',')[0]
    assert testAddressLat == form.addressLatData
    testAddressLong = testAddress.split(' ')[1]
    assert testAddressLong == form.addressLongData

    testWorkLocation = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[9]/span[2]').text
    assert testWorkLocation == form.workLocationData

    testDate = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[11]/span[2]').text
    dateTime = datetime.datetime.strptime(form.dateData, '%m%d%Y')
    form.dateTimeData = dateTime.strftime('%b %#d, %Y')
    assert testDate == form.dateTimeData

    testActive = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[13]/span[2]').text
    assert testActive == "Yes"

    testLength = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[16]/span[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div').text
    assert testLength == form.lengthData+form.lengthUnitData

    testWidth = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[16]/span[2]/div[1]/table/tbody/tr[2]/td[3]/div/div/div').text
    assert testWidth == form.widthData+form.widthUnitData

    testColor = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[16]/span[2]/div[1]/table/tbody/tr[2]/td[4]/div/div/div').text
    assert testColor == form.colorData

    testBrand1 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[2]/td[2]/div/div/div').text
    assert testBrand1 == form.brandList[0]

    testBrand2 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[3]/td[2]/div/div/div').text
    assert testBrand2 == form.brandList[1]

    testModel1 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[2]/td[3]/div/div/div').text
    assert testModel1 == form.modelList[0]

    testModel2 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[3]/td[3]/div/div/div').text
    assert testModel2 == form.modelList[1]

    testModelYear1 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[2]/td[4]/div/div/div').text
    assert testModelYear1 == form.modelYearList[0]

    testModelYear2 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[3]/td[4]/div/div/div').text
    assert testModelYear2 == form.modelYearList[1]

    testTrim1 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[2]/td[5]/div/div/div').text
    assert testTrim1 == form.trimList[0]

    testTrim2 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[3]/td[5]/div/div/div').text
    assert testTrim2 == form.trimList[1]

    testCarColor1 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[2]/td[6]/div/div/div').text
    assert testCarColor1 == form.carColorList[0]

    testCarColor2 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[3]/td[6]/div/div/div').text
    assert testCarColor2 == form.carColorList[1]

    testLicense1 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[2]/td[7]/div/div/div').text
    assert testLicense1 == form.licenseList[0]

    testLicense2 = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[17]/span[2]/div[1]/table/tbody/tr[3]/td[7]/div/div/div').text
    assert testLicense2 == form.licenseList[1]

# Verify Employee name is displayed as header
    response = get(redirect_url)
    header = BeautifulSoup(response.text, 'html.parser').h1
    testHeader = header.get_text().strip()
    assert testHeader == form.employeeData

# Verify the format of Address field and has google maps link
    map = form.driver.find_element_by_xpath('/html/body/div/div[2]/div[8]/span[2]/a')
    mapUrl = map.get_attribute("href")
    print(mapUrl)
    assert testAddress == form.addressLatData+", "+form.addressLongData+" "+map.text
    assert mapUrl.startswith('http://maps.google.com/')

def tearDown():
    time.sleep(4)
    form.driver.close()

if __name__ == '__main__':
    verify_form()
    tearDown()