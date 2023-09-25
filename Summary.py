import nltk
from pytorch_lightning.utilities.model_summary import summarize

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import urllib.request
from summarizer import Summarizer
from collections import defaultdict

# Tải danh sách từ ngừng tiếng Việt từ một URL
url = "https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/master/vietnamese-stopwords.txt"
response = urllib.request.urlopen(url)
stopwords_vi = set(response.read().decode("utf-8").splitlines())
stopwords_en = set(stopwords.words('english'))
file_path = "E:\\pythonProject\\Directory\\T.txt"
try:
    # Mở tệp văn bản .txt trong chế độ đọc (read)
    with open(file_path, "r", encoding="utf-8") as file:
        # Đọc nội dung của tệp và lưu vào biến content
        content = file.read()
        # In nội dung ra màn hình
        print("Nội dung tệp văn bản:")
        print(content)
except FileNotFoundError:
    print(f"Tệp {file_path} không tồn tại.")
except Exception as e:
    print(f"Lỗi: {str(e)}")
# In danh sách từ ngừng
#print("Danh sách từ ngừng tiếng Việt:")


# Loại bỏ các từ ngừng từ văn bản
text = "Đây là một ví dụ về cách loại bỏ các từ ngừng từ văn bản tiếng Việt."
words = content.split()
filtered_words = [word for word in words if word.lower() not in stopwords_vi]
print(text)
# In văn bản đã loại bỏ từ ngừng
filtered_text = " ".join(filtered_words)
print("Văn bản sau khi loại bỏ từ ngừng:")
print(filtered_text)



#tom tat van ban
text_to_summarize = content

model = Summarizer()

summary = model(text_to_summarize)

print("Tóm tắt văn bản:")
print(summary)

# Đọc văn bản từ một tệp
with open("E:\\pythonProject\\Directory\\T.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Tách văn bản thành danh sách các từ
words = content.split()

# Tạo danh sách từ ngừng tiếng Việt (ví dụ)
english_stopwords = set(stopwords.words('english'))

# Tạo từ điển để lưu số lần xuất hiện của các từ
word_count_dict = defaultdict(int)

# Đếm số lần xuất hiện của các từ (loại bỏ từ ngừng)
for word in words:
    # Loại bỏ các ký tự đặc biệt và chuyển thành chữ thường để tránh phân biệt in hoa và thường


    # Kiểm tra xem từ có trong danh sách từ ngừng không
    if word not in english_stopwords:
        word_count_dict[word] += 1

# In ra các từ xuất hiện nhiều nhất (top 10 ví dụ)
top_words = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 từ xuất hiện nhiều nhất (loại bỏ từ ngừng):")
for word, count in top_words:
    print(f"Từ '{word}' xuất hiện {count} lần trong văn bản.")

