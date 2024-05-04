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

excel_data = pandas.read_excel('Recipients data 1.xlsx', sheet_name='Recipients')

count = 48
failedMessage = []
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visible.")
f
