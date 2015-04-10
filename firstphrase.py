from numpy import *

def geticatenumber():
    frcate = open('tianchi_mobile_recommend_train_user/tianchi_mobile_recommend_train_user.csv')
    catelist = list()
    usrlist = list()
    catedat = str()
    usrdat = str()
    title = frcate.readline()
    for line in frcate.readlines():
	    linelist = line.strip().split(',')
	    if linelist[4] not in catelist:
		    catelist.append(linelist[4])
		    catedat = catedat + linelist[4] + '\r\n'
	    if linelist[0] not in usrlist:
		    usrlist.append(linelist[0])
		    usrdat = usrdat + linelist[0] + '\r\n'
    catenumber = len(catelist)
    usrnumber = len(usrlist)
    wrcate = open('preparatondata/category.dat','wb')
    wrusr = open('preparationdata/usr.dat','wb')
    wrcate.write(catedat)
    wrusr.write(usrdat)
    wrcate.flush()
    wrusr.flush()
    wrcate.close()
    wrusr.close()
    return catenumber,catelist,usrnumber,usrlist

def getpcatenumber():
    frcate = open('tianchi_mobile_recommend_train_item.csv')
    catelist = list()
    title = frcate.readline()
    for line in frcate.readlines():
	    linelist = line.strip().split(',')
	    if linelist[2] not in catelist:
		    catelist.append(linelist[2])
    catenumber = len(catelist)
    return catenumber,catelist

def creatematrix():
    catenumber,catelist,usrnumber,usrlist = geticatenumber()
    trainmat = zeros((usrnumber,catenumber))
    frtrain = open('tianchi_mobile_recommend_train_usr/tianchi_mobile_recommend_train_usr.csv')
    title = frtrain.readline()
    for line in frtrain.readlines():
	    linelist = line.strip.split(',')



