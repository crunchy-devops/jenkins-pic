#! /usr/bin/python

import boto3

# get S3
# resource
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


# create a bucket
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='mybucket')

# write a bucket
data = open('test.jpg', 'rb')
s3.Bucket('mybucket').put_object(Key="test.jpg",Body=data)