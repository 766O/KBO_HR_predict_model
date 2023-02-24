from selenium import webdriver
import time
browser=webdriver.Chrome('chromedriver.exe')

#네이버로 이동
browser.get('https://www.naver.com')

#로그인버튼클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

#ID,password 입력

input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "dpcksdl78", pw = "qweasd787")
    
time.sleep(3)
#browser.find_element_by_id('id').send_keys('dpcksdl78')
#browser.find_element_by_id('pw').send_keys('qweasd787')

browser.execute_script(input_js)
#로그인버튼 클릭
browser.find_element_by_id('log.login').click()


#id 새로 입력
#browser.find_element_by_id('id').clear()
#browser.find_element_by_id('id').send_keys("dpcksdl78")

#HTML 정보출력
#print(browser.page_source)

