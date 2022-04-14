import os
from fpdf import FPDF
from matplotlib.pyplot import text

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('Arial', 'B', 20)

pdf.cell(w=0, h=0, txt='Valores gastos pelo governo durante a pandema em 2021\n\n', align='C')

pdf.image(name="desafio_38/Figure_1.png", x=10, y=50, w=180)

pdf.output("Valores despendidos durante a pandeima 2021.pdf")

os.system('pause')