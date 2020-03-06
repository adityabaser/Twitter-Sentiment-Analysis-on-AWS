import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from twitter_file import TwitterClass

tw = TwitterClass()


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "devdb", table_name = "dev", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "devdb", table_name = "dev", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("sentiment", "long", "sentiment", "long"), ("twitterid", "long", "twitterid", "long"), ("tweet", "string", "tweet", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("sentiment", "long", "sentiment", "long"), ("twitterid", "long", "twitterid", "long"), ("tweet", "string", "tweet", "string")], transformation_ctx = "applymapping1")
## @type: DataSink
## @args: [connection_type = "s3", connection_options = {"path": "s3://group16-assignment-6/data_preprocess/dev"}, format = "json", transformation_ctx = "datasink2"]
## @return: datasink2
## @inputs: [frame = applymapping1]

def map_function(dynamicRecord):
    tweet = dynamicRecord["tweet"]
    features = tw.processed(tweet)
    dynamicRecord["features"] = features
    return dynamicRecord
map1 = Map.apply(frame = applymapping1, f = map_function, transformation_ctx = "map1")

datasink2 = glueContext.write_dynamic_frame.from_options(frame = map1, connection_type = "s3", connection_options = {"path": "s3://group16-assignment-6/data_preprocess/dev"}, format = "json", transformation_ctx = "datasink2")
job.commit()