import tweepy
import random
from time import sleep

//input all keys here

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

#print(str(api.get_user(screen_name = "@regularSimon")))

#start file reading
while True:
	
	rnd = random.randrange(0,973871)
	dct = open("dict.txt")
	#print(rnd)
	areWeThereYet = 0
	while areWeThereYet < rnd:
		dct.readline()
		areWeThereYet = areWeThereYet + 1

	res = dct.readline()	
	#print(res)

	placeh = True
	while placeh:
		if res.isupper():
			placeh = False
		else:
			res = dct.readline()

	print("Sandra's word of the day is: " + res)
	final = "Sandra's word of the day is: " + res
	ifUpper = True
	while ifUpper:
		res = dct.readline()
		if res.isupper():
			ifUpper = False
		else:
			if " " in res:
				print(res)
				final = final + res
	final1 = ""
	final2 = ""
	final3 = ""
	final4 = ""
	final5 = ""
	final6 = ""
	final7 = ""
	if len(final) > 140:
		final1 = final[:135]
		final2 = final[135:270]
		final3 = final[270:405]
		final4 = final[405:540]
		final5 = final[540:675]
		final6 = final[675:810]
		final7 = final[810:945]
	else:
		final1 = final

	ID = api.update_status(final1).id
	
	if " " in final2:
		ID = api.update_status(final2,ID).id
	if " " in final3:
		ID = api.update_status(final3,ID).id
	if " " in final4:
		ID = api.update_status(final4,ID).id
	if " " in final5:
		ID = api.update_status(final5,ID).id
	if " " in final6:
		ID = api.update_status(final6,ID).id
	if " " in final7:
		ID = api.update_status(final7,ID).id
	sleep(3600) 
	#10 mins
	

