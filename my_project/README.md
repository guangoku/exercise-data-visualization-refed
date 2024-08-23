### Steps:

1. Download Airtable "Federal Grants Database" from https://refed.org/food-waste/resources-and-guides/
2. `my_project/extract_data_from_pdf.py`
   - read pdf, convert to tabular data, and write to output.csv
3. `my_project/gen_charts.py` creates multiple data visualizations

Limit: the pdf extraction did not read grant amount correctly

### Visualizations

Pie chart of eligibility types using Altair

![Pie Chart of Eligibility Types](/my_project/charts/Pie%20Chart%20of%20Eligibility%20Types.png)

Heatmap of Application Due Dates
![Heatmap of Application Due text](/my_project/charts/Heatmap%20of%20Application%20Due%20Dates.png)

Number of Grants by Relevant Solution Type
![Relevant Solution Type](/my_project/charts/relevant%20solution%20type%20.png)

Gantt chart of grant timelines
![Alt text](/my_project/charts/Gantt%20chart%20of%20grant%20timelines.png)
