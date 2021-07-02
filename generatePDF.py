import asyncio
import pandas as pd
from pyppeteer import launch
from plottingspiderchart import create_graph

subskill = ['Comprehension', 'Vocabulary', 'Logical Reasoning', 'Verbal Reasoning', 'Information Literacy',
            'Media Literacy', 'Current Affairs', 'Science', 'Sports & Society', 'SST', 'Artificial Intelligence',
            'Information Technology']


async def main():
    # df = pd.read_csv('Untitled spreadsheet - Sheet1.csv')
    # fig = px.line_polar(df, r='Score', theta='Subskill', line_close=True)
    # fig.update_traces(fill='toself')
    # fig.update_layout(width=700, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4))
    # fig.write_image("bubble_chart.png")
    # generate radar chart in advance. Same will be used by HTML file for rendering.
    await create_graph()

    # open the HTML page.
    browser = await launch()
    page = await browser.newPage()
    await page.goto('file:///Users/akash/Projects/python/IDAAutomatedReport/htmlfinal/index.html')
    await page.emulateMedia('screen')

    #  Set the data.
    name = "Akash"
    school_name = "Your School"
    grade = "7th"
    nat_rank = 503
    obtained_mark = 37
    avg_nat_marks = 22
    total_marks = 40
    your_score = f"{obtained_mark}/{total_marks}"
    avg_nat_score = f"{avg_nat_marks}/{total_marks}"
    your_score_desc = f"<strong>Your Score:</strong> Total number of correct answers/Total number of questions attempted. Example: Your Score = {obtained_mark}/{total_marks} denotes you answered {obtained_mark} out of {total_marks} questions correctly where {total_marks} is the maximum number of questions in the challenge."
    nat_score_desc = f"<strong>National Average Score:</strong> This is the Average number of correct answers for the respective grade category/Maximum number of questions. For Example: National Score = {avg_nat_marks}/{total_marks} denotes on an average students answered {avg_nat_marks} out of {total_marks} questions correctly."

    # set the data to PDF
    await page.evaluate(f" document.getElementById('name').innerHTML = `{name}`")
    await page.evaluate(f" document.getElementById('school_name').innerHTML = `{school_name}`")
    await page.evaluate(f" document.getElementById('grade').innerHTML = `{grade}`")
    await page.evaluate(f" document.getElementById('nat_rank').innerHTML = `{nat_rank}`")
    await page.evaluate(f" document.getElementById('score').innerHTML = `{your_score}`")
    await page.evaluate(f" document.getElementById('your_score').innerHTML = `{your_score}`")
    await page.evaluate(f" document.getElementById('nat_avg_score').innerHTML = `{avg_nat_score}`")
    await page.evaluate(f" document.getElementById('your_score_desc').innerHTML = `{your_score_desc}`")
    await page.evaluate(f" document.getElementById('nat_score_desc').innerHTML = `{nat_score_desc}`")

    # Plot the bar chart
    score_string = """() =>  {  var chart = new CanvasJS.Chart('chartContainer', { title:{text: 'Score Report'}, data: [{dataPoints: [{x: 1, y: %s, label: 'Your Score'},{ x: 2, y: %s,  label: 'National Average Score' }]}]});chart.render();}""" % (obtained_mark, avg_nat_marks)
    await page.evaluate(score_string)

    # plot the skill wise table
    skill_df = pd.read_csv("Performance across Skills & Sub-Skills - Sheet1.csv")
    skill_node = ""
    s_header_node = "<thead><tr><td>Skill</td><td>Description</td><td>Right Answer</td><td>Wrong Answer</td></tr></thead>"
    skill_node += s_header_node
    for row in range(0, (skill_df.shape[0])):
        skill_node += f"<tr><td>{skill_df.values[row][0]}</td><td>{skill_df.values[row][1]}</td><td>{skill_df.values[row][2]}</td><td>{skill_df.values[row][3]}</td></tr>"
    skill_string = f" document.getElementById('skill_wise').innerHTML = `{skill_node}`"
    await page.evaluate(skill_string)

    list_df = pd.read_csv("FEC Certificates - Sheet6.csv")
    child_node = ""
    index = 0
    q_header_node = "<table><thead><tr><td>S.No</td><td>Skill Name</td><td>Subskill Name</td><td>Question Asked</td><td>Your Answer</td><td>Correct Answer</td><td>Result</td></tr></thead>"
    q_header_node_with_margin = "<table style='margin-top: 50px !important;'><thead><tr><td>S.No</td><td>Skill Name</td><td>Subskill Name</td><td>Question Asked</td><td>Your Answer</td><td>Correct Answer</td><td>Result</td></tr></thead>"
    for row in range(0, (list_df.shape[0])):
        if index % 10 == 0:
            if index != 0:
                child_node += "</table><p style='page-break-after:always;'/>"
                child_node += q_header_node_with_margin
            else:
                child_node += q_header_node
        child_node += f"<tr><td>{list_df.values[row][0]}</td><td>{list_df.values[row][1]}</td><td>{list_df.values[row][2]}</td><td>{list_df.values[row][3]}</td><td>{list_df.values[row][4]}</td><td>{list_df.values[row][5]}</td><td>{list_df.values[row][6]}</td></tr>"
        index += 1
    child_node += "</table><p style='page-break-after:always;'/>"
    insert_string = f" document.getElementById('question_wise').innerHTML = `{child_node}`"
    await page.evaluate(insert_string)
    await page.pdf({'path': 'IDAReport.pdf', 'displayHeaderFooter': True,
                    'margin': {'top': '35', 'right': '10', 'bottom': '35', 'left': '10'},
                    '-webkit-print-color-adjust': True, 'printBackground': True})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
