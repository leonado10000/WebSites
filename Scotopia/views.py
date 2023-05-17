from django.shortcuts import render
from datetime import datetime
from .models import Scotops,Tags
from .data import like as lk
# Create your views here.
import os

data = [
    [1,"15-05-2023","Idea test One",1001,["first","non-complete"],"Idiot A++",21],
    [2,"15-05-2023","Idea test One",1002,["first","non-complete"],"Idiot A+",5],
    [3,"15-05-2023","Idea test One",1003,["first","non-complete"],"Idiot B+",4],
    [4,"15-05-2023","Idea test One",1004,["first","non-complete"],"Idiot B-",5],
    [5,"15-05-2023","Idea test One",1005,["first","non-complete"],"Idiot C+",2],
    [6,"15-05-2023","Idea test One",1006,["first","non-complete"],"Idiot C-",3],
    [7,"15-05-2023","Idea test One",1007,["first","non-complete"],"Idiot D+",2],
    [8,"15-05-2023","Idea test One",1008,["first","non-complete"],"Idiot D-",4]
]


def openandwrite():
    lke = open('C:\\Users\\rjdis\\OneDrive\\Documents\\GitHub\\WebSites\\Scotopia\\data.py','r')
    likes=""
    exec(lke.readline())
    print(likes)

    # lk = open('C:\\Users\\rjdis\\OneDrive\\Documents\\GitHub\\WebSites\\Scotopia\\data.py','w')
    # lk.write(like + "like = {'4043':23}")

    # lk = open('C:\\Users\\rjdis\\OneDrive\\Documents\\GitHub\\WebSites\\Scotopia\\data.py','r')
    # exec(lk.read())
    # print(like)




#==================================================================================================================================
#==================================================================================================================================
# sc_id = ""
# sc_date = ""
# sc_name = ""
# sc_tags = ["A"]
# sc_auther = ""
# sc_likes = 1
#==================================================================================================================================
#   this funtion assisgns the abouve dummy globale varialbles any usefull and accurate data 
#   This right now can work two ways 
#   a) If all the entries are accuratly stored in the database Try: Directly call for Object with the given ID and assign all of them
#   b) If not then dummy entrys are available in a list of lists in a variable data
def getdetailbyID(n):
    print(n)
    try:
        obj = Scotops.objects.get(scoto_id=int(n))
        
        print("=====================================================")
        sc_id = n
        sc_date = obj.scoto_datetime
        sc_name = obj.scoto_name
        sc_tags = ["empty"]
        print(obj.scoto_tag)
        sc_auther = obj.scoto_auther
        sc_likes = 1
        # sc_likes = lk[n]
        
    except:
        index = int(n)- 1001
        print(index)
        sc_date = data[index][1]
        sc_name = data[index][2]
        sc_tags = data[index][4]
        sc_auther = data[index][5]
        sc_likes = lk[n]
    return [str(sc_date)[0:10],sc_name,sc_tags,sc_auther,sc_likes]



#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#   this funtion return a list of list where the later list contains details for most favourite entries
# DUring each run of the for loop a new list will be set and append to final list 
def createRanksEntries():
    s = sorted(lk.items(), key =lambda x: x[1],reverse=True)
    ScotoEntryList = []
    rank = 1
    EntryList = []
    n = min(10,len(s))


    for i in range(n):
        De = getdetailbyID(s[i][0])
        EntryList.append(rank) # rank
        EntryList.append(De[0]) # date
        EntryList.append(De[1]) # name
        EntryList.append(s[i][0]) #id
        EntryList.append(De[2]) # tags
        EntryList.append(De[3]) #auther
        EntryList.append(s[i][1]) #likes
        ScotoEntryList.append(EntryList) 
        EntryList = []
        rank+=1
        
    return ScotoEntryList


#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#   Simi;ar to the above funtion this funtion return a list of list where the later list contains details for most Latest entries
#   DUring each run of the for loop a new list will be set and append to final list
#   Only difference is the amount of data in eac entry is only three which all are accessed through the model objects of the objects 

# TO find the latest entry we just call all the objects put each ID in a templist and sort to last 10 of them
#   Automatically when the system will create a new entry it will be +1 to the last entry
def createLatestEntries():
    L = Scotops.objects.all()
    tempList = [] # for temp max id's
    for i in L:
        tempList.append(i.scoto_id)
    tempList.sort(reverse=True)
    n = min(10,len(tempList))
    EntryList = []
    ScotoEntryList = []


    for i in range(n):
        De = getdetailbyID(tempList[i])
        EntryList.append(De[1]) # name
        EntryList.append(tempList[i]) #id
        EntryList.append(De[3]) #auther
        ScotoEntryList.append(EntryList) 
        EntryList = []
    return ScotoEntryList



#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#   This funtion creates two lists of entries A: by rank B:latest ones
#   Then loads the main Scoto page
def scoto(request):
    openandwrite()
    A = createRanksEntries()
    B = createLatestEntries()
    return render(request, 'Scotopia.html',{
        "data_scoto":A,
        "data_latest":B
    })


#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
# Load a general page
def idea(request,page_id):
    try:
        data = Scotops.objects.get(scoto_id=page_id)
        return render(request, "Idea.html",{
            "iid":data.scoto_id,
            "iname":data.scoto_name,
            "iidea":data.scoto_idea_brief,
            "icont":data.scoto_idea_details,
            "iauther":data.scoto_auther,
            "idate":data.scoto_datetime,
            "itags":data.scoto_tag,
            "ilikes":lk[str(data.scoto_id)]
        })
    except :
        pass