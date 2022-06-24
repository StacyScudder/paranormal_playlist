# Pieces of the Book Playlist Puzzle

# Get a book ISBN and description

![Google Books logo](Google-book-logo.png)

The booksearch file takes the title of any book (not just paranormal romance...more's the pity) and uses Google Books API to find the ISBN and description for the book given Then the regex library cleans up the description text to get it ready for TF-IDF (not implemented in this file) when the piece gets put into the rest of the puzzle.

# Download 1000 spotify songs by genre

![Spotify Logo](Spotify_logo_with_text.png)

One piece of my [book playlist](https://github.com/StacyScudder/paranormal_playlist) puzzle!

This file will download 1000 tracks from Spotify, with ids, for any genre. You can find a list of genres sorted by popularity [here](https://everynoise.com/everynoise1d.cgi?vector=popularity&scope=all). It drops any tracks that are live or demo versions.
