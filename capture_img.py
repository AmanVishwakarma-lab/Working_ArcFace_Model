import cv2
import os
import time

# ======== ENTER STUDENT NAME HERE ========
student_name = input("Enter your name: ")  # change this every time
num_images = 10         # number of images to capture
delay = 0.5             # seconds between captures
# =========================================

dataset_path = "dataset"
student_path = os.path.join(dataset_path, student_name)

# Create folder if not exists
if not os.path.exists(student_path):
    os.makedirs(student_path)

# Start webcam
cap = cv2.VideoCapture(0)

print(f"[INFO] Capturing images for {student_name}")
print("[INFO] Press 'q' to quit early")

count = 0

while count < num_images:
    ret, frame = cap.read()
    if not ret:
        print("Failed to access camera")
        break

    cv2.imshow("Capture Dataset", frame)

    # Save image automatically
    img_path = os.path.join(student_path, f"{count+1}.jpg")
    cv2.imwrite(img_path, frame)
    print(f"[INFO] Saved {img_path}")

    count += 1
    time.sleep(delay)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("✅ Image capture completed!")
