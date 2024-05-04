# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers
# Author @inforkgodara

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas

version = "123_0_6312_122"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing".format(version)
chrome_driver_path = "/Users/amrhoballah/Documents/chromedriver-mac-x64/chromedriver".format(version)
service_options = webdriver.ChromeService(chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options, service=service_options)

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 230
failedMessage = []
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visible.")
for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(excel_data['Contact'][count], excel_data['Message'][count])
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        
        try:
            click_btn = WebDriverWait(driver,90).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Send']")))
        except Exception as e:
            failedMessage.append(excel_data['Contact'][count])
            print("Sorry message could not sent to " + str(excel_data['Contact'][count]))
        else:
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + str(excel_data['Contact'][count]))
            print(count)
        count = count + 1
    except Exception as e:
        failedMessage.append(excel_data['Contact'][count])
        print('Failed to send message to ' + str(excel_data['Contact'][count]) + str(e))
print("Failed to send messages to: ", failedMessage)
driver.quit()
print("The script executed successfully.")
