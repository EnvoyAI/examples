import glob, os
from fpdf import FPDF

class CustomPDF(FPDF):
 
    def header(self): 
        # Add a title
        self.set_font('Arial', 'B', 15)
        self.cell(60)
        self.cell(0, 5, 'EnvoyAI Sample PDF Report', ln=1)
 
        # Line break
        self.ln(20)
 
    def footer(self):
        self.set_y(-10)
 
        self.set_font('Arial', 'I', 8)
 
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

files = [f for f in glob.glob("/envoyai/input/dicom-series-in/*", recursive=False)]

pdf = CustomPDF()
pdf.alias_nb_pages()
pdf.add_page()

spacing = 1.5

pdf.set_font('Arial', 'B', 12)
col_width = pdf.w
row_height = pdf.font_size

pdf.cell(col_width, row_height*spacing, 'Content of \"/envoyai/input/dicom-series-in/\":')
pdf.ln(row_height*spacing)

pdf.set_font('Arial', '', 10)
col_width = pdf.w
row_height = pdf.font_size

for file in files:
    pdf.cell(col_width, row_height*spacing, os.path.basename(file))
    pdf.ln(row_height*spacing)

pdf.output('/envoyai/output/out.pdf', 'F')

exit(0)
