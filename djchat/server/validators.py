import os

from django.core.exceptions import ValidationError
from PIL import Image


def validate_file_size(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError(
                    f"Icon size must be less than 70x70 pixels. The provided image is {img.width}x{img.height} pixels"
                )


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".jpeg", ".png", "gif"]
    if ext.lower() not in valid_extensions:
        raise ValidationError(
            f'Unsupported file extension. Only {", ".join(valid_extensions)} are allowed.'
        )
