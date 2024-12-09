import cv2
import pytesseract

# Load the image
image_path = "pokemon_card_images/alakazam-base-set-bs-1.jpg"
image = cv2.imread(image_path)

# Crop the area where the illustrator's name appears (bottom-left corner)
height, width, _ = image.shape
cropped_image = image[int(height * 0.85):height, :int(width * 0.3)]

# Use Tesseract to extract text
pytesseract.pytesseract.tesseract_cmd = r"/c/Program Files/Tesseract-OCR/tesseract.exe"
extracted_text = pytesseract.image_to_string(cropped_image)

print("Illustrator's Name:", extracted_text)