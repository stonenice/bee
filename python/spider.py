# encoding:utf-8

#爬取阿里招聘信息

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery
import re

cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = False
cap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")

driver = webdriver.PhantomJS(executable_path="C:/usr/bin/phantomjs.exe",
                             desired_capabilities=cap)

driver.get("https://job.alibaba.com/zhaopin/positionList.htm")

driver.find_element_by_css_selector('.position-child[data-child-id="2"]').click()
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

table = '''<table>%s</table>''' % (driver.find_element_by_css_selector(".s-list-box table").get_attribute("innerHTML"))

driver.quit()

pq = PyQuery(table)

list = pq.find('tbody tr')

jobs = []

for x in list:
    job = {}
    trDom = PyQuery(x)
    info = map(lambda x: PyQuery(x).text(), trDom.find("td"))

    if trDom.attr('style'):
        continue

    link=trDom('td:first a').attr('href')
    m=re.search(r'positionId=(?P<id>\d+)',link)
    id=m.group('id')
    job['id']=id
    job['title'] = info[0]
    job['type'] = info[1]
    job['dest'] = info[2]
    job['num'] = info[3]
    job['date'] = info[4]

    job['postion_desc'] = PyQuery(PyQuery(trDom.next("tr")).find(".pt-20:first")).text()
    job['postion_require'] = PyQuery(PyQuery(trDom.next("tr")).find(".pt-20:last")).text()
    jobs.append(job)

for job in jobs:
    print job
