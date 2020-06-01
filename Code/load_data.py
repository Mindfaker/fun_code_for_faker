import os
import sys
import pandas as pd
from config.self_config import *

def read_raw_data(field_type_name: str, data_type: str = "train"):
    if data_type == "train":
        base_path = first_train_data
    elif data_type == "test":
        base_path = first_test_data
    else:
        return None

    file_name = data_type + "_" + field_type_name + ".csv"

    data_path = os.path.join(base_path, file_name)
    data = pd.read_csv(data_path, engine="python", encoding="utf-8")
    return data

if __name__ == '__main__':
    raw_user_train_data = read_raw_data("user")
    print(raw_user_train_data)
    pass