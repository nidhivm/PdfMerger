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
		

pdfcombiner(inputs)
