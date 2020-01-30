from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', 'a+') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"email: {email}\nsubject: {subject}\nmessage: {message}\n\n")


def write_to_csv(data):
    with open('database.csv', 'a+', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            'did not save to db'
    else:
        return 'something went wrong, try again!'