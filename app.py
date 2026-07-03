from flask import Flask, render_template, request, send_from_directory, redirect
import os

app = Flask(__name__)

# =====================================================
# Configuration
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =====================================================
# Home Page
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


# =====================================================
# Upload Page
# =====================================================

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if "file" not in request.files:
            return render_template(
                "upload.html",
                message="No file selected."
            )

        file = request.files["file"]

        if file.filename == "":
            return render_template(
                "upload.html",
                message="Please select a file."
            )

        save_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(save_path)

        return render_template(
            "upload.html",
            message="✅ File Uploaded Successfully!",
            filename=file.filename
        )

    return render_template("upload.html")


# =====================================================
# Browse Files
# =====================================================

@app.route("/files")
def files():

    file_list = []

    for filename in os.listdir(UPLOAD_FOLDER):

        path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        if os.path.isfile(path):

            size = round(
                os.path.getsize(path) / 1024,
                2
            )

            file_list.append({
                "name": filename,
                "size": size
            })

    return render_template(
        "files.html",
        files=file_list
    )


# =====================================================
# Download File
# =====================================================

@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename,
        as_attachment=True
    )


# =====================================================
# Delete File
# =====================================================

@app.route("/delete/<filename>")
def delete(filename):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect("/files")


# =====================================================
# Run Server
# =====================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )