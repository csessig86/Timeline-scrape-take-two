This scraper turns content (articles, photos, galleries, etc.) in the BLOX CMS into CSV files that can be read by ProPublica's Timeline-Setter:
http://propublica.github.com/timeline-setter/


Here's a quick walkthrough on how to set up your collection in BLOX:

1. Go into Blox and select any stories/documents/videos/etc. that you would like to have on the timeline. Give each item a uniform hashtag by selecting "Batch edit" when everything is selected and choosing "Keywords" > "Keywords to add." For this example, I hashtagged content related to our coverage of the Dunkerton's mayor's arrest (#dunkerton).

2. Create some sort of page in Blocks that will pull in everything you just tagged with your hashtag. For this example, I created these:
http://wcfcourier.com/test/scrape/dunkerton/
http://wcfcourier.com/remember911

(Note: For my own purposes, I also created: http://wcfcourier.com/test/scrape/. Personally, in the future, I will just use the same page and template to pull in content for new timelines. All I will have to do is add a new hashtag to the content I want to pull in and change the template to pull in the hash-tagged content.)

3. Use the Block template "core-blog-index-list" to pull in all the items. It is important that you use this template, otherwise the scraper will not work.

(Note: You can also have the Block template pull in certain sections. For our 9/11 coverage, all of our stories were put into "remember911/local," so I have the template pulling in articles in "remember911/local")

4. Load the page up. It should look like these:
http://wcfcourier.com/test/scrape/dunkerton/
http://wcfcourier.com/remember911

6. Paste the URL of the page into timeline.py after "url" (line 12):
url = 'http://wcfcourier.com/test/scrape/dunkerton/'
OR
url = 'http://wcfcourier.com/remember911'

7. If you haven't already, download BeautifulSoup. It's very easy to do:
http://www.crummy.com/software/BeautifulSoup/#Download

8. Go into your Terminal, navigate to the folder with Python script and run:
% python timeline.py

This will output a structured CSV file

9. If you haven't already, download Timeline-Setter. It's also really easy to do:
http://propublica.github.com/timeline-setter/

10. In your Terminal, run:
% timeline-setter -c timeline.csv (or whatever your CSV is called)

Note: Sometimes I have to bring the CSV into Excel and save it…Not sure what the problem is but it seems to work after I do that.

11. Tada! You now have Timeline-Setter timeline. See the output folder for a few examples.


- What's Next?
Timeline-Setter has additional customizations that you can add to the timeline:
http://propublica.github.com/timeline-setter/#csv

For instance, you can add series to each event on the timeline by adding new columns in the CSV before running "timeline-setter -c timeline.csv".