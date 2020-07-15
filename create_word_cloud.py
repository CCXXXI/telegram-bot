import codecs
from datetime import date
from os import listdir
from os.path import isfile

import imageio
import jieba
import numpy as np
import pandas
from wordcloud import WordCloud, ImageColorGenerator

stopwords_filename = 'word_cloud/stopwords.txt'
font_filename = 'word_cloud/font.ttf'
template_filename = 'word_cloud/template.png'


def get_seed():
    with open('word_cloud_seed.txt') as seed_file:
        return int(seed_file.readline())


def gen(input_filename):
    content = '\n'.join([
        line.strip() for line in codecs.open(input_filename, 'r', 'utf-8')
        if len(line.strip()) > 0
    ])
    stopwords = set([
        line.strip() for line in codecs.open(stopwords_filename, 'r', 'utf-8')
    ])

    segs = jieba.cut(content)
    words = []
    for seg in segs:
        word = seg.strip().lower()
        if len(word) > 1 and word not in stopwords:
            words.append(word)

    words_df = pandas.DataFrame({'word': words})
    words_stat = words_df.groupby(by=['word'])['word'].agg(np.size)
    words_stat = words_stat.to_frame()
    words_stat.columns = ['number']
    words_stat = words_stat.reset_index().sort_values(by="number",
                                                      ascending=False)
    print(len(words_stat), input_filename)

    input_prefix = input_filename
    if input_filename.find('.') != -1:
        input_prefix = '.'.join(input_filename.split('.')[:-1])

    if isfile(template_filename):
        b_img = imageio.imread(template_filename)
        seed = get_seed()
        print(f'{seed=}')
        word_cloud = WordCloud(
            font_path=font_filename,
            background_color='white',
            mask=b_img,
            max_font_size=500,
            random_state=seed,
            prefer_horizontal=1,
        )
        word_cloud = word_cloud.fit_words(
            dict(words_stat.head(100).itertuples(index=False)))

        b_img_colors = ImageColorGenerator(b_img)
        word_cloud.recolor(color_func=b_img_colors)

        output_filename = input_prefix + '.png'

        print('Saving', output_filename)
        word_cloud.to_file(output_filename)


if __name__ == '__main__':
    log_dir = f"word_cloud/{str(date.today())}"
    for f in listdir(log_dir):
        if f.endswith('.txt'):
            gen(f'{log_dir}/{f}')
