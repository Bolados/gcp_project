# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/gfg')
def gfg():
    return 'you the best'


app.add_url_rule('/', 'g2g', gfg)
# main driver function

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
# if __name__ == '__main__':

#     # run() method of Flask class runs the application
#     # on the local development server.
#     # app.add_url_rule('/','g2g', gfg)
#     app.run()
