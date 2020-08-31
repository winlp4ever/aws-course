import boto3
import json

class AwsComprehend:
    def __init__(self):
        self.cph = boto3.client(service_name='comprehend', region_name='eu-west-2')

    def detectLanguage(self, s):
        data = self.cph.detect_dominant_language(Text=s)
        print(json.dumps(data, indent=4))
        return data['Languages'][0]['LanguageCode']

    def extractKeyphrases(self, s, lang='en'):
        data = self.cph.detect_key_phrases(Text=s, LanguageCode=lang)    
        res = []
        for p in data['KeyPhrases']:
            res.append(p['Text'])
        return '\n'.join(res)
    def detectSentiment(self, s, lang='en'):
        data = self.cph.detect_sentiment(Text=s, LanguageCode=lang)
        print(json.dumps(data, indent=4))


if __name__ == '__main__':
    ac = AwsComprehend()        
    text = '''
    Yet three times he has been passed over for brigadier general, a prominent one-star rank that would put Colonel Henderson on the path to the top tier of Marine Corps leadership. Last year, the Navy secretary, Richard V. Spencer, even added a handwritten recommendation to Colonel Henderson’s candidacy: “Eminently qualified Marine we need now as BG,” he wrote.
    '''
    print(ac.detectLanguage(text))
    print(ac.extractKeyphrases(text, lang='fr'))
    print(ac.detectSentiment(text))