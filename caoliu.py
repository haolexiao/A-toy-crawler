# -*- coding: utf-8 -*-
from selenium import webdriver
import codecs
url = 'https://t66y.com/thread0806.php?fid=15&search=&page='
browser = webdriver.Chrome()
file_output = codecs.open('thefile.csv','w', 'utf_8_sig')
for i in xrange(1,100):
    browser.get(url+str(i))
    List = browser.find_elements_by_xpath("//h3/a[@target='_blank']")
    for x in List:
        file_output.write(x.text+','+x.get_attribute('href'))
file_output.close()
