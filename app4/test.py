import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("texts/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem.capitalize()
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)
    with open(filepath) as file:
        text = file.readlines()
        for line in text:
            pdf.set_font(family="Times", size=10)
            pdf.multi_cell(w=0,h=10, txt=line)

pdf.output("Animals.pdf")