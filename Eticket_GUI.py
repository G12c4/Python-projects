### Tkinter import ###
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, font
from datetime import datetime
### Selenium import ###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

### Tkinter start ###
height = 600
width = 400

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

root = tk.Tk()
root.title("E-Ticket Najava")

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg="#99b898", highlightbackground="green", highlightcolor="green", highlightthickness=2, width=100, height=100, bd= 0)
frame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.93)

name_label = tk.Label(frame, bg="#99b898",text="")
name_label.grid(row=2, column=0)

name_label = tk.Label(frame, text="Ime i Prezime:")
name_label.grid(row=4, column=1)

name_entry_1_var = StringVar()
name_entry_1_var.set('')
guest1["Ime"] = name_entry_1_var.get()

name_entry_1 = tk.Entry(frame, textvariable = name_entry_1_var)
name_entry_1.grid(row=5, column=1)

name_entry_2_var = StringVar()
name_entry_2_var.set('')
guest2["Ime"] = name_entry_2_var.get()

name_entry_2 = tk.Entry(frame, textvariable = name_entry_2_var)
name_entry_2.grid(row=6, column=1)

name_entry_3_var = StringVar()
name_entry_3_var.set('')
guest3["Ime"] = name_entry_3_var.get()

name_entry_3 = tk.Entry(frame, textvariable = name_entry_3_var)
name_entry_3.grid(row=7, column=1)

name_entry_4_var = StringVar()
name_entry_4_var.set('')
guest4["Ime"] = name_entry_4_var.get()

name_entry_4 = tk.Entry(frame, textvariable = name_entry_4_var)
name_entry_4.grid(row=8, column=1)

name_entry_5_var = StringVar()
name_entry_5_var.set('')
guest5["Ime"] = name_entry_5_var.get()

name_entry_5 = tk.Entry(frame, textvariable = name_entry_5_var)
name_entry_5.grid(row=9, column=1)

name_entry_6_var = StringVar()
name_entry_6_var.set('')
guest6["Ime"] = name_entry_6_var.get()

name_entry_6 = tk.Entry(frame, textvariable = name_entry_6_var)
name_entry_6.grid(row=10, column=1)

name_entry_7_var = StringVar()
name_entry_7_var.set('')
guest7["Ime"] = name_entry_7_var.get()

name_entry_7 = tk.Entry(frame, textvariable = name_entry_7_var)
name_entry_7.grid(row=11, column=1)

name_entry_8_var = StringVar()
name_entry_8_var.set('')
guest8["Ime"] = name_entry_8_var.get()

name_entry_8 = tk.Entry(frame, textvariable = name_entry_8_var)
name_entry_8.grid(row=12, column=1)

name_entry_9_var = StringVar()
name_entry_9_var.set('')
guest9["Ime"] = name_entry_9_var.get()

name_entry_9 = tk.Entry(frame, textvariable = name_entry_9_var)
name_entry_9.grid(row=13, column=1)

name_entry_10_var = StringVar()
name_entry_10_var.set('')
guest10["Ime"] = name_entry_10_var.get()

name_entry_10 = tk.Entry(frame, textvariable = name_entry_10_var)
name_entry_10.grid(row=14, column=1)

dob_label = tk.Label(frame, text="Datum rođenja:")
dob_label.grid(row=4, column=2)

name_entry_1_var = StringVar()
name_entry_1_var.set('')
guest1["DOB"] = name_entry_1_var.get()

dob_entry_1 = tk.Entry(frame, textvariable = name_entry_1_var)
dob_entry_1.grid(row=5, column=2)

dob_entry_2_var = StringVar()
dob_entry_2_var.set('')
guest2["DOB"] = dob_entry_2_var.get()

dob_entry_2 = tk.Entry(frame, textvariable = name_entry_2_var)
dob_entry_2.grid(row=6, column=2)

dob_entry_3_var = StringVar()
dob_entry_3_var.set('')
guest3["DOB"] = dob_entry_3_var.get()

dob_entry_3 = tk.Entry(frame, textvariable = name_entry_3_var)
dob_entry_3.grid(row=7, column=2)

dob_entry_4_var = StringVar()
dob_entry_4_var.set('')
guest4["DOB"] = dob_entry_4_var.get()

dob_entry_4 = tk.Entry(frame, textvariable = name_entry_4_var)
dob_entry_4.grid(row=8, column=2)

dob_entry_5_var = StringVar()
dob_entry_5_var.set('')
guest5["DOB"] = dob_entry_5_var.get()

dob_entry_5 = tk.Entry(frame, textvariable = name_entry_5_var)
dob_entry_5.grid(row=9, column=2)

dob_entry_6_var = StringVar()
dob_entry_6_var.set('')
guest6["DOB"] = dob_entry_6_var.get()

dob_entry_6 = tk.Entry(frame, textvariable = name_entry_6_var)
dob_entry_6.grid(row=10, column=2)

dob_entry_7_var = StringVar()
dob_entry_7_var.set('')
guest7["DOB"] = dob_entry_7_var.get()

dob_entry_7 = tk.Entry(frame, textvariable = name_entry_7_var)
dob_entry_7.grid(row=11, column=2)

dob_entry_8_var = StringVar()
dob_entry_8_var.set('')
guest8["DOB"] = dob_entry_8_var.get()

dob_entry_8 = tk.Entry(frame, textvariable = name_entry_8_var)
dob_entry_8.grid(row=12, column=2)

dob_entry_9_var = StringVar()
dob_entry_9_var.set('')
guest9["DOB"] = dob_entry_9_var.get()

dob_entry_9 = tk.Entry(frame, textvariable = name_entry_9_var)
dob_entry_9.grid(row=13, column=2)

dob_entry_10_var = StringVar()
dob_entry_10_var.set('')
guest10["DOB"] = dob_entry_10_var.get()

dob_entry_10 = tk.Entry(frame, textvariable = name_entry_10_var)
dob_entry_10.grid(row=14, column=2)

dob_label = tk.Label(frame, text="Odaberite ulaznicu:")
dob_label.grid(row=4, column=3)

# Create a Tkinter variable
ticket_guest1 = tk.StringVar(root)

# Dictionary with options
choices1_ticket1 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest1.set('Grupa odraslih') # set the default option

popupMenu_ticket1 = tk.OptionMenu(frame, ticket_guest1, *choices1_ticket1)
popupMenu_ticket1.grid(row = 5, column =3)

# on change dropdown value
def change_dropdown_ticket1(*args):
    #print( ticket_guest1.get() )
    guest1["Ulaznica"] = ticket_guest1.get()
    print(guest1["Ulaznica"])
    
# link function to change dropdown
ticket_guest1.trace('w', change_dropdown_ticket1)

# Create a Tkinter variable
ticket_guest2 = tk.StringVar(root)

# Dictionary with options
choices1_ticket2 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest2.set('Grupa odraslih') # set the default option

popupMenu_ticket2 = tk.OptionMenu(frame, ticket_guest2, *choices1_ticket2)
popupMenu_ticket2.grid(row =6, column =3)

# on change dropdown value
def change_dropdown_ticket2(*args):
    #print( ticket_guest2.get() )
    guest1["Ulaznica"] = ticket_guest2.get()
    print(guest1["Ulaznica"])    
# link function to change dropdown
ticket_guest2.trace('w', change_dropdown_ticket2)

# Create a Tkinter variable
ticket_guest3 = tk.StringVar(root)

# Dictionary with options
choices1_ticket3 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest3.set('Grupa odraslih') # set the default option

popupMenu_ticket3 = tk.OptionMenu(frame, ticket_guest3, *choices1_ticket3)
popupMenu_ticket3.grid(row =7, column =3)

# on change dropdown value
def change_dropdown_ticket3(*args):
    #print( ticket_guest3.get() )
    guest1["Ulaznica"] = ticket_guest3.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest3.trace('w', change_dropdown_ticket3)

# Create a Tkinter variable
ticket_guest4 = tk.StringVar(root)

# Dictionary with options
choices1_ticket4 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest4.set('Grupa odraslih') # set the default option

popupMenu_ticket4 = tk.OptionMenu(frame, ticket_guest4, *choices1_ticket4)
popupMenu_ticket4.grid(row =8, column =3)

# on change dropdown value
def change_dropdown_ticket4(*args):
    #print( ticket_guest4.get() )
    guest1["Ulaznica"] = ticket_guest4.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest4.trace('w', change_dropdown_ticket4)

# Create a Tkinter variable
ticket_guest5 = tk.StringVar(root)

# Dictionary with options
choices1_ticket5 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest5.set('Grupa odraslih') # set the default option

popupMenu_ticket5 = tk.OptionMenu(frame, ticket_guest5, *choices1_ticket5)
popupMenu_ticket5.grid(row =9, column =3)

# on change dropdown value
def change_dropdown_ticket5(*args):
    #print( ticket_guest5.get() )
    guest1["Ulaznica"] = ticket_guest5.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest5.trace('w', change_dropdown_ticket5)

# Create a Tkinter variable
ticket_guest6 = tk.StringVar(root)

# Dictionary with options
choices1_ticket6 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest6.set('Grupa odraslih') # set the default option

popupMenu_ticket6 = tk.OptionMenu(frame, ticket_guest6, *choices1_ticket6)
popupMenu_ticket6.grid(row =10, column =3)

# on change dropdown value
def change_dropdown_ticket6(*args):
    #print( ticket_guest6.get() )
    guest1["Ulaznica"] = ticket_guest6.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest6.trace('w', change_dropdown_ticket6)

# Create a Tkinter variable
ticket_guest7 = tk.StringVar(root)

# Dictionary with options
choices1_ticket7 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest7.set('Grupa odraslih') # set the default option

popupMenu_ticket7 = tk.OptionMenu(frame, ticket_guest7, *choices1_ticket7)
popupMenu_ticket7.grid(row =11, column =3)

# on change dropdown value
def change_dropdown_ticket7(*args):
    #print( ticket_guest7.get() )
    guest1["Ulaznica"] = ticket_guest7.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest7.trace('w', change_dropdown_ticket6)

# Create a Tkinter variable
ticket_guest8 = tk.StringVar(root)

# Dictionary with options
choices1_ticket8 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest8.set('Grupa odraslih') # set the default option

popupMenu_ticket8 = tk.OptionMenu(frame, ticket_guest8, *choices1_ticket8)
popupMenu_ticket8.grid(row =12, column =3)

# on change dropdown value
def change_dropdown_ticket8(*args):
    #print( ticket_guest8.get() )
    guest1["Ulaznica"] = ticket_guest8.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest8.trace('w', change_dropdown_ticket8)

# Create a Tkinter variable
ticket_guest9 = tk.StringVar(root)

# Dictionary with options
choices1_ticket9 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest9.set('Grupa odraslih') # set the default option

popupMenu_ticket9 = tk.OptionMenu(frame, ticket_guest9, *choices1_ticket9)
popupMenu_ticket9.grid(row =13, column =3)

# on change dropdown value
def change_dropdown_ticket9(*args):
    #print( ticket_guest9.get() )
    guest1["Ulaznica"] = ticket_guest9.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest9.trace('w', change_dropdown_ticket9)

# Create a Tkinter variable
ticket_guest10 = tk.StringVar(root)

# Dictionary with options
choices1_ticket10 = { "Grupa djece 0-7", "Grupa djece", "Grupa odraslih", }
#ticket_guest10.set('Grupa odraslih') # set the default option

popupMenu_ticket10 = tk.OptionMenu(frame, ticket_guest10, *choices1_ticket10)
popupMenu_ticket10.grid(row =14, column =3)

# on change dropdown value
def change_dropdown_ticket10(*args):
    #print( ticket_guest10.get() )
    guest1["Ulaznica"] = ticket_guest10.get()
    print(guest1["Ulaznica"])
# link function to change dropdown
ticket_guest10.trace('w', change_dropdown_ticket10)

date_of_arrival_label = tk.Label(frame, text="Datum:")
date_of_arrival_label.grid(row=0, column=1)

def app_date():
    def print_sel():
        print(cal.selection_get())
        cal.see(datetime.date(year=2020, month=2, day=5))
        top.destroy()
        
    top = tk.Toplevel(frame)

    import datetime
    today = datetime.date.today()

    mindate = today
    maxdate = today + datetime.timedelta(days=5)
    #print(mindate, maxdate)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2020, month=6, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

ttk.Button(frame, text='Izaberi datum', command=app_date).grid(row=1, column=1)

#date_of_arrival_entry_1 = tk.Entry(frame)
#date_of_arrival_entry_1.grid(row=1, column=1)

time_of_arrival_label = tk.Label(frame, text="Vrijeme:")
time_of_arrival_label.grid(row=0, column=2)

class app_time(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'8')
        self.hour = tk.Spinbox(self,from_=8,to=17,wrap=True,textvariable=self.hourstr,width=5,state="readonly")
        self.minstr=tk.StringVar(self,'15')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,values=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55), wrap=True,textvariable=self.minstr,width=5,state="readonly")
        self.hour.grid(row=0,column=2)
        self.min.grid(row=0,column=3)

    def trace_var(self,*args):
        if self.last_value == "55" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="17" else 8)
        self.last_value = self.minstr.get()

app_time(frame).grid(row=1,column=2)

#time_of_arrival_entry_1 = tk.Entry(frame)
#time_of_arrival_entry_1.grid(row=1, column=2)

entry_location_label = tk.Label(frame, text="Ulaz:")
entry_location_label.grid(row=0, column=3)

# Create a Tkinter variable
tkvar1 = tk.StringVar(root)

# Dictionary with options
choices1 = { "KISTANJE", "LUGAREVA KUĆA", "BURNUM", "PULJANI", "LOZOVAC", "KAMP", "ROŠKI SLAP", "SKRADIN", }
tkvar1.set('LOZOVAC') # set the default option

popupMenu = tk.OptionMenu(frame, tkvar1, *choices1)
popupMenu.grid(row = 1, column =3)

# on change dropdown value
def change_dropdown(*args):
    #print( tkvar1.get() )
    glavni_ulaz = tkvar1.get()
    print("--> " + glavni_ulaz)
    

# link function to change dropdown
tkvar1.trace('w', change_dropdown)

lower_frame = tk.Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=2, width=100, height=100, bd= 0)
lower_frame.place(relx= 0.5, rely=0.73, relwidth=0.75, relheight=0.1, anchor='n')

label_output = tk.Label(lower_frame, font=('Courier', 10))
label_output.place(relwidth=1, relheight=1)

label_output['text'] = "Radim ko crv u kamenu!\n Pričekaj ..."

button = tk.Button(frame, text="Test button", fg="black")
button.place(relx=0.37, rely=0.88, relwidth=0.25, relheight=0.1)

root.mainloop()

### Tkinter end ###

### Selenium eticket bot start ###
def selen_eticket_bot():
    ### start driver ###
    driver = webdriver.Firefox(executable_path=r'C:\Users\Admin\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
    driver.implicitly_wait(10)
    driver.get("http://oa.rao.hr:8050/#/eticket/partner-web")
    
    ### set user name, pass, login positions ###
    Username_fld = driver.find_element_by_css_selector("#username")
    Password_fld = driver.find_element_by_css_selector("#password")
    Login_btn = driver.find_element_by_css_selector(".btn")

    ### enter user name, pass and click login button ###
    Username_fld.send_keys("dgrcic0")
    Password_fld.send_keys("EYyROp")
    Login_btn.click()
    time.sleep(1)
    select_krka = driver.find_element_by_css_selector(".col-md-12 > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)").click()
    time.sleep(2)

    ### open url ###
    driver.get("http://oa.rao.hr:8050/#/eticket/partner-web/nova-najava-krka")

    ### select vrata krke from popup ###
    select_client_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Odaberite klijenta')]"))).click()
    select_client = driver.find_element_by_xpath("//a[contains(text(),'VRATA KRKE D.O.O.')]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_client)
    actions.click(select_client)
    actions.perform()

    ###select datum dolaska ###
    click_date_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Datum dolaska')]"))).click()
    time.sleep(1)
    ################################ enter if loop #######
    select_date = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/button[1]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_date)
    actions.click(select_date)
    actions.perform()
    
    ### select vrijeme dolaska ###
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
    if glavni_ulaz == "LOZOVAC":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'LOZOVAC')]")
    elif glavni_ulaz == "SKRADIN":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'SKRADIN')]")
    elif glavni_ulaz == "KISTANJE":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'KISTANJE')]")
    elif glavni_ulaz == "LUGAREVA KUĆA":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'LUGAREVA KUĆA')]")
    elif glavni_ulaz == "BURNUM":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'BURNUM')]")
    elif glavni_ulaz == "PULJANI":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'PULJANI')]")
    elif glavni_ulaz == "KAMP":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'KAMP')]")
    elif glavni_ulaz == "ROŠKI SLAP":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'ROŠKI SLAP')]")
        
    actions = ActionChains(driver)
    actions.move_to_element(select_entrance)
    actions.click(select_entrance)
    actions.perform()

    select_exit_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Odaberite izlaz')]"))).click()    
    if glavni_ulaz == "LOZOVAC":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'LOZOVAC')]")
    elif glavni_ulaz == "SKRADIN":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'SKRADIN')]")
    elif glavni_ulaz == "KISTANJE":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'KISTANJE')]")
    elif glavni_ulaz == "LUGAREVA KUĆA":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'LUGAREVA KUĆA')]")
    elif glavni_ulaz == "BURNUM":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'BURNUM')]")
    elif glavni_ulaz == "PULJANI":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'PULJANI')]")
    elif glavni_ulaz == "KAMP":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'KAMP')]")
    elif glavni_ulaz == "ROŠKI SLAP":
        select_entrance = driver.find_element_by_xpath("//div[contains(@class,'btn-group open')]//a[contains(@class,'ng-binding ng-scope')][contains(text(),'ROŠKI SLAP')]")
    
    actions = ActionChains(driver)
    actions.move_to_element(select_exit)
    actions.click(select_exit)
    actions.perform()

    click_get_database = driver.find_element_by_xpath("//a[contains(@class,'btn btn-primary fa fa-database')]").click()
    time.sleep(1)

    add_ticket_btn = driver.find_element_by_xpath("//button[contains(text(),'Dodaj ulaznicu')]").click() 
    time.sleep(1)
    if 
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

selen_eticket_bot()
### Selenium eticket bot end ###