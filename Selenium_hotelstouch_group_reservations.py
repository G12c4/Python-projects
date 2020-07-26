from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

df = pd.read_excel(r'C:\Users\Admin\Documents\test.xlsx')
driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')

def login_to_HT():
    """ Read Excel file and open HT Management page """
	
    driver.implicitly_wait(10)
    driver.get("https://management.hotelstouch.com/login/auth")

	### Login page ###
    Username_fld = driver.find_element_by_css_selector("#username")
    Password_fld = driver.find_element_by_css_selector("#password")
    Login_btn = driver.find_element_by_css_selector(".details-footer > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")

    Username_fld.send_keys("josip@vratakrke.com")
    Password_fld.send_keys("josip1234")
    Login_btn.click()

	### Managment page ###
    Menu_btn = driver.find_element_by_css_selector("#switchAppButton")
    Menu_btn.click()
    Front_desk_btn = driver.find_element_by_css_selector("#wrapper > div.ht-header-container > div > div.ht-header-actions-container > div.options-container.relative-position > div.menu-icon-container > div > div.allApps > div > a:nth-child(2) > div")
    Front_desk_btn.click()

login_to_HT()

def get_rooms(url):
	### Reservation page ###
    
    room_list = []
    driver.get(url)
    time.sleep(1)
    group_btn = driver.find_element_by_css_selector("#action2").click()
    room_nums = driver.find_elements_by_xpath("//div[@class='row-title'][contains(text(),'-')]")
    for i in room_nums:
    	room_list.append(i.text)
     
    room_list_filt = []
    for i in room_list:
        room_list_filt.append(''.join([c for c in i if c.isdigit() or c == '.']))
        
    print(room_list_filt)

get_rooms("https://frontdesk.hotelstouch.com/reservation/info/Reservation_51018")  
    
def get_room_urls():
    room_url_list = []
    room_list_urls = driver.find_elements_by_xpath("//div/a[contains(@href,'info')]")
    for i in room_list_urls:
    	room_url_list.append(i.get_attribute('href'))
    
    print(room_url_list)
    time.sleep(2)
    driver.close()

get_room_urls()
	# for i in range(0, len(df)):
	# 	Actions_btn = driver.find_element_by_css_selector(".infoActions > div:nth-child(7)")
	# 	Actions_btn.click()
	# 	Add_guest_btn = driver.find_element_by_css_selector("#addGuestAction")
	# 	Add_guest_btn.click()
	# 	First_name_fld = driver.find_element_by_css_selector("#firstName").send_keys(df.iloc[i]['First Name'])
	# 	Last_name_fld = driver.find_element_by_css_selector("#lastName").send_keys(df.iloc[i]['Last Name'])
	# 	body = driver.find_element_by_css_selector('body')
	# 	body.click()
	# 	body.send_keys(Keys.PAGE_DOWN)
	# 	time.sleep(2)
	# 	Doc_type_fld = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='documentTypeSelect']"))).click()
	# 	Doc_type_fld2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'hotelstouch-select active')]//input[contains(@placeholder,'search...')]"))).send_keys(df.iloc[i]['Document type'])
	# 	time.sleep(2)
	# 	Doc_type_fld3 = driver.find_element_by_xpath('//*[@id="documentTypeSelect"]/div/div[1]')
	# 	actions = ActionChains(driver)
	# 	actions.move_to_element(Doc_type_fld3)
	# 	actions.click(Doc_type_fld3)
	# 	actions.perform()
	# 	Doc_num_fld = driver.find_element_by_css_selector("#documentNumber").send_keys(str(df.iloc[i]['Doc Number']))
	# 	Residence_country_fld = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='residenceCountrySelect']"))).click()
	# 	Residence_country_fld2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='residenceCountrySelect']//input[@placeholder='search...']"))).send_keys(df.iloc[i]['Country'])
	# 	time.sleep(2)
	# 	Residence_country_fld3 = driver.find_element_by_xpath("//div[@id='residenceCountrySelect']//div[@class='row-title'][contains(text(),'Republika Hrvatska')]")
	# 	actions = ActionChains(driver)
	# 	actions.move_to_element(Residence_country_fld3)
	# 	actions.click(Residence_country_fld3)
	# 	actions.perform()
	# 	Birth_country_fld = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='birthCountrySelect']"))).click()
	# 	Birth_country_fld2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='birthCountrySelect']//input[@placeholder='search...']"))).send_keys(df.iloc[i]['Country'])
	# 	time.sleep(2)
	# 	Birth_country_fld3 = driver.find_element_by_xpath("//div[@id='birthCountrySelect']//div[@class='row-title'][contains(text(),'Republika Hrvatska')]")
	# 	actions = ActionChains(driver)
	# 	actions.move_to_element(Birth_country_fld3)
	# 	actions.click(Birth_country_fld3)
	# 	actions.perform()
	# 	Citizenship_fld = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='citizenshipSelect']"))).click()
	# 	Citizenship_fld2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='citizenshipSelect']//input[@placeholder='search...']"))).send_keys(df.iloc[i]['Country'])
	# 	time.sleep(2)
	# 	Citizenship_fld3 = driver.find_element_by_xpath("//div[@id='citizenshipSelect']//div[@class='row-title'][contains(text(),'Republika Hrvatska')]")
	# 	actions = ActionChains(driver)
	# 	actions.move_to_element(Citizenship_fld3)
	# 	actions.click(Citizenship_fld3)
	# 	actions.perform()
	# 	Residence_city_fld = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='residenceCitySelect']"))).click()
	# 	Residence_city_fld2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='residenceCitySelect']//input[contains(@placeholder,'search...')]"))).send_keys(df.iloc[i]['City'])
	# 	time.sleep(2)
	# 	Residence_city_fld3 = driver.find_element_by_xpath("//div[@class='row-title'][contains(text(),'Zagreb')]")
	# 	actions = ActionChains(driver)
	# 	actions.move_to_element(Residence_city_fld3)
	# 	actions.click(Residence_city_fld3)
	# 	actions.perform()
	# 	Gender_fld = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='genderSelect']"))).click()
	# 	Gender_fld3 = driver.find_element_by_xpath('//*[@id="genderSelect"]/div/div[2]')
		
	# 	actions = ActionChains(driver)
	# 	actions.move_to_element(Gender_fld3)
	# 	actions.click(Gender_fld3)
	# 	actions.perform()
	# 	Dob_fld = driver.find_element_by_css_selector("#birthDate").send_keys(df.iloc[i]['DOB'])
	# 	Cancel_button = driver.find_element_by_xpath("//a[@class='hotelstouch-button']").click()
	# print('Done!')
	# time.sleep(5)
	# driver.close()
	
