from PIL import Image

# Open the input image (replace 'input_image' with the actual file path)
input_image = Image.open('../tattoo_canvas/1695278175322.octet-stream')

# Convert the image to RGB mode
input_image = input_image.convert('RGB')

# Save the converted image as a JPG file (replace 'output_image.jpg' with the desired output file name)
input_image.save('reference_image.jpg', 'JPEG')

# Close the input image
input_image.close()