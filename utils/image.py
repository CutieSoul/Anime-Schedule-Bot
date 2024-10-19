# Do not remove credits given in this repo.
# Importing this repo instead of forking is strictly prohibited.
# Kindly fork and edit as you wish. Feel free to give credits to the developer.

import os
import random
import logging

logger = logging.getLogger(__name__)

IMAGE_DIR = "images"

# Check if the image directory exists
if not os.path.isdir(IMAGE_DIR):
    logger.error(f"{IMAGE_DIR} is not a valid directory.")
    exit(1)

def get_random_image() -> str:
    """Return a random image path from the images directory, excluding 'msg.jpg'."""
    images = [img for img in os.listdir(IMAGE_DIR)
              if img.endswith(('.png', '.jpg', '.jpeg')) and img != 'msg.jpg']
    if not images:
        logger.error("No images found in the directory.")
        return None
    selected_image = random.choice(images)
    logger.info(f"Selected image: {selected_image}")
    return os.path.join(IMAGE_DIR, selected_image)
