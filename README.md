# pyYoutubeSongDownloader
A selenium script that fetches a youtube url of a preferred song and and downloads it in a mp3 format for listening pleasure. 


## Bugs and Fixes that need to be made

The program gets a little buggy when you use it on an unstable connection, but overall works. Right now I was'nt able to get it 
download the mp3 file, but it does take you to the final screen where you just have to push the download button.

## Webdriver
I used the Chrome Options to disbale the notifications on the ytmp3.cc website as there is a pop up that comes up when you download
a new song.
Now depending on which webdriver you are going to using you'll need to change that.


## Something to note

If the program keeps on crashing or showing any eror, its just your internet connection that could be making the program to lag
a bit. I highly recommend using the find_element_by_xpath in my oponion its much more reliable than using any of the other 
element finders. A raise TimeoutException(message, screen, stacktrace) exeception may be raised that may just be the
download button waiting to load. Overall this whole program highly relies on the strength of your internet connection. So if 
you keep on getting error messages like any of these, just try to run it again.

## Enjoy your favourite songs for free

Well I guess whats left to do, is to enjoy your favorite songs for free. The main reason I created this file, was because whenever
I would stream music on youtube it would get annoying because ads would play inbetween. Also because I'm too cheap to pay for 
youtube music, so why not write a program for it! Right 🤷🏽‍♂️
