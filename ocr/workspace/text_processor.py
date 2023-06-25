import pandas as pd
import numpy as np
import nltk
import spacy
import gensim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


class TextProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def process_text(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        spacy.cli.download('pl_core_news_sm')
        stop_words = nltk.corpus.stopwords.words('polish')
        nlp = spacy.load('pl_core_news_sm')
        df = pd.DataFrame(columns=['text'])
        for file_path in glob.glob(os.path.join(self.folder_path, '*.txt')):
            with open(file_path, 'r') as text_file:
                text = text_file.read()
                doc = nlp(text)
                lemmas = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
                df = df.append({'text': ' '.join(lemmas)}, ignore_index=True)
        vectorizer = CountVectorizer(stop_words=stop_words)
        X = vectorizer.fit_transform(df['text'])
        lda = LatentDirichletAllocation(n_components=10, random_state=42)
        lda.fit(X)
        for idx, topic in enumerate(lda.components_):
            print(f'Topic {idx}:')
            print([vectorizer.get_feature_names()[i] for i in topic.argsort()[-10:]])
            print('\n')
