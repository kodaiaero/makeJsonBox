import cv2
import json
import os

def get_image_files(folder):
    return sorted([f for f in os.listdir(folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))])

def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, drawing, bounding_boxes, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_x, end_y = x, y
        bounding_boxes.append({
            "x_min": start_x, "y_min": start_y,
            "x_max": end_x, "y_max": end_y
        })
        cv2.rectangle(img_copy, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("Image", img_copy)

current_folder = os.getcwd()
output_folder = os.path.join(os.path.dirname(current_folder), "output")
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, f"{os.path.basename(current_folder)}.json")

drawing = False
start_x, start_y = -1, -1
bounding_boxes = []
results = []

image_files = get_image_files(current_folder)

for image_name in image_files:
    image_path = os.path.join(current_folder, image_name)
    img = cv2.imread(image_path)
    img_copy = img.copy()

    bounding_boxes = []

    cv2.imshow("Image", img_copy)
    cv2.setMouseCallback("Image", draw_rectangle)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cv2.destroyAllWindows()

    results.append({
        "image": image_name,
        "bounding_boxes": bounding_boxes
    })

with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

print(f"Bounding box data saved to {output_file}")
