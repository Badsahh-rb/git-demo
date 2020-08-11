from flask import Flask

app=Flask(__name__)

@app.route('/')

def function():
	return"Hello"
if _name_== ""__main__"":
	  app.run(debug=True)