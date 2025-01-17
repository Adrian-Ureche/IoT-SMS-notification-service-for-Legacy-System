from fpdf import FPDF

class Pdf(FPDF):
    def header(self):
        # self.image("img.png", 10, 8, 25)
        self.set_font("helvetica", "B", 20)
        self.cell(80)
        self.cell(30, 10, "Widget Report", ln=1, align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 10)
        self.cell(0, 10, f'Page {self.page_no}', align = 'C')
