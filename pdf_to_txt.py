from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from io import StringIO
import pre_process
import os

class pdf_2_txt():

    def __init__(name):
        self.name = name

    def txt_conv(name):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open(self.name, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
        name_txt = self.name.replace(".pdf" ,"").replace("books","book_txt") 
        print(name_txt)
        if os.path.exists("D:/projects/ZInc/New folder/book_txt"):
            pass
        else : os.mkdir("D:/projects/ZInc/New folder/book_txt")   

        with open(name_txt + ".txt","w",encoding="utf-8") as f:
            f.writelines(text)
        fp.close()
        device.close()
        retstr.close()

    def pdf_txt():
        book_name = os.listdir("D:/projects/ZInc/New folder/books")
        for names in book_name:
            txt_conv("D:/projects/ZInc/New folder/books/" + names )

    def final():
    pdf_txt()
    book_data = []
    book_name = os.listdir("D:/projects/ZInc/New folder/book_txt")
    for books in book_name:
        with open("D:/projects/ZInc/New folder/book_txt/" + books , "r",encoding='utf=8' ) as f :
        data = f.readlines() 
        data = " ".join(data)
        print("preprocessing")
        data = pre_process.preprocess(data)
        
        book_data.append(data)
    print(type(book_data))

    return book_data