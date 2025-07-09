from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/lesson')
def lesson():
    return render_template("lesson.html")

@app.route('/practice')
def practice():
    return render_template("practice.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

@app.route('/project')
def project():
    return render_template("project.html")

if __name__ == '__main__':
    app.run(debug=True)
