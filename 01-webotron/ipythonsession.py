import boto3

session = boto3.Session(profile_name='alexa-info-isengard')
s3 = session.resource('s3')

