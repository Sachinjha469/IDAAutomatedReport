import plotly.graph_objects as go
import csv
import numpy as np

subskill = ['Comprehension', 'Vocabulary', 'Logical Reasoning', 'Verbal Reasoning', 'Information Literacy',
            'Media Literacy', 'Current Affairs', 'Science', 'Sports & Society', 'SST', 'Artificial Intelligence',
            'Information Technology']


async def create_graph(x):
    comm = []
    ct = [0, 0]
    dl = [0, 0, 0, 0]
    gk = [0, 0, 0, 0, 0, 0]
    ta = [0, 0, 0, 0, 0, 0, 0, 0]
    length = len(subskill)
    print(length)
    count = 0
    with open('Para Article Data - Page 3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            count = count + 1
            if count > 1:
                if row[3] == x:  
                    if row[0] == 'Communication':
                        comm.append(row[2])
                    elif row[0] == 'Critical Thinking':
                        ct.append(row[2])
                    elif row[0] == 'Digital Literacy':
                        dl.append(row[2])
                    elif row[0] == 'General Knowledge':
                        gk.append(row[2])
                    elif row[0] == 'Technology Aptitude':
                        ta.append(row[2])

        print(comm)
        len_comm = len(comm)
        comm = np.array(comm)
        comm.resize(12)
        comm[len_comm:] = 0
        print(comm)
        len_ct = len(ct)
        ct = np.array(ct)
        ct.resize(12)
        ct[len_ct:] = 0
        print(ct)
        len_dl = len(dl)
        dl = np.array(dl)
        dl.resize(12)
        dl[len_dl:] = 0
        print(dl)
        len_gk = len(gk)
        gk = np.array(gk)
        gk.resize(12)
        gk[len_gk:] = 0
        print(gk)
        len_ta = len(ta)
        ta = np.array(ta)
        ta.resize(12)
        ta[len_ta:] = 0
        print(ta)

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=ct, theta=subskill, fill='toself', name='Critical Thinking'))
    fig.add_trace(go.Scatterpolar(r=comm, theta=subskill, fill='toself', name='Communication'))
    fig.add_trace(go.Scatterpolar(r=dl, theta=subskill, fill='toself', name='Digital Literacy'))
    fig.add_trace(go.Scatterpolar(r=gk, theta=subskill, fill='toself', name='General Knowledge'))
    fig.add_trace(go.Scatterpolar(r=ta, theta=subskill, fill='toself', name='Technical Aptitude'))
    fig.update_layout(width=500, height=500, margin=dict(l=70, r=70, b=100, t=100, pad=4),
                      polar=dict(radialaxis=dict(visible=True, range=[0, 6])), showlegend=False)
    fig.write_image("radar_chart.png", scale=1.0)
