import boto3
import time 
import json
import urllib

s3 = boto3.resource('s3')

filename = 'reflection.mp3'
bucket_name = 'my-music-123'

# upload file to s3
data = open('reflection.mp3', 'rb')
s3.Bucket(bucket_name).put_object(Key=filename, Body=data, ContentType='audio/mp3')
data.close()

job_name = 'transcript'
job_uri = 'https://s3.amazonaws.com/%s/%s' % (bucket_name, filename)

# init transcribe client
transcribe = boto3.client('transcribe', region_name='eu-west-3')
# launch transcription job
transcribe.start_transcription_job(TranscriptionJobName=job_name, Media={'MediaFileUri': job_uri}, MediaFormat='mp3', LanguageCode='en-US')

# track the process
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(2)
print(status)

# print out the results
if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    response = urllib.request.urlopen(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
    data = json.loads(response.read())
    print(json.dumps(data, indent=4))
    text = data['results']['transcripts'][0]['transcript']
    print(text)

# delete job
transcribe.delete_transcription_job(TranscriptionJobName=job_name)