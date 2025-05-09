# Student-facing routes

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import StudentApplicationForm
from app.models import db, Application

bp = Blueprint('student', __name__, url_prefix='/student')

# @bp.route('/apply', methods=['GET', 'POST'])
# def apply():
#     form = StudentApplicationForm()
#     if form.validate_on_submit():
#         application = Application(
#             name=form.name.data,
#             email=form.email.data,
#             academic_background=form.academic_background.data
#         )
#         db.session.add(application)
#         db.session.commit()
#         flash('Application submitted successfully!', 'success')
#         return redirect(url_for('student.apply'))
#     return render_template('student_form.html', form=form)

from werkzeug.utils import secure_filename
import os

@bp.route('/apply', methods=['GET', 'POST'])
def apply():
    form = StudentApplicationForm()
    if form.validate_on_submit():
        # Handle file upload
        degree_certificate = form.degree_certificate.data
        id_proof = form.id_proof.data
        
        degree_certificate_path = None
        id_proof_path = None
        
        if degree_certificate:
            degree_certificate_filename = secure_filename(degree_certificate.filename)
            degree_certificate_path = os.path.join('uploads', degree_certificate_filename)
            degree_certificate.save(degree_certificate_path)
        
        if id_proof:
            id_proof_filename = secure_filename(id_proof.filename)
            id_proof_path = os.path.join('uploads', id_proof_filename)
            id_proof.save(id_proof_path)
        
        # Save application data to the database
        application = Application(
            name=form.name.data,
            email=form.email.data,
            academic_background=form.academic_background.data,
            degree_certificate=degree_certificate_path,
            id_proof=id_proof_path
        )
        db.session.add(application)
        db.session.commit()
        
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('student.apply'))
    print(form.errors)
    print("not valid")
    return render_template('student_form.html', form=form)

