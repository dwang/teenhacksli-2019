import newspaper
import basic_weather
import content_classification
import datetime
import re
import string

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)
pattern = re.compile(r"[^a-zA-Z0-9-]")
allowed_categories = ['Jobs & Education', 'Law & Government', 'News', 'Business & Industrial', 'People & Society', 'Finance', 'Health']

header = '<!doctype html><meta charset=utf-8><meta content="width=device-width,initial-scale=1,viewport-fit=cover" name=viewport><title>MirrorDashboard</title><style>body{font-family:Arial,Helvetica,sans-serif;background-color:#fafafa}main{max-width:70ch;padding:2ch;margin:auto}.text{line-height:1.4}a{text-decoration:none;outline:0}</style></head><main><h1><a href="/index.html">MirrorDashboard</a></h1><br>'

index = open("index.html", "w")
index.write(header + '<h1><a href="weather.html">Weather</a></h1>')

weather = open("weather.html", "w")
weather.write(header + "<h1>Weather</h1><p>" + basic_weather.get_weather() + "</p></main></body></html>")

news = open('news.html','w')
news.write(header + "<h1>Latest News</h1>")

index.write('<h1><a href="news.html">Latest News</a></h1> <h1> <a href="firstaid.html">First Aid</a></h1>')

with open('firstaid.html', 'w') as f:
    with open('firstaid.txt', 'r') as txt:
        f.seek(0, 0)
        f.write(header.rstrip('\r\n') + '\n' + txt.read())

count = 0

for article in cnn.articles:
    try:
        article.download()
        article.parse()

        article_title = article.html.split('<h2 style="margin-top:0px;">')[1].split('</h2>')[0]
        article_text = article.html.split('</div><div><p>')[1].split('</p></div></div>')[0]

        print("[{} / {}] {}".format(count, len(cnn.articles) - 3, article_title))

        count += 1

        category = list(content_classification.classify(article_text).keys())[0].split("/")[1]
        if category not in allowed_categories:
            continue

        file_name = pattern.sub('', article_title.replace(" ", "-")).lower() + ".html"

        with open("articles/" + file_name, 'w') as out:
            out.write(header + "<h1>" + article_title + "</h1><br><p class='text'>" + article_text + "</p></main></body></html>")

        news.write("<a href='articles/{}'>".format(file_name) + article_title + "</a><br><br>")
    except Exception as e:
        pass

index.write("<h3>Last Updated: " + datetime.datetime.now().strftime("%b %d %Y %I:%M:%S") + "</h3></main></body></html>")
index.close()

news.write("</main></body></html>")
news.close()
