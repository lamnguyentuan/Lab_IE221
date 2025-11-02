
def printNV(dsNV : list): 
    for nv in dsNV:
        print(list(nv.values()))

    list(map(print, dsNV))
    list(map(lambda nv:print(list(nv.values())), dsNV))

def tinhLuongHT(ds:list):
    for nv in ds:
        if 'soNG' in nv:
            nv['luongNV'] = 1
        
        elif nv.get('soSP', 0) > 0:
            nv['luongHT'] = 2
        



if __name__ == "__main__":

studentList = [

]

