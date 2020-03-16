from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, html5lib
from bs4 import BeautifulSoup as bs
import time
# from selenium.webdriver.chrome.options import Options
#     options = Options()
#     options.add_argument("--headless")
#     self.driver = webdriver.Chrome(options=options)

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


		# browser = webdriver.ChromeOptions()
#       CHROME_PATH = '/usr/bin/google-chrome'
#       CHROMEDRIVER_PATH = '/home/s7pp8hre5rg7/vijana/chromedriver'
#       WINDOW_SIZE = "1920, 1080"

#       chrome_options = Options()  
#       chrome_options.add_argument("--headless")  
#       chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#       chrome_options.binary_location = CHROME_PATH
		
		t = time.time()

		browser = webdriver.PhantomJS('/home/emt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
#       browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
#                             chrome_options=chrome_options)
		#   browser = webdriver.PhantomJS('home/s7pp8hre5rg7/vijana/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
		# browser.add_argument('headless')

		# browser.add_argument('window-size=1200x600')

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


		# # browser.save_screenshot('login.png')
		# s = requests.session()
		# s.headers.update(headers)

		# for cookie in browser.get_cookies():
		#     c = {cookie['name']: cookie['value']}
		#     s.cookies.update(c)

		# r = s.get(imgurl, allow_redirects=True)
		# # open('results'+ '.jpeg','r+').write(r.content)
		# #cv2.imwrite('results.png', r.content)
		# x = r.text

		# y = bs(x, 'html5lib')

		
		# return [td for td in y.find_all('td')]

#       cred = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/strong')
#       grade = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/strong')
#       gpa = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/strong')
#       remarks = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/table[2]/tbody/tr/td/table/tbody/tr[7]/td[2]/strong')
#       student = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/b')
		
#       credits = f'Total Credit = {cred.text}'

#       grade = f'Total Grade Points = {grade.text}'

#       GPA = f'GPA = {gpa.text}'

#       rem = f'Remarks = {remarks.text}'

#       name = f'Hello {student.text}'

		x = browser.current_url
		
		s = requests.session()
		s.headers.update(headers)
		
		for cookie in browser.get_cookies():
			c = {cookie['name']:cookie['value']}
			s.cookies.update(c)
		   

		newurl = s.get(x, allow_redirects=True).text
		
#       if "https" in newurl:
			
#           newurl = newurl.replace('https', 'http')
		
		cur = bs(newurl, 'html5lib')
		
		browser.close()
		
		tf = time.time()
		
				
		z = ("".join(cur.strings))

		return f'it took {tf - t}s to complete {z}'




if __name__ == '__main__':
	ARIS.login(usernamee, passwordd)
