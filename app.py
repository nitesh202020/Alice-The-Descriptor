from flask import Flask, render_template, redirect, request
import Caption
# instantiate
app = Flask(__name__)
# Routes

@app.route('/')
def hello():
	return render_template("index.html" )

@app.route('/', methods =['POST'])
def submit_data():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename)
		f.save(path)
		caption = Caption.caption_the_image(path)
		result_dic = {
		'image' : path,
		'caption' : caption
		}
	return render_template("index.html",your_res = result_dic)


if __name__=='__main__' :
	app.run(debug = True)

