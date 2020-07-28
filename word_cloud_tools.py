import codecs
from datetime import date
from os import listdir
from os.path import isfile

import imageio
import jieba
import numpy as np
import pandas
from wordcloud import WordCloud, ImageColorGenerator

from conf_tools import get_conf

stopwords_filename = 'word_cloud/stopwords.txt'
font_filename = 'word_cloud/font.ttf'
template_filename = 'word_cloud/template.png'


def gen_word_cloud(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = '\n'.join(filter(None, (line.strip() for line in f)))
    with open(stopwords_filename, 'r', encoding='utf-8') as f:
        stopwords = set(filter(None, (line.strip() for line in f)))

    words = [
        word for seg in jieba.cut(content)
        if len(word := seg.strip().lower()) > 1 and word not in stopwords
    ]

    words_df = pandas.DataFrame({'word': words})
    words_stat = words_df.groupby(by=['word'])['word'].agg(np.size)
    words_stat = words_stat.to_frame()
    words_stat.columns = ['number']
    words_stat = words_stat.reset_index().sort_values(by="number",
                                                      ascending=False)
    print(len(words_stat), input_filename)

    b_img = imageio.imread(template_filename)
    seed = get_conf('random_seed')
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

    assert input_filename.endswith('txt')
    output_filename = input_filename[:-3] + 'png'
    print('Saving', output_filename)
    word_cloud.to_file(output_filename)


if __name__ == '__main__':
    log_dir = f"word_cloud/{str(date.today())}"
    for test_filename in listdir(log_dir):
        if test_filename.endswith('.txt'):
            gen_word_cloud(f'{log_dir}/{test_filename}')
