##
##
## Program designed to source all committee meeting information
##
## By: Sean Tobin, MPP & EL DAPA
## 
##


from bs4 import BeautifulSoup as bs
import requests as r

##
## House Process. Current edition only most recent session
##

home = "http://www.house.mi.gov/"
Origin = "http://www.house.mi.gov/MHRPublic/committee.aspx"
comteCH = '/MHRPublic/CommitteeInfo.aspx?comkey='

response = r.get(Origin)
soup = bs(response.text, 'lxml')

idlist = []

for option in soup.find_all('option'):
    #Give a list of Comte names and their ID(called a 'key')
    # Connects option['value'] to comte chunk after 'home'
    if int(option['value']) > 1:
        idlist.append(option['value'])
    else:
        print("V blank_comte_page V")
    print(option.text)

#generate urls
comte_urls = set([home+comteCH+x for x in idlist])

# grab urls
responses = [r.get(x) for x in comte_urls]

# get page info
info = [bs(x.text, 'lxml') for x in responses]

comte_minutes = []
comte_testimony = []
## STILL HAVE TO WRITE TESTIMONY to file ##

for page in info:
    for option in page.find_all('option'):
        #Give a list of Comte names and their ID(called a 'key')
        # Connects option['value'] to comte chunk after 'home'
        if 'testimony' in str(option):
            comte_testimony.append(option['value'])
        if 'Minutes' in str(option):
            comte_minutes.append(option['value'])

## grab all links to minute pdfs
#minute_pdfs = [r.get(home+x) for x in set(comte_minutes)]

def dir_2_name(source):
    name = source.split('/')[-1]
    return name

for x in set(comte_minutes):
    response = r.get(home+x)
    with open('minute_pdfs/'+dir_2_name(x), 'wb') as f:
        f.write(response.content)
   
print("We're done here, go home!")        