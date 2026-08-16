from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["UPLOAD_FOLDER"] = str(UPLOAD_DIR)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB per request

ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif"}
TITLE_OPTIONS = ["Mr.", "Ms.", "Others"]
MARITAL_STATUS_OPTIONS = ["Single", "Married", "Divorced", "Widowed"]
CATEGORY_OPTIONS = ["General", "OBC", "SC", "ST"]
RELIGION_OPTIONS = ["Hindu", "Muslim", "Jain", "Christianity"]
STATE_OPTIONS = [
    "Andhra Pradesh", "Andaman and Nicobar Islands", "Arunachal Pradesh", "Assam", "Bihar",
    "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Lakshadweep",
    "Puducherry", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]
LANGUAGES = ["Hindi", "English", "Urdu"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form.to_dict(flat=True)
        errors = validate_form(request)

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "index.html",
                form=form_data,
                success=False,
                title_options=TITLE_OPTIONS,
                marital_status_options=MARITAL_STATUS_OPTIONS,
                category_options=CATEGORY_OPTIONS,
                religion_options=RELIGION_OPTIONS,
                state_options=STATE_OPTIONS,
                languages=LANGUAGES,
            )

        saved_files = save_uploads(request)
        application_id = datetime.now().strftime("DOEACC-%Y%m%d-%H%M%S")

        return render_template(
            "index.html",
            form={},
            success=True,
            application_id=application_id,
            saved_files=saved_files,
            applicant_name=form_data.get("full_name", "Applicant"),
            title_options=TITLE_OPTIONS,
            marital_status_options=MARITAL_STATUS_OPTIONS,
            category_options=CATEGORY_OPTIONS,
            religion_options=RELIGION_OPTIONS,
            state_options=STATE_OPTIONS,
            languages=LANGUAGES,
        )

    return render_template(
        "index.html",
        form={},
        success=False,
        title_options=TITLE_OPTIONS,
        marital_status_options=MARITAL_STATUS_OPTIONS,
        category_options=CATEGORY_OPTIONS,
        religion_options=RELIGION_OPTIONS,
        state_options=STATE_OPTIONS,
        languages=LANGUAGES,
    )


def validate_form(req) -> List[str]:
    data = req.form
    errors: List[str] = []

    required_fields: Dict[str, str] = {
        "title": "Title",
        "full_name": "Applicant full name",
        "father_name": "Father's name",
        "mother_name": "Mother's name",
        "gender": "Gender",
        "dob": "Date of birth",
        "marital_status": "Marital status",
        "category": "Category",
        "religion": "Religion",
        "mobile": "Mobile number",
        "email": "Email ID",
        "address1": "Address line 1",
        "city": "City",
        "state": "State",
        "pincode": "Pin code",
    }

    for key, label in required_fields.items():
        if not data.get(key, "").strip():
            errors.append(f"{label} is required.")

    full_name = data.get("full_name", "").strip()
    if full_name and len(full_name) < 3:
        errors.append("Applicant full name must be at least 3 characters.")

    mobile = data.get("mobile", "").strip()
    if mobile and not re.fullmatch(r"\d{10}", mobile):
        errors.append("Mobile number must be exactly 10 digits.")

    pincode = data.get("pincode", "").strip()
    if pincode and not re.fullmatch(r"\d{6}", pincode):
        errors.append("Pin code must be exactly 6 digits.")

    aadhaar = data.get("aadhaar", "").strip()
    if aadhaar and not re.fullmatch(r"\d{12}", aadhaar):
        errors.append("Aadhaar number must be exactly 12 digits.")

    pan = data.get("pan", "").strip().upper()
    if pan and not re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan):
        errors.append("PAN card format must be like ABCDE1234F.")

    email = data.get("email", "").strip()
    if email and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        errors.append("Please enter a valid email address.")

    dob = data.get("dob", "").strip()
    if dob:
        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
            if dob_date >= datetime.today().date():
                errors.append("Date of birth must be in the past.")
        except ValueError:
            errors.append("Invalid date of birth.")

    for file_key, label in {"photo": "Photo", "signature": "Signature"}.items():
        file = req.files.get(file_key)
        if file and file.filename:
            if not allowed_file(file.filename):
                errors.append(f"{label} must be an image file (png, jpg, jpeg, webp, gif).")

    return errors


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def save_uploads(req) -> Dict[str, str]:
    saved: Dict[str, str] = {}
    for key in ["photo", "signature"]:
        file = req.files.get(key)
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
            final_name = f"{timestamp}_{filename}"
            path = UPLOAD_DIR / final_name
            file.save(path)
            saved[key] = final_name
    return saved


@app.errorhandler(413)
def file_too_large(_error):
    flash("Uploaded file is too large. Maximum allowed size is 5 MB.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
