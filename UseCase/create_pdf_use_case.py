from fpdf import FPDF
import json

def get_order():
    return """{
    "uuid": "0bada7889b4ec72b57c0436cef6fba1296520c6fe756595091d50e5b9eed7d6c",
    "company_name":"Synerglass-Soft",
    "internal_reference": "OF: 2022-13",
    "customer_reference": "Customer ref 13",
    "wished_delivery_date": "2023-07-17",
    "commentary": "commentary offer 13",
    "default_margin": 80,
    "additional_margin": 14.42,
    "delivery_address_uuid": "595b5a5bbd9b98da5292884c49e39ba6ae42da6cb69f1a7e9d2b65cc5e586f2c",
    "offer_lines": [
        {
            "uuid": "560ae92ce14470269979cfe140ed7aebb967cea0c1745fc119373466237adb9b",
            "line_number": 1,
            "quantity": 6,
            "chassis_marker": "chassis_marker_1",
            "width": 1000,
            "height": 1000,
            "item_description": "Description for line 1",
            "surface": 1,
            "reference": "reference for line 1",
            "price_detail": {
                "purchase_price": 440,
                "selling_price_excluding_vat": 181,
                "amount_vat": 34,
                "selling_price_including_vat": 110
            },
            "catalogue_uuid": "37522f729a0e1b836888fd03cc0f09ddc148ae9705d87758857b6df09bbe8c34",
            "item_uuid": "21cbb893282831e11f87a9033858687ba2f67691f86c1551d091c69ccffa855b",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "aa23e471b4700947c2188900ba15a0540dadc195c20b0458c7d567f7963b79e3",
            "line_number": 2,
            "quantity": 6,
            "chassis_marker": "",
            "width": 0,
            "height": 0,
            "item_description": "Description for line 2",
            "surface": 0,
            "reference": "reference for line 2",
            "price_detail": {
                "purchase_price": 484,
                "selling_price_excluding_vat": 42,
                "amount_vat": 10,
                "selling_price_including_vat": 26
            },
            "catalogue_uuid": "055823e65a5291d33014d3b40875c2007fd0ab98b8fe8af404cb79185d23e623",
            "item_uuid": "8849ccc958f19987a5987b63231810445839e6e58daa62dbc261747dbf676b64",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "63ae512e3b2948d3d25348773124f3e7b18bc6031f970800c2cec2db008ac1f9",
            "line_number": 3,
            "quantity": 9,
            "chassis_marker": "",
            "width": 0,
            "height": 0,
            "item_description": "Description for line 3",
            "surface": 0,
            "reference": "reference for line 3",
            "price_detail": {
                "purchase_price": 117,
                "selling_price_excluding_vat": 194,
                "amount_vat": 49,
                "selling_price_including_vat": 421
            },
            "catalogue_uuid": "0000000000000000000000000000000000000000000000000000000000000000",
            "item_uuid": "0000000000000000000000000000000000000000000000000000000000000000",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "ce0d53272392e8e41214d253f26a62fa0acb3e6cf1bd0029b13d90fde7041129",
            "line_number": 4,
            "quantity": 9,
            "chassis_marker": "chassis_marker_4",
            "width": 4000,
            "height": 4000,
            "item_description": "Description for line 4",
            "surface": 16,
            "reference": "reference for line 4",
            "price_detail": {
                "purchase_price": 265,
                "selling_price_excluding_vat": 342,
                "amount_vat": 33,
                "selling_price_including_vat": 246
            },
            "catalogue_uuid": "37522f729a0e1b836888fd03cc0f09ddc148ae9705d87758857b6df09bbe8c34",
            "item_uuid": "21cbb893282831e11f87a9033858687ba2f67691f86c1551d091c69ccffa855b",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "7d7081f7f3268368d4303366e394118475e4e5d480bc30dd540c22c68d92de95",
            "line_number": 6,
            "quantity": 2,
            "chassis_marker": "",
            "width": 0,
            "height": 0,
            "item_description": "Description for line 6",
            "surface": 0,
            "reference": "reference for line 6",
            "price_detail": {
                "purchase_price": 354,
                "selling_price_excluding_vat": 226,
                "amount_vat": 30,
                "selling_price_including_vat": 131
            },
            "catalogue_uuid": "0000000000000000000000000000000000000000000000000000000000000000",
            "item_uuid": "0000000000000000000000000000000000000000000000000000000000000000",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "9ccc59b98aa3216ffda6b33bec9676e0bb1923c7395a912d267fe64b4450bc74",
            "line_number": 7,
            "quantity": 3,
            "chassis_marker": "chassis_marker_7",
            "width": 7000,
            "height": 7000,
            "item_description": "Description for line 7",
            "surface": 49,
            "reference": "reference for line 7",
            "price_detail": {
                "purchase_price": 425,
                "selling_price_excluding_vat": 106,
                "amount_vat": 35,
                "selling_price_including_vat": 487
            },
            "catalogue_uuid": "37522f729a0e1b836888fd03cc0f09ddc148ae9705d87758857b6df09bbe8c34",
            "item_uuid": "21cbb893282831e11f87a9033858687ba2f67691f86c1551d091c69ccffa855b",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "e12db18b353393efa3dd197c88d825b4b5a2f015e8ecda8f182f4ce1dc2d82c9",
            "line_number": 8,
            "quantity": 4,
            "chassis_marker": "",
            "width": 0,
            "height": 0,
            "item_description": "Description for line 8",
            "surface": 0,
            "reference": "reference for line 8",
            "price_detail": {
                "purchase_price": 489,
                "selling_price_excluding_vat": 416,
                "amount_vat": 54,
                "selling_price_including_vat": 128
            },
            "catalogue_uuid": "055823e65a5291d33014d3b40875c2007fd0ab98b8fe8af404cb79185d23e623",
            "item_uuid": "8849ccc958f19987a5987b63231810445839e6e58daa62dbc261747dbf676b64",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        },
        {
            "uuid": "a60c31149299f4fa82136934e722f91512d8c2bc7705fcdbb1f89e58e803c59a",
            "line_number": 9,
            "quantity": 2,
            "chassis_marker": "",
            "width": 0,
            "height": 0,
            "item_description": "Description for line 9",
            "surface": 0,
            "reference": "reference for line 9",
            "price_detail": {
                "purchase_price": 490,
                "selling_price_excluding_vat": 235,
                "amount_vat": 77,
                "selling_price_including_vat": 316
            },
            "catalogue_uuid": "0000000000000000000000000000000000000000000000000000000000000000",
            "item_uuid": "0000000000000000000000000000000000000000000000000000000000000000",
            "type_uuid": "0000000000000000000000000000000000000000000000000000000000000000"
        }
    ],
    "totals": {
        "quantity": 54,
        "surface": 54,
        "amout_energetic_surcharge": 54,
        "amount_excluding_vat": 54,
        "amount_vat": 54,
        "amount_including_vat": 54
    }
}"""

def create_pdf_fpdf(order):
    pdf = FPDF('P','mm','Letter')

    pdf.add_page()

    pdf.set_font('helvetica', '', 16)

    # pdf.set_fill_color(200,100,58)
    
    pdf.cell(100,10, 'company_name : '+order["company_name"], 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'internal_reference : '+order["internal_reference"], 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'customer_reference : '+order["customer_reference"], 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'wished_delivery_date : '+order["wished_delivery_date"], 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'commentary : '+order["commentary"], 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'default_margin : '+str(order["default_margin"]), 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'additional_margin : '+str(order["additional_margin"]), 1, 1, 'L', fill=False)
    
    pdf.cell(100,10, '', 1, 1, 'L', fill=False)
    
    
    pdf.cell(100,10, 'Offer_lines : ', 1, 1, 'L', fill=False)
    
    pdf.cell(100,10, '', 1, 1, 'L', fill=False)
    
    pdf.cell(100,10, 'totals : ', 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'quantity : '+str(order["totals"]["quantity"]), 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'surface : '+str(order["totals"]["surface"]), 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'amout_energetic_surcharge : '+str(order["totals"]["amout_energetic_surcharge"]), 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'amount_excluding_vat : '+str(order["totals"]["amount_excluding_vat"]), 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'amount_vat : '+str(order["totals"]["amount_vat"]), 1, 1, 'L', fill=False)
    pdf.cell(100,10, 'amount_including_vat : '+str(order["totals"]["amount_including_vat"]), 1, 1, 'L', fill=False)
    
    # with pdf.table() as table:
    #     row = table.row
    #     row.cell("Hello")
    
    pdf.output('pdf_1.pdf')

order = json.loads(get_order())
create_pdf_fpdf(order)