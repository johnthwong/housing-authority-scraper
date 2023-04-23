# Introuduction
The Housing Authority's data on secondary transactions of government-built, privately-owned flats are notoriously difficult to access as the agency does not offer a way to download transaction data or an API and data must be requested with a web form by month.

The Housing Authority Scraper gathers the transaction count of these flats by month and year and generates a csv file that can be easily used for further research, such as the analysis of housing market momentum or affordability.

Sidenote: Government-built, privately-owned flats are typically referred to as subsidized sale flats (SSF) but also referred to as Home Ownership Flats (HOS) at times (the latter of which being a misnomer, but that’s a whole other story). 

# How to Use
Before running, the following are necessary. Installation guides can be found online.
- Download the GitHub folder that contains this text file (click the Code button, select Download ZIP from the dropdown menu)
- Have access to Terminal (Mac) or Powershell (Windows)
- Install Python, latest version
- Install Chrome or Firefox
- Install WebDriver (for Chrome) or geckdriver (for Firefox)
- Install the following Python packages: pandas, Selenium

Once all the dependencies are installed, to run the scraper, run the following lines of code in Terminal/Powershell:
```
python3 
import sys 
sys.path.append(‘Users/john/Downloads’) # replace the file path with where the downloaded folder is located on your computer
from housing-authority-scraper-main.ha_scrape_4 import scrape
scrape(2021, 2022) # input any number of years you’d like to scrape
```

Once run, the scraper will generate a .csv file with the requested data in your working directory. If you do not know where your working directory is, run the following lines of code to find out where the output file is stored.
```
python3
import os
os.getcwd()
```

Have fun!
