# Classifies topic that the search query
# For example if input = "Donald Trump", classification = politics

from google.cloud import language


def classify(text):
    client = language.LanguageServiceClient.from_service_account_json("cloud_credentials.json")

    while len(text.split(" ")) <= 20:
        text += " " + text

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT,
        language="en")

    response = client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        result[category.name] = category.confidence

    return result


if __name__ == '__main__':
    result = classify("I like to eat ice cream.")
    if result:
        print(result)
