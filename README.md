# Beer-Menu-Scrape

About It
-------------
This little program's intent is to gather data from around the web regarding Beer
Beer styles, prices, and breweries to be exact.

As the owner of a very small brewery, i try to keep up on what beers are selling for in my area.
if a particular style of beer is more expensive, and what isn generally on tap.

This helps me keep an eye on the craft beer market on a local level by targeting only the bars on my area.

The eventual hope for this program is to write this data on a daily basis to a SQL database.
Currently it is just a simple python script to scrape data out of tables found at beermenus.com

beermenus.com provides bars, restaurants and breweries with a method of posting their current drafts online.
scaping the data from local establishments that use beermenus.com can help build historical pricing information.

Prerequisites
---------------
This script is written in Python, and was written and tested using Python 3.5.1, Older versions may work but i would try to stick with Python 3.0+.

Thought Process
---------------
Being a small startup brewery, we don't have much money for things like Market Research, Focus Groups, or Conjoint analsys. But you do want to have a rough idea of your market when your trying to formulate a business plan and see if things will even work (financially speaking).

I wrote this little script to try and pull data from local bars use of beermenus.com and gather info about what types of beers are on tap, the average price per ounce of certain styles, price per ounnce of alchohol (%abv * serving size)/Price,  and if the prices in the local market have changed over time. 

The hope is that this will give us a better idea of where we should be pricing in the market place to remain competitive.
