from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/artifact/<name>')
def artifact_page(name):
    return render_template("artifact_template.html", artifact_name=name)

if __name__ == '__main__':
    app.run(debug=True)