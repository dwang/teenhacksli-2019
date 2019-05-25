from flask import Flask
app = Flask(__name__)

import newspaper

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)

@app.route("/")
def index():
    article = cnn.articles[0]
    article.download()
    article.parse()
    article.nlp()
    return article.text

if __name__ == "__main__":
    app.run(debug=True)