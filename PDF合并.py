import PyPDF2
filenames = ("PDFread 1.pdf" , "PDFread 2.pdf")
merger = PyPDF2.PdfFileMerger()
for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))
merger.write("合并.pdf")