from fpdf import FPDF
pdf=FPDF()

# Add a Page

pdf.add_page()
pdf.set_font("Arial",size=25)
pdf.cell(200,10,txt="Hello this is ak",ln=1,align="C")
pdf.output("/home/arun/Documents/AKpdf.pdf")
