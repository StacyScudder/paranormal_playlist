# paranormal_playlist
This is a recommender system that lets you enter a paranormal romance book and get back a list of 20 hair metal songs as a soundtrack

<img src="https://github.com/StacyScudder/paranormal_playlist/blob/main/Slide2.JPG" width=600 align=right>

About:<br>
This was my final project at allWomen Tech DS Bootcamp (5/2021-7/2021).<br>
My video presentation can be seen here: https://youtu.be/Ke0LeeY-LK8?t=1367 <br>
My presentation without narration can be seen here: https://sway.office.com/W0qWgUcxXmIMwpbV?ref=Link

Process:<br>
Start in the books folder to get the initial csv for books.
After that, start with either scraped or found lyrics folder. 
In the scraped lyrics folder, the json files that are scraped aren't included, but you can skip that folder and go directly to the combined lyrics folder since I've included the resultant csv file of scraped lyrics. 
Once the combined lyrics notebook has finished, go to the main folder and work in the book_sountrack notebook to combine everything into one dataframe, do some basic EDA and visualizations, and finally get your song recommendations!

Next Steps:
+ Scrape track numbers from Spotify - either use fuzzy match to work with csv I have or scrape track info and combine csv files
+ Create a webapp so people can use this themselves
+ Allow users to sign into their own Spotify account to create their own playlists
+ Set up automatic scraping of books
