from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pyautogui as pg
import pyperclip
import random
import string
import time

### global variables ###
ime = []
prezime = []
adresa = []
mobitel = []
oib = []
email = []

### GUI positions ###
ime_fld = (225, 83)
prezime_fld = (225, 132)
adresa_fld = (225, 183)
mobitel_fld = (225, 231)
oib_fld = (225, 289)
email_fld = (225, 332)

### random email generator ###
def rand_email_gen(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
email.append(rand_email_gen(8)+"@cdc.com")

### copy from GUI fields ###
def copy_paste(position):
    pyperclip.copy("")
    pg.click(position, button='left')
    pg.hotkey('ctrl', 'a')
    #time.sleep(1)
    pg.hotkey('ctrl', 'c')
    time.sleep(1)
    return pyperclip.paste()

### copy ime field ###
paste = copy_paste(ime_fld)
ime.append(paste)

### copy prezime field ###
paste = copy_paste(prezime_fld)
prezime.append(paste)

### copy adresa field ###
paste = copy_paste(adresa_fld)
adresa.append(paste)

### copy mobitel field ###
paste = copy_paste(mobitel_fld)
mobitel.append(paste)

### copy oib field ###
paste = copy_paste(oib_fld)
oib.append(paste)

### copy email field ###
paste = copy_paste(email_fld)
email.append(paste)

# print(ime)
# print(prezime)
# print(adresa)
# print(mobitel)
# print(oib)
# print(email)

### firefox webdriver headless setup ###
# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options, executable_path=r"C:\Users\Admin\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe")
driver = webdriver.Firefox(executable_path=r"C:\Users\Admin\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe")

def login_to_scheduler():
    
    driver.implicitly_wait(10)
    driver.get("https://scheduler.live/default.aspx?alarm=1")

	### Login page ###
    Username_fld = driver.find_element_by_css_selector("#txKorisnik")
    Password_fld = driver.find_element_by_css_selector("#txLozinka")
    Login_btn = driver.find_element_by_css_selector("#gmbLogIn")

    Username_fld.send_keys("Sladic")
    Password_fld.send_keys("sladic")
    Login_btn.click()
    
login_to_scheduler()

def input_new_patient():
    
    pacijenti_btn = driver.find_element_by_xpath("//span[contains(text(),'Pacijenti')]").click()
    time.sleep(1)
    dodaj_pacijenta_btn = driver.find_element_by_xpath("//a[contains(text(),'Dodavanje novog pacijenta')]").click()
    
    IME = driver.find_element_by_css_selector('#txPacijentiIme').send_keys(ime)
    PREZIME = driver.find_element_by_css_selector('#txPacijentiPrezime').send_keys(prezime)	
    ADRESA = driver.find_element_by_css_selector('#txPacijentiAdresa').send_keys(adresa)	
    #TELEFON = driver.find_element_by_css_selector('#txPacijentiTelefon1').send_keys("")	
    MOBITEL = driver.find_element_by_css_selector('#txPacijentiMobitel1').send_keys(mobitel)	
    OIB = driver.find_element_by_css_selector('#txPacijentiFax').send_keys(oib)	
    EMAIL = driver.find_element_by_css_selector('#txPacijentiMail').send_keys(email)	
    #NAPOMENA = driver.find_element_by_css_selector('#txPacijentiNapomena').send_keys("")	
    ORDINACIJA = driver.find_element_by_css_selector('#izbPacijentiOrdinacija').click()
    ORDINACIJA_SLADIC = driver.find_element_by_xpath("//option[contains(text(),'Ordinacija1 SLADIC')]").click()
    DRZAVA = driver.find_element_by_xpath("//option[contains(text(),'Italija')]").click()
    # CANCEL = driver.find_element_by_xpath('//*[@id="gmbPopUpOdustani"]').click()
    # SAVE = driver.find_element_by_xpath('//*[@id="gmbPopUpSnimi"]').click()
    
input_new_patient()
#driver.close()
