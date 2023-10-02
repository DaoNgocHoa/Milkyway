import underthesea
from collections import Counter
import networkx as nx

# Văn bản đầu vào
text = "Tôi đã sử dụng một thuật toán trích xuất từ khóa để xác định các từ khóa quan trọng từ văn bản của bạn. Thuật toán này dựa trên các yếu tố như tần suất xuất hiện và vị trí của các từ trong văn bản. Các từ khóa quan trọng được chọn dựa trên những yếu tố này. Dựa trên danh sách các từ khóa bạn đưa ra, có vẻ như thuật toán đã hoạt động tốt trong việc xác định các từ khóa quan trọng từ văn bản của bạn."

# Phân đoạn văn bản thành các câu
sentences = underthesea.sent_tokenize(text)

# Khởi tạo một đồ thị để ánh xạ mối quan hệ giữa các cụm từ
G = nx.Graph()

# Tạo danh sách các từ khóa và tần suất xuất hiện
keywords = []

for sentence in sentences:
    words = underthesea.word_tokenize(sentence)
    keywords.extend(words)

# Tính tần suất xuất hiện của các từ khóa
keyword_freq = Counter(keywords)

# Tạo các cạnh giữa các từ khóa trong đồ thị
for keyword1 in keyword_freq:
    for keyword2 in keyword_freq:
        if keyword1 != keyword2:
            G.add_edge(keyword1, keyword2, weight=keyword_freq[keyword1] * keyword_freq[keyword2])

# Sử dụng TextRank để tìm ra các từ khóa quan trọng
keywords_textrank = nx.pagerank(G, weight='weight')

# Sắp xếp các từ khóa theo xếp hạng giảm dần
sorted_keywords = sorted(keywords_textrank.items(), key=lambda x: x[1], reverse=True)

# Lấy ra các từ khóa quan trọng (ví dụ: top 5 từ khóa)
top_keywords = [keyword for keyword, score in sorted_keywords[:5]]

# In ra câu chủ đề
topic_sentence = "Câu chủ đề: " + ", ".join(top_keywords)
print(topic_sentence)