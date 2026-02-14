import pickle
import cv2
from insightface.app import FaceAnalysis
from utils import cosine_similarity

ENCODINGS_FILE = "encodings.pkl"

app = FaceAnalysis(name="buffalo_l",providers=['CPUExecutionProvider'])
app.prepare(ctx_id=-1)

with open(ENCODINGS_FILE, "rb") as f:
    known_embeddings = pickle.load(f)

THRESHOLD = 0.5

def recognize_faces(image_path):

    img = cv2.imread(image_path)
    faces = app.get(img)

    recognized_names = []

    for face in faces:
        embedding = face.embedding

        best_match = "Unknown"
        best_score = 0

        for name, embeddings_list in known_embeddings.items():

            for known_embedding in embeddings_list:

                score = cosine_similarity(embedding, known_embedding)

                if score > best_score:
                    best_score = score
                    best_match = name

        if best_score < THRESHOLD:
            best_match = "Unknown"

        recognized_names.append(best_match)

    return recognized_names
