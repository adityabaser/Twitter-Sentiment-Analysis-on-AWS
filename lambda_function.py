import json
import boto3
import time
import datetime


from twitter_file import TwitterClass
tw = TwitterClass()

sage_maker_client = boto3.client("runtime.sagemaker")


def lambda_handler(event, context): 

    now = datetime.datetime.now()
    Date_and_Time = str(now)


    initial_time = time.time_ns()

    tweet = event["tweet"]
    features = tw.processed(tweet)
   
    final_time  = time.time_ns()
    Preprocessing_time = final_time-initial_time
    print('Preprocessing time:',Preprocessing_time)

    model_payload = {
        'embedding_input': features,
    }

    model_initial_time= time.clock()
    
    model_response = sage_maker_client.invoke_endpoint(
        EndpointName="sentiment-model",
        ContentType="application/json",
        Body=json.dumps(model_payload))
    
    model_final_time= time.clock()
    model_inf_time = model_final_time - model_initial_time
    print('Model inference time:',model_inf_time)   
    

    result = json.loads(model_response["Body"].read().decode())
    
    response = {}
    
    response["tweet"] = tweet

    if result["predictions"][0][0] >= 0.5:
        response["sentiment"] = "positive"
    else:
        response["sentiment"] = "negative"
    
    response['Date_and_Time'] = Date_and_Time
    response['Preprocessing_time in nanoseconds'] = Preprocessing_time
    response['model_inf_time in seconds'] = model_inf_time
    response['probability'] = result["predictions"][0][0]
    
    
    print ("Result: " + json.dumps(response, indent = 2))
    # TODO implement
    return response