# Twitter-Sentiment-Analysis-on-AWS

Preprocessing Library: Contains the code to preprocess a raw tweet and return features.

Glue Spark Code: Directory containing files to generate JSON files from the csv data

CNN Model: Code to run the model

SageMaker: Code to read the data from ASW S3 bucket and train the CNN model

Lambda function: AWS function to test the sentiment of a tweet in real-time

Deploy the lambda function and with the REST API Gateway, host the model to run it remotely using the Invoke URL

Embedding dict: https://twittera6.s3.amazonaws.com/parent_folder/embedding_list/glove.txt


Train: https://twittera6.s3.amazonaws.com/parent_folder/train/train.json

Dev: https://twittera6.s3.amazonaws.com/parent_folder/dev/dev.json

Eval: https://twittera6.s3.amazonaws.com/parent_folder/eval/eval.json


Model: https://twittera6.s3.amazonaws.com/parent_folder/model127.tar.gz
