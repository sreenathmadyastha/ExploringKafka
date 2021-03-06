from PyPDF2 import PdfFileReader
def getTextPDF (pdfFileName, password=''):
  pdf_file = open(pdfFileName, 'rb')
  read_pdf = PdfFileReader(pdf_file)
  if password != '':
   read_pdf.decrypt(password)
  text = []
  for i in range(-1,read_pdf.getNumPages()-1):
   text.append(read_pdf.getPage(i).extractText())
  return '\n'.join(text)