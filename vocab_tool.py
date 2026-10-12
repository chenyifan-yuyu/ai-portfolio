# -*- coding: utf-8 -*-
# vocab_tool.py 生词表小工具

import csv

def load_words(filename):
    words = []
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            words.append(row)
    return words

def filter_by_level(words, level):
    result = []
    for w in words:
        if w['HSK等级'] == str(level):
            result.append(w)
    return result

def count_by_pos(words):
    stats = {}
    for w in words:
        pos = w['词性']
        if pos in stats:
            stats[pos] = stats[pos] + 1
        else:
            stats[pos] = 1
    return stats

def gen_exercises(words, out_file):
    lines = []
    for w in words:
        word = w['词汇']
        pos = w['词性']
        lines.append('用“{}”造一个句子。({})'.format(word, pos))
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == '__main__':
    all_words = load_words('data/生词表.csv')
    print('一共读入生词：', len(all_words), '个')
    lv3 = filter_by_level(all_words, 3)
    print('HSK3级生词：', len(lv3), '个')
    pos_stats = count_by_pos(all_words)
    print('词性分布：', pos_stats)
    gen_exercises(all_words, '练习.txt')
    print('练习题已生成：练习.txt')
