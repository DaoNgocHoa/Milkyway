import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import nltk


text = open('E:\\pythonProject\\T.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, 'english')

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []
with open('Directory/emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    compound = score['compound']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibe")

    labels = ['Neg', 'Neu', 'Pos', 'Comp ']
    values = [neg, neu, pos, compound]
    plt.bar(labels, values)
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Score')

    plt.xticks(rotation=45, ha='right')

    plt.show()


sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
