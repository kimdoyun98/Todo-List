import time
from selenium import webdriver

class Checking_Homework:
    def check_homework(self, id, pw):
        url = 'C:/Users/KDOY/PycharmProjects/chromedriver_win32/chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(url, options=options)

        #LMS 로그인
        driver.get("https://learn.hoseo.ac.kr/login.php")

        time.sleep(0.5)
        driver.find_element_by_name('username').send_keys(id)

        time.sleep(0.5)
        driver.find_element_by_name('password').send_keys(pw)
        driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div[1]/div[2]/div[1]/form/div[3]/button').click()

        # 데이터 추출
        homework_list = []
        #과목 번호 추출
        subject_numbers = []
        course_links = driver.find_elements_by_css_selector(".course_link")
        for course_link in course_links:
            href_link = course_link.get_attribute('href')
            _, subject_number = href_link.split('=')
            subject_numbers.append(subject_number)

        # 과목 번호로 url 접속 후 과제 체크
        for number in subject_numbers:
            try:
                # 과제 체크
                driver.get("https://learn.hoseo.ac.kr/mod/assign/index.php?id="+number)
                subject_name = driver.find_element_by_class_name("coursename")
                week = driver.find_elements_by_class_name('cell')

                #성적 제외하고 추출
                sub_list = []
                sub_list.append(subject_name.text)
                i = 1
                for w in week:
                    if (i % 5 == 0):
                        i = 0
                        pass
                    else:
                        sub_list.append(w.text)
                    i += 1

                homework_list.append(sub_list)


            except:
                pass

        return homework_list
