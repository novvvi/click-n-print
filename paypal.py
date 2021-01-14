import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import urllib.request

class Paypal :
    username = 'novehui@gmail.com'
    password = 'Nafia@213!'
    driver = webdriver.Chrome()
    
    def getLabel(self, data):
        # datastructure [country, To, st1, st2, city, state, zip, email, carrier, type, package]
        self.driver.get('https://www.paypal.com/shiplabel/create')
        time.sleep(2)
        Select(self.driver.find_element_by_id('countrySelector')).select_by_value(data[0])
        self.driver.find_element_by_id('addresseeName').send_keys(data[1])
        self.driver.find_element_by_id('street1').send_keys(data[2])
        self.driver.find_element_by_id('street2').send_keys(data[3])
        self.driver.find_element_by_id('city').send_keys(data[4])
        Select(self.driver.find_element_by_id('stateOrProvince')).select_by_value(data[5])
        self.driver.find_element_by_id('postalCode').send_keys(data[6])
        self.driver.find_element_by_id('email').send_keys('')
        self.driver.find_element_by_id('SaveToAddress').click()
        time.sleep(3)
        Select(self.driver.find_element_by_id('carrierList')).select_by_value(data[7])
        Select(self.driver.find_element_by_id('service-type')).select_by_value(data[8])
        Select(self.driver.find_element_by_id('packageType')).select_by_value(data[9])
        time.sleep(5)
        if data[8] == 'PRIORITY_MAIL' and data[9] == 'PACKAGE_OR_FLAT_ENVELOPE':
            self.driver.find_element_by_id('weightKGorLB').send_keys(data[10])
            self.driver.find_element_by_id('length').send_keys(data[11])
            self.driver.find_element_by_id('width').send_keys(data[12])
            self.driver.find_element_by_id('height').send_keys(data[13])
        if data[8] == 'FIRST_CLASS_MAIL' and data[9] == 'PACKAGE_OR_FLAT_ENVELOPE' :
            self.driver.find_element_by_id('weightGMorOZ').send_keys(data[10])
        time.sleep(5)
        self.driver.find_element_by_id('calculateShippingCost').click()
        time.sleep(10)
        self.driver.find_element_by_id('confirmButton').click()
        time.sleep(5)
        pdfUrl = self.driver.find_element_by_id('printFinalLabel').get_attribute("data-labelurl")
        pdfUrlSplitArr = pdfUrl.rsplit('/', 1)
        fullfilename = os.path.join('D:\project','wechat\WechatBot-master\labels', pdfUrlSplitArr[len(pdfUrlSplitArr) -1] )
        print (fullfilename)
        urllib.request.urlretrieve(pdfUrl, fullfilename)

    def login(self):
        self.driver.get('https://www.paypal.com/shiplabel/create')
        inputel = self.driver.find_element_by_id('email')
        inputel.send_keys(self.username)
        self.driver.find_element_by_id('btnNext').click()
        time.sleep(3)
        inputel = self.driver.find_element_by_id('password')
        inputel.send_keys(self.password)
        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(3)

# <button class="pull-right btn btn-small vx_btn vx_btn-small" id="printFinalLabel" 
# data-labelurl="https://web-prd3.gcs.pitneybowes.com/usps/355916097/outbound/label/
# 586c564383d54ae1a259b02a5f2b1893.pdf">Print</button>

if __name__ == "__main__":
    paypal = Paypal()
    data = [
        ['US', 'ka Lok Hui', '123 apple st', '', 'Chicago', 'IL', '60616', '', 'USPS', 'PRIORITY_MAIL', 'PADDED_FLAT_RATE_ENVELOPE'],
        ['US', 'ka Lok Hui', '123 apple st', '', 'Chicago', 'IL', '60616', '', 'USPS', 'PRIORITY_MAIL', 'PADDED_FLAT_RATE_ENVELOPE'],
        ['US', 'ka Lok Hui', '123 apple st', '', 'Chicago', 'IL', '60616', '', 'USPS', 'PRIORITY_MAIL', 'PADDED_FLAT_RATE_ENVELOPE'],
        ['US', 'ka Lok Hui', '123 apple st', '', 'Chicago', 'IL', '60616', '', 'USPS', 'PRIORITY_MAIL', 'PADDED_FLAT_RATE_ENVELOPE'],
        ['US', 'ka Lok Hui', '123 apple st', '', 'Chicago', 'IL', '60616', '', 'USPS', 'PRIORITY_MAIL', 'PADDED_FLAT_RATE_ENVELOPE'],
        ['US', 'ka Lok Hui', '123 apple st', '', 'Chicago', 'IL', '60616', '', 'USPS', 'PRIORITY_MAIL', 'PADDED_FLAT_RATE_ENVELOPE']
    ]
    paypal.login()
    for address in data:
        while True:
            try:
                paypal.getLabel(address)
            except Exception as e:
                print(str(e))
                continue
            break