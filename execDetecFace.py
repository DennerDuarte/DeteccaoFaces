import cv2

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

foto = cv2.imread("grupoPessoas.jpg")
foto_cinza = cv2.cvtColor(foto, cv2.COLOR_RGB2GRAY)
faces_detectadas = detector.detectMultiScale(foto,scaleFactor=1.02, minSize=(5,5), maxSize=(100,100))
print("Pessoas detectadas: ", len(faces_detectadas))

for x, y, l, a in faces_detectadas:
    #Arquivo da imagem, ponto incial, ponto final, cor, espessura em pixels
    foto = cv2.rectangle(foto, (x,y), (x+l, y+a), (0,0,255))

print(faces_detectadas)
cv2.imshow("Grupo de pessoas", foto)
cv2.waitKey()
