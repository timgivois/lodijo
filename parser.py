import pytesseract
import cv2
import re
import datefinder
from PIL import Image

def get_text_from_image(image_path):
    image = cv2.imread(image_path)
    blurred = cv2.blur(image, (3,3))

    img = Image.fromarray(blurred)

    text = pytesseract.image_to_string(img)

    return text


def get_details_from_text(text):
    splited_text = text.split('\n')

    username = None
    possible_username = re.search('@([^\s]+)', splited_text[0])
    if possible_username:
        username = possible_username.group()

    date = None
    possibe_dates = datefinder.find_dates(splited_text[0])
    if possibe_dates:
        date = [date for date in possibe_dates][0]

    # TODO: clean text

    return {
        'date': date,
        'username': username,
        'text': splited_text[1:],
    }
