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
    
    #print Simpul
    def printSimpul(self):
       print(list(self.dictgraf.keys())) 

    def getInDegree(self,simpul):
        return len(self.dictgraf[simpul])

    def getAllZeroInDegree(self):
        count = 0
        for simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) == 0:
                count +=1
        return count
    def getZeroInDegree(self):
        for simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) == 0:
                return simpul

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

    # get Degree

#MAIN DRIVER

#read file
p =[]
#filename = input("filename (with extension): ")

#pokokna ini mah masukin text di file ke array  formatnya[['C1','C3'],['C2','C1','C4']]
with open("case.txt") as f:
    lines = [line.rstrip().rstrip(".").replace(", ","") for line in f]
for item in lines:
    out = [(item[i:i+2]) for i in range(0, len(item), 2)]   
    p.append(out)


#sekarang inisiasi graf kosong

grf = graf()

#masukin semua simpul dan sisi ke graf
for array in range(len(p)):
    grf.addSimpul(p[array][0])
    tempsimpul = p[array][0]
    del p[array][0]
    for isiarray in range(len(p[array])):
        grf.addSisi(p[array][isiarray],tempsimpul)
# grf.printSisi()
# grf.printSimpul()

#topologi sortnya disini
answer = []
loop = grf.getAllZeroInDegree()
def TopSort(answer):
    simpulzero = grf.getZeroInDegree()
    grf.delSisi(simpulzero)
    grf.delSimpul(simpulzero)
    answer.append(simpulzero)
for i in range(loop):
    #ambil simpul yang degreenya 0


# udah bisaaaaa tapi gatau ngeprintnya gmn wkwkwk   




#answer.append(simpulzero)

# for i in range(len(answer)):
#     print("Semester", i+1,end=": ")
#     print(answer[i])    