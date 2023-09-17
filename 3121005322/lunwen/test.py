import string
import unittest

import jieba
import numpy as np


# 函数：对文本进行预处理和分词
def preprocess_and_tokenize(text):
    # 使用jieba分词进行预处理
    words = jieba.cut(text)
    return [word for word in words]


# 函数：计算两个文本之间的余弦相似度
def calculate_cosine_similarity(text1, text2):
    # 预处理和分词
    words1 = preprocess_and_tokenize(text1)
    words2 = preprocess_and_tokenize(text2)

    # 构建词频向量
    word_set = set(words1).union(set(words2))
    vector1 = [words1.count(word) for word in word_set]
    vector2 = [words2.count(word) for word in word_set]

    # 计算余弦相似度
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    else:
        return dot_product / (magnitude1 * magnitude2)


# 主函数：计算相似度并写入答案文件

def preprocess_text(text):
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    return text


class TestCosineSimilarityCalculation(unittest.TestCase):

    def test_identical_texts(self):
        text1 = "这是一个相同的文本。"
        text2 = "这是一个相同的文本。"
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_one_empty_text(self):
        text1 = "非空文本"
        text2 = ""
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.0, places=5)


    def test_same_word_order(self):
        text1 = "这是一个测试句子。"
        text2 = "一个测试句子这是。"
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_empty_and_nonempty_texts(self):
        text1 = ""
        text2 = "非空文本"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.0, places=5)

    def test_single_word_and_empty_text(self):
        text1 = "测试"
        text2 = ""
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.0, places=5)

    def test_similar_texts_with_repeating_words(self):
        text1 = "这是一个测试测试测试测试。"
        text2 = "这是一个测试测试测试测试。"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_very_short_texts(self):
        text1 = "短"
        text2 = "短"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_nonascii_characters(self):
        text1 = "这是一些非ASCII字符：öäü"
        text2 = "这是一些非ASCII字符：öäü"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_texts_with_newlines(self):
        text1 = "这是第一行。\n这是第二行。"
        text2 = "这是第一行。\n这是第二行。"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)



    def test_special_characters(self):
        text1 = "特殊字符测试%^&*"
        text2 = "特殊字符测试@#$%"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_repeated_words(self):
        text1 = "这是测试句子。" * 10
        text2 = "这是测试句子。" * 10
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    # Add more modified test cases

    def test_similar_empty_texts(self):
        text1 = "   "
        text2 = "   "
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_single_word_texts(self):
        text1 = "测试"
        text2 = "测试"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 1.0, places=5)

    def test_single_word_different_texts(self):
        text1 = "测试"
        text2 = "不同"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.0, places=5)

    def test_texts_with_multiple_languages(self):
        text1 = "This is a multilingual test."
        text2 = "这是一个多语言测试。"
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.0, places=5)


    def test_texts_with_different_languages(self):
        text1 = "这是一个中文文本。"
        text2 = "This is an English text."
        # 去除标点符号
        text1 = preprocess_text(text1)
        text2 = preprocess_text(text2)
        similarity = calculate_cosine_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.0, places=5)


if __name__ == '__main__':
    unittest.main()
