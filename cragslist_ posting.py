from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
import os.path
from bs4 import BeautifulSoup
import requests
from time import sleep
import os, sys

class botbot:

     def __init__(self):

       options = webdriver.ChromeOptions()
       options.add_experimental_option("detach", True)
       driver = webdriver.Chrome(options=options, executable_path=r'C:\webdrivers\chromedriver.exe')

       driver.get('https://sfbay.craigslist.org')
       sleep(2)
       #create posting
       driver.find_element_by_xpath('//*[@id="post"]').click()

       #1:san Francisco 2:south_bay 3:east_bay 4:peninsula 5:north_bay 6:santa cruz
       driver.find_element_by_css_selector("input[type='radio'][value='3']").click()
       driver.find_element_by_class_name('pickbutton').click()
       sleep(2.1)
       #0 : pass the subarea specification
       driver.find_element_by_css_selector("input[type='radio'][value='0']").click()
       sleep(1.5)
       #fsd: for sale by dealer , fso: for sale by owner
       driver.find_element_by_css_selector(f"input[type='radio'][value='{fsofsd}']").click()
       driver.find_element_by_class_name('pickbutton').click()
       sleep(1.7)
       #146 (dealer)cars and trucks 145 owner cars and trucks

       driver.find_element_by_css_selector(f"input[type='radio'][value='{fs_value}']").click()


       sleep(1.4)
       #start of text filling
       driver.find_element_by_id("PostingTitle").clear()
       PostTitle=driver.find_element_by_id("PostingTitle")
       #title of the post
       PostTitle.send_keys(TITLE)
       sleep(1.8)
       driver.find_element_by_xpath('//input[@name="price"]').clear()
       price=driver.find_element_by_xpath('//input[@name="price"]')
       #asking price
       price.send_keys(PRICE)
       sleep(1.2)
       driver.find_element_by_xpath('//input[@name="geographic_area"]').clear()
       area=driver.find_element_by_xpath('//input[@name="geographic_area"]')
       #optional item
       area.send_keys(AREA)
       sleep(1.6)
       driver.find_element_by_xpath('//input[@name="postal"]').clear()
       zip=driver.find_element_by_xpath('//input[@name="postal"]')
       #postal_zipCode
       zip.send_keys(ZIP)
       sleep(2.1)
       driver.find_element_by_xpath('//textarea[@name="PostingBody"]').clear()
       body=driver.find_element_by_xpath('//textarea[@name="PostingBody"]')
       #description
       body.send_keys(DESCRIPTION)
       sleep(1.4)
       driver.find_element_by_xpath('//input[@name="auto_vin"]').clear()
       vin=driver.find_element_by_xpath('//input[@name="auto_vin"]')
       # VIN
       vin.send_keys(VIN)
       sleep(1.5)
       driver.find_element_by_xpath('//input[@name="auto_miles"]').clear()
       miles=driver.find_element_by_xpath('//input[@name="auto_miles"]')
       # odometer reading
       miles.send_keys(ODOMETER)
       sleep(0.4)
       driver.find_element_by_xpath('//input[@name="auto_make_model"]').clear()
       makeModel=driver.find_element_by_xpath('//input[@name="auto_make_model"]')
       #make and model
       makeModel.send_keys(MAKE+" "+MODEL)
       sleep(1)

       #fuel type
       driver.find_element_by_xpath('//*[@id="ui-id-6-button"]').click()
       # fuel 2:gas 3:diesel 4:hybrid 5:electric
       driver.find_element_by_xpath(f'/html/body/div[5]/ul/li[{fuel}]').click()
       #title status
       sleep(0.7)
       driver.find_element_by_xpath('//*[@id="ui-id-9-button"]').click()
       #20:clean , 21:salvage , 22:rebuilt
       driver.find_element_by_xpath(f'//*[@id="ui-id-{title}"]').click()
       #transmission
       sleep(0.9)
       driver.find_element_by_xpath('//*[@id="ui-id-10-button"]').click()
       #//*[@id="ui-id-28"] automatic ,//*[@id="ui-id-27"] manual
       driver.find_element_by_xpath(f'//*[@id="ui-id-{gear}"]').click()
       sleep(0.3)
       #Year
       driver.find_element_by_xpath('//*[@id="ui-id-12-button"]').click()
       #//*[@id="ui-id-37"] 2015, //*[@id="ui-id-47"] 2005
       driver.find_element_by_xpath(f'//*[@id="ui-id-{YEAR_CRAG}"]').click()
       sleep(0.8)

       #email
       driver.find_element_by_xpath('//input[@name="FromEMail"]').clear()
       dealerEmail=driver.find_element_by_xpath('//input[@name="FromEMail"]')
       dealerEmail.send_keys(EMAIL)
       sleep(0.8)

       #Potential "SHOW MY NUMBER" for direct contact
       #Potential "SHOW MY ADDRESS" for direct contact
       #CONTINUE for dealer
       driver.find_element_by_xpath('//*[@id="new-edit"]/div/div[3]/div/button').click()
       sleep(1)
       #MAP IS SHOWN, ANOTHER CONTINUE
       driver.find_element_by_xpath('//*[@id="leafletForm"]/button').click()
       #ADD IMAGES
       sleep(1)
       driver.find_element_by_xpath('//a[@id="classic"]').click()

       img=[]

       valid_img=['.jpg','.gif','.png','.tga']
       for f in os.listdir(path):
           ext = os.path.splitext(f)[1]
           if ext.lower() not in valid_img:
            continue

           img.append(path + f"\{f}")
            #iterating over images
       cc=0
       for i in img:
            cc+=1
            add_images=driver.find_element_by_xpath('//input[@name="file"]')
            add_images.clear()
            sleep(0.5)
            add_images.send_keys(i)
            if cc==24:
                break
       sleep(0.4)
       driver.find_element_by_xpath('//button[@value="Done with Images"]').click()

       #publish and close the browser
       driver.find_element_by_xpath('//*[@id="publish_top"]/button').click()
       sleep(1.2)
       driver.close() #will close only the current chrome window.

for file in os.listdir(r'C:\Users\Silmi\Desktop\Dealerships_automation\citiTrading_cars'):
    path=rf'C:\Users\Silmi\Desktop\Dealerships_automation\citiTrading_cars\{file}'
    with open(rf'C:\Users\Silmi\Desktop\Dealerships_automation\citiTrading_cars\{file}\info.txt') as f:
        lineList = f.readlines()
        car =lineList[0].split(",,")
        TITLE=car[0]
        MAKE=car[1]
        MODEL=car[2]
        VIN=car[3]
        YEAR_ORGIN=car[4]
        DESCRIPTION=". ." +car[5]
        ODOMETER=car[6]
        PRICE=car[7]
        #YEAR_CRAG=yeardict[YEAR_ORGIN]
        YEAR_CRAG="45"
        AREA=""
        ZIP="94536"
        fuel="2"# fuel 2:gas 3:diesel 4:hybrid 5:electric
        title="32"#32:clean , 33:salvage , 34:rebuilt
        gear="40"#40= automatic ,39= manual


        EMAIL="samisilmi91@gmail.com"
        fsofsd="fsd"
        fs_value="146"
        botbot()
        sleep(1)
        f.close()


#dealer_name="APEXCARS.NET"
#dealer_address="4949 Thornton Ave, Fremont, CA 94536"
#dealer_phone="(510) 266-0801"
