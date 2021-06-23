from flask import Flask, render_template, request
from json import loads

app = Flask(__name__)

words = loads(open('dictionary.json', 'r').read())

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		word = request.form.get('word').lower()
		try:
			return words[word]
		except KeyError:
			return "null-word"
	return render_template('index.html')



if __name__ == '__main__':
	Flask.run(app, port=5000, debug=False)
