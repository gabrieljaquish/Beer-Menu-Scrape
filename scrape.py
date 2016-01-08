from bs4 import BeautifulSoup
import urllib2
import time
import csv

req = urllib2.Request('http://www.voidspace.org.uk')
response = urllib2.urlopen(req)
the_page = response.read()

for line in the_page:
    if line.find('table.beermenu')
        the_page = line

print(the_page)

filename = time.strftime("%d-%m-%Y")

with open(filename, 'w', newline='') as fp:
    csv_file = csv.writer(fp, delimiter=',')
    csv_file.writerows(data)
