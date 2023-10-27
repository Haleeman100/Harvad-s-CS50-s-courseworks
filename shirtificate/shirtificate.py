from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

# add page
pdf.add_page()
# add font 
pdf.set_font("helvetica", "B", 30)
# add CS50 Shirtificate on top of page
pdf.cell(0, 60, 'CS50 Shirtificate', align='C')
# add image
pdf.image("shirtificate.png", x = 0, y = 70)

