# resizeAndAddLogo.py

The script processes all supported image files (`.png`, `.jpg`, `.gif`, `.bmp`) in the current working directory (excluding `catlogo.png`). For each image:

1. **Filters** out images narrower than 200 px (via a conditional check).
2. **Resizes** the image only if **both** width and height exceed 300 px, scaling it down to fit within a 300×300 square while preserving the original aspect ratio.
3. **Pastes** a pre‑resized 100×100 px version of `catlogo.png` onto the bottom‑right corner.
4. **Saves** the modified image to a `withLogo/` subdirectory. JPEG outputs are converted to RGB mode before saving.

In summary, it uniformly adds a cat logo to qualifying images and ensures no image exceeds 300×300 pixels (when both dimensions are large), outputting everything to a dedicated folder.