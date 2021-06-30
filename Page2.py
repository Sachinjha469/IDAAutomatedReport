import matplotlib.pyplot as plt

data = [23, 85]
labels = ['Your Score', 'National Average Score']
plt.xticks(range(len(data)), labels, fontweight='bold', fontsize=11.0)
plt.ylabel('Percentage Accuracy', fontweight='bold', fontsize=14.0)
# plt.title('I am title')
x_pos = (0, 1)
bar_list = plt.bar(range(len(data)), data, width=0.3, align='center')
bar_list[0].set_color('b')
bar_list[1].set_color('tab:orange')
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
# plt.show()


# **** table page2 *************

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas

# body text  style used for wrapping  data on flowables
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
# used alignment if required
styleN.alignment = TA_LEFT

# doc = SimpleDocTemplate("Templatetoadd (copy).pdf", pagesize=letter)
# elements=[]
packet = io.BytesIO()
mm = 8
pagesize = (150 * mm, 105 * mm)
c = canvas.Canvas(packet, pagesize=pagesize)
styleBH = styles["Normal"]
styleBH.alignment = TA_LEFT

hdescrpcion1 = Paragraph('''<b>Name</b>''', styleBH)
hdescrpcion = Paragraph('''<b>School</b>''', styleBH)
hdescrpcion2 = Paragraph('''<b>Grade</b>''', styleBH)
hdescrpcion3 = Paragraph('''<b>National Rank</b>''', styleBH)
hpartida = Paragraph('''<b>Score</b>''', styleBH)
hpartida1 = Paragraph('''<b>National Avg Score</b>''', styleBH)
# 1

name = Paragraph('Sachin Jha', styleN)
school = Paragraph('City Montessori School', styleN)
grade = Paragraph('5', styleN)
national = Paragraph('500', styleN)
score = Paragraph('32/40', styleN)
avgscore = Paragraph('24/40', styleN)

data = [[hdescrpcion1, name], [hdescrpcion, school], [hdescrpcion2, grade], [hdescrpcion3, national], [hpartida, score],
        [hpartida1, avgscore]]

from reportlab.lib.units import inch

table = Table(data, colWidths=[1.5 * inch, 1 * inch, 1.25 * inch, 1.25 * inch, 1 * inch])

table_style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ('BACKGROUND', (0, 0), (0, 5), colors.yellow),
    ('VALIGN', (0, 0), (5, 5), 'TOP'),
    ('TEXTCOLOR', (0, 0), (4, 4), colors.red)]
)

table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page124.pdf", pagesize=pagesize)
table.wrapOn(c, 75, 200)
table.drawOn(c, 250, 380)

# 
# c.showPage()
c.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.35)
page.mergePage(new_pdf.getPage(0))
# page.scaleBy(1.5)
output.addPage(page)
outputStream = open("page2revised.pdf", "wb")
output.write(outputStream)
outputStream.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
string = "Helping students identify their"
string1 = "capabilities and prepare them"
string2 = "for today’s competitive world."

can.drawString(25, 500, string)
can.drawString(25, 480, string1)
can.drawString(25, 460, string2)
can.setFont('Helvetica-Bold', 15)
can.drawString(25, 520, "Summary")
# #################################################3333
str1 = "Your Score: Total number of correct answers/Total number of questions attempted. Example: Your Score = 32/40 denotes you"
str2 = "answered 32 out of 40 questions correctly where 40 is the maximum number of questions in the challenge."
str3 = "National Average Score: This is the Average number of correct answers for the respective grade category/Maximum number of"
str4 = "questions. For Example: National Score = 24/40 denotes on an average students answered 24 out of 40 questions correctly."
can.setFont('Helvetica', 9)
can.drawString(25, 320, str1)
can.drawString(25, 305, str2)
can.drawString(25, 285, str3)
can.drawString(25, 270, str4)

##########################################################################################

can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("page2revised.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("page2-revised.pdf", "wb")
output.write(outputStream)
outputStream.close()

# ********************Histogram************
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from io import BytesIO
import os
from reportlab.lib.utils import ImageReader

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
imgPath = os.path.join(THIS_FOLDER, 'histogram.png')
print(imgPath)

# Using ReportLab to insert image into PDF
imgTemp = BytesIO()
imgDoc = canvas.Canvas(imgTemp)

# Draw image on Canvas and save PDF in buffer
# imgPath = "/home/sachin/Files/child-image.jpeg"
reader = ImageReader(imgPath)
imgDoc.drawImage(reader, 100, 40, 300, 180)  ## at (399,760) with size 160x160
imgDoc.save()
print(imgDoc)

# Use PyPDF to merge the image-PDF into the template

page = PdfFileReader("page2-revised.pdf", "rb").getPage(0)
overlay = PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0)
page.mergePage(overlay)

# Save the result
output = PdfFileWriter()
output.addPage(page)
# output.write('output_file.pdf')
pdfOutput = open('page2-revised1.pdf', 'wb')
output.write(pdfOutput)
pdfOutput.close()
