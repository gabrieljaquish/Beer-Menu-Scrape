from bs4 import BeautifulSoup
import urllib2
import time
import sys
import csv

####################### Functions

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

    #Remove the escaped chars from each line as they mess up BeautifulSoup
    for line in raw_page:
        if line.find('table') != -1:
            #REMOVE Escape Chars
            line = line.replace("\\n","")
            line = line.replace("\\\"","\"")
            line = line.replace("\\/","/")
            soup = BeautifulSoup(line, 'html.parser')
            tbody = []
            tbody = soup.findAll('table')
            return tbody

#################################################################
############ Main

#open the file containing the menu numbers to scrape
#hardcoded at the moment to a filename,
#this will take filename as an argument in the future.
with open("menu-numbers.txt") as f:
    MenuNumbersFile = f.readlines()

#loop through the file to get menu numbers
#lines that start with # are comments ignored, just like in python
menu_numbers = []
for line in MenuNumbersFile:
    if line.startswith("#"):
        print(line)
    #elif line.isdigit():
    else:
        menu_numbers.append(line)

#Array to store html tables (pages contain multiple tables)
html_tables = []
for menu in menu_numbers:
    #passes back an array of BeautifulSoup Objects each containg 1 table
    html_tables = ScrapeMenu(menu)

    #Array to store rows of a table
    table_rows = []
    cells = []
    aBeer = []
    Beers =[]

    for table in html_tables:
        #record the table headers in the first index
        table_rows = table.find_all("th")
        for cell in table_rows:
            if cell.getText().strip():
                aBeer += "," + str(cell.getText().strip())
        Beers.append(aBeer)
        aBeer = ""

        #Pull out all table rowes and store them
        table_rows = table.find_all("tr")
        #iterate through the table rows
        for row in table_rows:
            #add each table row's cells to the 2D array
            cells.append(row.find_all("td"))

        for each_row in cells:
            for each_cell in each_row:
                if each_cell.getText().strip():
                    if aBeer == "":
                        aBeer += each_cell.getText().strip()
                    else:
                        aBeer += "," + each_cell.getText().strip()
            Beers.append(aBeer)
            aBeer = ""


#Name the scrape file with todays date + the menu number
date_filename = time.strftime("%d-%m-%Y") + "_" + menu +".csv"
f = open(date_filename, 'w')


for each_beer in Beers:
    f.write(str(each_beer) + "\n")
