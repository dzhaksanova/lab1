import requests
import re

def take_emails(site): #выгружает сайт
    emails = []
    html = requests.get(site).text
    print(site)
    mailsrch = re.compile(r'[\w.][\w.]+@[\w][\w\.]+[a-zA-Z]{1,4}') #регулярка для поиска емайлов
    for line in html.split():
        emails += (re.findall(mailsrch, line))
    emails = set(emails) #Удаляет лишние емайлы
    print(emails)


take_emails('http://www.mosigra.ru/')
