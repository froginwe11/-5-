# -*- encoding: utf-8 -*-
"""
@File    :   generate.py
@Author  :   Joshua
@Contact :   froginwe11@163.com
@Time    :   2020/08/12 16:18:52
@Desc    :   
"""
import json
from copy import deepcopy
from random import shuffle
from utils.fanyi import iciba

ipynb_format = {
    "cells": [
    ],
    "metadata": {
        "celltoolbar": "幻灯片",
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}


with open('./english.txt', encoding='utf-8') as f:
    text = f.read()

engs = text.split('\n')

shuffle(engs)

for day, i in enumerate(range(0, len(engs), 5), start=1):
    ipynb = deepcopy(ipynb_format)
    cells = [{
        "cell_type": "markdown",
        "metadata": {
            "slideshow": {
                "slide_type": "slide"
            }
        },
        "source": [f'# Day{day}\n']
    }]

    for eng in engs[i:i+5]:
        cells.append(iciba(eng))

    cells.append({
        "cell_type": "markdown",
        "metadata": {
            "slideshow": {
                "slide_type": "slide"
            }
        },
        "source": ['# 回顾\n', '\n', '**暂停5秒，回想一下我们今天所学的单词**\n']
    })
    cells.append({
        "cell_type": "markdown",
        "metadata": {
            "slideshow": {
                "slide_type": "slide"
            }
        },
        "source": ['**准备好了吗?**\n']
    })
    cells.append({
        "cell_type": "markdown",
        "metadata": {
            "slideshow": {
                "slide_type": "slide"
            }
        },
        "source": [f'{index}. {eng}\n' for index, eng in enumerate(engs[i:i+5], start=1)]
    })
    ipynb['cells'] = cells

    with open(f'day{day}.ipynb', 'w', encoding='utf-8') as f:
        f.write(json.dumps(ipynb, indent=2, ensure_ascii=False))

    print(f'day{day}.ipynb')
