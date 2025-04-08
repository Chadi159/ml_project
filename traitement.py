import pandas as pd

# Sample DataFrame
data = {
    "image_name": ["img1", "img2", "img3"],
    "label": [1, 2, 3]
}
df = pd.DataFrame(data)

cle = "img2"
label_value = df.loc[df["image_name"] == cle, "label"].values[0]
print(label_value)