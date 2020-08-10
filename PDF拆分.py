import PyPDF2

# from PyPDF2 import PdfFileReader ,PdfFileWriter
pdfR = PyPDF2.PdfFileReader("001.pdf")
pdfN = pdfR.numPages
Ii = 1
Oo = pdfN // Ii + 1 if pdfN % Ii else 0
for num in range(1, pdfN+1):
    pdfW = PyPDF2.PdfFileWriter()
    for pageNum in range(Ii * (num - 1), Ii * num if num != Oo else pdfN):
        pageObj = pdfR.getPage(pageNum)
        pdfW.addPage(pageObj)
    with open("PDFread %s" % num + ".pdf", "wb")as pdfOutputFile:
            pdfW.write(pdfOutputFile)
