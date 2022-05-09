<img src = "img/heart_hair.png"  alt = "PNR book covers on heart with background of hair metal band logos" width = "400">

**About**  
This was my final project at allWomen Tech data science bootcamp (5/2021-7/2021)

To view the presentation video for my project, click the image below.

<a href="https://youtu.be/Ke0LeeY-LK8?t=1367"><img src="https://i3.ytimg.com/vi/Ke0LeeY-LK8/0.jpg" alt="allWomen Demo Days Presentation" width="200" target = _blank></a>

To view the presentation without the video, you can view the Sway by clicking the image below.

<a href = "https://sway.office.com/W0qWgUcxXmIMwpbV?ref=Link&loc=mysways"><img src = "img/reading.png"  alt = "Sway Presentation of Paranormal Playlist" width = "200" target = _blank></a>

This is a recommender system that lets you enter a paranormal romance book and get back a list of 20 hair metal songs as a soundtrack. I looked around for an app or website that would let a reader create a playlist based on a book, but there weren't any. Every recommender I found stayed within the same mediums: book to book, music to music, etc. So I thought I'd have some fun and create my own. 

**Book Data**  
Since this was my first project, I wanted to keep it as simple as I could, while still stretching myself to learn new things. I found several datasets of books, but they either didn't have the genre or didn't have the book blurb. I finally found a large dataset of books (~50,000) that had both the genre and blurb, but it wasn't as easy to clean as some of the other book data, and it was extremely large. I pulled out all the paranormal romance books and ended up with a much smaller dataset (~4,500). The data was much messier than I'd dealt with before, and it took several days to get it cleaned to the point where the odd non-English or missing values wouldn't cause problems. 

**Lyrics Data**  
Because my final book dataset was small, I thought I should pair it with a small set of music, too. I wanted a playlist of 10 to 20 songs, so I thought the music dataset should have between 2,000 and 4,000 songs. To do that, I decided on a genre near and dear to my heart. Being a child of the 80s, I grew up listening to hair metal and thought it would make an interesting counterpoint to my PNR romance books. I had a difficult time finding a dataset that would work, so I decided to scrape the songs from [Genius](https://genius.com/) and [AZ lyrics](https://www.azlyrics.com/). I put together a list of the some hair metal bands and went to work creating a dataset. When I'd finished my scraping, I found that I didn't have enough songse so I started searching again for datasets. I luckily found one with lyrics for several genres of music, including some hair metal. I pulled out the data I could use from that dataset and joined it with the dataset I'd scraped (~5,000). There were some instrumental songs in the dataset - I have no idea how! - so I set to work cleaning. Cleaning this data didn't take nearly as long as cleaning the books, thank goodness! 

**Reccomender System**  
Once both datasets were cleaned and ready to use, I added a column for formats with 0 for books and 1 for music and merged them. I then started working on putting together my model. I went with TF-IDF and cosine similarity to compare the content of the book descriptions and song lyrics. 

![book cover with playlist for book](/img/Slide2.png)

**To Use**
- Start in the books folder to get the initial csv for books.
- After that, start with either scraped or found lyrics folder. 
- In the scraped lyrics folder, the json files that are scraped aren't included, but you can skip that folder and go directly to the combined lyrics folder since I've included the resultant csv file of scraped lyrics. 
- Once the combined lyrics notebook has finished, go to the main folder and work in the book_sountrack notebook to combine everything into one dataframe and finally get your song recommendations!

<div align = "center"><img src = "img/pop_monstersm.png"  alt = "bar chart showing most popular monsters are vampires" width = "400"></div>

**Next Steps**
+ Scrape track numbers from Spotify - either use fuzzy match to work with csv I have or scrape track info and combine csv files
+ Create a webapp so people can use this themselves
+ Allow users to sign into their own Spotify account to create their own playlists
+ Set up automatic scraping of books
+ Change directions - give some songs from a playlist and suggest a book (thanks Anu!)
+ better playlist suggestions for moods (thanks Neslihan)
+ suggest book based on ambiance of memes, pictures, general feelings etc. (thanks Kat and Neslihan!)
