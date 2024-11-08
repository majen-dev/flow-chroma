import sys
import os

# Add the project root to `sys.path`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bucketing_logic import create_bucket_column, create_bucket_column_pandas


import time


start = time.time()
create_bucket_column_pandas(
    "post_truncated.csv",
    "post_truncated_bucket.csv",
    [384, 512, 640, 768, 896, 1024],
    step=8,
    ratio_cutoff=2,
    height_col_name="image_height",
    width_col_name="image_width",
    chunksize=1000,
)
stop = time.time()

print(stop-start)
start = time.time()
create_bucket_column(
    "post_truncated.csv",
    "post_truncated_bucket.csv",
    [384, 512, 640, 768, 896, 1024],
    step=8,
    ratio_cutoff=2,
    height_col_name="image_height",
    width_col_name="image_width",
    bucket_col_name="bucket",
    return_bucket=False,
)
stop = time.time()
print(stop-start)