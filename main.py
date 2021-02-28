#bikin structure graf
#pake OOP kyknya gampang
#idenya pake dictionary aja
class graf:
    #bikin constructornya duls
    def __init__(self,dictgraf = None):
        #jangan lupa bikin inisialisasi dictnya
        if dictgraf is None:
            dictgraf = {}
        self.dictgraf = dictgraf
 
    #bikin methodnya bro
    #methodnya ada:
    #1.vertex simpul
    # nambah simpul
    def addSimpul(self,simpul):
        #klo ga ada simpul di dictnya,  add jadi keys dalam dictionary
        if simpul not in self.dictgraf:
            self.dictgraf[simpul] = []
    # delete simpul
    def delSimpul(self,simpul):
        if simpul in self.dictgraf:
            del self.dictgraf[simpul]
    
    def getSimpul(self):
        return len(self.dictgraf.keys())
    #print Simpul
    def printSimpul(self):
       print(list(self.dictgraf.keys())) 

    def getInDegree(self,simpul):
        return len(self.dictgraf[simpul])

    def countAllZeroInDegree(self):
        count = 0
        for simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) == 0:
                count +=1
        return count

    #ambil semua simpul berderajat 0 masukan kedalam list
    def getZeroInDegree(self):
        templist = []
        for simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) == 0:
                templist.append(simpul)
        return templist

    #2.edge sisi
    def addSisi(self, sisi,simpul):
        if simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) ==0:
                self.dictgraf[simpul] = [sisi]
            else:
                self.dictgraf[simpul].append(sisi)
            
    def delSisi(self,sisi):
        tempval = sisi
        list2 ={simpul: [a for a in sisina if a not in tempval] for simpul,sisina in self.dictgraf.items()}
        self.dictgraf = list2
    #     for simpul in self.dictgraf.keys():
    #         for value in self.dictgraf[simpul]:
    #                 for realvalue in value:
    #                     if realvalue == sisi:
    #                         del self.dictgraf[simpul]
    #                         print("Haloo")
    #                     i += 1                    
        #     for listvalue in tempsisi:
        #         for i in range(len(listvalue)):
        #             if listvalue[i] == sisi:
        #                 del listvalue[i]
        # print(self.dictgraf.items())
    #  print sisi
    def printSisi(self):
        print(list(self.dictgraf.values()))

        #for simpul in self.dictgraf.keys()):
        #      len(self.dictgraf.[i])
        #     if max < len
        

    # get Degree

#ambil semua simpul yang nol degree innya
#delSisi
#delSimpul
#masukin si simpul nol ke answer
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

#read file
p =[]
p2 = []
#pokokna ini mah masukin text di file ke array  formatnya[['C1','C3'],['C2','C1','C4']]
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


#sekarang inisiasi graf kosong
grf = graf()

#masukin semua simpul dan sisi ke graf
for array in range(len(p)):
    grf.addSimpul(p[array][0])
    tempsimpul = p[array][0]
    del p[array][0]
    for isiarray in range(len(p[array])):
        grf.addSisi(p[array][isiarray],tempsimpul)



#topologi sortnya disini

#######
answer = []
for i in range(8):
    TopSort(answer)
#dapet jawabannya
#cek masih ada isi array keys ga klo ada berarti error
#
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
# udah bisaaaaa tapi gatau ngeprintnya gmn wkwkwk   