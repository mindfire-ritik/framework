import configparser
import os

configs = configparser.RawConfigParser()

# getting current working directory
final_path_directory = os.getcwd() + r"\utils\testdata.properties"
configs.read(final_path_directory)

