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
pdf.set_font_size(32)
pdf.set_text_color(255,255,255)
pdf.text(x=50, y=150, txt =f"{name} took CS50")
pdf.output("shirtificate.pdf")
