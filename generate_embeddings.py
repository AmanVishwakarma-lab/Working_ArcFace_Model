import os
import pickle
import cv2
from insightface.app import FaceAnalysis

DATASET_PATH = "dataset"
ENCODINGS_FILE = "encodings.pkl"

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=-1)  # CPU

known_embeddings = {}

for person_name in os.listdir(DATASET_PATH):

    person_path = os.path.join(DATASET_PATH, person_name)

    if not os.path.isdir(person_path):
        continue

    embeddings_list = []

    for image_file in os.listdir(person_path):

        if image_file.endswith((".jpg", ".png", ".jpeg")):

            img_path = os.path.join(person_path, image_file)
            img = cv2.imread(img_path)

            faces = app.get(img)

            if len(faces) > 0:
                embedding = faces[0].embedding
                embeddings_list.append(embedding)
                print(f"[INFO] Added embedding for {person_name} - {image_file}")
            else:
                print(f"[WARNING] No face found in {img_path}")

    if len(embeddings_list) > 0:
        known_embeddings[person_name] = embeddings_list

with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump(known_embeddings, f)

print("✅ All embeddings saved successfully!")
