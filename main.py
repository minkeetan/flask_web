"""
flask web
"""
import flask

app = flask.Flask(__name__)
@app.route('/')
def hello():
    "hello"
    return '你好,这是第一个Flask Web程序!'

if __name__== '__main__':
    app.run(debug=True)
