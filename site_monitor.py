# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# Import date and time (to print the time the script was executed)
import datetime
now = datetime.datetime.now()

# This is a pretty simple script. The script downloads the homepage of xyz, and if it finds some text, emails me.
# If it does not find some text, it waits 2 hours and downloads the homepage again.

# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "https://www.kbc-zagreb.hr/pocetna/natjecaji/natjecaji-za-posao/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(soup).find("prvostupnik sestrinstva") == -1:
        # wait 2 hours,
        time.sleep(7200)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with a subject line,
        subject = 'Subject: Provjeri natjecaj za posao!'
        # create body text
        text = 'Link za natjecaj: https://www.kbc-zagreb.hr/pocetna/natjecaji/natjecaji-za-posao/'
        # set the 'from' address,
        fromaddr = 'josipgrcic@gmail.com'
        # set the 'to' addresses,
        toaddrs  = ['magdalena.kunic@gmail.com']

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (fromaddr, ", ".join(toaddrs), subject, text)

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("josipgrcic@gmail.com", "rtosqjauefblhbuq")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Subject: ' + subject)
        print('Body: ' + text)
        print ("Current date and time:")
        print (now)

        # send the email
        server.sendmail(fromaddr, toaddrs, message)
        # disconnect from the server
        server.quit()

        break
