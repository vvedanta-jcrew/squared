from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def fact_show():
	return render_template('index.html')
	
@app.route('/squared', methods=['POST'])
def squared():
	if request.method == 'POST':
		res = int(request.form['fnum'])
		res = res*res
		return render_template("fact.html", res=res)
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)