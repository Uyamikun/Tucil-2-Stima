#structure graf
class graf:
    #constructor
    def __init__(self,dictgraf = None):
        #inisialisasi dictionary
        if dictgraf is None:
            dictgraf = {}
        self.dictgraf = dictgraf
 
    #METHOD

    #METHOD SIMPUL

    #add simpul
    def addSimpul(self,simpul):
        if simpul not in self.dictgraf:
            self.dictgraf[simpul] = []

    # delete simpul
    def delSimpul(self,simpul):
        if simpul in self.dictgraf:
            del self.dictgraf[simpul]
    
    # get banyak simpul
    def getSimpul(self):
        return len(self.dictgraf.keys())

    # print Simpul
    def printSimpul(self):
       print(list(self.dictgraf.keys())) 

    # get derajat masuk
    def getInDegree(self,simpul):
        return len(self.dictgraf[simpul])

    #ambil semua simpul berderajat 0 masukan kedalam list
    def getZeroInDegree(self):
        templist = []
        for simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) == 0:
                templist.append(simpul)
        return templist

    #METHOD SISI

    #add sisi
    def addSisi(self, sisi,simpul):
        if simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) ==0:
                self.dictgraf[simpul] = [sisi]
            else:
                self.dictgraf[simpul].append(sisi)
    
    #delete sisi
    def delSisi(self,sisi):
        tempval = sisi
        list2 ={simpul: [a for a in sisina if a not in tempval] for simpul,sisina in self.dictgraf.items()}
        self.dictgraf = list2

    #print sisi
    def printSisi(self):
        print(list(self.dictgraf.values()))


# Topological Sort
#ambil semua simpul yang nol degree innya
#delSisi
#delSimpul
#masukin simpul derajat nol ke array
def TopSort(answer):
    tempsimp = grf.getZeroInDegree()
    arrsimpul = []
    for i in tempsimp:
        simpulzero = i
        grf.delSisi(simpulzero)
        grf.delSimpul(simpulzero)
        arrsimpul.append(simpulzero)
    if len(arrsimpul) != 0:
        answer.append(arrsimpul)


#MAIN DRIVER
#inisialisasi array
p =[]
p2 = []

#read file
#append ke list dengan formatnya[['C1','C3'],['C2','C1','C4']]
filename = input("enter filename (with extension): ")
with open(filename) as f:
    lines = [line.rstrip().replace(".",",").replace(" ","")for line in f]
for item in lines:
    realitem = item.split(",")
    for k in realitem:
        if k != "":
            p2.append(k)
    p.append(p2)
    p2 = []


#inisiasi graf kosong
grf = graf()

#masukin semua simpul dan sisi ke graf
for array in range(len(p)):
    grf.addSimpul(p[array][0])
    tempsimpul = p[array][0]
    del p[array][0]
    for isiarray in range(len(p[array])):
        grf.addSisi(p[array][isiarray],tempsimpul)

#Olah data memakai Topological Sort
answer = []
for i in range(8):
    TopSort(answer)

#Handle yang ga bisa petakan
if grf.getSimpul() == 0:
    for x in range(len(answer)):
        print("Semester", x+1,":",end=" ")
        for i in range(len(answer[x])):
            if i == len(answer[x])-1:
                print(answer[x][i])
            else:
                print(answer[x][i],end=", ")
else:
    print("Tidak bisa menata mata kuliah")
    print("Semester tidak cukup (>8 semester)")
print("")
input("-----Press any key to continue-----")