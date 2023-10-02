import underthesea
import yake

# Bước 1: Sử dụng Underthesea để phân đoạn văn bản và trích xuất các cụm từ có nghĩa
text = "TextRank là một thuật toán được sử dụng trong xử lý ngôn ngữ tự nhiên (NLP) để trích xuất các từ khóa hoặc tóm tắt văn bản. Nó dựa trên ý tưởng của PageRank, thuật toán được sử dụng bởi Google để xếp hạng các trang web trên Internet. TextRank được áp dụng cho việc xác định tính quan trọng của các từ hoặc cụm từ trong văn bản dựa trên mối liên quan của chúng đến các từ hoặc cụm từ khác trong văn bản."
sentences = underthesea.sent_tokenize(text)
meaningful_phrases = []
# Tải danh sách từ ngừng tiếng Việt từ một URL
stopwords_file_path = "E:\\pythonProject\\Stopwords.txt"
# Đọc tệp từ điển stop words và tạo danh sách
with open(stopwords_file_path, 'r', encoding='utf-8') as file:
    stopwords_vi = [line.strip() for line in file]

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
            if word not in stopwords_file_path:  # Kiểm tra từ khóa có trong stopwords không
                meaningful_phrases.append(word)

# Bước 2: Kết hợp các cụm từ có nghĩa thành một chuỗi văn bản duy nhất
combined_text = ' '.join(meaningful_phrases)

# Bước 3: Sử dụng YAKE để trích xuất từ khóa từ chuỗi văn bản duy nhất
language = "vi"
max_ngram_size = 2
deduplication_threshold = 0.5
yake_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=20, features=None)
keywords = yake_extractor.extract_keywords(combined_text)


# Bước 4: In ra các từ khóa và chỉ số tương ứng
for score, keyword in keywords:
    print(f"{keyword}: {score}")



