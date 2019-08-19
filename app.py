from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hey, we sdfsf Flask in minishift!'

@app.route('/hi')
def hi():
	return 'Hey, we have Flaaasask sdfin aHI!'


if __name__ == '__main__':
	app.run(host='0.0.0.0')
