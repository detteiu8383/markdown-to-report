import sys
import PyPDF2
import os

if os.path.exists("./cover.pdf"):
    args = sys.argv
    merger = PyPDF2.PdfFileMerger()

    for path in args[1:-1]:
        merger.append(path)

    merger.write(args[-1])
    merger.close()
else:
    os.rename("./template.pdf", "./output.pdf")
