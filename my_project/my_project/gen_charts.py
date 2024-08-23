import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('output.csv')
import altair as alt
import pandas as pd
from vega_datasets import data


# Pie chart of eligibility types using Altair
eligibility_counts = df['Eligibility'].str.split('\n', expand=True).stack().value_counts().reset_index()
eligibility_counts.columns = ['Eligibility Type', 'Count']
chart2 = alt.Chart(eligibility_counts).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field='Count', type='quantitative'),
    color=alt.Color(field='Eligibility Type', type='nominal', scale=alt.Scale(scheme='tableau20')),
    tooltip=[alt.Tooltip('Eligibility Type:N', title='Eligibility Type'), alt.Tooltip('Count:Q', title='Count')]
).properties(
    title='Distribution of Eligibility Types for Grants',
    width=400,
    height=400
).configure_title(
    fontSize=16,
    anchor='start'
)

chart2.show()

# alendar Heatmap of Application Due Dates
df.rename(columns={'Application Deadline': 'Application Due Date'}, inplace=True)
df['Application Due Date'] = pd.to_datetime(df['Application Due Date'], errors='coerce')

df['Year'] = df['Application Due Date'].dt.year
df['Month'] = df['Application Due Date'].dt.month
df['Day'] = df['Application Due Date'].dt.day

df = df.dropna(subset=['Application Due Date'])

heatmap_data = df.groupby(['Month', 'Day']).size().reset_index(name='Count')

heatmap = alt.Chart(heatmap_data).mark_rect().encode(
    x=alt.X('Day:O', title='Day of the Month'),
    y=alt.Y('Month:O', title='Month'),
    color=alt.Color('Count:Q', scale=alt.Scale(scheme='greens'), title='Number of Due Dates'),
    tooltip=[
        alt.Tooltip('Month:O', title='Month'),
        alt.Tooltip('Day:O', title='Day of the Month'),
        alt.Tooltip('Count:Q', title='Number of Due Dates')
    ]
).properties(
    title='Calendar Heatmap of Application Due Dates',
    width=600,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16,
    anchor='start'
)

heatmap.show()


# Number of Grants by Relevant Solution Type
solution_type_counts = df['Relevant Solution Type'].str.split('\n', expand=True).stack().value_counts().reset_index()
solution_type_counts.columns = ['Relevant Solution Type', 'Count']

chart = alt.Chart(solution_type_counts).mark_bar().encode(
    x='Relevant Solution Type:N',
    y='Count:Q',
    tooltip=['Relevant Solution Type:N', 'Count:Q']
).properties(
    title='Number of Grants by Relevant Solution Type',
    width=800,
    height=400
)

chart.show()

# Gantt chart of grant timelines

df['Application Due Date'] = pd.to_datetime(df['Application Due Date'], errors='coerce')

if 'Start Date' not in df.columns:
    df['Start Date'] = pd.to_datetime('2024-01-01')  # Example: a default start date for all grants
df = df.dropna(subset=['Application Due Date'])

df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')

gantt_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Start Date:T', title='Start Date'),
    x2='Application Due Date:T',
    y=alt.Y('Grant Name:N', title='Grant Name', sort='-x'),  # Replace with the actual column name for grant names
    color=alt.Color('Agency:N', legend=alt.Legend(title="Agency")),  # Use 'Agency' for color coding
    tooltip=[
        alt.Tooltip('Grant Name:N', title='Grant Name'),
        alt.Tooltip('Start Date:T', title='Start Date'),
        alt.Tooltip('Application Due Date:T', title='Due Date'),
        alt.Tooltip('Agency:N', title='Agency')
    ]
).properties(
    title='Gantt Chart of Grant Timelines',
    width=800,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16,
    anchor='start'
)

gantt_chart.show()
