# Admin-facing routes
from flask import Blueprint, render_template, redirect, url_for, flash, send_file
from app.models import db, Application
from app.utils.pdf_generator import generate_admission_letter
import os

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/review')
def review():
    applications = Application.query.all()
    return render_template('admin_dashboard.html', applications=applications)

@bp.route('/approve/<int:app_id>')
def approve(app_id):
    print(f"Approving application with ID: {app_id}")
    application = Application.query.get_or_404(app_id)
    if application.status != 'pending':
        flash('Application has already been processed.', 'warning')
        return redirect(url_for('admin.review'))
    pdf_path = generate_admission_letter(application)
    application.status = 'approved'
    db.session.commit()
    print(f"Application {app_id} approved and letter generated at {pdf_path}")
    flash('Application approved and letter generated.', 'success')
    return send_file(pdf_path, as_attachment=True)
