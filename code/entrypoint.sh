#!/bin/sh

set -e

python -m pip install sklearn #在doker环境下下载需要用到的机器学习库sklearn
python /code/test1.py #打开code文件夹，在docker环境下运行test1.py文件
