def create_youtube_video(title, description, hashtag):
	hashtag1 = hashtag
	if len(hashtag)>5:
		hashtag1 = hashtag[0:5]
	n_vid_info = {"title" : title, "description" : description, "likes" : 0, "dislikes": 0, "comments": {}, "hashtag" : hashtag1}
	return n_vid_info

def likes(dict1):
	dict1["likes"] += 1
	return dict1

def dislike(dict2):
	dict2["dislikes"] += 1
	return dict2

def comments(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

def similarity_to_video(vid1, vid2):
	hash1 = vid1["hashtag"]
	hash2 = vid2["hashtag"]
	if len(hash1) > len(hash2):
		short = hash1
		lon = hash2
	else:
		short = hash2
		lon = hash1
	count = 0
	for i in short:
		if i in lon: count += 1
	floater = count/len(lon)
	return str(floater*100)[0:-2] + "%"


vid_list = {}
vid_list["first_vid"] = create_youtube_video("Steve", "cutests person ever", ["cute", "steve", "butterfly", "yellow", "literature", "random"])
vid_list["second_vid"] = create_youtube_video("George", "coolest person ever", ["cute", "george", "birds", "karyoke", "yellow"])

for i in range(495):
	likes(vid_list["first_vid"])
dislike(vid_list["first_vid"])
comments(vid_list["first_vid"], "peterval", "she is the cutests ever")
print(vid_list["first_vid"])
print(similarity_to_video(vid_list["first_vid"], vid_list["second_vid"]))