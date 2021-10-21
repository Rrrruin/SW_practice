# -*- coding: utf-8 -*-
# @Time : 2021/10/18 7:22 下午
# @Author : Ruin
# @Email : wangkairui0108@gmail.com
# @File : test_pd.py
# @software : PyCharm

import pandas as pd

data = {
    'name': ['paper1', 'paper2'],
    'content': ['ajkshdksahdkuhasdlkjhaskdhjkajvsgdaiuv gi', 'hsakduha isuhdvk g aiugf gfa']
}

df = pd.DataFrame(data)

list_ = df['content']
print(type(list_[0]))
