from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

### Entry ###
glavni_ulaz = "LOZOVAC"

### Time ###
vrijeme = ""

### Date ###
datum = ""

### Guest data ###
guest1 = {}
guest2 = {}
guest3 = {}
guest4 = {}
guest5 = {}
guest6 = {}
guest7 = {}
guest8 = {}
guest9 = {}
guest10 = {}

def login():
    """ Login to eticket url and select KRKA from popup """
    driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
    driver.implicitly_wait(10)
    driver.get("http://oa.rao.hr:8050/#/eticket/partner-web")

    Username_fld = driver.find_element_by_css_selector("#username")
    Password_fld = driver.find_element_by_css_selector("#password")
    Login_btn = driver.find_element_by_css_selector(".btn")

    Username_fld.send_keys("dgrcic0")
    Password_fld.send_keys("EYyROp")
    Login_btn.click()
    time.sleep(1)
    select_krka = driver.find_element_by_css_selector(".col-md-12 > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)").click()
    time.sleep(2)

    driver.get("http://oa.rao.hr:8050/#/eticket/partner-web/nova-najava-krka")

login()

def input_data():
    """ Input data in Nova Najava """
    select_client_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Odaberite klijenta')]"))).click()
    select_client = driver.find_element_by_xpath("//a[contains(text(),'VRATA KRKE D.O.O.')]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_client)
    actions.click(select_client)
    actions.perform()

    click_date_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Datum dolaska')]"))).click()
    time.sleep(1)
    select_date = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/button[1]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_date)
    actions.click(select_date)
    actions.perform()

    time.sleep(1)
    click_time_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Vrijeme dolaska')]"))).click()
    select_time_hours = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[18]")
    select_time_minutes = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_time_hours)
    actions.click(select_time_hours)
    actions.perform()
    time.sleep(2)
    actions.move_to_element(select_time_minutes)
    actions.click(select_time_minutes)
    actions.perform()

    done_btn = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[3]/button").click()

    select_entrance_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Odaberite ulaz')]"))).click()
    select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'LOZOVAC')]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_entrance)
    actions.click(select_entrance)
    actions.perform()

    select_exit_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Odaberite izlaz')]"))).click()
    select_exit = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'LOZOVAC')]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_exit)
    actions.click(select_exit)
    actions.perform()

    click_get_database = driver.find_element_by_xpath("//a[contains(@class,'btn btn-primary fa fa-database')]").click()
    time.sleep(1)

    add_ticket_btn = driver.find_element_by_xpath("//button[contains(text(),'Dodaj ulaznicu')]").click() 
    time.sleep(1)
    select_ticket_btn = driver.find_element_by_xpath("//div[@id='modal-ticket']//td[contains(@class,'ng-binding')][contains(text(),'Grupe odraslih')]").click()
    time.sleep(1)
    select_ticket_amount = driver.find_element_by_xpath("//div[@id='modal-ticket-quantity']//input[@id='form1']").send_keys("2")
    select_add_ticket = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/main[1]/div[5]/div[1]/div[1]/div[3]/button[1]").click()

    #time.sleep(1)
    #ticket_code = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/main[1]/div[4]/div[1]/div[1]/div[1]/h4[1]').text
    #head, sep, tail = ticket_code.partition(" [")
    #ticket_code = head
    #print("Kod: "+ ticket_code + " je uspješno kopiran.")

    # //h4[@class='modal-title ng-binding'] <--- ticket code?
    # /html[1]/body[1]/div[1]/div[1]/main[1]/div[4]/div[1]/div[1]/div[1]/h4[1]

input_data()