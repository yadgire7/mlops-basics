# import required libraries
import os
import pandas as pd
import yaml
import argparse

def read_params(config_path):
    with open("params.yaml", "r") as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# method to get data
def get_data(config_path):
    config = read_params(config_path)
    data_path = config['data_source']['s3_source']
    df = pd.read_csv(data_path, sep=";", encoding='utf-8')
    return df

# adding sample comment

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default= "params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)


