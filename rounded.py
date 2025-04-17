from PIL import Image, ImageDraw
import os

input_dir = "./images/blockchain"
output_dir = "./images"
resize_to = (52, 52)
radius = 15  # smaller radius for smaller image

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"rounded_{filename}")
        
        image = Image.open(input_path).convert("RGBA")

        # ✅ Resize using correct resampling mode for Pillow >= 10
        image = image.resize(resize_to, Image.Resampling.LANCZOS)

        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, *image.size], radius=radius, fill=255)

        rounded_image = Image.new("RGBA", image.size)
        rounded_image.paste(image, (0, 0), mask)

        rounded_image.save(output_path)

print("All images processed!")
