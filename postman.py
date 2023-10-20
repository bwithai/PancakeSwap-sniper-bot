import requests

# Define the URLs for the endpoints
skin_canvas_url = "http://202.166.170.106:14500/arhamsoft/skin_canvas/"
bg_removal_url = "http://202.166.170.106:14500/arhamsoft/bg_removal/"

# Test the skin_canvas endpoint
# skin_canvas_payload = {
#     "preview_image_url": "http://skin-canvas.arhamsoft.org/images/1695278173284.octet-stream",
#     "reference_image_url": "http://skin-canvas.arhamsoft.org/images/1695278175322.octet-stream"
# }
skin_canvas_payload = {
    "preview_image_url": ("preview_image.jpg", open("../tattoo_canvas/preview_image.jpg", "rb")),
    "reference_image_url": ("reference_image.jpg", open("../tattoo_canvas/reference_image.jpg", "rb"))
}

skin_canvas_response = requests.post(skin_canvas_url, files=skin_canvas_payload)

if skin_canvas_response.status_code == 200:
    print("skin_canvas Request was successful.")
    print(skin_canvas_response.json())
else:
    print(f"skin_canvas Request failed with status code: {skin_canvas_response.status_code}")

# Test the bg_removal endpoint
bg_removal_payload = {
    "image_urls": [
        "https://images.unsplash.com/photo-1610088441520-4352457e7095?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG1lbnxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80"
    ]
}

bg_removal_response = requests.post(bg_removal_url, json=bg_removal_payload)

if bg_removal_response.status_code == 200:
    print("bg_removal Request was successful.")
    print(bg_removal_response.json())
else:
    print(f"bg_removal Request failed with status code: {bg_removal_response.status_code}")
