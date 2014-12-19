README
======================

Author: Jason Lim @jasonsslim
Created: 19 Dec 2014
Site: http://www.jasonsslim.info
eMail: jason.sslim@gmail.com
Purpose: Download selectively videos on user's channel

This scipt parse the youtube video data using YouTube Data API (v3) and download the available videos by importing pafy library.

Here, I would like to thanks nagev for his pafy.py.
For full documentation, please visit: http://pythonhosted.org/Pafy/
For Github, please visit: https://github.com/np1/pafy

How to use:
Place youtubedownload.py and pafy.py in the same directory.

Usage example:
cmd >> python youtubedownload.py GoogleDevelopers 
- This will parse all videos available in GoogleDevelopers's channel and ready for download

cmd >>  cmd >> python youtubedownload.py GoogleDevelopers YouTube
- This will parse all available videos with match keyword 'YouTube' in GoogleDevelopers's channel and ready for download

