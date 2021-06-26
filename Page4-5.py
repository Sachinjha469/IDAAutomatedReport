from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle,SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.colors import red

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# bodytext  style used for wrapping  data on flowables 
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

# doc = SimpleDocTemplate("Templatetoadd (copy).pdf", pagesize=letter)
# elements=[]
packet = io.BytesIO()
mm=8
pagesize = (150*mm, 105*mm)
c= canvas.Canvas(packet, pagesize=pagesize)
styleBH = styles["Normal"]
styleBH.alignment = TA_LEFT

hdescrpcion1 = Paragraph('''<b>S.N.</b>''', styleBH)
hdescrpcion = Paragraph('''<b>Skill</b>''', styleBH)
hdescrpcion2 = Paragraph('''<b>SubSkill</b>''', styleBH)
hdescrpcion3 = Paragraph('''<b>Question Asked</b>''', styleBH)
hpartida = Paragraph('''<b>Your Answer</b>''', styleBH)
hpartida1 = Paragraph('''<b>Correct Answer</b>''', styleBH)
hpartida2 = Paragraph('''<b>Result</b>''', styleBH)

data=[]
values = [hdescrpcion1,hdescrpcion, hdescrpcion2, hdescrpcion3,hpartida,hpartida1,hpartida2]
data.append(values)
import csv
count=0
with open('FEC Certificates - Sheet6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for r in csv_reader:
        print(r)
        print(r[0])
        count=count+1
        if(count>1 and count<=9):
            num1=r[0]
            descrpcion = Paragraph(r[1], styleN)
            partida = Paragraph(r[2], styleN)
            p1=Paragraph(r[3],styleN)
            p2=Paragraph(r[4],styleN)
            st1=Paragraph(r[5],styleN)
            st2=Paragraph(r[6],styleN)
            data.append([num1,descrpcion,partida,p1,p2,st1,st2])

table = Table(data)

table_style=TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND', (0, 0), (6, 0), '#FFC200'),
                       ('VALIGN',(0,0),(6,6),'TOP')
                       ])


table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page124.pdf", pagesize=pagesize)
table.wrapOn(c, 50, 50)
table.drawOn(c, 35,85)

# 
# c.showPage()
c.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.5)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("Trying1.pdf", "wb")
output.write(outputStream)
outputStream.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can= canvas.Canvas(packet, pagesize=letter)
string="Question-wise Report"
# string1="Skills and Subskills"

can.setFont('Helvetica-Bold', 15)
can.drawString(40, 580, string)
# can.drawString(235, 650, string1
# c.save()
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Trying1.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("Trying.pdf", "wb")
output.write(outputStream)
outputStream.close()

###############Skill2 ---###############
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle,SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.colors import red

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# bodytext  style used for wrapping  data on flowables 
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

# doc = SimpleDocTemplate("Templatetoadd (copy).pdf", pagesize=letter)
# elements=[]
packet = io.BytesIO()
mm=8
pagesize = (150*mm, 105*mm)
c= canvas.Canvas(packet, pagesize=pagesize)
styleBH = styles["Normal"]
styleBH.alignment = TA_LEFT

hdescrpcion1 = Paragraph('''<b>S.N.</b>''', styleBH)
hdescrpcion = Paragraph('''<b>Skill</b>''', styleBH)
hdescrpcion2 = Paragraph('''<b>SubSkill</b>''', styleBH)
hdescrpcion3 = Paragraph('''<b>Question Asked</b>''', styleBH)
hpartida = Paragraph('''<b>Your Answer</b>''', styleBH)
hpartida1 = Paragraph('''<b>Correct Answer</b>''', styleBH)
hpartida2 = Paragraph('''<b>Result</b>''', styleBH)

data=[]
values = [hdescrpcion1,hdescrpcion, hdescrpcion2, hdescrpcion3,hpartida,hpartida1,hpartida2]
data.append(values)
import csv
count=0
with open('FEC Certificates - Sheet6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for r in csv_reader:
        print(r)
        print(r[0])
        count=count+1
        if(count>9 and count<=17):
            num1=r[0]
            descrpcion = Paragraph(r[1], styleN)
            partida = Paragraph(r[2], styleN)
            p1=Paragraph(r[3],styleN)
            p2=Paragraph(r[4],styleN)
            st1=Paragraph(r[5],styleN)
            st2=Paragraph(r[6],styleN)
            data.append([num1,descrpcion,partida,p1,p2,st1,st2])

table = Table(data)

table_style=TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND', (0, 0), (6, 0), '#FFC200'),
                       ('VALIGN',(0,0),(6,6),'TOP')
                       ])


table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page124.pdf", pagesize=pagesize)
table.wrapOn(c, 50, 50)
table.drawOn(c, 35,120)

# 
# c.showPage()
c.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.5)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("Trying1.pdf", "wb")
output.write(outputStream)
outputStream.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can= canvas.Canvas(packet, pagesize=letter)
string="Question-wise Report"
# string1="Skills and Subskills"

can.setFont('Helvetica-Bold', 15)
can.drawString(40, 580, string)
# can.drawString(235, 650, string1
# c.save()
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Trying1.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("Trying-skill2.pdf", "wb")
output.write(outputStream)
outputStream.close()

###############Skill3---------
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

# doc = SimpleDocTemplate("Templatetoadd (copy).pdf", pagesize=letter)
# elements=[]
packet = io.BytesIO()
mm=8
pagesize = (150*mm, 105*mm)
c= canvas.Canvas(packet, pagesize=pagesize)
styleBH = styles["Normal"]
styleBH.alignment = TA_LEFT

hdescrpcion1 = Paragraph('''<b>S.N.</b>''', styleBH)
hdescrpcion = Paragraph('''<b>Skill</b>''', styleBH)
hdescrpcion2 = Paragraph('''<b>SubSkill</b>''', styleBH)
hdescrpcion3 = Paragraph('''<b>Question Asked</b>''', styleBH)
hpartida = Paragraph('''<b>Your Answer</b>''', styleBH)
hpartida1 = Paragraph('''<b>Correct Answer</b>''', styleBH)
hpartida2 = Paragraph('''<b>Result</b>''', styleBH)

data=[]
values = [hdescrpcion1,hdescrpcion, hdescrpcion2, hdescrpcion3,hpartida,hpartida1,hpartida2]
data.append(values)
import csv
count=0
with open('FEC Certificates - Sheet6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for r in csv_reader:
        print(r)
        print(r[0])
        count=count+1
        if(count>17 and count<=25):
            num1=r[0]
            descrpcion = Paragraph(r[1], styleN)
            partida = Paragraph(r[2], styleN)
            p1=Paragraph(r[3],styleN)
            p2=Paragraph(r[4],styleN)
            st1=Paragraph(r[5],styleN)
            st2=Paragraph(r[6],styleN)
            data.append([num1,descrpcion,partida,p1,p2,st1,st2])

table = Table(data)

table_style=TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND', (0, 0), (6, 0), '#FFC200'),
                       ('VALIGN',(0,0),(6,6),'TOP')
                       ])


table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page124.pdf", pagesize=pagesize)
table.wrapOn(c, 50, 50)
table.drawOn(c, 35,240)

# 
# c.showPage()
c.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.5)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("Trying1.pdf", "wb")
output.write(outputStream)
outputStream.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can= canvas.Canvas(packet, pagesize=letter)
string="Question-wise Report"
# string1="Skills and Subskills"

can.setFont('Helvetica-Bold', 15)
can.drawString(40, 580, string)
# can.drawString(235, 650, string1
# c.save()
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Trying1.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("Trying-skill3.pdf", "wb")
output.write(outputStream)
outputStream.close()
###########skill4----------
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

# doc = SimpleDocTemplate("Templatetoadd (copy).pdf", pagesize=letter)
# elements=[]
packet = io.BytesIO()
mm=8
pagesize = (150*mm, 105*mm)
c= canvas.Canvas(packet, pagesize=pagesize)
styleBH = styles["Normal"]
styleBH.alignment = TA_LEFT

hdescrpcion1 = Paragraph('''<b>S.N.</b>''', styleBH)
hdescrpcion = Paragraph('''<b>Skill</b>''', styleBH)
hdescrpcion2 = Paragraph('''<b>SubSkill</b>''', styleBH)
hdescrpcion3 = Paragraph('''<b>Question Asked</b>''', styleBH)
hpartida = Paragraph('''<b>Your Answer</b>''', styleBH)
hpartida1 = Paragraph('''<b>Correct Answer</b>''', styleBH)
hpartida2 = Paragraph('''<b>Result</b>''', styleBH)

data=[]
values = [hdescrpcion1,hdescrpcion, hdescrpcion2, hdescrpcion3,hpartida,hpartida1,hpartida2]
data.append(values)
import csv
count=0
with open('FEC Certificates - Sheet6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for r in csv_reader:
        print(r)
        print(r[0])
        count=count+1
        if(count>25 and count<=33):
            num1=r[0]
            descrpcion = Paragraph(r[1], styleN)
            partida = Paragraph(r[2], styleN)
            p1=Paragraph(r[3],styleN)
            p2=Paragraph(r[4],styleN)
            st1=Paragraph(r[5],styleN)
            st2=Paragraph(r[6],styleN)
            data.append([num1,descrpcion,partida,p1,p2,st1,st2])

table = Table(data)

table_style=TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND', (0, 0), (6, 0), '#FFC200'),
                       ('VALIGN',(0,0),(6,6),'TOP')
                       ])


table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page124.pdf", pagesize=pagesize)
table.wrapOn(c, 50, 50)
table.drawOn(c, 35,90)

# 
# c.showPage()
c.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.5)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("Trying1.pdf", "wb")
output.write(outputStream)
outputStream.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can= canvas.Canvas(packet, pagesize=letter)
string="Question-wise Report"
# string1="Skills and Subskills"

can.setFont('Helvetica-Bold', 15)
can.drawString(40, 580, string)
# can.drawString(235, 650, string1
# c.save()
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Trying1.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("Trying-skill4.pdf", "wb")
output.write(outputStream)
outputStream.close()
###################Skill5---------------
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

# doc = SimpleDocTemplate("Templatetoadd (copy).pdf", pagesize=letter)
# elements=[]
packet = io.BytesIO()
mm=8
pagesize = (150*mm, 105*mm)
c= canvas.Canvas(packet, pagesize=pagesize)
styleBH = styles["Normal"]
styleBH.alignment = TA_LEFT

hdescrpcion1 = Paragraph('''<b>S.N.</b>''', styleBH)
hdescrpcion = Paragraph('''<b>Skill</b>''', styleBH)
hdescrpcion2 = Paragraph('''<b>SubSkill</b>''', styleBH)
hdescrpcion3 = Paragraph('''<b>Question Asked</b>''', styleBH)
hpartida = Paragraph('''<b>Your Answer</b>''', styleBH)
hpartida1 = Paragraph('''<b>Correct Answer</b>''', styleBH)
hpartida2 = Paragraph('''<b>Result</b>''', styleBH)

data=[]
values = [hdescrpcion1,hdescrpcion, hdescrpcion2, hdescrpcion3,hpartida,hpartida1,hpartida2]
data.append(values)
import csv
count=0
with open('FEC Certificates - Sheet6.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for r in csv_reader:
        print(r)
        print(r[0])
        count=count+1
        if(count>33):
            num1=r[0]
            descrpcion = Paragraph(r[1], styleN)
            partida = Paragraph(r[2], styleN)
            p1=Paragraph(r[3],styleN)
            p2=Paragraph(r[4],styleN)
            st1=Paragraph(r[5],styleN)
            st2=Paragraph(r[6],styleN)
            data.append([num1,descrpcion,partida,p1,p2,st1,st2])

table = Table(data)

table_style=TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND', (0, 0), (6, 0), '#FFC200'),
                       ('VALIGN',(0,0),(6,6),'TOP'),
                       ('ALIGN',(0,0),(6,6),'CENTER')
                       ])


table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page124.pdf", pagesize=pagesize)
table.wrapOn(c, 50, 50)
table.drawOn(c, 35,160)

# 
# c.showPage()
c.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.5)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = open("Trying1.pdf", "wb")
output.write(outputStream)
outputStream.close()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can= canvas.Canvas(packet, pagesize=letter)
string="Question-wise Report"
# string1="Skills and Subskills"

can.setFont('Helvetica-Bold', 15)
can.drawString(40, 580, string)
# can.drawString(235, 650, string1
# c.save()
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Trying1.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("Trying-skill5.pdf", "wb")
output.write(outputStream)
outputStream.close()

#***********page3---------------------------------------


packet = io.BytesIO()
mm=12
pagesize = (150*mm, 105*mm)
c= canvas.Canvas(packet, pagesize=pagesize)

# bodytext  style used for wrapping  data on flowables 
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER


hdescrpcion = Paragraph('''<b>Skill</b>''', styleBH)
hpartida = Paragraph('''<b>Description</b>''', styleBH)
hpartida1 = Paragraph('''<b>Right Answer</b>''', styleBH)
hpartida2 = Paragraph('''<b>Wrong Answer</b>''', styleBH)



descrpcion = Paragraph('Knowledge about many different things, as opposed to detailed knowledge about one particular subject  ', styleN)
partida = Paragraph('General Knowledge', styleN)
p1=Paragraph('25,26,27,28,29,30,31,32',styleN)
p2=Paragraph('-',styleN)

str1=Paragraph('Technology Aptitude',styleN)
str2=Paragraph('Ability to possess a high intellect in electronics and technology',styleN)
p3=Paragraph('33,34,35,36,37,38,39,40',styleN)
p4=Paragraph('-',styleN)

str3=Paragraph("Critical Thinking",styleN)
str4=Paragraph("Ability to analyse facts to form a judgment",styleN)
p5=Paragraph("1,3,4,5,6,7,8",styleN)
p6=Paragraph("2,5",styleN)

str5=Paragraph("Digital Literacy",styleN)
str6=Paragraph("Ability to find, evaluate, and clearly communicate",styleN)
p7=Paragraph("9,11,14,15,16",styleN)
p8=Paragraph("10,12,13",styleN)


str7=Paragraph("Communication",styleN)
str8=Paragraph("Ability you use when giving and receiving different kinds of information",styleN)
p9=Paragraph("17,18,23,24",styleN)
p10=Paragraph("19,20,21",styleN)

data= [[hdescrpcion, hpartida,hpartida1,hpartida2],
        [str3,str4,p5,p6],
        [str5,str6,p7,p8],
        [str7,str8,p9,p10],
       [partida ,descrpcion,p1,p2],
       [str1,str2,p3,p4]]



table = Table(data,colWidths=[85,85])

table_style=TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND', (0, 0), (3, 0), '#FFC200'),
                       ('VALIGN',(0,0),(5,5),'TOP'),
                       ('VALIGN',(2,0),(5,5),'CENTER')
                       ])

table.setStyle(table_style)
# mm=7
# pagesize = (150*mm, 105*mm)
# c = canvas.Canvas("Page3.pdf", pagesize=pagesize)
table.wrapOn(c, 50, 50)
table.drawOn(c, 40,190)
c.save() 
c.showPage()
packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("Templatetoadd.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.scaleBy(1.5)
page.mergePage(new_pdf.getPage(0))
# page.scaleTo(800,800)
output.addPage(page)
outputStream = open("newpdf1.pdf", "wb")
output.write(outputStream)
outputStream.close()


packet = io.BytesIO()
# create a new PDF with Reportlab
can= canvas.Canvas(packet, pagesize=letter)
string="Performance across different Skills and Subskills"
# string1=""

can.setFont('Helvetica-Bold', 13)
can.drawString(40, 580, string)
# can.drawString(235, 650, string1)

can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("newpdf1.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)

page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("newpdf-page3.pdf", "wb")
output.write(outputStream)
outputStream.close()







