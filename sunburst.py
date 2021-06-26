import plotly.express as px
import pandas as pd
df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
print(df.head(10))
fig = px.line_polar(df, r='Score', theta='Subskill', line_close=True)
fig.update_traces(fill='toself')
fig.update_layout(
    width=500,
    height=500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ))
fig.show()
fig.write_image("fig2.png")

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from io import BytesIO
import os
from reportlab.lib.utils import ImageReader

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
imgPath1 = os.path.join(THIS_FOLDER, 'fig2.png')
print(imgPath1)

# Using ReportLab to insert image into PDF
imgTemp1 = BytesIO()
imgDoc1 = canvas.Canvas(imgTemp1)


###for bottom table
reader = ImageReader(imgPath1)
imgDoc1.drawImage(reader, 360, 770, 430, 430)    ## at (399,760) with size 160x160
imgDoc1.save()
print(imgDoc1)

# Use PyPDF to merge the image-PDF into the template

page = PdfFileReader("page3.pdf","rb").getPage(0)
# page.scaleBy(1.45)
overlay = PdfFileReader(BytesIO(imgTemp1.getvalue())).getPage(0)
page.mergePage(overlay)

#Save the result
output = PdfFileWriter()
output.addPage(page)
# output.write('output_file.pdf')
pdfOutput = open('output_page1103.pdf', 'wb')
output.write(pdfOutput)
pdfOutput.close()

