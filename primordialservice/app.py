from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') 

app.add_url_rule('/home','home', home)

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/service')
def service():
    return render_template('service.html') 

@app.route('/servicemenu')
def servicemenu():
    return render_template('servicemenu.html') 

@app.route('/areasofapp')
def areasofapp():
    return render_template('areasofapp.html') 

@app.route('/generalpest')
def generalpest():
    return render_template('generalpest.html') 

@app.route('/pestcontrol')
def pestcontrol():
    return render_template('pestcontrol.html') 

@app.route('/sanitization')
def sanitization():
    return render_template('sanitization.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html') 

if __name__ == '__main__':
    app.run(debug=True)



