import email_f, news
from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        interest = request.form.get('interest')
        email_f.getInfo(users=name, emails=email, interests=interest)
    return render_template('index.html')



@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/success")
def success():
    return render_template('success.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
    
    