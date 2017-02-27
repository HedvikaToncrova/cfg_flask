from flask import Flask
from flask import render_template, request
import requests

app = Flask("MyApp")

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
	name = name.title() if name is not None else None
	return render_template('hello.html', name=name)


@app.route('/signup', methods=['POST'])
def signup():
	print "In signup"
	form_data = request.form
	print "Name = ", form_data['name']
	email_address = form_data['email']
	print "Email = ", email_address
	send_simple_message(email_address)
	return "All OK"


def send_simple_message(email_address):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc47ef19a01e644138b62190eef2218b6.mailgun.org/messages",
        auth=("api", "key-020824c0934063966f0347efa8cccd17"),
        data={"from": "Excited User <mailgun@sandboxc47ef19a01e644138b62190eef2218b6.mailgun.org>",
              "to": [email_address],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


app.run()
