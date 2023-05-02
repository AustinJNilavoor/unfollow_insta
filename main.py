f1 = open("following.html", "r")
f2 = open("followers.html", "r")
f3 = open("exclude.txt", "r")
f4 = open("unfollowed.txt", "w")
followingFile = f1.read()
followersFile = f2.read()
exclude = f3.read().splitlines()
followers = []
following = []
diff = []
key = ""
lenFollowers = len(followersFile)
lenFollowing = len(followingFile)

def listFollowers(p):
    key = ""
    c= 0
    item = ''
    for x in range(p,lenFollowers):
        if(followersFile[x] == "<"):
            for i in range(0,24):
                if(x+i<lenFollowers):
                    if(followersFile[x+i] == 'd'):
                        break
                    key += str(followersFile[x+i])
            if(key == '<a target="_blank" href='):
                k = x+24
                while(followersFile[k] != '>'):
                    k+=1
                while(followersFile[k+1] != '<'):
                    item += followersFile[k+1]
                    k+=1
                followers.append(item)
                c+=1
            key = ""
            item = ""

def listFollowing(p):
    key = ""
    c= 0
    item = ''
    for x in range(p,lenFollowing):
        if(followingFile[x] == "<"):
            for i in range(0,24):
                if(x+i<lenFollowing):
                    if(followingFile[x+i] == 'd'):
                        break
                    key += str(followingFile[x+i])
            if(key == '<a target="_blank" href='):
                k = x+24
                while(followingFile[k] != '>'):
                    k+=1
                while(followingFile[k+1] != '<'):
                    item += followingFile[k+1]
                    k+=1
                following.append(item)
                c+=1
            key = ""
            item = ""


for x in range(lenFollowers):
    if(followersFile[x] == "<"):
        for i in range(0,5):
            key += str(followersFile[x+i])
        if(key == '<body'):
            listFollowers(x)
            break
            
        key = ""
for x in range(lenFollowing):
    if(followingFile[x] == "<"):
        for i in range(0,5):
            key += str(followingFile[x+i])
        if(key == '<body'):
            listFollowing(x)
            break
            
        key = ""

for l in following:
    if (l not in followers and l not in exclude):
        diff.append(l)
for x in diff:
    f4.write(x+'\n')

f1.close()
f2.close()
f3.close()
f4.close()

