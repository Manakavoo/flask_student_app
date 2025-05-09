# Functional Requirement Document (FRD)

## Project Title: Student Admission Portal

## 1. Introduction

The **Student Admission Portal** is a web-based system designed to streamline the process of student applications for academic admission. This document outlines the key functionalities, user roles, and system behavior in detail to ensure clear understanding and alignment before and during development.

---

## 2. Objective

The main objective of this project is to allow students to submit admission applications online and enable administrators to review, approve, or reject applications. Upon approval, the system will automatically generate and provide a downloadable **admission letter in PDF format**.

---

## 3. Users and Roles

### 1. Student
- Can access the application form.
- Can fill in personal details, academic background, and upload documents (degree certificate and ID proof).
- Can submit the form and receive confirmation.
- Upon approval, can download the admission letter.

### 2. Admin
- Can access the admin dashboard to review all submitted applications.
- Can view application details and attached documents.
- Can approve or reject applications.
- On approval, the system generates a PDF admission letter.

---

## 4. Functional Requirements

### 4.1 Student Application Form
- The form should collect:
  - Full Name (required)
  - Email (required, valid format)
  - Academic Background (required, text)
  - Degree Certificate (PDF upload, required)
  - ID Proof (PDF upload, required)
- Form validation for required fields and file types
- On successful submission, application is saved in the database.

### 4.2 Admin Dashboard
- Admin can log in (if authentication is implemented in future versions).
- Admin can view a list of all submitted applications.
- Each application can be opened to view full details and attachments.
- Admin can click:
  - ✅ **Approve** → Generates a PDF admission letter and stores it for download.
  - ❌ **Reject** → Updates status to rejected.

### 4.3 Admission Letter Generation
- On approval, the system:
  - Generates a PDF admission letter.
  - Saves the file under the `/static/` directory.
  - Provides a download link for the student.
- PDF includes:
  - Student’s name and email
  - Academic details
  - Admission approval date
  - Admission confirmation message

---

## 5. Non-Functional Requirements

- Clean and responsive frontend using HTML/CSS.
- Backend developed using Python and Flask.
- SQLite as the default database; MySQL support with `.env` switch.
- Use of Flask-Migrate for database versioning.
- Use of Jinja2 templates for rendering views.
- Organized project structure for scalability and maintainability.

---

## 6. Database Design

**Table: applications**
| Field               | Type        | Description                          |
|--------------------|-------------|--------------------------------------|
| id                 | Integer     | Primary Key                          |
| name               | String      | Student full name                    |
| email              | String      | Student email                        |
| academic_background| Text        | Educational details                  |
| degree_certificate | String      | Filename/path to uploaded PDF        |
| id_proof           | String      | Filename/path to uploaded PDF        |
| status             | String      | 'pending', 'approved', 'rejected'    |
| pdf_letter         | String      | Path to generated PDF (if approved)  |
| submitted_at       | DateTime    | Submission timestamp                 |

---

## 7. Future Enhancements (Optional)

- Admin authentication system
- Email notifications for approval/rejection
- Upload document preview feature
- Pagination or search in admin dashboard
- Student dashboard to track application status

---

## 8. Assumptions

- All uploads are in PDF format.
- There is no user registration/authentication at this stage.
- Admin actions are accessible without login.
- Application IDs are unique and auto-generated.

---

## 9. Glossary

- **FRD**: Functional Requirement Document
- **PDF**: Portable Document Format
- **CRUD**: Create, Read, Update, Delete

---

## 10. Conclusion

This FRD serves as the baseline blueprint for developing the student admission system. It helps align development efforts with clearly defined user roles, behaviors, and system expectations.
