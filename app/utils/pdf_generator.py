import os

def generate_admission_letter(application):
    # static_dir = os.path.join(os.path.dirname(__file__), 'static')
    # output_path = os.path.join(static_dir, f'admission_letter_{application.id}.pdf')
    # Get the absolute path to the project root
    project_root = os.path.dirname(os.path.dirname(__file__))

    # Point to the static directory inside app/
    static_dir = os.path.join(project_root, 'static')

    # Final path to store the file
    output_path = os.path.join(static_dir, f'admission_letter_{application.id}.pdf')

    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    c = canvas.Canvas(output_path, pagesize=letter)
    text = c.beginText(50, 750)
    text.setFont("Helvetica", 12)
    
    lines = [
        f"Admission Letter",
        "",
        f"Dear {application.name},",
        "Congratulations! Your application has been approved.",
        "",
        f"Email: {application.email}",
        f"Academic Background: {application.academic_background}",
        "",
        "Welcome aboard!"
    ]

    for line in lines:
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()

    return output_path
