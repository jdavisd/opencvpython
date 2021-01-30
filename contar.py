import cv2

class Contar:
      def __init__(self,imagen,tipo,contar):
         self.imagen=imagen
         self.tipo=tipo
         self.contar=contar
      def add(self): 
         image = cv2.imread(self.imagen)
         gaussian_3 = cv2.GaussianBlur(image, (9,9), 2)
         #unsharp_image = cv2.addWeighted(gaussian_3, 2, gaussian_3, -1, 0, self.imagen)    
         gray = cv2.cvtColor( gaussian_3 , cv2.COLOR_BGR2GRAY)
         canny = cv2.Canny( gray,10, 150)
         #canny = cv2.dilate(gaussian_3,None, iterations=1)
         #canny = cv2.erode(canny,None, iterations=1)
         cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         #cv2.drawContours(image, cnts, -1, (0,255,0), 3)
         for c in cnts:              
              epsilon = 0.01*cv2.arcLength(c,True)
              approx = cv2.approxPolyDP(c,epsilon,True)
              #print(len(approx))
              x,y,w,h = cv2.boundingRect(approx)
              if len(approx)==3 and self.tipo=='triangulo':
                  #cv2.putText(image,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
                  perimetro=cv2.arcLength(c,True)
                  #self.listaPeri.append(perimetro)               
                  print('triangulo')
              if len(approx)==4 and self.tipo=='cuadrado':
                  aspect_ratio = float(w)/h
                  #print('aspect_ratio= ', aspect_ratio)     
                  if aspect_ratio > 0.90 and aspect_ratio < 1.10 :
                      #cv2.putText(image,'Cuadrado',(x,y-5),1,1.5,(255,0,0),2)
                      perimetro=cv2.arcLength(c,True)
                      #self.listaPeri.append(perimetro)
                      self.contar=self.contar+1 
                                                                           
                  elif self.tipo=='rectangulo':
                      #cv2.putText(image,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
                   
                          print('rectangulo')                      
              if len(approx)==5 and self.tipo=='pentagono':
                   #cv2.putText(image,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
      
                    print('pentagono')                   
              if len(approx)==6 and self.tipo=='hexagono':
                   #cv2.putText(image,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
                
                    print('hexagono')                   
              if len(approx)>10 and self.tipo=='circulo':
                  #cv2.putText(image,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
             
                    print('circulo')    
         print('la cantidad encontrada es ',self.contar)            

  