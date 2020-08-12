# -*- encoding: utf-8 -*-
"""
@File    :   fanyi.py
@Author  :   Joshua
@Contact :   froginwe11@163.com
@Time    :   2020/08/12 13:41:12
@Desc    :   
"""
import re
import requests
from requests_html import HTMLSession


def simple(eng):
    res = requests.post('https://fanyi.baidu.com/sug',
                        data={'kw': eng})
    for i in res.json()['data']:
        if i['k'] == eng:
            pos = re.findall(r'[a-z]+\. ', i['v'])
            mean = [i for i in re.split(r'[a-z]+\. ', i['v']) if i]
            return '\n'.join([p+m for p, m in zip(pos, mean)])


def iciba(eng, sentence_len=2):
    source = []
    session = HTMLSession()
    res = session.get(f'http://www.iciba.com/word?w={eng}')
    symbols = [re.sub(r'([\[\]])', r'\\\1', i.text) for i in res.html.xpath(
        '//ul[@class="Mean_symbols__5dQX7"]/li')]
    means = [i.text.replace('\n', ' ') for i in res.html.xpath(
        '//ul[@class="Mean_part__1RA2V"]/li')]
    sentences = [i.text.split('\n')[:2] for i in res.html.xpath(
        '//div[@class="NormalSentence_sentence__3q5Wk"]')[:sentence_len]]

    source.extend([f'# {eng}\n', '\n'])
    source.extend([' '.join(symbols)+'\n', '\n'])
    source.extend([f"**[释义](https://fanyi.baidu.com/#en/zh/{eng})**\n", '\n'])
    for mean in means:
        source.extend([mean+'\n', '\n'])
    source.extend(["**例句**：\n", '\n'])
    for sentence in sentences:
        source.extend([f'{sentence[0]}  \n', f'{sentence[1]}\n', '\n'])
    

    return {
        "cell_type": "markdown",
        "metadata": {
            "slideshow": {
                "slide_type": "slide"
            }
        },
        "source": source
    }


if __name__ == '__main__':
    # print(simple('book'))
    # print(simple(input()))
    print(iciba('critical'))
