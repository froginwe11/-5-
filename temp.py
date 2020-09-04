# -*- encoding: utf-8 -*-
"""
@File    :   test.py
@Author  :   Joshua
@Contact :   froginwe11@163.com
@Time    :   2020/09/04 10:41:34
@Desc    :   
"""
import json
import re
import pathlib
basedir = pathlib.Path(__file__).parent.parent

print(basedir.absolute())
a = sorted(list(basedir.glob('day*.ipynb')),
           key=lambda x: int(re.search(r"day(\d+)", x.name).group(1)))

for num, i in enumerate(a, start=2):
    f = open(i.absolute(), encoding='utf-8')
    ipynb_old = json.load(f)
    f.close()
    ipynb_old['cells'].insert(1, {
        "cell_type": "markdown",
        "metadata": {
            "slideshow": {
                "slide_type": "slide"
            }
        },
        "source": [
            "<https://www.bilibili.com/video/BV1ht4y1D7H9?p={}>\n".format(num)
        ]
    })
    f = open(i.absolute(), 'w', encoding='utf-8')
    json.dump(ipynb_old, f, ensure_ascii=False)
    f.close()
    print(i.name)
