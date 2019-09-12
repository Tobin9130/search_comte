##
##
## Program designed to source all committee meeting information
##
## By: Sean Tobin, MPP & EL DAPA
## 
##


##
## Senate Process
##
from bs4 import BeautifulSoup as bs
import requests as r

home = "http://www.senate.michigan.gov/committees/files/"
#audio = "http://www.senate.michigan.gov/committeeaudio/"
#webfiles = "http://www.senate.michigan.gov/committees/files/"

response = r.get(home)
soup = bs(response.text, 'lxml')

# Senate allows for accessing directory of all committee files since 2009
# I wanna analyse when they upload these files

# Senate allows for easy yank of all direct links to files
comte_urls = list(set([home+ option.text for option in soup.find_all('a')[:-3]]))    

#Separate Minutes & Testimony
    # In the senate, apparently the way to differentiate between testimony 
    # and minutes are the Date numerals. How to handle smoothly?
    # if 01-01-01-01 = testimony
    # if 01-01-01 = Minutes

comte_minutes = []
comte_testimony = []
failFile = []

for x in comte_urls:
    doc = x.count('-')
    if doc == 6:
        comte_testimony.append(x)
    elif doc == 5:
        comte_minutes.append(x)
    elif doc == 0 :
        failFile.append(x)

#Because we can grab links to files directly, we just need to name and save them

for x in comte_minutes:
    response = r.get(x)
    name = x.replace(home,'')
    with open('minute_pdfs/'+name, 'wb') as f:
        f.write(response.content)
   
print("We're done here, go home!")   