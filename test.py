from transformers import pipeline

# Load BLIP captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Path to any test image you have in img/
image_path = "img/test.png"   # put any small JPG in that folder

result = captioner(image_path)
print("Generated caption:", result[0]["generated_text"])
 