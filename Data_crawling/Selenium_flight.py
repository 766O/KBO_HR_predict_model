from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window()

url='https://flight.naver.com/'
browser.get(url)

elem=browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[2]').click()
time.sleep(2)

browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
#동일날짜 처리방법
#2/27 - 3/27 선택시 27에 해당하는 a 태그중 첫번째 항목이 2월거 두번째 항목이 3월거
#날짜 선택
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.container_SearchModalContainer__2wVab > div.container_content__2w_MI.container_as_calendar__17CQb > div.calendar_calendar__2OzxE > div.calendar_content__1Xc5a > div > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2) > button > b').click() #이번달
time.sleep(2)
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.container_SearchModalContainer__2wVab > div.container_content__2w_MI.container_as_calendar__17CQb > div.calendar_calendar__2OzxE > div.calendar_content__1Xc5a > div > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(3) > button > b').click() #이번달  
time.sleep(2)

#도착지
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.end > i').click()
time.sleep(2)

#국내
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_content__3RhAZ > section > section > button:nth-child(1)').click()
time.sleep(2)

#제주
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_content__3RhAZ > section > section > div > button:nth-child(2) > span > i.autocomplete_location__TDL6g').click()
time.sleep(2)

#항공권 검색
browser.find_element_by_css_selector('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > button').click()

#첫번째 결과 출력
try:
    elem=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')))
    #elem=browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')
    print(elem.text)
finally:
    browser.quit()


