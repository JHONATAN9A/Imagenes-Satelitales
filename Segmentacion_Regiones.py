from skimage import data, io, segmentation, color
import matplotlib.pyplot as plt
#Lib. de RGB a GREY
from skimage.color import rgb2gray
#Lib. de Umbral
from skimage.filters import threshold_otsu
#lib. de filtro sobel
from skimage.filters import sobel
#Lib. de algor de cuencas.
from skimage import morphology
from scipy import ndimage as ndi
#Lib. de ecualizacion
from skimage import exposure
#Lib. Binarizacion
from skimage import img_as_uint

#Lib. Opencv
import cv2

#Lib. visualizar y datos
import matplotlib.pyplot as plt
import numpy as np



class CDARA():
    def __init__(self, img):
        self.img = img
        plt.imshow(self.img)
        plt.show() 

    def rgb_grey(self):
        self.grey = rgb2gray(self.img)
        #Transformacion de RGB  a escala de grises.
        plt.imshow(self.grey, cmap=plt.cm.gray)
        plt.show()

    def norm_equal(self):
        self.norm = cv2.normalize(self.grey, None, 0, 255, cv2.NORM_MINMAX)
        print(self.norm.min(), self.norm.max())
        #Se reliza la normalizacion de la imagen
        self.ecual = exposure.equalize_hist(self.grey)
        #Se realiza la ecualizacion del hsitograma
        plt.imshow(self.norm, cmap=plt.cm.gray)
        plt.show()

    def Histograma(self):
        plt.hist(self.grey.ravel(), bins= 256, color='black')
        plt.show()

        #plt.hist(self.ecual.ravel(), bins= 256, color='black')
        #plt.show()
        
    def filtro_sobel(self):
        self.filtro = sobel(self.norm)
        #se aplica un filtro de paso alto a la imagen.
        plt.imshow(self.filtro, cmap=plt.cm.gray)
        plt.show()
        
    def umbralizacion(self):
        self.markers = np.zeros_like(self.norm)
        self.markers[self.norm < 80] = 1
        self.markers[self.norm > 110] = 2
        plt.imshow(self.markers, cmap=plt.cm.gray)
        plt.show()

    def watershed(self):
        self.segmentation = morphology.watershed(self.filtro, self.markers)
        #Sobreposicion del Filtro y el Umbral
        plt.imshow(self.segmentation, cmap=plt.cm.gray)
        plt.show()
        self.segmentation = ndi.binary_fill_holes(self.segmentation - 1)
        #Segmentacion de regiones 
        plt.imshow(self.segmentation, cmap=plt.cm.gray)
        plt.show()
        cleaned = morphology.remove_small_objects(self.segmentation, 450)
        #Depuracion de informacion. 
        plt.imshow(cleaned, cmap=plt.cm.gray)
        plt.show()

        self.segmentacion = cleaned

    def save(self):
        binary = self.grey >= self.segmentacion
        io.imsave("Oput/segmentacion1.tif", img_as_uint(binary))
        #Guardar resultado
    
        

def Imagen():
    imagen = io.imread('Input\Zoon194.tif')
    return imagen

if __name__=="__main__":
    Segmentacion = CDARA(Imagen())
    Segmentacion.rgb_grey()
    Segmentacion.norm_equal()
    Segmentacion.Histograma()
    Segmentacion.filtro_sobel()
    Segmentacion.umbralizacion()
    Segmentacion.watershed()
    #Segmentacion.save() 




