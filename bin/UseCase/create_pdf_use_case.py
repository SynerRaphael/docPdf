from fpdf import FPDF
import json

class CreatePdfUseCase:
    
    def __init__(self, order):
        self.order = order
        self.currency = order["currency"]
        self.pdf = FPDF('P', 'mm', 'Letter')


    def create_pdf_fpdf(self):
        self.pdf.add_page()
        self.pdf.set_font('arial', '', 16)

        # self.pdf.set_fill_color(200,100,58)
        self.add_line("company", self.get_data("company"))
        self.add_line("customer", self.get_data("customer"))
        self.add_line("billing address", self.get_data("billing_address"))
        self.add_line("delivery address", self.get_data("delivery_address"))
        self.add_line("desired delivery", self.get_data("desired_delivery"))
        self.add_line("agreed delivery", self.get_data("agreed_delivery"))
        
        for offer_line in self.order["offer_lines"]:
            self.add_line_empty()
            self.add_line("quantity", self.get_sub_data(offer_line, "quantity"))
            self.add_line("product", self.get_sub_data(offer_line, "product"))
            self.add_line("unit price", self.get_sub_data(offer_line, "unit_price"),self.currency)
            self.add_line("orderline price", self.get_sub_data(offer_line, "orderline_price"),self.currency)
        
        self.add_line_empty()
        self.add_line("total", self.get_data("total"), self.currency)
        
    def add_line(self, title, data, currency = ""):
        self.pdf.cell(100, 10, title+" : "+str(data)+currency, 1, 1, 'L', fill=False)
    
    def add_line_empty(self):
        self.pdf.cell(100, 10,"", 1, 1, 'L', fill=False)
    
    def get_data(self, key):
        return self.order[key]
    
    def get_sub_data(self, tab, key):
        return tab[key]
    
    def save_file(self, path):
        
        self.pdf.output(path)
        
def get_order():
        return """{
    "company":"Ma super companie",
    "customer":"Mon super customer",
    "billing_address":"Rue du moulin 24",
    "delivery_address":"Rue de la loi 12",
    "desired_delivery":"07/07/2024",
    "agreed_delivery":"02/12/2025",
    "currency":"euro",
    "lang":"FR",
    "offer_lines":[
        {
            "quantity":6,
            "product":"product name 1",
            "unit_price":1,
            "orderline_price":6
        },
        {
            "quantity":2,
            "product":"product name 2",
            "unit_price":2.5,
            "orderline_price":5
        }
    ],
    "total":11
    }"""
    
order = json.loads(get_order())
pdf = CreatePdfUseCase(order)
pdf.create_pdf_fpdf()
pdf.save_file("pdf_1.pdf")
