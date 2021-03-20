import sys
import PyPDF2

inputs = sys.argv[1:] #grabs all argvs

#pdf reader
with open('test1.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        #print(reader.numPages)    #get num pages
        page = reader.getPage(0)   #get page 0 in page
        page.rotateClockwise(90)   #rotate clockwise
        writer = PyPDF2.PdfFileWriter()  #creating writer object
        writer.addPage(page)       #add page to the object
        with open('tilt.pdf', 'wb') as new_file: 
                writer.write(new_file)  #create a new tilt.pdf

#merge files    
def pdfcombiner(pdf_list):
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
                merger.append(pdf)
        merger.write('super.pdf')

#watermark all pages (wtr.pdf)
template      = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark     = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output        = PyPDF2.PdfFileWriter()

def pdfwatermark(pdffile):
        for i in range(pdffile.getNumPages()):
                pdf_page = pdffile.getPage(i)
                pdf_page.mergePage(watermark.getPage(0))                
                output.addPage(pdf_page)

                with open('watermarked_output.pdf', 'wb') as file:
                        output.write(file)

                        
pdfwatermark(template)
pdfcombiner(inputs)
