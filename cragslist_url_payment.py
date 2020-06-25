from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
import os.path
import requests
from time import sleep
import os, sys

url="https://post.craigslist.org/u/HHAM7Siw6hGzNd6RqqyKew/kark8"
FirstName="firstnamestring"
LastName="lastnamestring"
cardnumber="cardnumber"
expiration="MM/YY"
CVcode="cardnumber"
streetAddress="streeet"
zipCode="zipcoode"
city="zipcoode"
state="CA"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=r'C:\webdrivers\chromedriver.exe')
sleep(2.5)
driver.get(url)
sleep(1.3)

#accept the term of use
#driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[2]/div[1]/button').click()
sleep(1.4)

#pay now via credit card
driver.find_element_by_xpath("/html/body/article/section/form/div/div/label/label[2]/input").click()

sleep(1.7)
#continue posting in sf bayarea
driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[2]/div/button').click()
sleep(0.9)


driver.find_element_by_xpath('//*[@id="cardFirstName"]').clear()
sleep(1.5)
card_FirstName=driver.find_element_by_xpath('//*[@id="cardFirstName"]')

for f in FirstName:
    card_FirstName.send_keys(f)
    sleep(0.3)

driver.find_element_by_xpath('//*[@id="cardLastName"]').clear()
sleep(1.2)
card_LastName=driver.find_element_by_xpath('//*[@id="cardLastName"]')

for l in LastName:
    card_LastName.send_keys(l)
    sleep(0.2)

driver.find_element_by_xpath('//*[@id="cardNumber"]').clear()
sleep(1.7)
card_number=driver.find_element_by_xpath('//*[@id="cardNumber"]')

for c in cardnumber:
    card_number.send_keys(c)
    sleep(0.3)

driver.find_element_by_xpath('//*[@id="expDate"]').clear()
sleep(1.4)
expDate=driver.find_element_by_xpath('//*[@id="expDate"]')

for m in expiration:
    expDate.send_keys(m)
    sleep(0.2)


driver.find_element_by_xpath('//*[@id="cvNumber"]').clear()
sleep(1.6)
cvNumber=driver.find_element_by_xpath('//*[@id="cvNumber"]')

for v in CVcode:
    cvNumber.send_keys(v)
    sleep(0.3)

driver.find_element_by_xpath('//*[@id="ccinfo"]/input[2]').clear()
sleep(1.7)
address=driver.find_element_by_xpath('//*[@id="ccinfo"]/input[2]')

for s in streetAddress:
    address.send_keys(s)
    sleep(0.3)

driver.find_element_by_xpath('//*[@id="cardPostal"]').clear()
sleep(1.5)
zip=driver.find_element_by_xpath('//*[@id="cardPostal"]')

for z in zipCode:
    zip.send_keys(z)
    sleep(0.2)

driver.find_element_by_xpath('//*[@id="cardCity"]').clear()
sleep(1.8)
City=driver.find_element_by_xpath('//*[@id="cardCity"]')

for o in city:
    City.send_keys(o)
    sleep(0.3)

driver.find_element_by_xpath('//*[@id="cardState"]').clear()
sleep(1.3)
State=driver.find_element_by_xpath('//*[@id="cardState"]')

for s in state:
    State.send_keys(s)
    sleep(0.2)


#pay button
sleep(1.4)
#driver.find_element_by_xpath('//*[@id="submitter"]').click()
