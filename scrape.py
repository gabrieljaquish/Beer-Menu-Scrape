from bs4 import BeautifulSoup
import urllib2
import time
import csv

def GetHTML(url):
    #Pull down the menu number's widget page
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    #Use .readLINES() here to get html line by line
    return response.readlines()

def ScrapeMenu(menu_num):
    #Beer Menus widget base url
    url_base = 'https://www.beermenus.com/menu_widgets/'

    #Beer Menus baseurl + the menue number we want
    url = url_base + menu_num

    #Get the HTML from the page using the get HTML function
    raw_page = GetHTML(url)

    #Array of strings with \ stripped out
    the_page = []

    #Remove the backslashes from each line as they mess up BeautifulSoup
    for line in raw_page:
        if line.find('table') != -1:
            #REMOVE Escape Chars
            #remove \n's
            line = line.replace("\\n","")
            #make \" just "
            line = line.replace("\\\"","\"")
            #make \/ just /
            line = line.replace("\\/","/")
            the_page.append(line)
            soup = BeautifulSoup(the_page[0], 'html.parser')
            print(soup.prettify())


#open the file containing the menu numbers to scrape
with open("menu-numbers.txt") as f:
    MenuNumbersFile = f.readlines()

menu_numbers = []
#loop through the file to get menu numbers
#lines that start with # are comments ignored, just like in python


for line in MenuNumbersFile:
    if line.startswith("#"):
        print(line)
    else:
        #NEEDS ERROR CHECKING
        menu_numbers.append(line)

for menu in menu_numbers:
    ScrapeMenu(menu)


#Name the scrape file with todays date + the menu number
date_filename = time.strftime("%d-%m-%Y") + "_" + "1234"

#testing
print(date_filename)

#Write the file as a csv to disk using the date-filename
