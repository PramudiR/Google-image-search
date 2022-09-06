from serpapi import GoogleSearch
import os, json

my_secret = os.environ['secret_api_key']
params = {
  "api_key": my_secret,
  "engine": "google",
  "q": "sea",
  "hl": "en",
  "tbm": "isch"
}

search = GoogleSearch(params)
results = search.get_dict()
# print(results["images_results"])

image_results = []

for image in results["images_results"]:
  image_results.append({
        "original": image["original"]
        })

# print(image_results)
img=json.dumps(image_results, indent=2)

# print(image_results[0]["original"])

from PIL import Image
import requests
url = image_results[0]["original"]
im = Image.open(requests.get(url, stream=True).raw)

import matplotlib.pyplot as plt
imgplot = plt.imshow(im)
plt.show()