import os
from pathlib import Path
from time import time

import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.models import load_model

# os.environ["CUDA_VISIBLE_PROCESS"] = "-1"

DATA_PATH = Path("/app/data")
JPG_PATH = Path(DATA_PATH.joinpath("Flag"))
MODEL_PATH = Path(DATA_PATH.joinpath("Model.h5"))


def preprocess_img(path):
    img = Image.open(path)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


if __name__ == "__main__":
    start_time = time()
    model = load_model(
        MODEL_PATH, custom_objects={"Rescaling": tf.keras.layers.Rescaling}
    )
    jpg_list = list(JPG_PATH.glob("**/*.jpg"))
    row_list = [int(img.name.split("_")[0]) for img in jpg_list]
    col_list = [int(img.name.split("_")[1].split(".")[0]) for img in jpg_list]
    nb_row = max(row_list) + 1
    nb_col = max(col_list) + 1

    data = np.zeros((nb_row, nb_col, 3), dtype=np.uint8)

    nb_iter = jpg_list.__len__()
    counter = 1
    for img in jpg_list:
        print(f"{(counter/nb_iter)*100:.2f}% ({counter}/{nb_iter})")
        predict = model.predict(preprocess_img(img))
        x = int(img.name.split("_")[0])
        y = int(img.name.split("_")[1].split(".")[0])
        if predict > 0.65:
            data[x, y] = [0, 0, 0]
        else:
            data[x, y] = [255, 255, 255]
        counter += 1
    Image.fromarray(data).save("/app/output/result.jpg")
    end_time = time()
    print(f"End of Process after {end_time-start_time} seconds running")
