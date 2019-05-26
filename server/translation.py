from google.cloud import translate
import six

translate_client = translate.Client.from_service_account_json("cloud_credentials.json")
text = "how was your day"
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')
    

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
result = translate_client.translate(
    text, target_language= 'so')

print(u'Text: {}'.format(result['input']))
print(u'Translation: {}'.format(result['translatedText']))
print(u'Detected source language: {}'.format(
    result['detectedSourceLanguage']))