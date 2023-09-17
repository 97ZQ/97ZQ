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
def main(orig_file, plagiarized_file, answer_file):
    try:
        # 读取原文和抄袭版论文
        with open(orig_file, "r", encoding="utf-8") as orig_file:
            original_text = orig_file.read()

        with open(plagiarized_file, "r", encoding="utf-8") as plagiarized_file:
            plagiarized_text = plagiarized_file.read()

        # 计算重复率
        similarity = calculate_cosine_similarity(original_text, plagiarized_text)

        # 将结果写入答案文件
        with open(answer_file, "a", encoding="utf-8") as answer_file:
            answer_file.write("{}和{}的相似度是{:.2f}\n".format(orig_file, plagiarized_file, similarity))
    except FileNotFoundError as e:
        print(f"Error: {e}. Please provide valid file paths.")
    except UnicodeDecodeError as e:
        print(f"Error: Unable to decode file with specified encoding. {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import sys

    # 获取命令行参数
    if len(sys.argv) != 4:
        print("Usage: python main.py [原文文件] [抄袭版论文的文件] [答案文件]")
        sys.exit(1)

    orig_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    answer_file = sys.argv[3]
    main(orig_file, plagiarized_file, answer_file)
