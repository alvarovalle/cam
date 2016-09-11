from core import BytesDaImagem,Imprima

bytesDaImagem = BytesDaImagem('cam_data.pkl')
bytesDaImagem.calcula()
bytesDaImagem.refazImagem()
imprima = Imprima(480,640,bytesDaImagem)
imprima.show()