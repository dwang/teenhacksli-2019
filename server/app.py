import newspaper, basicWeather, content_classification, datetime
import re
import string

cnn = newspaper.build("https://lite.cnn.io", memoize_articles=False)
pattern = re.compile(r"[^a-zA-Z0-9-]")
allowed_categories = ['Jobs & Education', 'Law & Government', 'News', 'Business & Industrial', 'People & Society', 'Finance', 'Health']
count = 0
today = datetime.datetime.now()
index = open("index.html", "w")
header = '<!doctype html><meta charset=utf-8><meta cpontent="width=device-width,initial-scale=1,viewport-fit=cover" name=viewport><title>News</title><style>body{font-family:Arial,Helvetica,sans-serif;background-color:#fafafa}main{max-width:70ch;padding:2ch;margin:auto}.text{line-height:1.4}a{text-decoration:none;outline:0}</style><main>'
index.write(header)
index.write("<h1>Weather</h1>")
index.write("<p>" + basicWeather.getWeather() + "</>")
index.write("<h1>Latest News</h1>")
indexes = []
for article in cnn.articles:
    try:
        article.download()
        article.parse()

        article_title = article.html.split('<h2 style="margin-top:0px;">')[1].split('</h2>')[0]
        article_text = article.html.split('</div><div><p>')[1].split('</p></div></div>')[0]

        category = list(content_classification.classify(article_text).keys())[0].split("/")[1]
        if category not in allowed_categories:
            continue
    
        subheader = category

        file_name = pattern.sub('', article_title.replace(" ", "-")).lower() + ".html"

        with open("articles/" + file_name, 'w') as out:
            out.write(header + "<h1>" + article_title + "</h1> <br> <h3>" + subheader + "</h3>" +  "<p class='text'>" + article_text + "</p>")

        indexes.append(subheader + " - " + article_title)
        
        count += 1
    except Exception:
        pass

indexes.sort()
index.write("<h2>" + indexes[0][0: indexes[0].index("-") - 1] +"</h2>")
for i in range (0, len(indexes) - 2):
    index.write("<a href='articles/{}'>".format(pattern.sub('', indexes[i][indexes[i].index("-") + 2:].replace(" ", "-")).lower() + ".html") + indexes[i] + "</a><br><br>" )
    if(indexes[i][0] != indexes[i+1][0]):
        index.write("<h2>" + indexes[i+1][0:(indexes[i+1].index("-")-1)] + "</h2>")

index.write("<h3>Last Updated: " + today.strftime("%b %d %Y %I:%M:%S") + "</h3>")
index.write("</main></body></html>")
index.close()
