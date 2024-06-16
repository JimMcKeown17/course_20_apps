from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="mm", format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    topic = row["Topic"]
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
    pdf.line(x1=5,y1=24,x2=200,y2=24)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

pdf.output("output.pdf")