import asyncio
from pyppeteer import launch
import pandas as pd
import plotly.express as px

data = {"name": "sachin", "school": "School Name", "Grade": "Grade", "n_rank": 500, "score": 32, "total": 50}


async def main():
    df = pd.read_csv('Untitled spreadsheet - Sheet1.csv')
    print(df.head(10))
    fig = px.line_polar(df, r='Score', theta='Subskill', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(width=700, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4))
    fig.write_image("bubble_chart.png")

    browser = await launch()
    page = await browser.newPage()
    await page.goto('file:///Users/akash/Projects/python/IDAAutomatedReport/htmlfinal/index.html')
    await page.emulateMedia('screen')

    #  Set the name.
    name = "Akash"
    await page.evaluate(f" document.getElementById('name').innerHTML = `{name}`")

    # Plot the bar chart
    await page.evaluate("() =>  {  var chart = new CanvasJS.Chart('chartContainer', { title:{text: ''}, data: [{dataPoints: [{x: 1, y: 90, label: 'Your Score'},{ x: 2, y: 60,  label: 'National Average Score' }]}]});chart.render();}")
    list_df = pd.read_csv("FEC Certificates - Sheet6.csv")
    child_node = ""
    index = 0
    header_node = "<table><thead><tr><td>S.No</td><td>Skill Name</td><td>Subskill Name</td><td>Question Asked</td><td>Your Answer</td><td>Correct Answer</td><td>Result</td></tr></thead>"
    header_node_with_margin = "<table style='margin-top: 50px !important;'><thead><tr><td>S.No</td><td>Skill Name</td><td>Subskill Name</td><td>Question Asked</td><td>Your Answer</td><td>Correct Answer</td><td>Result</td></tr></thead>"
    for row in range(0, (list_df.shape[0] - 10)):
        if index % 10 == 0:
            if index != 0:
                child_node += "</table><p style='page-break-after:always;'/>"
                child_node += header_node_with_margin
            else:
                child_node += header_node
        child_node += f"<tr><td>{list_df.values[row][0]}</td><td>{list_df.values[row][1]}</td><td>{list_df.values[row][2]}</td><td>{list_df.values[row][3]}</td><td>{list_df.values[row][4]}</td><td>{list_df.values[row][5]}</td><td>{list_df.values[row][6]}</td></tr>"
        index += 1
    child_node += "</table><p style='page-break-after:always;'/>"
    insert_string = f" document.getElementById('question_wise').innerHTML = `{child_node}`"
    await page.evaluate(insert_string)
    await page.pdf({'path': 'Olympiad Result.pdf', 'displayHeaderFooter': True,
                    'margin': {'top': '35', 'right': '10', 'bottom': '35', 'left': '10'},
                    '-webkit-print-color-adjust': True, 'printBackground': True})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
