from PIL import Image
import pickle
import pdb

class BytesDaImagem:
    pesos = []
    dados = []
    comprimento = 0
    maiorPeso = -1
    menorPeso = 999999
    altura = 0
    def __init__(self, nomeDoArquivo):
        with open(nomeDoArquivo, 'rb') as input:
            cam_data = pickle.load(input)
            if cam_data[0]:
                self.comprimento = cam_data[1].__len__()
                for x in range(cam_data[1].__len__()):
                    colunas = []
                    colunasPesos = []
                    if self.altura == 0:
                        self.altura = cam_data[1][x].__len__()
                    for y in range(cam_data[1][x].__len__()):
                        colunas.append((cam_data[1][x][y][0],cam_data[1][x][y][1],cam_data[1][x][y][2]))
                        colunasPesos.append(0)                          
                    self.dados.append(colunas)
                    self.pesos.append(colunasPesos)



    def calcula(self):
        for x in range(self.comprimento):
            for y in range(self.altura):
                self.calculaPesos(x,y)


    def calculaPesos(self,w,h):
        if(w-1>=0)and(h-1>=0)and(w+1<self.comprimento)and(h+1<self.altura):
            self.pesos[w][h] = self.calculaCore(w,h)
        else:
            self.pesos[w][h] = 0

    def calculaCore(self,w,h):
        peso = []
        for rgb in [ 0, 1, 2 ]:
            peso.append(0)
            for x in [ -1, 0, 1 ]:
                for y in [ -1, 0, 1 ]:
                    peso[rgb] += abs(self.dados[w][h][rgb] - self.dados[w+x][h+y][rgb]) 

        pesoTotal = peso[0]+peso[1]+peso[2];
        if self.maiorPeso < pesoTotal:
            self.maiorPeso = pesoTotal
        if self.menorPeso > pesoTotal and pesoTotal > 0:
            self.menorPeso = pesoTotal            
        return pesoTotal
    def refazImagem(self):
        media = ((self.maiorPeso - self.menorPeso)/2)
        for x in range(self.comprimento):
            for y in range(self.altura):
                if self.pesos[x][y] > media:
                    self.dados[x][y] = (255,0,0)
                elif self.pesos[x][y] > media / 2:
                    self.dados[x][y] = (0,255,0)
                else:
                    self.dados[x][y] = (0,0,255)


class Imprima:
    _pixels = []
    _img = 0  
    def __init__(self,w,h,bytesDaImagem):
        self._img = Image.new( 'RGB', (w,h), "black") # create a new black image
        self._pixels = self._img.load() # create the pixel map
        if(bytesDaImagem):
            for x in range(w):
                for y in range(h):
                    self._pixels[x,y] = bytesDaImagem.dados[x][y]
        


    def show(self):
        self._img.show()
        