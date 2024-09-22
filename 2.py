import pymysql
import subprocess as sp
import datetime

con = pymysql.connect(host='localhost',user='root',password='M@h@rn@v29122003',db='Ammajaan_Rhyme_Videos',cursorclass=pymysql.cursors.DictCursor)

print("connection successful")
tmp = input("press any key to continue>")
if tmp is not None:
	tmp = sp.call('clear', shell=True)
	
print()
print("Welcome, please use the provided menu to operate on the database Ammajaan Rhyme Videos")
print()

while(1):
	print("1. Insert a new user")
	print("2. Update a user's status to premium")
	print("3. Update a user's status to normal")
	print("4. Delete a user")
	print("5. Insert a new rhyme")
	print("6. Remove a rhyme")
	print("7. Insert a new creator")
	print("8. Remove a creator")
	print("9. Insert a new device")
	print("10. Remove a device")
	print("11. Insert a new profile")
	print("12. Remove a profile")
	print("13. Play a rhyme by a creator on a device")
	print("14. Create a new playlist by a user")
	print("15. Delete a playlist by a user")
	print("16. Save a playlist")
	print("17. Unsave a playlist")
	print("18. Like a rhyme")
	print("19. Unlike a rhyme")
	print("20. Subscribe to a creator")
	print("21. Unsubscribe from a creator")
	print("22. Add a rhyme to a playlist by a user")
	print("23. Remove a rhyme from a playlist by a user")
	print("24. Select all creators' records with more than n subscribers")
	print("25. Select all rhyme id and names with age group n")
	print("26. Select all playlist id and name for a creator")
	print("27. Select all playlist id and name for a user")
	print("28. Select creator id and name with most subscribers")
	print("29. Select playlist id and name with most saves")
	print("30. Search rhyme by a given keyword (creator name, rhyme name, playlist name)")
	print("31. Search premium users with a given plan")
#	print("32. Get top n popular playlists based on number of saves")
#	print("33. Get top n favourite creator based on number of liked rhymes from the creator")
	print("enter -1 to exit")
	print()
	
	choice = int(input("Please enter the index corresponding to your choice> "))
	tmp = sp.call('clear', shell=True)
	
	if choice==1:
		print("Please enter the following details to add a new user-")
		User_id = int(input("User ID: "))
		User_name = input("User name: ")
		User_email = input("User email: ")
		User_password = input("User password (length >15): ")
		print("User registration date and time (format- YYYY MM DD HH MM SS): ")
		year = int(input("Year: "))
		month = int(input("Month: "))
		day = int(input("Day: "))
		hour = int(input("Hour: "))
		minute = int(input("Minute: "))
		second = int(input("Second: "))
		User_registration_date = datetime.datetime(year,month,day,hour,minute,second)
		User_state = input("User state: ")
		User_country = input("User country: ")
		User_mobile_number = input("User mobile number: ")
		print()
		print("Adding user...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO USER(User_id,User_name,User_email,User_password,User_registration_date,User_state,User_country,User_mobile_number) VALUES({},"{}","{}","{}",\'{}\',"{}","{}","{}")'
				cur.execute(sql.format(User_id,User_name,User_email,User_password,User_registration_date,User_state,User_country,User_mobile_number))
			con.commit()
			print("User added")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==2:
		print("Please enter the following details to update user status to premium-")
		User_id = int(input("User ID: "))
		Plan_id = int(input("Plan ID: "))
		print()
		print("Updating user status...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO Premium_User(User_id,Plan_id) VALUES({},{})'
				cur.execute(sql.format(User_id, Plan_id))
			con.commit()
			print("User status updated")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==3:
		print("Please enter the following details to update user status to normal-")
		User_id = int(input("User ID: "))
		print()
		print("Updating user status...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM Premium_User WHERE User_id={}'
				cur.execute(sql.format(User_id))
				sql = 'INSERT INTO Normal_User(User_id) VALUES({})'
				cur.execute(sql.format(User_id))
			con.commit()
			print("User status updated")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==4:
		print("Please enter the following details to delete a user-")
		User_id = int(input("User ID: "))
		print()
		print("Deleting user...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM USER WHERE User_id={}'
				cur.execute(sql.format(User_id))
			con.commit()
			print("User deleted")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==5:
		print("Please enter the following details to insert a rhyme-")
		Rhyme_id = int(input("Rhyme ID: "))
		Rhyme_title = input("Rhyme title: ")
		Rhyme_duration = int(input("Rhyme duration (in seconds): "))
		print("Date and time added (format- YYYY MM DD HH MM SS): ")
		year = int(input("Year: "))
		month = int(input("Month: "))
		day = int(input("Day: "))
		hour = int(input("Hour: "))
		minute = int(input("Minute: "))
		second = int(input("Second: "))
		Date_added = datetime.datetime(year,month,day,hour,minute,second)
		Rhyme_path = input("Rhyme path in the database: ")
		Creator_id = int(input("Creator ID: "))
		print()
		print("Adding rhyme...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO RHYME(Rhyme_id,Rhyme_title,Rhyme_duration,Date_added,Rhyme_path,Creator_id) VALUES({},"{}",{},\'{}\',"{}",{})' 
				cur.execute(sql.format(Rhyme_id,Rhyme_title,Rhyme_duration,Date_added,Rhyme_path,Creator_id))
			con.commit()
			print("Rhyme added")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==6:
		print("Please enter the following details to delete a rhyme-")
		Rhyme_id = int(input("Rhyme ID: "))
		print()
		print("Deleting rhyme...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM RHYME WHERE Rhyme_id={}'
				cur.execute(sql.format(Rhyme_id))
			con.commit()
			print("Rhyme deleted")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==7:
		print("Please enter the following details to insert a new creator-")
		Creator_id = int(input("Creator ID: "))
		Creator_name = input("Creator name: ")
		Creator_subscribers = int(input("Creator subscriber count: "))
		Creator_language = input("Creator language: ")
		print()
		print("Adding creator...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO CREATOR(Creator_id,Creator_name,Creator_subscribers,Creator_language) VALUES({},"{}",{},"{}")'
				cur.execute(sql.format(Creator_id,Creator_name,Creator_subscribers,Creator_language))
			con.commit()
			print("Creator added")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==8:
		print("Please enter the following details to delete a creator-")
		Creator_id = int(input("Creator ID: "))
		print()
		print("Deleting creator...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM CREATOR WHERE Creator_id={}'
				cur.execute(sql.format(Creator_id))
			con.commit()
			print("Creator deleted")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==9:
		print("Please enter the following details to insert a new device-")
		Device_id = int(input("Device ID: "))
		Device_user_id = int(input("Device's user's ID: "))
		Resolution = int(input("Device's Resolution (Pixel count along height): "))
		Type = input("Type of device: ")
		print()
		print("Adding device...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO DEVICE(Device_id,Device_user_id,Resolution,Type) VALUES({},{},{},"{}")'
				cur.execute(sql.format(Device_id,Device_user_id,Resolution,Type))
			con.commit()
			print("Device Added")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==10:
		print("Please enter the following details to delete a device-")
		Device_id = int(input("Device ID: "))
		print()
		print("Deleting device...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM DEVICE WHERE Device_id={}'
				cur.execute(sql.format(Device_id))
			con.commit()
			print("Device deleted")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==11:
		print("Please enter the following details to insert a new profile-")
		Profile_user_id = int(input("Profile's user's ID: "))
		Profile_id = int(input("Profile ID: "))
		Profile_name = input("Profile name: ")
		Pin_exists = input("Do you want to keep a pin (TRUE or FALSE): ")
		Pin = "NULL"
		if Pin_exists=="TRUE":
			Pin = int(input("Pin: "))
		print()
		print("Adding profile...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO PROFILE(Profile_user_id,Profile_id,Profile_name,Pin_exists,Pin) VALUES({},{},"{}",{},{})'
				cur.execute(sql.format(Profile_user_id,Profile_id,Profile_name,Pin_exists,Pin))
			con.commit()
			print("Profile added")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==12:
		print("Please enter the following details to remove a profile-")
		Profile_id = int(input("Profile ID: "))
		print()
		print("Deleting profile...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM PROFILE WHERE Profile_id={}'
				cur.execute(sql.format(Profile_id))
			con.commit()
			print("Profile deleted")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==13:
		print("Please enter the following details to play a rhyme by a creator on a device-")
		User_id = int(input("User ID: "))
		Rhyme_id = int(input("Rhyme ID: "))
		Creator_id = int(input("Creator ID: "))
		Device_id = int(input("Device ID: "))
		print()
		print("Playing rhyme using given credentials...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO USER_plays_RHYME_by_CREATOR_on_DEVICE(User_id,Rhyme_id,Creator_id,Device_id) VALUES({},{},{},{})'
				cur.execute(sql.format(User_id,Rhyme_id,Creator_id,Device_id))
			con.commit()
			print("Rhyme played")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==14:
		print("Please enter the following details to create a new playlist by a user-")
		User_id = int(input("User ID: "))
		Playlist_id = int(input("Playlist ID: "))
		Playlist_name = input("Playlist name: ")
		print("Playlist created date and time (format- YYYY MM DD HH MM SS): ")
		year = int(input("Year: "))
		month = int(input("Month: "))
		day = int(input("Day: "))
		hour = int(input("Hour: "))
		minute = int(input("Minute: "))
		second = int(input("Second: "))
		Playlist_create_date = datetime.datetime(year,month,day,hour,minute,second)
		print()
		print("Creating playlist...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO PLAYLIST(User_id,Playlist_id,Playlist_name,Playlist_create_date) VALUES({},{},"{}",\'{}\')'
				cur.execute(sql.format(User_id,Playlist_id,Playlist_name,Playlist_create_date))
			con.commit()
			print("Playlist created")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==15:
		print("Please enter the following details to delete a playlist-")
		Playlist_id = int(input("Playlist ID: "))
		print()
		print("Deleting playlist...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM PLAYLIST WHERE Playlist_id={}'
				cur.execute(sql.format(Playlist_id))
			con.commit()
			print("Playlist deleted")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==16:
		print("Please enter the following details to save a playlist-")
		User_id = int(input("User ID: "))
		Playlist_id = int(input("Playlist ID: "))
		print()
		print("Saving playlist...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO saves(User_id,Playlist_id) VALUES({},{})'
				cur.execute(sql.format(User_id,Playlist_id))
			con.commit()
			print("Playlist saved")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==17:
		print("Please enter the following details to unsave a playlist-")
		User_id = int(input("User ID: "))
		Playlist_id = int(input("Playlist ID: "))
		print()
		print("Unsaving playlist...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM saves WHERE User_id={} AND Playlist_id={}'
				cur.execute(sql.format(User_id,Playlist_id))
			con.commit()
			print("Playlist unsaved")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==18:
		print("Please enter the following details to like a rhyme-")
		User_id = int(input("User ID: "))
		Rhyme_id = int(input("Rhyme ID: "))
		print()
		print("Liking rhyme...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO likes(User_id,Rhyme_id) VALUES({},{})'
				cur.execute(sql.format(User_id,Rhyme_id))
			con.commit()
			print("Rhyme liked")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==19:
		print("Please enter the following details to unlike a rhyme-")
		User_id = int(input("User ID: "))
		Rhyme_id = int(input("Rhyme ID: "))
		print()
		print("Unliking rhyme...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM likes WHERE User_id={} AND Rhyme_id={}'
				cur.execute(sql.format(User_id,Rhyme_id))
			con.commit()
			print("Rhyme unliked")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==20:
		print("Please enter the following details to subscribe to a creator-")
		User_id = int(input("User ID: "))
		Creator_id = int(input("Creator ID: "))
		print()
		print("Subscribing to creator...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO subscribes(User_id,Creator_id) VALUES({},{})'
				cur.execute(sql.format(User_id,Creator_id))
				sql = 'UPDATE CREATOR SET Creator_subscribers=Creator_subscribers+1 WHERE Creator_id={}'
				cur.execute(sql.format(Creator_id))
			con.commit()
			print("Subscribed to creator")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==21:
		print("Please enter the following details to unsubscribe to a creator-")
		User_id = int(input("User ID: "))
		Creator_id = int(input("Creator ID: "))
		print()
		print("Unsubscribing to creator...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM subscribes WHERE User_id={} AND Creator_id={}'
				cur.execute(sql.format(User_id,Creator_id))
				sql = 'UPDATE CREATOR SET Creator_subscribers=Creator_subscribers-1 WHERE Creator_id={}'
				cur.execute(sql.format(Creator_id))
			con.commit()
			print("Unsubscribed to creator")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==22:
		print("Please enter the following details to add a rhyme to a playlist by a user-")
		Playlist_id = int(input("Playlist ID for playlist by user: "))
		Rhyme_id = int(input("Rhyme ID: "))
		Creator_id = int(input("Creator ID: "))
		print()
		print("Adding rhyme to playlist...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'INSERT INTO PLAYLIST_has_RHYME_by_CREATOR(Playlist_id,Rhyme_id,Creator_id) VALUES({},{},{})'
				cur.execute(sql.format(Playlist_id,Rhyme_id,Creator_id))
			con.commit()
			print("Added rhyme to playlist")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==23:
		print("Please enter the following details to delete a rhyme from a playlist by a user-")
		Playlist_id = int(input("Playlist ID for playlist by user: "))
		Rhyme_id = int(input("Rhyme ID: "))
		Creator_id = int(input("Creator ID: "))
		print()
		print("Deleting rhyme to playlist...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'DELETE FROM PLAYLIST_has_RHYME_by_CREATOR WHERE Playlist_id={} AND Rhyme_id={} AND Creator_id={}'
				cur.execute(sql.format(Playlist_id,Rhyme_id,Creator_id))
			con.commit()
			print("Deleted rhyme from playlist")
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==24:
		n = int(input("Enter value of n: "))
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT * FROM CREATOR WHERE Creator_subscribers>{}'
				cur.execute(sql.format(n))
				rows = cur.fetchall()
			print("Creator_id | Creator_name | Creator_subscribers | Creator_language")
			for row in rows:
				print(row['Creator_id']," | ",row['Creator_name']," | ",row['Creator_subscribers']," | ",row['Creator_language'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==25:
		n = input("Enter value of n (age group): ")
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT Rhyme_id,Rhyme_title FROM RHYME WHERE Rhyme_id IN (SELECT DISTINCT Rhyme_id FROM Age_Group WHERE Rhyme_age_group="{}")'
				cur.execute(sql.format(n))
				rows = cur.fetchall()
			print("Rhyme_id | Rhyme_title")
			for row in rows:
				print(row['Rhyme_id']," | ",row['Rhyme_title'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==26:
		n = int(input("Creator_id: "))
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT Playlist_id,Playlist_name FROM PLAYLIST WHERE Playlist_id IN (SELECT DISTINCT Playlist_id FROM PLAYLIST_has_RHYME_by_CREATOR WHERE Creator_id={})'
				cur.execute(sql.format(n))
				rows = cur.fetchall()
			print("Playlist_id | Playlist_name")
			for row in rows:
				print(row['Playlist_id']," | ",row['Playlist_name'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==27:
		n = int(input("User_id: "))
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT Playlist_id,Playlist_name FROM PLAYLIST WHERE User_id={}'
				cur.execute(sql.format(n))
				rows = cur.fetchall()
			print("Playlist_id | Playlist_name")
			for row in rows:
				print(row['Playlist_id']," | ",row['Playlist_name'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==28:
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT Creator_id,Creator_name FROM CREATOR ORDER BY Creator_subscribers DESC LIMIT 1'
				cur.execute(sql)
				rows = cur.fetchall()
				print("Creator_id | Creator_name")
			for row in rows:
				print(row['Creator_id']," | ",row['Creator_name'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==29:
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT Playlist_id,Playlist_name FROM PLAYLIST WHERE Playlist_id=(SELECT Playlist_id FROM saves GROUP BY Playlist_id ORDER BY COUNT(Playlist_id) DESC LIMIT 1)'
				cur.execute(sql)
				rows = cur.fetchall()
			print("Playlist_id | Playlist_name")
			for row in rows:
				print(row['Playlist_id']," | ",row['Playlist_name'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==30:
		keyword = input("Enter keyword: ")
		
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT Rhyme_id,Rhyme_title FROM RHYME WHERE Creator_id IN (SELECT Creator_id FROM CREATOR WHERE Creator_name REGEXP \'{}\')'
				cur.execute(sql.format(keyword))
				rows1 = cur.fetchall()
				sql = 'SELECT Rhyme_id, Rhyme_title FROM RHYME WHERE Rhyme_title REGEXP \'{}\''
				cur.execute(sql.format(keyword))
				rows2 = cur.fetchall()
				sql = 'SELECT Rhyme_id, Rhyme_title FROM RHYME WHERE Rhyme_id IN (SELECT Rhyme_id FROM PLAYLIST_has_RHYME_by_CREATOR WHERE Playlist_id IN (SELECT Playlist_id FROM PLAYLIST WHERE Playlist_name REGEXP \'{}\'))'
				cur.execute(sql.format(keyword))
				rows3 = cur.fetchall()
			print("Rhyme_id | Rhyme_title")
			for row in rows1:
				print(row['Rhyme_id']," | ",row['Rhyme_title'],sep='')
			for row in rows2:
				print(row['Rhyme_id']," | ",row['Rhyme_title'],sep='')
			for row in rows3:
				print(row['Rhyme_id']," | ",row['Rhyme_title'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
			
	elif choice==31:
		Plan_id = int(input("Plan ID: "))
		
		print()
		print("Fetching results...")
		print()
		
		try:
			with con.cursor() as cur:
				sql = 'SELECT * FROM USER WHERE User_id IN (SELECT User_id FROM Premium_User WHERE Plan_id={})'
				cur.execute(sql.format(Plan_id))
				rows = cur.fetchall()
			print("User_id | User_name | User_email | User_password | User_registration_date | User_state | User_country | User_mobile_number")
			for row in rows:
				print(row['User_id']," | ",row['User_name']," | ",row['User_password']," | ",row['User_registration_date']," | ",row['User_state']," | ",row['User_country']," | ",row['User_mobile_number'],sep='')
		except Exception as e:
			print("Error received")
			print(e)
#	elif choice==32:
#		n = int(input("Enter value of n: "))
#		
#		print()
#		print("Fetching results...")
#		print()
#		
#		try:
#			with con.cursor() as cur:
#				sql = 'SELECT Playlist_id,Playlist_name FROM PLAYLIST WHERE Playlist_id IN (SELECT DISTINCT Playlist_id FROM saves GROUP BY Playlist_id ORDER BY COUNT(Playlist_id) DESC LIMIT {})'
#				cur.execute(sql.format(n))
#				rows = cur.fetchall()
#			print("Playlist_id | Playlist_name")
#			for row in rows:
#				print(row['Playlist_id']," | ",row['Playlist_name'],sep='')
#		except Exception as e:
#			print("Error received")
#			print(e)
#			
#	elif choice==33:
#		n = int(input("Enter value of n: "))
#		
#		print()
#		print("Fetching results...")
#		print()
#		
#		try:
#			with con.cursor() as cur:
#				sql = 'SELECT a.Creator_id,a.Creator_name FROM CREATOR a INNER JOIN RHYME b ON a.Creator_id=b.Creator_id INNER JOIN likes c ON b.Rhyme_id=c.Rhyme_id GROUP BY a.Creator_id SORT BY COUNT(*) LIMIT {})'
#				cur.execute(sql.format(n))
#				rows = cur.fetchall()
#			print("Creator_id | Creator_name")
#			for row in rows:
#				print(row['Creator_id']," | ",row['Creator_name'],sep='')
#		except Exception as e:
#			print("Error received")
#			print(e)
			
	elif choice==-1:
		print("Bye")
		break
	
	else:
		print("Wrong input, please try again")
		
	print()
	tmp = input("press any key to continue>")
	if tmp is not None:
		tmp = sp.call('clear', shell=True)
		
con.close()