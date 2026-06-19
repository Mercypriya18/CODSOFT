from transformers import VisionEncoderDecoderModel
from transformers import ViTImageProcessor
from transformers import AutoTokenizer
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

processor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

image = Image.open("sample.jpg")

pixel_values = processor(
    images=image,
    return_tensors="pt"
).pixel_values

output_ids = model.generate(pixel_values)

caption = tokenizer.decode(
    output_ids[0],
    skip_special_tokens=True
)

print("Caption:", caption)