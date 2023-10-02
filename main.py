import underthesea
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
def extract_meaningful_phrases(text):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
   # Phân đoạn câu
    sentences = underthesea.sent_tokenize(text)

    # Tạo danh sách các cụm từ có nghĩa
    meaningful_phrases = []
    # Tạo danh sách các từ khóa
    keywords = []
    for sentence in sentences:

        # Encode văn bản thành mã UTF-8 trước khi sử dụng underthesea
        sentence_utf8 = sentence.encode('utf-8')

        # Phân đoạn câu thành các cụm từ có nghĩa (chunking)
        chunks = underthesea.chunk(sentence_utf8)

        # Tạo các cụm từ có nghĩa bằng cách kết hợp các từ trong cùng một chunk
        phrases = [' '.join(chunk) for chunk in chunks]

        # Thêm các cụm từ vào danh sách
        meaningful_phrases.extend(phrases)

        # Trích xuất từ khóa từ câu
        words = underthesea.word_tokenize(sentence_utf8)
        if isinstance(words, list):
            words = ' '.join(words)  # Chuyển danh sách thành chuỗi bằng cách nối các từ
        pos_tags = underthesea.pos_tag(words)
        for word, pos_tag in pos_tags:
            if pos_tag in ['N', 'Np', 'Nu', 'Ny', 'A']:  # Chọn danh từ và tính từ
                keywords.append(word)

    # Đếm số lần xuất hiện của từng cụm từ có nghĩa
    phrase_counts = Counter(meaningful_phrases)

    # Đếm số lần xuất hiện của từng từ khóa
    keyword_counts = Counter(keywords)


    return phrase_counts, keyword_counts




# Văn bản đầu vào
file_path = 'E:\\pythonProject\\Directory\\J.txt'
print("Văn bản gốc:")
print(file_path)

# Trích xuất cụm từ có nghĩa và đếm số lần xuất hiện
phrase_counts, keyword_counts = extract_meaningful_phrases(file_path )

# In danh sách từ khóa và số lần xuất hiện
print("Số lần xuất hiện của các từ khóa:")
for keyword, count in keyword_counts.items():
    print(f"{keyword}:{count}")



