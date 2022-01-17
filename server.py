from flask import Flask, render_template

app = Flask(__name__)

print (__name__)

@app.route('/')
@app.route('/<int:width>')
@app.route('/<int:width>/<int:height>')
@app.route('/<int:width>/<int:height>/<color1>')
@app.route('/<int:width>/<int:height>/<color1>/<color2>')
def index(width=8, height=8, color1="forestgreen", color2="firebrick"):
    return render_template('index.html', width=width, height=height, color1=color1, color2=color2)


if __name__ =='__main__':
    app.run(debug=True)