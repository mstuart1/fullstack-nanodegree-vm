from flask import Flask # import Flask class from flask library
app = Flask(__name__) # create instance with name of running app as argument; special variable called name is defined for the app and all of the imports it uses.

@app.route('/') # decorator function app.route is predefined in flask, if either of these gets sent from the browser it will run our HelloWorld function.
@app.route('/hello')
# our function definition
def HelloWorld():
	return "Hello World"

if __name__ == '__main__': # main is for python interpreter, if you are importing into another python file, don't run this.
	app.debug = True # server will reload each time it notices a change
	app.run(host = '0.0.0.0', port = 5000) # only accessible from host machine and nowhere else.

