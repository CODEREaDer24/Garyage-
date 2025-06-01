from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return redirect("/market")

@app.route("/market", methods=["GET"])
def market():
    return render_template("virtual_market.html", filename=None)

@app.route("/upload", methods=["POST"])
def upload_image():
    if 'image' not in request.files:
        return "❌ No file part in request"
    file = request.files['image']
    if file.filename == '':
        return "❌ No selected file"
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    return render_template("virtual_market.html", filename=filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
