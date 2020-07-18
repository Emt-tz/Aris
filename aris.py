from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, html5lib
from bs4 import BeautifulSoup as bs
import time

Author = {
	'Name':'Emmanuel H Mtera',
	'Tel': '+255 693 677 033',
	'Email':'peterkelvin16@gmail.com'
}

global headers

headers = {
"User-Agent":
	"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

print(Author)

class ARIS:

	def login(usernamee, passwordd):

		t = time.time()

		browser = webdriver.PhantomJS('/home/emt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

		browser.get("https://aris2.udsm.ac.tz")
		username = browser.find_element_by_id("un")
		password = browser.find_element_by_id('pwd')

		#Credentials
	
		username.send_keys(usernamee)
		password.send_keys(passwordd)
	
		try:
			login_attempt = browser.find_element_by_name('login').click(); 
		except:
			return "invalid login Credentials"
	
		results = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td/div[1]/div[2]/div/a').click()


		firstyear = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/div/ul/li/a').click()

		x = browser.current_url
		
		s = requests.session()
		s.headers.update(headers)
		
		for cookie in browser.get_cookies():
			c = {cookie['name']:cookie['value']}
			s.cookies.update(c)
		   

		newurl = s.get(x, allow_redirects=True).text

		
		cur = bs(newurl, 'html5lib')
		
		browser.close()
		
		tf = time.time()
		
				
		z = ("".join(cur.strings))

		return f'it took {tf - t}s to complete {z}'


if __name__ == '__main__':
	ARIS.login(usernamee, passwordd)
