from fpdf import FPDF

title='20,000 Leagues Under the Sea'

class PDF(FPDF):
    def header(self):
            # the path, the x-coordinate, the y-coordinate, the width (height will be set automatically if i only give width)
            self.image('Masi Logo Colour.png', 10, 8, 25)
            title_w = self.get_string_width(title) + 6
            doc_w = self.w
            self.set_x((doc_w - title_w) / 2)


            self.set_font('helvetica', 'B', 15)
            # title
            self.cell(30, 10, 'Title', ln=1, align="C")
            self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}', align='C')

pdf = PDF(orientation="P", unit="mm", format="A4")

pdf.alias_nb_pages()

pdf.add_page()

# there's a good default here, but if you want to set the bottom margin, you can alter it here
pdf.set_auto_page_break(auto=True, margin=20)
# specify font
# the blank sets the default bond to 'regular'
pdf.set_font('helvetica', '', 16)
# w = width, using ln=True tells the cursor to move to the next line
for i in range(1, 41):
    # width of 0 equals the entire line of the PDF
    pdf.cell(0, 10, f'This is line{i} :D', ln=True)
    # pdf.cell(80, 10, 'Hello World!')

pdf.output('pdf_2.pdf')
