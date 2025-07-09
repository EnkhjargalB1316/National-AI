from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def ai_intro():
    return render_template("about.html")

@app.route('/lesson')
def ai_in_education():
    return render_template("lesson.html")

@app.route('/practice')
def teacher_training():
    return render_template("practice.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

@app.route('/project')
def future():
    return render_template("project.html")

if __name__ == '__main__':
    app.run(debug=True)
