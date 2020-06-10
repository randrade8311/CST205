from PIL import Image
import hw1_hist_plotter as hp
import pickle

le = Image.open("images/cow1.jpg")

def task2(my_file):
	list=[]
	redlist=[]
	greenlist=[]
	bluelist=[]
	for x in range(len(my_file)):
		for y in range(len(my_file[x])):
			redlist.append(my_file[x][y][0])
			greenlist.append(my_file[x][y][1])
			bluelist.append(my_file[x][y][2])
	list.append(redlist)
	list.append(greenlist)
	list.append(bluelist)
	return list

listHist = le.histogram()

with open(str(listHist), 'rb') as pickle_file:
	my_file = pickle.load(pickle_file)

hp.hist_plotter(task2(my_file))


"""def entropy(signal):
    '''
    function returns entropy of a signal
    signal must be a 1-D numpy array
    '''
    lensig=signal.size
    symset=list(set(signal))
    numsym=len(symset)
    propab=[np.size(signal[signal==i])/(1.0*lensig) for i in symset]
    ent=np.sum([p*np.log2(1.0/p) for p in propab])
    return ent
"""
#le.show()

#print(dir(le))

#print(len(le.histogram()))


"""(le.thumbnail((100,100))

le.show())"""

#im = Image.new("RGB", (le.width, le.height))

#im.entropy(le, 5)

#im.show()