from mysql_dbconnect import *
import gc


data = [
["Brijesh","Vala","BV","000","B1","8"],
["Warish","Patel","WP","000","B2","8"],
["Darshna","Parmar","DP","001","B1","8"],
["Nirali","Naik","NN","001","B2","8"],
["Harshal","Shah","HS","002","B3","8"],
["Tanaya","Ganguly","TG","002","B3","8"],
["Jayanthi","J","JJ","003","B4","8"],
["Makhduma","Saiyad","MS","004","B2","6"],
["Tanaya","Ganguly","TG","004","B3","6"],
["Anil","Patel","AP","004","B1","6"],
["Nisha","Panchal","NP","004","B6","6"],
["Ankita","Gandhi","AG","005","B1","6"],
["Manoranjan","Behra","MB","005","B2","6"],
["Mitali","Acharya","MA","005","B3","6"],
["Mitali","Acharya","MA","005","B6","6"],
["Darshna","Parmar","DP","005","B4","6"],
["Parth","Singh","PS","005","B5","6"],
["Khushali","Mistry","KM","006","B3","6"],
["Khushali","Mistry","KM","006","B6","6"],
["Abhijitsinh","Parmar","AP","006","B1","6"],
["Abhijitsinh","Parmar","AP","006","B4","6"],
["Neeshu","Chaudhari","NC","006","B2","6"],
["Neeshu","Chaudhari","NC","006","B5","6"],
["Hetal","Bhaidasa","HB","007","B1","6"],
["Hetal","Bhaidasa","HB","007","B6","6"],
["Ankit","Chouhan","AC","007","B2","6"],
["Ankit","Chouhan","AC","007","B4","6"],
["Ashish","Patel","AP","007","B3","6"],
["Poonam","Naik","PN","007","B5","6"],
["Anju","Kakkad","AK","008","B6","6"],
["Rasika","Thakre","RT","009","B4","6"],
["Rasika","Thakre","RT","009","B5","6"],
["Shital","Pathar","SP","010","B1","6"],
["Shital","Pathar","SP","010","B4","6"],
["Jaydeep","Viradiya","JV","010","B2","6"],
["Jaydeep","Viradiya","JV","010","B3","6"],
]

faculty_new_data = [
[1, "Brijesh Vala", "BV", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[2, "Warish Patel", "WP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[3, "Darshna Patmar","DP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[4, "Nirali Naik", "NN","PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[5, "Harshal Shah", "HS", "PIET", "CSE", "Professor", "@", "123", "img"],
[6, "Tanaya Ganguly", "TG", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[7, "Jayanti J", "JJ", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[8,"Makhduma Saiyad","MS", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[9, "Anil Patel", "AP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[10,"Nisha Panchal", "NP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[11,"Ankita Gandhi", "AG", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[12, "Manornajan Behra","MB", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[13, "Mitali Acharya", "MA", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[14, "Parth Singh", "PS", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[15, "Khushali Mistry", "KM", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[16, "Abhijitsingh Parmar","ASP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[17, "Neeshu Chaudhari", "NC", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[18, "Hetal Bhaidasa","HB","PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[19, "Ankit Chouhan","AC", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[20, "Ashish PAtel", "AP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[21, "Poonam Naik","PN", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[22, "Anju Kakkad", "AK", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[23, "Rasika Thakre", "RT", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[24, "Shital Pathar", "SP", "PIET", "CSE", "Assistant Professor", "@", "123", "img"],
[25, "Jaydeep Viradiya", "JV", "PIET", "CSE", "Assistant Professor", "@", "123", "img"]
]

semester = "8"
c, conn = connect_to("pumis")
c.execute("SELECT class FROM semester_info WHERE semester=(%s)", (semester))
x = c.fetchall()
l = list()
for i in x:
    l.append(i[0])
print(l)
