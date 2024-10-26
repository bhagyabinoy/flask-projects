from flask import render_template, redirect, url_for
from app import db
from app.forms import ContactForm
from app.models import Contact
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(email=form.email.data)
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('main.success'))
    return render_template('contact.html', form=form)

@bp.route('/success')
def success():
    return "Contact successfully created!"
