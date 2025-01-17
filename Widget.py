from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from twilio.rest import Client
from CloudView import CloudView
import re
import Keys
from Pdf import Pdf
from datetime import datetime
import os

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(Keys.site_url)

class Widget:
    client_ = Client(Keys.sid, Keys.token)

    def __init__(self, id, minThreshold = Keys.minThreshold, maxThreshold = Keys.maxThreshold):
        self.id = id
        self.widgetElement = driver.find_element(By.ID, id)
        self.previousValue = self.widgetElement.get_attribute('value')
        self.latestValue = self.previousValue
        self.minThreshold = minThreshold
        self.maxThreshold = maxThreshold
        self.cloudView = CloudView()
        self.smsAlreadySent = False


    def isValueChanged(self):
        self.latestValue = self.widgetElement.get_attribute('value')
        return self.latestValue != self.previousValue


    def updateValue(self):
        self.previousValue = self.latestValue
        self.cloudView.create_or_update_entity(self.id, self.latestValue)


    def checkIfIsOverThreshold(self):
        match = re.search(r'(\d+\.\d+|\d+)', self.latestValue)

        if match:
            float_value = float(match.group(1))
            if float_value < self.minThreshold:
                if not self.smsAlreadySent:
                    self.smsAlreadySent = True
                    self.sendAlarm(float_value, False)
                self.createReport(float_value, False)
            elif float_value > self.maxThreshold:
                if not self.smsAlreadySent:
                    self.smsAlreadySent = True
                    self.sendAlarm(float_value, True)
                self.createReport(float_value, True)
        else:
            print("Nu s-a găsit niciun număr în șir.")


    def createReport(self, value, isOverThreshold):
        if isOverThreshold:
            bodyText = "Widget over threshold: " + str(self.maxThreshold)
        else:
            bodyText = "Widget under threshold: " + str(self.minThreshold)

        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().time().strftime("%H-%M-%S")

        pdf = Pdf("P", "mm", "Letter")
        pdf.add_page()
        pdf.set_font("helvetica", "", 16)
        pdf.cell(100, 10, bodyText, ln=1)
        pdf.cell(100, 10, "Acctual Value = " + str(value), ln=1)
        pdf.cell(100, 10, "Date: " + str(date), ln=1)
        pdf.cell(100, 10, "Time: " + str(time), ln=1)

        if not os.path.exists(f"Reports\\{date}"):
            os.makedirs(f"Reports\\{date}")
        
        pdf.output(f'Reports\\{date}\\{self.id}_{time}.pdf')
        print("Report Created: ", f'Reports\\{date}\\{self.id}_{time}.pdf')
    

    def sendAlarm(self, value, isOverThreshold):
        if isOverThreshold:
            bodyText = "Widget over threshold"
        else:
            bodyText = "Widget under threshold"
            
        message = Widget.client_.messages.create(
            body = bodyText,
            from_ = Keys.twilio_numer,
            to = Keys.my_number
        )
        print(message.body + "Threshold: " + str(self.maxThreshold)+ "; Actual value: " + self.latestValue)