import time
import os,  sys, traceback
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import urllib.request
import shippingtype as stype
from dotenv import load_dotenv
load_dotenv()


class Paypal :
    driver = webdriver.Chrome()
    
    def __init__(self, username, password, shippingType):
        self.username = username
        self.password = password
        self.shippingType = shippingType

    def getLabel(self, data):
        currentShippingType = self.shippingType.paypalShippingTypes(data['shippingType'])
        zipcode = str(data['zipCode'])
        if len(zipcode) == 4:
            zipcode = '0' + zipcode
        # datastructure [country, To, st1, st2, city, state, zip, email, carrier, type, package]
        self.driver.get('https://www.paypal.com/shiplabel/create')
        time.sleep(5)
        Select(self.driver.find_element_by_id('countrySelector')).select_by_value(data['country'])
        self.driver.find_element_by_id('addresseeName').send_keys(data['name'])
        self.driver.find_element_by_id('street1').send_keys(data['streetOne'])
        self.driver.find_element_by_id('street2').send_keys(data['streetTwo'])
        self.driver.find_element_by_id('city').send_keys(data['city'])
        Select(self.driver.find_element_by_id('stateOrProvince')).select_by_value(data['state'])
        self.driver.find_element_by_id('postalCode').send_keys(zipcode)
        self.driver.find_element_by_id('email').send_keys('')
        self.driver.find_element_by_id('SaveToAddress').click()
        time.sleep(5)
        Select(self.driver.find_element_by_id('carrierList')).select_by_value(currentShippingType['carrier'])
        Select(self.driver.find_element_by_id('service-type')).select_by_value(currentShippingType['serviceType'])
        Select(self.driver.find_element_by_id('packageType')).select_by_value(currentShippingType['packageType'])
        time.sleep(5)
        if currentShippingType['serviceType'] == 'PRIORITY_MAIL' and currentShippingType['packageType'] == 'PACKAGE_OR_FLAT_ENVELOPE':
            self.driver.find_element_by_id('weightKGorLB').send_keys(str(data['lbs']))
            self.driver.find_element_by_id('length').send_keys(str(data['length']))
            self.driver.find_element_by_id('width').send_keys(str(data['width']))
            self.driver.find_element_by_id('height').send_keys(str(data['height']))
        if currentShippingType['serviceType'] == 'FIRST_CLASS_MAIL' and currentShippingType['packageType'] == 'PACKAGE_OR_FLAT_ENVELOPE' :
            self.driver.find_element_by_id('weightGMorOZ').send_keys(str(data['oz']))
        time.sleep(5)
        for i in range(0, 20):
            try:
                self.driver.find_element_by_id('calculateShippingCost').click()
                time.sleep(5)
                self.driver.find_element_by_id('confirmButton').click()
            except Exception as err:
                print(str(i) + 'times ' + str(err))
                time.sleep(20)
                traceback.print_exc() 
                continue
            break

        time.sleep(5)
        pdfUrl = self.driver.find_element_by_id('printFinalLabel').get_attribute("data-labelurl")
        pdfUrlSplitArr = pdfUrl.rsplit('/', 1)
        fullfilename = os.path.join('D:\project','click-n-print\labels', pdfUrlSplitArr[len(pdfUrlSplitArr) -1] )
        print (fullfilename)
        urllib.request.urlretrieve(pdfUrl, fullfilename)

    def login(self):
        self.driver.get('https://www.paypal.com/shiplabel/create')
        time.sleep(5)
        inputel = self.driver.find_element_by_id('email')
        inputel.send_keys(self.username)
        self.driver.find_element_by_id('btnNext').click()
        time.sleep(3)
        inputel = self.driver.find_element_by_id('password')
        inputel.send_keys(self.password)
        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(5)


if __name__ == "__main__":
    paypal = Paypal(os.getenv("PAYPAL_USER"),os.getenv("PAYPAL_PASS"), stype.ShippingType())
    data = [{'country': 'US', 'name': 'Ka Lok Hui', 'streetOne': '3001 s king dr', 'streetTwo': 'apt 1903', 'city': 'Chicago', 'state': 'IL', 'zipCode': 60616, 'shippingType': 1, 'oz': '', 'lbs': '', 'length': '', 'width': '', 'height': ''},
    {'country': 'US', 'name': 'Ka Lok Hui', 'streetOne': '3002 s king dr', 'streetTwo': '', 'city': 'Chicago', 'state': 'IL', 'zipCode': 60616, 'shippingType': 1, 'oz': '', 'lbs': '', 'length': '', 'width': '', 'height': ''}]
    
    paypal.login()
    for address in data:
        while True:
            try:
                paypal.getLabel(address)
            except Exception as e:
                print(str(e))
                continue
            break