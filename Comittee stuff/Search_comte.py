##
##
## Program designed to take inputs and find all instances
## in supplied pdfs. (House Comte mtgs now)
##
## By: Sean Tobin, MPP & EL DAPA
## 
## CURRENTLY CANNOT APPEND TO EXISTING FILE

import os
from shutil import copyfile

search = input('Enter search terms: ')

dirDown = "Webstuff_getall/text_files/"

files = [dirDown+x for x in os.listdir(dirDown)]

resulting_documents = []

for x in files:
    with open(x, encoding = 'utf-8', mode ='r') as f:
        text = f.read()
        if search in text:
            resulting_documents.append(x)

def nameChange(resultTEXTdoc):
    # grabs pdfs in seperate directory for human review
    # to be copied into search results file. 
    
    file = resultTEXTdoc.replace('text_files', 'minute_pdfs')
    file = file.replace('txt', 'pdf')
    return file

def dir_2_name(source):
    name = source.split('/')[-1]
    return name    


humanPDF = [nameChange(x) for x in resulting_documents]

# Copies relevant pdfs where search terms were found in text docs
os.makedirs("results/"+search)
[copyfile(x, "results/"+search+'/'+dir_2_name(x)) for x in humanPDF]           
  

