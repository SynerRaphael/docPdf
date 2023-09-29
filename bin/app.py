from flask import Flask, make_response
from UseCase.create_pdf_use_case import CreatePdfUseCase
import json

app = Flask(__name__)

def get_order():
        return """{
    "company":"Ma super companie",
    "customer":"Mon super customer",
    "billing_address":"Rue du moulin 24",
    "delivery_address":"Rue de la loi 12",
    "desired_delivery":"07/07/2024",
    "agreed_delivery":"02/12/2025",
    "currency":"euro",
    "offer_lines":[
        {
            "quantity":6,
            "product":"product 1",
            "unit_price":1,
            "orderline_price":6
        },
        {
            "quantity":2,
            "product":"product 2",
            "unit_price":2.5,
            "orderline_price":5
        }
    ],
    "total":11
    }"""

@app.get('/v1/document')
def get_pdf():
    order = json.loads(get_order())
    
    pdf = CreatePdfUseCase(order)
    response = make_response(pdf)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
