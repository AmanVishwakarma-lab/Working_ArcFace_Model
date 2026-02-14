from flask import Flask, request, jsonify
import os
from recognition import recognize_faces

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/recognize", methods=["POST"])
def recognize():

    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    recognized = recognize_faces(filepath)

    return jsonify({
        "recognized_faces": recognized
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)