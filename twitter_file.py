"""
Pre processing
"""

import re
import os
import zipfile


from nltoolkit import TweetTokenizer



class TwitterClass:
    """
    Generates padded embeddings of tweet
    """
    def __init__(self, max_length_tweet=50, max_length_dictionary=100000):

        """
        Initialize class
        :param max_length_tweet:
        :param max_length_dictionary:
        :param embeddings_dict:
        :param file_path
        """
        self.max_length_tweet = max_length_tweet
        self.max_length_dictionary = max_length_dictionary


        #importing word_list
        file_path = './word_list.txt'
        # if ".zip/" in file_path:
        #     archive_path = os.path.abspath(file_path)
        #     split = archive_path.split(".zip/")
        #     archive_path = split[0] + ".zip"
        #     path_inside = split[1]
        #     archive = zipfile.ZipFile(archive_path, "r")
        #     self.embeddings = archive.read(path_inside).decode("utf8").split("\n")
        #     self.embeddings = self.embeddings[:max_length_dictionary]

        # else:
        self.embeddings = open(file_path, 'r', encoding="utf-8").read().split("\n")

        self.tokenizer = TweetTokenizer()



    @staticmethod
    def remove_stop_words(tweet):
        """
        Remove stopwords
        """

        file_path = './english'
        # if ".zip/" in file_path:
        #     archive_path = os.path.abspath(file_path)
        #     split = archive_path.split(".zip/")
        #     archive_path = split[0] + ".zip"
        #     path_inside = split[1]
        #     archive = zipfile.ZipFile(archive_path, "r")
        #     stopwords = archive.read(path_inside).decode("utf8").split("\n")

        # else:
        stopwords = []
        with open("english") as files:
            for line in files:
                values = line.split()
                word = values[0]
                stopwords.append(word)
        # stop_words = set(stopwords.words('english'))
        pattern = re.compile(r'\b(' + r'|'.join(stopwords) + r')\b\s*')
        tweet = pattern.sub('', tweet)
        return tweet

    def clean_text(self, tweet):
        """
        Clean text
        """

        # URL
        tweet = re.sub(r"(www|http)\S+", " ", tweet)
        tweet = tweet.lower()

        # Numbers
        tweet = re.sub(r"[0-9]+", '', tweet)

        # Stopwords
        tweet = self.remove_stop_words(tweet)

        # Removing #
        tweet = re.sub(r"#", '', tweet)

        # Removing handle
        tweet = re.sub(r"@[a-zA-Z0-9]+", '', tweet)

        return tweet


    def tokenize_text(self, tweet):

        """
        Tokenize
        """

        return self.tokenizer.tokenize(tweet)

    def replace_token_with_index(self, token_list):
        """
        Replace token
        """
        index_list = []
        for token in token_list:
            try:
                token_index = self.embeddings.index(token)
                index_list.append(token_index)
            except ValueError:
                embed = self.embeddings.index('<unknown>')
                index_list.append(embed)
        return index_list


    def pad_sequence(self, index_list):
        """
        Pad tokenized sequence
        """
        length = len(index_list)

        if length < self.max_length_tweet:
            req_d = self.max_length_tweet - length
            pad = [self.embeddings.index('<pad>')]
            index_list.extend(pad*req_d)
            token_pad = index_list

        elif length > self.max_length_tweet:
            token_pad = index_list[:self.max_length_tweet]

        else:
            token_pad = index_list

        return token_pad

    def processed(self, tweet):
        """
        Function to return final output
        """
        cleaned = self.clean_text(tweet)
        tokens = self.tokenize_text(cleaned)
        embeddings = self.replace_token_with_index(tokens)
        padded = self.pad_sequence(embeddings)

        return padded




# # # file_path = "glove_1.txt"
#tweet = "Namo faces shameful loss in elections."
#TW = TwitterClass()
#print (TW.processed(tweet))


# print (self.embeddings)
#
# print(TW.pad_sequence(TW.replace_token_with_index(TW.tokenize_text \

# (TW.clean_text("Hi Namo wins")))))
