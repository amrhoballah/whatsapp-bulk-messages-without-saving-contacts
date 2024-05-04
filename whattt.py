# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers

from time import sleep
import pywhatkit
import pandas

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')
failedMessage = []
count = 34
#input("Press ENTER after login into Whatsapp Web and your chats are visible.")
for column in excel_data['Contact'].tolist():
    try:
        sent = False        
        pywhatkit.sendwhatmsg_instantly("+" + str(int(excel_data['Contact'][count])), excel_data['Message'][count], 20, True,5)
        sent = True
        print('Message sent to: ' + str(excel_data['Contact'][count]))
        print(count)
        count = count + 1
    except Exception as e:
        failedMessage.append(excel_data['Contact'][count])
        print('Failed to send message to ' + str(excel_data['Contact'][count]) + str(e))
print("Failed to send messages to: ", failedMessage)
print("The script executed successfully.")

