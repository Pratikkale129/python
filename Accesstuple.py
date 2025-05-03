#1. Access Tuple Items
ashutosh = ("Shinchan","Doraemon","Bheem")
print(ashutosh[1])

#2. Negative Indexing
ashutosh = ("Shinchan","Doraemon","Bheem")
print(ashutosh[-1])

#3. Range of Indexes
ashutosh = ("Shinchan","Doraemon","Bheem","Pokemon","Hattori","MotuPatlu")
print(ashutosh[2:5])

#4. By leaving Range of Indexes
ashutosh = ("Shinchan","Doraemon","Bheem","Pokemon","Hattori","MotuPatlu")
print(ashutosh[:5])

ashutosh = ("Shinchan","Doraemon","Bheem","Pokemon","Hattori","MotuPatlu")
print(ashutosh[2:])

#5. Range of Megative Indexing
ashutosh = ("Shinchan","Doraemon","Bheem","Pokemon","Hattori","MotuPatlu")
print(ashutosh[-5:-2])

#6. Check If item Exists
ashutosh = ("Shinchan","Doraemon","Bheem","Pokemon","Hattori","MotuPatlu")
if "Doraemon" in ashutosh:
    print("Yes, 'Doraemon' is in the Cartoon tuple")
