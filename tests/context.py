import os
import sys

# Temporarily add the repo root to your $PATH
FILE_BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.dirname(FILE_BASE_PATH))
sys.path.insert(0, ROOT_PATH)

from libsongtext import errors, songtext
