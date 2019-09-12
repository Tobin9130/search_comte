#Sadnbox dev for programmatically understanding committee actions
# this just converts all pdfs in the directory to raw text

# By Sean Tobin

import PyPDF2, re, os

    
def pdfData(PDF):
    # takes listed pdfs and converts them to PyPDF objects
    
    pdfFileObj = open(PDF, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    index = pdfReader.numPages
    pageslist = []
    i = 0
    while i < index:
        page = pdfReader.getPage(i).extractText()
        pageslist.append(page)
        i = i + 1
        
    return pageslist

def stringManip(textList):
    output = []
    for x in textList:
        add = x.replace('\n', '')
        add = re.sub(' +',' ', add)
        output.append(add)
    output = ''.join(output)
    return output

fileList = [x for x in os.listdir('minute_pdfs') if x[-3:]=="pdf"]


for x in fileList:
    file = x
    one = pdfData('minute_pdfs/'+file)
    two = stringManip(one)
    with open(str('text_files/' + file[:-3]) + 'txt',encoding = 'utf-8', mode ='w') as f:
        f.write(two)

print("That was fun! Now NLP")