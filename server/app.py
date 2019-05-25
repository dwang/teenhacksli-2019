from flask import Flask
app = Flask(__name__)

import newspaper

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)

@app.route("/")
def index():
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

if __name__ == "__main__":
    app.run(debug=True)
