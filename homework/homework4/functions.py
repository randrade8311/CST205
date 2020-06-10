from glob import glob
def getPicDict():
    dates_dict = {'names': []}
    for x in glob('static/*.jpg'):
        name = glob(x)
        name = name[0].lstrip('static\\')
        dates_dict['names'].append(name)
    return dates_dict