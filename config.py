""" Stores settings for the app """
DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP = os.path.join(BASE_DIR, 'app')
STATIC = os.path.join(APP, 'static')
INPUT_FILE = os.path.join(STATIC, 'movies.csv')
OUTPUT_FILE = os.path.join(STATIC, 'dump')
