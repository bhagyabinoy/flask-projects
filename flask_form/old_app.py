# from flask import Flask, render_template, redirect, url_for, flash
# from flask_wtf import FlaskForm
# from wtforms import validators
# from wtforms_components import EmailField
# from forms import ContactForm

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     form = ContactForm()
#     if form.validate_on_submit():
#         # Process the form data (e.g., send email)
#         email = form.email.data
#         # ... (Implement email sending logic)
#         flash('Message Sent!', 'success')
#         return redirect(url_for('home'))
#     return render_template('contact.html', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)
