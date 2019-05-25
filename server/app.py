from flask import Flask
app = Flask(__name__)

import newspaper

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)

@app.route("/")
def index():
<<<<<<< HEAD
    toAdd = ""
    for article in cnn.articles:
        article.download()
        article.parse()
        article.nlp()
        toAdd += article.text
    return toAdd
=======
    article = cnn.articles  
    count = 0
    print(len(cnn.articles))
    for i in article:
        file = open("article" + str(count), 'w')
        article[count].download()
        article[count].parse()
        article[count].nlp()
        file.write(cnn.articles[count].text)
        file.close()
        count += 1

    return "200"
>>>>>>> aae7cbde0db4169d1e464018cefa44d7ff14a976

if __name__ == "__main__":
    app.run(debug=True)
