import pyautogui as pg
import pandas as pd
import time

pg.FAILSAFE = True
pg.PAUSE = 0.25
df = pd.read_excel(r'C:\Users\Admin\Documents\test.xlsx')

Actions_btn = (1163, 183)
Add_guest_btn = (1165, 213)
First_name_fld = (370, 590)
Last_name_fld = (836, 587)
Doc_num_fld = (722, 340)
Country_fld = (378, 420)
Birth_country_fld = (367, 503)
Citizenship_fld = (377, 612)
Resident_city_fld = (594, 418)
Gender_fld = (609, 613)
Bod_fld = (802, 505)
def Document_type_fld():
	pg.click(619, 552)
	pg.hotkey('pgdn')
	time.sleep(1)
	pg.click(373, 335)

pg.click(Actions_btn, button='left')
time.sleep(1)

pg.click(Add_guest_btn, button='left')
time.sleep(5)

pg.click(First_name_fld, button='left')
time.sleep(1)
for i in range(0, len(df)):
	pg.typewrite(df.iloc[i]['First Name'], interval=0.05)

	pg.click(Last_name_fld, button='left')
	time.sleep(1)
	pg.typewrite(df.iloc[i]['Last Name'], interval=0.05)

	Document_type_fld()
	pg.typewrite('Osobna iskaznica', interval=0.05)
	time.sleep(1)
	pg.click(399, 380)

	pg.click(Doc_num_fld, button='left')
	time.sleep(1)
	pg.typewrite(str(df.iloc[i]['Doc Number']), interval=0.05)

	pg.click(Country_fld, button='left')
	time.sleep(3)
	pg.typewrite(df.iloc[i]['Country'], interval=0.05)
	pg.click(383, 473)

	pg.click(Birth_country_fld, button='left')
	time.sleep(3)
	pg.typewrite(df.iloc[i]['Country'], interval=0.05)
	pg.click(384, 562)

	pg.click(Citizenship_fld, button='left')
	time.sleep(3)
	pg.typewrite(df.iloc[i]['Country'], interval=0.05)
	pg.click(376, 651)

	pg.click(Resident_city_fld, button='left')
	time.sleep(3)
	pg.typewrite('Zagreb', interval=0.05)
	pg.click(589, 459)

	pg.click(Gender_fld, button='left')
	time.sleep(3)
	pg.click(579, 637)

	pg.click(Bod_fld, button='left')
	time.sleep(3)
	pg.typewrite(df.iloc[i]['DOB'])

	pg.click(556, 860)
	pg.click(752, 850)
	break