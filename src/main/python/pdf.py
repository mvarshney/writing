from PyPDF2 import PdfFileWriter, PdfFileReader

# open the input pdf
inp = PdfFileReader(open("/Users/mvarshne/Downloads/test.pdf", "rb"))

# these are the number of pages in doc
docpages = inp.getNumPages()
print "Doc has pages: ", docpages

# these must be the pages in the book (multiple for 4)
bookpages = docpages
if docpages % 4 != 0:
    bookpages = 4 * ((docpages // 4) + 1)

print "Book will have pages: ", bookpages

# this is the array of page index
pages = [i for i in xrange(0, bookpages)]

# our imposition algorithm
imposed_pages = []
while len(pages) > 0:
    imposed_pages.append(pages[-1])
    imposed_pages.append(pages[0])
    imposed_pages.append(pages[1])
    imposed_pages.append(pages[-2])
    pages = pages[2:-2]

print "Imposition: ", imposed_pages


output = PdfFileWriter()
if docpages != bookpages:
    temp = PdfFileWriter()
    temp.addPage(inp.getPage(0))
    temp.addBlankPage()
    blank = temp.getPage(1)

for i in imposed_pages:
    if i >= docpages:
        output.addPage(blank)
    else:
        output.addPage(inp.getPage(i))

outputStream = file("/Users/mvarshne/Downloads/output.pdf", "wb")
output.write(outputStream)