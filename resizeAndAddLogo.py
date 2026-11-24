#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((100, 100))
logoWidth, logoHeight = logoIm.size
print(logoHeight)
print(logoWidth)

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    extension = filename.lower().rpartition('.')
    extension = '.' + extension[2]
    #print(extension)
    if not (extension == '.png' or extension == '.jpg' or extension == '.gif' or extension == '.bmp') \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    if 2 * logoWidth > width and 2 * logoHeight > logoHeight:
        continue

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo.
    print('Adding logo to %s...' % (filename))

    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    if extension == '.jpg':
        im = im.convert('RGB')  # Convert to RGB if it's a JPG

    # Save changes.
    im.save(os.path.join('withLogo', filename))
