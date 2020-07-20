import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

#Function for getting update
res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find("div",{"class":"maincounter-number"}).get_text().strip()

#Function for notification
def notify(title,message):
    notification.notify(
        title=title,
        message= message,
        timeout= 5
    )
while True:
    notify('Total no. of cases: ',cases)
    time.sleep(30)
