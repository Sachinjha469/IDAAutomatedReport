import asyncio
import pandas as pd
from pyppeteer import launch
from plottingspiderchart import create_graph

subskill = ['Comprehension', 'Vocabulary', 'Logical Reasoning', 'Verbal Reasoning', 'Information Literacy',
            'Media Literacy', 'Current Affairs', 'Science', 'Sports & Society', 'SST', 'Artificial Intelligence',
            'Information Technology']


async def main():
    school_df = pd.read_csv("Schoolwise report.csv")
    school_list = school_df.groupby(school_df.columns.values[0])
    for school in school_list:  # .count()
        student_df = pd.read_csv("Schoolwise report.csv")
        student_list = student_df.loc[student_df['school name'] == school[0]]
        print(student_list.shape[0])

        await create_graph()
        # open the HTML page.
        browser = await launch()
        page = await browser.newPage()
        await page.goto('file:///Users/akash/Projects/python/IDAAutomatedReport/htmlfinal/index.html')
        await page.emulateMedia('screen')
        # set the data to PDF
        await page.evaluate(f" document.getElementById('school_name_c').innerHTML = `{school[0]}`")
        await page.evaluate(f" document.getElementById('school_name').innerHTML = `{school[0]}`")
        await page.evaluate(f" document.getElementById('ptc_count').innerHTML = ` Number of Participants: {student_list.shape[0]}`")

        # plot the table
        child_node = ""
        index = 0
        q_header_node = "<table><thead><tr><td>S.No</td><td>Name</td><td>Grade</td><td>Communication</td><td>Critical Thinking</td><td>Digital Literacy</td><td>General Knowledge</td><td>Technology Aptitude</td></tr></thead>"
        q_header_node_with_margin = "<table style='margin-top: 50px !important;'><thead><tr><td>S.No</td><td>Name</td><td>Grade</td><td>Communication</td><td>Critical Thinking</td><td>Digital Literacy</td><td>General Knowledge</td><td>Technology Aptitude</td></tr></thead>"
        for row in range(0, (student_list.shape[0])):
            if index % 10 == 0:
                if index != 0:
                    child_node += "</table><p style='page-break-after:always;'/>"
                    child_node += q_header_node_with_margin
                else:
                    child_node += q_header_node
            child_node += f"<tr><td>{row + 1}</td><td>{student_list.values[row][1]}</td><td>{student_list.values[row][2]}</td><td>{student_list.values[row][3]}</td><td>{student_list.values[row][4]}</td><td>{student_list.values[row][5]}</td><td>{student_list.values[row][6]}</td><td>{student_list.values[row][7]}</td></tr>"
            index += 1
        child_node += "</table><p style='page-break-after:always;'/>"
        insert_string = f" document.getElementById('school_wise').innerHTML = `{child_node}`"
        await page.evaluate(insert_string)
        await page.pdf({'path': "{}.pdf".format(school[0]), 'displayHeaderFooter': False,
                        'margin': {'top': '35', 'right': '10', 'bottom': '35', 'left': '10'},
                        '-webkit-print-color-adjust': True, 'printBackground': True})
        await browser.close()
        break


asyncio.get_event_loop().run_until_complete(main())


# school_df = pd.read_csv("Schoolwise report.csv")
# school_list = school_df.groupby(school_df.columns.values[0])
#
# for school in school_list:  # .count()
#     student_df = pd.read_csv("Schoolwise report.csv")
#     school_name = student_df['school name'][0]
#     # test = student_df.loc["school_name" != ""]
#     test = student_df.loc[student_df['school name'] == school[0]]
#     print(student_df['school name'] == school[0])
#     # print(student_df['school name'][0])
