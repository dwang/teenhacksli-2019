import newspaper, basicWeather
import re
import string

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)
pattern = re.compile(r"[^a-zA-Z0-9-]")
count = 0

index = open("index.html", "w")
header = '<!doctype html><meta charset=utf-8><meta content="width=device-width,initial-scale=1,viewport-fit=cover" name=viewport><title>News</title><style>body{font-family:Arial,Helvetica,sans-serif;background-color:#fafafa}main{max-width:70ch;padding:2ch;margin:auto}.text{line-height:1.4}a{text-decoration:none;outline:0}</style><main>'
index.write(header + "<h1>Weather</h1>")
index.write("<p>" + basicWeather.getWeather() + "</p>")
index.write("<h1>Latest News</h1>")

for article in cnn.articles:
    try:
        article.download()
        article.parse()
        
        article_title = article.html.split('<h2 style="margin-top:0px;">')[1].split('</h2>')[0]
        file_name = pattern.sub('', article_title.replace(" ", "-")).lower() + ".html"
        
        with open("articles/" + file_name, 'w') as out:
            out.write(header + "<h1>" + article_title + "</h1> <br> <p class='text'>" + article.text + "</p>")

        index.write("<a href='articles/{}'>".format(file_name) + article_title + "</a><br><br>")

        count += 1
    except Exception as e:
        print(e)

index.close()