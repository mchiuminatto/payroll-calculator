import os
from pathlib import PurePath

ROOT_DIR_APP: str = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR: str = str(PurePath(ROOT_DIR_APP).parent)
TEST_RECORDS = 10000
DECIMAL_PLACES = 1