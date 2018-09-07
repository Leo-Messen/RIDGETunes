import math
import os
import csv
import sys
import random

def m_to_s(a):
    return((int(a[0]+a[1])*60)+int(a[3]+a[4]))

def m_plus_m(a,b):
    t_seconds = m_to_s(a)+m_to_s(b)
    if int(math.floor(t_seconds/60))< 10:
        start="0"+str(int(math.floor(t_seconds/60)))
    else:
        start=str(int(math.floor(t_seconds/60)))
    return(str(start)+":"+str(t_seconds%60))

def s_to_m(a):
    if int(math.floor(a/60))< 10:
        start="0"+str(int(math.floor(a/60)))
    else:
        start=str(int(math.floor(a/60)))
    if a%60<10:
        end="0"+str(a%60)
    else:
        end=str(a%60)
    return(str(start)+":"+str(end))
    
loggedin=False
while loggedin==False:
    users=open("users.csv","r+",newline="\n")
    readusers=csv.reader(users,delimiter=',')
    writeusers=csv.writer(users,delimiter=',')
    status=input("Enter '1' to log in, '2' to register an account or type 'exit' to quit RIDGETunes:")

    if status.upper()=="EXIT":
        print("Goodbye")
        sys.exit()

    elif status=="1":
        username=input("Username(case sensitive):")
        password=input("Password(case sensitive):")
        for row in readusers:
            if row[0]==username and row [1]==password:
                print("Log-in successful")
                loggedin=True

        if loggedin==False:
            print("Your log-in details weren't found, please register an account or try again making sure that your username and password are spelt correctly.")

    elif status=="2":
        taken=True
        while taken==True:
            triggered=False
            newuser=input("Please enter your desired username:")
            for row in readusers:
                if newuser==row[0]:
                    print("That username is already taken, pick another one.")
                    triggered=True
                    
            if triggered==False:
                taken=False

        same=False
        while same==False:
            newpassword=input("Enter a password:")
            passwordcheck=input("Re-enter your password:")
            if newpassword==passwordcheck:
                same=True
            else:
                print("Your passwords didn't match, try again.")        
            
        newDOB=input("Enter your date of birth in the form DD/MM/YYYY:")   
        newartist=input("Who is your favourite artist?:")
        newgenre=input("What is your favourite genre?:")
            
        users.write(newuser+","+newpassword+","+newDOB+","+newartist+","+newgenre+"\n")
        users.close()
    else:
        print("Please only enter '1' or '2'")
users.close()            

if not os.path.exists(username):
    os.makedirs(username)
                
while True:
    with open("options.txt")as options:
        print(options.read())
    songs=open("songs.csv","r")
    readsongs=csv.reader(songs,delimiter=',')
    users=open("users.csv","r+",newline="\n")
    readusers=csv.reader(users,delimiter=',')
    choice=input("Please select an option:")

    if choice=="1":
        sys.exit()

    elif choice=="2":
        with open("tempusers.csv","w",newline="\n") as temp:
            change=input("Who is your new favourite artist?:")
            for row in readusers:
                if username==row[0]:
                    temp.write(row[0]+","+row[1]+","+row[2]+","+change+","+row[4]+"\n")
                else:
                    temp.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+"\n")
        users.close()
        os.remove("users.csv")
        os.rename("tempusers.csv","users.csv")
        print("Done.")        
    elif choice=="3":
        with open("tempusers.csv","w",newline="\n") as temp:
            change=input("What is your new favourite genre?:")
            for row in readusers:
                if username==row[0]:
                    temp.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+change+"\n")
                else:
                    temp.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+"\n")
        users.close()
        os.remove("users.csv")
        os.rename("tempusers.csv","users.csv")
        print("Done.")
        
    elif choice=="4":
        lst=[]
        count=0
        for row in readsongs:
            lst.append(row[0])
        sort_list=sorted(lst,key=str.upper)
        print("Name-Artist-Length")
        while True:
            songs.close()
            songs=open("songs.csv","r")
            readsongs=csv.reader(songs,delimiter=',')
            for row in readsongs:
                if count==len(sort_list):
                    break
                elif row[0]==sort_list[count]:
                    print(row[0],"-",row[1],"-",row[3])
                    count=count+1
            if count==len(sort_list):
                    break
               
    elif choice=="5":
        while True:
            playlist=input("What would you like to call your new playlist?:")
            if not os.path.exists(username):
                os.makedirs(username)
            if not os.path.exists(username+'/'+playlist+".csv"):
                with open(username+'/'+playlist+".csv","a",newline="\n") as newplaylist:
                    while True:
                        songs.close()
                        songs=open("songs.csv","r")
                        readsongs=csv.reader(songs,delimiter=',')
                        add=input("Pick a song to add to your playlist? (or type 'save' to finish creating your playlist):")
                        if add.upper()=="SAVE":
                            break
                        else:
                            added=False
                            for row in readsongs:
                                if add.upper()==row[0].upper():
                                    newplaylist.write(row[0]+","+row[1]+","+row[3]+"\n")
                                    print("Added.")
                                    added=True
                            if added==False:
                                print("That song isn't registered in our library.")
                    break
                
            else:
                print("You already have a playlist with that name, pick another name.")
                       
        newplaylist.close()

    elif choice=="6":
        print("Your saved playlists are:")
        f=os.listdir(username)
        for file in f:
            print(file[:-4])
        view=input("Which playlist would you like to view?:")
        there=False
        for file in f:
            if view+".csv"==file:
                there=True
                file=open(username+"/"+file,"r")
                readfile=csv.reader(file,delimiter=",")
                for row in readfile:
                    print(row[0]+"-"+row[1]+"-"+row[2])
                file.close()
        if there==False:
            print("That playlist wasn't found.")
    
    elif choice=="7":
        print("Your saved playlists are:")
        f=os.listdir(username)
        for file in f:
            print(file[:-4])
        view=input("Which playlist would you like to delete?:")
        there=False
        for file in f:
            if view+".csv"==file:
                there=True
                os.remove(username+"/"+file)
                print("Done.")
        if there==False:
            print("That isn't one of your saved playlists.")
        
    elif choice=="8":
        while True:
            time=input("Approximately how long would you like your playlist to last(e.g.09:35)?")
            name=input("What would you like to call it?:")
            if len(time) != 5:
                print("Please format your input like the example provided(mm:ss e.g. 08:27).")
            else:
                break
        time=m_to_s(time)
        elapsed=0
        lst=[]
        for row in readsongs:
            lst.append(row[0])
        b=False
        while True:
            songs.close()
            songs=open("songs.csv","r")
            readsongs=csv.reader(songs,delimiter=',')
            rand=random.choice(lst)
            playlist=open(username+"/"+name+".csv","a",newline="\n")
            for row in readsongs:
                if rand==row[0]:
                    if m_to_s(row[3])+elapsed<=time:
                        elapsed=m_to_s(row[3])+elapsed
                        playlist.write(row[0]+","+row[1]+","+row[3]+"\n")
                    else:
                        b=True
                        break
            if b==True:
                break
        print("The playlist generated is called",name,"and it lasts for",s_to_m(elapsed))
        playlist.close()               
                    
        
    elif choice=="9":
        count=0
        genre=input("At the moment we have 4 genres.Pop,Rap,Rock and Reggae.Which genre would you like your playlist to contain?:")
        if genre.lower() !="rap" and genre.lower()!="pop" and genre.lower()!="reggae" and genre.lower()!="rock":
            print("We don't have that genre.")
        else:
            name=input("What would you like to call it?:")
            playlist=open(username+"/"+name+".csv","a",newline="\n")
            lst=[]
            for row in readsongs:
                if genre.upper()==row[2].upper():
                    lst.append(row[0])
            for x in lst:
                if count==5:
                    break
                songs.close()
                songs=open("songs.csv","r")
                readsongs=csv.reader(songs,delimiter=',')
                for row in readsongs:
                    if row[0]==x:
                        count += 1
                        playlist.write(row[0]+","+row[1]+","+row[3]+"\n")
            playlist.close()
            print("Your playlist,",name,",has been created.")
        
    elif choice=="10":
        songs.close()
        songs=open("songs.csv","r")
        readsongs=csv.reader(songs,delimiter=',')
        artist=input("Which artist's songs would you like to compile?:")
        if os.path.exists(username+"/"+artist+" songs.txt"):
            os.remove(username+"/"+artist+" songs.txt")
        text=open(username+"/"+artist+" songs.txt","w")
        for row in readsongs:
            if row[1].upper()==artist.upper():
                text.write(row[0]+",")
        text.close()
        print("You can find the text file in your account's folder in the RIDGETunes folder.\nIf we have no songs by your artist the text file will be blank.")
        
    elif choice=="11":
        password=input("Enter the admin password:")
        with open("adminonly.txt","r") as admin:
            if password != admin.read():
                print("Access denied.")
            else:
                pop=0
                rock=0
                rap=0
                reggae=0
                p_count=0
                ro_count=0
                ra_count=0
                re_count=0
                for row in readsongs:
                    if row[2]=="Pop":
                        p_count += 1
                        pop=pop+m_to_s(row[3])
                        
                    elif row[2]=="Rock":
                        ro_count += 1
                        rock=rock+m_to_s(row[3])
                        
                    elif row[2]=="Reggae":
                        re_count += 1
                        reggae=reggae+m_to_s(row[3])
                        
                    elif row[2]=="Rap":
                        ra_count += 1
                        rap=rap+m_to_s(row[3])
                print("Average song length times in each genre:\nPop -",s_to_m(pop/p_count),"\nRock -",s_to_m(rock/ro_count),"\nRap -",s_to_m(rap/ra_count),"\nReggae -",s_to_m(reggae/re_count)) 
                    
    else:
        print("That isn't a valid option number, try again.")
        
        
        

    
