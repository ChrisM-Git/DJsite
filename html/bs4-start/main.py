
#import beautiful soup
from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")
# now we can use variables to grab content from the site, for example, lets print the title
print(soup.title)
#print the title tag name
print(soup.title.name)

#print all of the html with indent
 #print(soup.prettify())

#find different tags
 #anchor tag soup.a
 #line item soup.li

#print the first paragraph in webpage
#print(soup.p)

#get all of the tags in page, find all tag where name is = a
all_anchor_tags = soup.find_all(name = "a")
print(all_anchor_tags)

#find a specific heading and tag
heading = soup.find(name="h1", id="name")
print(heading)

#find a class tag, you need the underscore so it doesnt conflict with python class variables
sectionheading = soup.find(name="h3", class_="heading")
print(sectionheading)

#use selectone to find the first item in a page, select finds all the items
#find an anchor tag inside of paragraph tag
companyurl = soup.select_one(selector="p a")
print(companyurl)

#you can also use the #sign to get a hold of an ID
name= soup.select_one(selector="#name")
print(name)
#get all headings
headings = soup.select(".heading")
print(headings)

#lets grab a specific tag from all anchor tags
#for tag in all_anchor_tags:
    #print all the tags print(tag.getText())
    #print(tag.get("href")) #print al href links in site