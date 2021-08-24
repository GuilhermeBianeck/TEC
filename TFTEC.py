from pathlib import Path
import sys

comando = list()
pathName = Path("in/") #SET .IN FILE FOLDER 

class add:
    def __init__(self, cur_st, cur_sy, new_sy, di, new_st):
        self.cur_st = cur_st #Current State
        self.cur_sy = cur_sy #Current Symbol
        self.new_sy = new_sy #New Symbol
        self.di = di #Direction
        self.new_st = new_st #New State

class Turing:
    def __init__(self,tm_ty, st, op):
        self.ty = tm_ty #TYPE
        self.st = st #STATES
        self.op = op #OPERATION
        self.ini = "0" #INITIAL STATE

def nf(turing, new_tm): #newfile Creates New File with Turing Machine Data
    with open(cur_file.name.split(".")[0] + "." + "out", 'w') as new_data:
        sys.stdout = new_data
        print(";" + str(new_tm.ty))
        for op in new_tm.op:
                print(str(op.cur_st) + " " + str(op.cur_sy) + " " + str(op.new_sy) + " " + str(op.di) + " " + str(op.new_st))


def SI(turing):

    turing.ty = "I"

    #mudar o número do estado com 1 para criar um novo estado 0 que prepara a fita
    for op in turing.op:
        op.cur_st = op.cur_st + "1"
        op.new_st = op.new_st + "1"

    new_st = list()
    for st in turing.st:
        new_st.append(st + "1")

    turing.st = new_st

    #para todo estado uma regra que caso leia # voltar para a fita
    for st in turing.st:
        turing.op.append(add(st,"§","§","r",st))

    #comando para colocar # no começo da fita
    turing.op.insert(0,add(0,"*","*","l","estado "))
    turing.op.insert(1,add("estado ","_","§","r",turing.ini+"1")) #voltar para o estado inicial original

    return turing

#colocar símbolo especial # no começo da fita, mover fita uma casa para a direita quando chega em #
def IS(turing):

    turing.ty = "S"

    #mudar o número do estado com 1 para criar um novo estado 0 que prepara a fita
    for op in turing.op:
        op.cur_st = op.cur_st + "1"
        op.new_st = op.new_st + "1"

    new_st = list()
    for st in turing.st:
        new_st.append(st + "1")

    turing.st = new_st

    #primeiro espaço:
    #dependendo do que lê (1 ou 0) vai para estados intermediários para manter a informação salva enquanto move fita
    turing.op.insert(0,add(0,"1","§","r","estado 1")) #1
    turing.op.insert(1,add(0,"0","§","r","estado 2")) #0
    turing.op.insert(2,add("estado 1","1","_","l","estado 3")) #11
    turing.op.insert(3,add("estado 1","0","_","l","estado 4")) #10
    turing.op.insert(4,add("estado 2","1","_","l","estado 5")) #01
    turing.op.insert(5,add("estado 2","0","_","l","estado 6")) #00
    turing.op.insert(6,add("estado 3","§","§","r","estado 3")) #11
    turing.op.insert(7,add("estado 3","_","_","r","estado 3")) #11
    turing.op.insert(8,add("estado 3","1","1","r","estado 7")) #11
    turing.op.insert(9,add("estado 3","0","1","r","estado 8")) #10
    turing.op.insert(10,add("estado 4","§","§","r","estado 4")) #10
    turing.op.insert(11,add("estado 4","_","_","r","estado 4")) #10
    turing.op.insert(12,add("estado 4","1","1","r","estado 9")) #01
    turing.op.insert(13,add("estado 4","0","1","r","estado 10")) #00
    turing.op.insert(14,add("estado 5","§","§","r","estado 5")) #01
    turing.op.insert(15,add("estado 5","_","_","r","estado 5")) #01
    turing.op.insert(16,add("estado 5","1","0","r","estado 7")) #11
    turing.op.insert(17,add("estado 5","0","0","r","estado 8")) #10
    turing.op.insert(18,add("estado 6","§","§","r","estado 6")) #00
    turing.op.insert(19,add("estado 6","_","_","r","estado 6")) #00
    turing.op.insert(20,add("estado 6","1","0","r","estado 9")) #01
    turing.op.insert(21,add("estado 6","0","0","r","estado 10")) #00
    turing.op.insert(22,add("estado 7","_","1","r","estado 11")) #1
    turing.op.insert(23,add("estado 7","1","1","r","estado 7")) #11
    turing.op.insert(24,add("estado 7","0","1","r","estado 8")) #10
    turing.op.insert(25,add("estado 8","_","1","r","estado 12")) #0
    turing.op.insert(26,add("estado 8","1","1","r","estado 9")) #01
    turing.op.insert(27,add("estado 8","0","1","r","estado 10")) #00
    turing.op.insert(28,add("estado 9","_","0","r","estado 11")) #1
    turing.op.insert(29,add("estado 9","1","0","r","estado 7")) #11
    turing.op.insert(30,add("estado 9","0","0","r","estado 8")) #10
    turing.op.insert(31,add("estado 10","_","0","r","estado 12")) #0
    turing.op.insert(32,add("estado 10","1","0","r","estado 9")) #01
    turing.op.insert(33,add("estado 10","0","0","r","estado 10")) #00
    turing.op.insert(34,add("estado 11","_","1","l","estado 13")) #
    turing.op.insert(35,add("estado 12","_","0","l","estado 13")) #
    turing.op.insert(36,add("estado 13","*","*","l","estado 13")) #
    turing.op.insert(37,add("estado 13","_","_","r",turing.ini+"1")) #voltar para o estado inicial original  

    #rotine otina de espaço para cada estado
    #para qualquer estado, caso leia # então mover, colocar _ e empurrar fita para a direita
    for st in turing.st:
        turing.op.append(add(st,"§","§","r",str(st)+"rotine "))
        turing.op.append(add(str(st)+"rotine ","_","_","r",str(st)+"rotine "))
        turing.op.append(add(str(st)+"rotine ","1","_","r",str(st)+"rotine 1")) #1
        turing.op.append(add(str(st)+"rotine ","0","_","r",str(st)+"rotine 2")) #0
        turing.op.append(add(str(st)+"rotine 1","1","1","r",str(st)+"rotine 1")) #1
        turing.op.append(add(str(st)+"rotine 1","0","1","r",str(st)+"rotine 2")) #0
        turing.op.append(add(str(st)+"rotine 1","_","1","r",str(st)+"rotine 3")) #
        turing.op.append(add(str(st)+"rotine 2","1","0","r",str(st)+"rotine 1")) #1
        turing.op.append(add(str(st)+"rotine 2","0","0","r",str(st)+"rotine 2")) #0
        turing.op.append(add(str(st)+"rotine 2","_","0","r",str(st)+"rotine 3")) #
        turing.op.append(add(str(st)+"rotine 3","*","*","l",str(st)+"rotine 3")) #
        turing.op.append(add(str(st)+"rotine 3","§","§","r",st)) #
    
    return turing

if __name__ == "__main__":
    
    file_directory = pathName
    for cur_file in file_directory.iterdir():
        if cur_file.is_file():
            with open(cur_file, 'r') as data_file:
                lines = [line[:-1] for line in data_file]
                for line in lines:
                    if line[0] == ';':
                        mt_ty = line[1]
                    else:
                        line_data = [x for x in line.split(" ")]
                        comando.append(add(line_data[0],line_data[1],line_data[2],line_data[3],line_data[4]))

                st = set([x.cur_st for x in comando])
                turing = Turing(mt_ty, st, comando)

                if(turing.ty == "I"):
                    new_tm = IS(turing)
                elif(turing.ty == "S"):
                    new_tm = SI(turing)

                nf(turing, new_tm) #New File With Turing
                

                comando.clear()