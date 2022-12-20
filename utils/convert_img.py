# import PIL module
from PIL import Image
import os
from utils.request_url import download_url

path = os.getcwd()
# Back Image
bg = 'bg.jpeg'


def convert_bg(card_url):
    # Download front image to local directory
    card_jpg = download_url(card_url)
    frontImage = Image.open(card_jpg).resize((325, 400))
    print('Size...', frontImage.size)
    # Open Background Image
    background = Image.open(bg)
    # Convert image to RGBA
    frontImage = frontImage.convert("RGBA")
    # Convert image to RGBA
    background = background.convert("RGBA")
    # Calculate width to be at the center
    width = (background.width - frontImage.width) // 2
    # Calculate height to be at the center
    height = (background.height - frontImage.height) // 2
    # Paste the frontImage at (width, height)
    background.paste(frontImage, (width, height), frontImage)
    # Save this image
    background.save("composed.png", format="png")
    return f'{path}/composed.png'

