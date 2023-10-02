from collections import Counter

import underthesea
import re
# Văn bản đầu vào
file_path = "E:\\pythonProject\\Directory\\J.txt"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("Nội dung tệp văn bản:")
    print(content)

# Phân đoạn văn bản thành các câu
sentences = underthesea.sent_tokenize(content)

# Tải danh sách từ dừng tiếng Việt từ một nguồn nào đó, ví dụ từ một tệp tin
stopwords = set()
with open("E:\\pythonProject\\Stopwords.txt", "r", encoding="utf-8") as file:
    stopwords.update(file.read().splitlines())

# Khởi tạo danh sách để lưu trữ từ khóa
keywords = []

# Loại bỏ các ký tự dấu và trích xuất từ khóa từ mỗi câu
for sentence in sentences:
    # Loại bỏ các ký tự dấu (chấm, phẩy, ngoặc, dấu cách dư thừa, v.v.) bằng biểu thức chính quy
    sentence_cleaned = re.sub(r'[.,();:\[\]{}!?\\\-+*/"]', '', sentence)

    # Phân đoạn câu đã được làm sạch thành các từ
    words = underthesea.word_tokenize(sentence_cleaned)

    # Trích xuất từ khóa từ mỗi câu và loại bỏ các từ dừng
    for word in words:
        if word not in stopwords:
            keywords.append(word)

# Thống kê số lần xuất hiện của từng từ khóa
keyword_counts = Counter(keywords)


sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

top_keywords = sorted_keywords[:15]
# In ra danh sách các từ khóa
print("Danh sách các từ khóa:")
for keyword, count in top_keywords:  # Lấy 10 từ khóa xuất hiện nhiều nhất
    print(f"{keyword}: {1/count}")

