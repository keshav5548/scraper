from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r'C:/Users/Keshav/Downloads/chromedriver_win32/chromedriver.exe');
true_link='https://www.truecaller.com/auth/sign-in'
driver.get(true_link)
driver.implicitly_wait(2)
#driver.find_element_by_xpath('//a[contains(@href,"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&amp;respone_mode=query&amp;redirect_uri=https%3A%2F%2Fwww.truecaller.com%2Fauth%2Fmicrosoft%2Fcallback&amp;client_id=000000004818BA61&amp;scope=openid+profile+email+User.Read+Contacts.Read")]').click()
#driver.find_element_by_partial_link_text(" Sign in with Microsoft ").click()
#driver.find_element_by_css_selector('[href^=https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&amp;respone_mode=query&amp;redirect_uri=https%3A%2F%2Fwww.truecaller.com%2Fauth%2Fmicrosoft%2Fcallback&amp;client_id=000000004818BA61&amp;scope=openid+profile+email+User.Read+Contacts.Read]').click()
driver.find_element(By.cssSelector("a[href*='https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&amp;respone_mode=query&amp;redirect_uri=https%3A%2F%2Fwww.truecaller.com%2Fauth%2Fmicrosoft%2Fcallback&amp;client_id=000000004818BA61&amp;scope=openid+profile+email+User.Read+Contacts.Read']"));