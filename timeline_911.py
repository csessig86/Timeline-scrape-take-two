import urllib2
from BeautifulSoup import BeautifulSoup
import datetime
import re

now = datetime.datetime.now()

# Create a CSV where we'll save our data. See further docs:
# http://propublica.github.com/timeline-setter/#csv
f = open('timeline_911.csv', 'w')

# Make the header rows. These are based on headers recognized by TimelineSetter.
f.write("date" + "," + "description" + "," + "link" + "," + "html" + "\n")

# URL of the XML file we will scrape
url = 'http://wcfcourier.com/remember911/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

# We'll determine how many events appear in the XML document and then run a loop through each one, scraping our data along the way.
events = soup.findAll('div', attrs={'class': 'story-block'})
for x in events:

    # Tell us which event is being scraped
    print "Getting data for " + x.find('h3').text
	
    # Information within the XML file that we will scrape
    date = x.find('p', attrs={'class': 'story-more'})('em')
    link = x.find('fb:like')['href']
    headline = x.find('h3').text
    description = x.find('div', attrs={'id': 'blox-story-text'})('p', limit=1)
    image = x.find('img')
    
    # Extract that information in strings
    date2 = str(date)
    link2 = str(link)
    headline2 = str(headline)
    image2 = str(image)
    
    # These are pulled from outside the loop
    description2 = str(description)
    
    # We'll replace commas with dashes so we don't screw up the CSV. You can change the dash to whatever character you want
    date3 = date2.replace(",", " -") 
    link3 = link2.replace(",", " -")
    headline3 = headline2.replace(",", " -")
    description3 = description2.replace(",", " -")
    image3 = image2.replace(",", " -")
    
    # We will adjust the width of all images to 300 pixels. Also, Python spits out the word 'None' if it doesn't find an image. Delete that.
    image4 = re.sub(r'width="\d\d\d"', 'width="300"', image3)
    image5 = image4.replace('None', "")
    
    # Extra formatting needed for dates to get rid of em tags and unnecessary formatting
    date4 = date3.replace('[<em>', "")
    date5 = date4.replace('</em>]', "")
    date6 = date5.replace('- ', "")
    date7 = date6.replace("at ", "")
    
    # If the story has been updated recently, an em class tag will appear on the page showing the time but not the date. We will delete the class and replace it with today's date. We can change the date in the CSV if we need to.
    date8 = date7.replace('[<em class="item-updated badge">Updated:', str(now.strftime("%Y-%m-%d %H:%M")))
    
    # Extra formatting is also need for the description to get rid of p tags and new line returns
    description4 = description3.replace('[<p>', "")
    description5 = description4.replace('</p>]', "")
    description6 = description5.replace('\n', " ")
    description7 = description6.replace('[]', "")

    # Write the information to the file. The HTML code is based on coding recognized by TimelineSetter
    f.write(date8 + "," + description7 + "," + link3 + "," + '<h2 class="timeline-img-hed">' + headline3 + '</h2>' + image5 + "\n")

#You're done! Close file.	
f.close()