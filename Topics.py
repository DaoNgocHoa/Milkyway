import gensim
import spacy
from gensim import corpora, models
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



# Văn bản mẫu
text = "E:\\pythonProject\\T.txt"

with open(text, "r", encoding="utf-8") as file:
    # Đọc nội dung của tệp và lưu vào biến content
    content = file.read()
    print("Nội dung tệp văn bản:")
    print(content)

# Tách từ và loại bỏ stopwords
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text)
words = content.split()
filtered_tokens = [word for word in words if word.lower() not in stop_words]

# In văn bản đã loại bỏ từ ngừng
filtered_text = " ".join(filtered_tokens)
print("Văn bản sau khi loại bỏ từ ngừng:")
print(filtered_text)
# Tạo từ điển từ vựng
dictionary = corpora.Dictionary([filtered_tokens])

# Tạo corpus (tập hợp các tài liệu)
corpus = [dictionary.doc2bow(filtered_tokens)]

# Xây dựng mô hình LDA
lda_model = gensim.models.LdaModel(corpus, num_topics=1, id2word=dictionary, passes=15)

# Trích xuất câu chủ đề
topic = lda_model.show_topic(0)
print("Câu chủ đề: ", topic)