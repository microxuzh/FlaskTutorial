from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return '<h1>Hello World!</h1>'


if __name__ == '__main__':
	app.run(debug=True)                       # app.run()  default listen on localhost:5000

	# app.run(host='0.0.0.0',port='8080')     # you can set the port you like; and can be accessed from any remote client.