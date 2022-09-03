from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from notifiers import get_notifier
import schedule
import time
import datetime

def main():
    global browser
    chromedriver = "C:/CH/chromedriver.exe"
    options = Options()
    options.page_load_strategy = 'normal'
    browser = webdriver.Chrome(options=options, executable_path=chromedriver)
    browser.get("http://ftp.kubsu.ru/ranged/09.03.03_793_ofo_d.html")

    lastupdate = browser.find_element(By.CLASS_NAME, value='style_8').text
    rankingInArray()
    browser.quit()
    messages = (f'ВАШЕ ФИО\n'
               f'Снилс: ВАШ СНИЛС\n'
               f'Последнее изменение таблицы: {lastupdate}\n'
               f'Список с оригиналом и оплатой: {rankArrayMoney.index(maxSnils)} место из 55 мест\n'
               f'Список с оригиналом без оплаты: {rankArrayFull.index(maxSnils)} место из 55 мест')
    telegram.notify(message=messages, token='5103076975:AAHkT_5T2CnyK0vWREMgFAqnXP22Vdm-w0U', chat_id=chat_ID1)
    telegram.notify(message=messages, token='5103076975:AAHkT_5T2CnyK0vWREMgFAqnXP22Vdm-w0U', chat_id=chat_ID2)

telegram = get_notifier('telegram')
chat_ID1 = ВАШ ЧАТ ИД
chat_ID2 = ВАШ ЧАТ ИД



rankArrayMoney = []
rankArrayFull = []
maxSnils = 'ВАШ НОМЕР СНИЛСА'


def ParsePeople(number):
    snils = browser.find_element(By.CSS_SELECTOR, f"#__bookmark_3 > tbody > tr:nth-child({number+3}) > td:nth-child(2) > div").text
    originalCertificate = browser.find_element(By.CSS_SELECTOR, f"#__bookmark_3 > tbody > tr:nth-child({number+3}) > td:nth-child(9) > div").text
    agree = browser.find_element(By.CSS_SELECTOR, f"#__bookmark_3 > tbody > tr:nth-child({number+3}) > td:nth-child(10) > div").text
    return snils, originalCertificate, agree


def rankingInArray():
    for number in range(450):
        print(number)
        infoOfPerson= ParsePeople(number)
        if infoOfPerson[1] == 'Ориг.' and infoOfPerson[2] == 'Есть, закл. дог.':
            rankArrayMoney.append(infoOfPerson[0])
            rankArrayFull.append(infoOfPerson[0])
        elif infoOfPerson[1] == 'Ориг.' and infoOfPerson[2] == 'Есть':
            rankArrayFull.append(infoOfPerson[0])
    print('Последнее срабатывание программы было', datetime.datetime.now())






main()