from flask import Flask,render_template
app = Flask(__name__, static_folder='./templates/img')

@app.route('/')
def hello():
    name = "Hello World"
    #return name

    return render_template('main.html', title='😺社会性フィルター😺', name=name) #変更

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
