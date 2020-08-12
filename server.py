import csv
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
import os
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_csv(data):
#     with open('database.csv', mode='a') as database
#         first_name = data['first_name']
#         last_name = data['last_name']
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         csv_writer = csv.writer(database, delimiter=',', quotecher='', quoting=csv.QUOTE_MINIMAL))


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return redirect('thankyou.html')
    else:
        return 'something went wrong. Try again!'