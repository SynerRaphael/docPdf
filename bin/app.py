from flask import Flask, make_response
import UseCase.create_pdf_use_case
import json

app = Flask(__name__)


@app.get('/v1/document')
def get_pdf():
    test = '{ "Hello":"world " }'
    # order = json.loads(UseCase.create_pdf_use_case.get_order())
    # pdf = UseCase.create_pdf_use_case.create_pdf_fpdf(order)
    # response = make_response(pdf)
    return test


if __name__ == '__main__':
    app.run(host='0.0.0.0')
