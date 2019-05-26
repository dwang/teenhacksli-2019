import newspaper, basicWeather, content_classification, datetime
import re
import string

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)
pattern = re.compile(r"[^a-zA-Z0-9-]")
allowed_categories = ['Jobs & Education', 'Law & Government', 'News', 'Business & Industrial', 'People & Society', 'Finance', 'Health']
count = 0
today = datetime.datetime.now()
index = open("index.html", "w")
header = '<!doctype html><meta charset=utf-8><meta content="width=device-width,initial-scale=1,viewport-fit=cover" name=viewport><title>News</title><style>body{font-family:Arial,Helvetica,sans-serif;background-color:#fafafa}main{max-width:70ch;padding:2ch;margin:auto}.text{line-height:1.4}a{text-decoration:none;outline:0}</style><main>'
index.write(header)
index.write("<h1>Weather</h1>")
index.write("<p>" + basicWeather.getWeather() + "</p>")
index.write("<h1>Latest News</h1>")

for article in cnn.articles:
    try:
        article.download()
        article.parse()

        article_title = article.html.split('<h2 style="margin-top:0px;">')[1].split('</h2>')[0]
        article_text = article.html.split('</div><div><p>')[1].split('</p></div></div>')[0]

        category = list(content_classification.classify(article_text).keys())[0].split("/")[1]
        if category not in allowed_categories:
            continue

        file_name = pattern.sub('', article_title.replace(" ", "-")).lower() + ".html"

        with open("articles/" + file_name, 'w') as out:
            out.write(header + "<h1>" + article_title + "</h1> <br> <p class='text'>" + article_text + "</p>")

        index.write("<a href='articles/{}'>".format(file_name) + article_title + "</a><br><br>")

        count += 1
    except Exception as e:
        print(e)

index.write("<h3>Last Updated: " + today.strftime("%b %d %Y %I:%M:%S") + "</h3>")
index.write("</main></body></html>")
index.close()
