from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.google.co.in/")
term = driver.find_element_by_name('q')
search_term = raw_input('Enter search term: ')
term.send_keys(search_term)
#term.submit()
button = driver.find_element_by_name('btnG')
button.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source)
links = soup.find_all('h3',attrs={'class':'r'})
print "Links:"
for link in links:
	s = link.find('a')
	print
	print link.string
	print s.get('href')

