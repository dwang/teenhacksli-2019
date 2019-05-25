from flask import Flask
app = Flask(__name__)

import newspaper

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)

@app.route("/")
def index():
    toAdd = ""
    for article in cnn.articles:
        article.download()
        article.parse()
        article.nlp()
        toAdd += article.text
    return toAdd

if __name__ == "__main__":
    app.run(debug=True)
