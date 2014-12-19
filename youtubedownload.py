import os
import sys
import json
import re
import pafy

from urllib import urlopen
from urlparse import parse_qs, urlparse;
from time import sleep

apiKey = {Your API Key}
videos = []

def parseYouTubeVid():
	print "Parsing " + username + "'s YouTube Channel Videos... ",
	foundAll = False
	inp = urlopen(r'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=' + username + '&key=' + apiKey)
	resp = json.load(inp)
	inp.close()

	playlistID = resp['items'][0]['contentDetails']['relatedPlaylists']['uploads']
	nextPageToken = ''

	while not foundAll:
		try:
			inp = urlopen(r'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken=' + nextPageToken + '&playlistId=' + playlistID + '&key=' + apiKey)
			resp = json.load(inp)
			inp.close()
			if resp['nextPageToken']:
				nextPageToken = resp['nextPageToken']
				returnedVideos = resp['items']
				for video in returnedVideos:
					if keyword in video['snippet']['title'].lower():
						videos.append(video)
		except:
			returnedVideos = resp['items']
			
			for video in returnedVideos:
				if keyword in video['snippet']['title'].lower():
					videos.append(video)
			foundAll = True

	print "[DONE]"
	sleep(1.5)
	os.system('cls')
	
	try:
		inp = urlopen(r'https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername=' + username + '&key=' + apiKey)
		resp = json.load(inp)
		inp.close()	
		
		channelTitle = resp['items'][0]['snippet']['title']
		print "YouTube's username: ", channelTitle
		print "Keyword searched: ", keyword
		#print "Total number of videos found: ", len(videos)
	except:
		print "YouTube's username: ", username
		print "Keyword searched: ", keyword
	
	return len(videos)

def downloadYouTubeVid():
	os.system('cls')
	print " =========== Downloading video =========== "
	print ""
	for video in videos:
		try:
			id = video['snippet']['resourceId']['videoId']
			url = 'https://www.youtube.com/watch?v=' + id
			
			print video['snippet']['title'].encode('ascii', 'ignore').decode('ascii').replace("/", "-") # video title
			tempvideo = pafy.new(url)
			best = tempvideo.getbest()
			best.download(quiet=False);
			print ""
			
			#print video['snippet']['resourceId']['videoId'] #video id
		except:
			print "Error!"
	print ""
	
def downloadYoutubeAudio():
	os.system('cls')
	print " =========== Downloading audio =========== "
	print ""
	for video in videos:
			try:
				id = video['snippet']['resourceId']['videoId']
				url = 'https://www.youtube.com/watch?v=' + id
				
				print video['snippet']['title'].encode('ascii', 'ignore').decode('ascii').replace("/", "-") # video title
				tempvideo = pafy.new(url)
				bestaudio = tempvideo.getbestaudio()
				bestaudio.download();
				print ""
				
			except:
				print "Error!"
	print ""
	
def userPrompt():
	print "[1] List all the available matched videos"
	print "[2] Download all video(s) at best quality"
	print "[3] Download all audio(s) at best quality"
	print "[4] Remove the unwanted videos from list"
	print "[5] Exit"
	choice = raw_input('Enter your choice: ');
	print ""
	
	while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
		print "Please select only [1] or [2] or [3] or [4]."
		print "[1] List all the available matched videos"
		print "[2] Download all video(s) at best quality"
		print "[3] Download all audio(s) at best quality"
		print "[4] Remove the unwanted videos from list"
		print "[5] Exit"
		choice = raw_input('Enter your choice: ');
		print ""
	
	if choice == '1':
		listYoutubeVideos()
	elif choice == '2':
		downloadYouTubeVid()
	elif choice == '3':
		downloadYoutubeAudio()
	elif choice == '4':
		removeYouTubeVid()
	else:
		sys.exit(0)

def listYoutubeVideos():
	print " =========== All available videos =========== "
	print ""
	i = 1
	for video in videos:
		try:
			print '[' + str(i) + '] ' + video['snippet']['title'].encode('ascii', 'ignore').decode('ascii').replace("/", "-") # video title
			print ""
			i += 1
		except:
			print "Error!"
	
	print " ================ End of List =============== "
	print ""
	print ""
	userPrompt()

def removeYouTubeVid():
	while videos:
		num = raw_input('Enter the number of video that you want to delete (Enter "0" back to menu): ');		
		if int(num) > 0 and int(num) <= len(videos):
			del videos[int(num)-1]
			print ""
			listYoutubeVideos()
			break
		elif int(num) == 0:
			break
		else:
			print "Value out of range!"
			break
	
	print ""
	userPrompt()
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Usage: python youtubedownload.py <username> <optional:single keyword | default=all>"
		print "Example: python youtubedownload.py GoogleDevelopers YouTube"
		sys.exit(0)

	username = sys.argv[1]
	if len(sys.argv) == 2:
		keyword = ''
	else:
		keyword = sys.argv[2]
	
	os.system('cls')
	
	videoFound = parseYouTubeVid()
	
	if videoFound > 0:
		print "Total number of videos found: ", len(videos)
		print ""
		userPrompt()
	else:
		print "Your search '" + keyword + "' did not match any videos. Please try again."
		sys.exit(0)
