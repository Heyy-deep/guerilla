import sys
import subprocess

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

img_path = '/Users/soumyadeepde/.gemini/antigravity/scratch/igloo_portfolio/assets/bike_img.jpg'
im = Image.open(img_path)
min_dim = min(im.size)
im_new = crop_center(im, min_dim, min_dim)
im_new.save(img_path, quality=95)
print(f"Cropped to {min_dim}x{min_dim}")
