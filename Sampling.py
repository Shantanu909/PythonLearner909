
#Python Code:

from matplotlib import pyplot as plt
import numpy as np 
from scipy import ndimage
from scipy import fftpack
import scipy
from numpy import exp 
import scipy.integrate  
from math import sqrt
from scipy import interpolate  
from scipy.interpolate import interp1d  
import scipy.misc as misc
from scipy import linalg



# #Task 1:Frequency in terms of Hertz
# fre  = 1
# fre_samp = 100
# t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
# a = np.sin(fre  * 2 * np.pi * t)
# t=np.linspace(0,1,10)
# A =fftpack.fft(a)
# frequency =fftpack.fftfreq(len(a))*fre
# plt.stem(frequency, np.abs(A),use_line_collection=True)
# plt.xlabel('Frequency in Hz')
# plt.ylabel('Frequency Spectrum Magnitude')
# plt.show()

# #SciPy integrate
 
# f = lambda x:exp(-x**2)  

# i = scipy.integrate.quad(f, 0, 1)  
# print(i)  

# #Task 2:Multiple Integrals
  
# f = lambda x, y :2*x*y  
# g =lambda x :0 
# h =lambda y :4*y**2 
# i=scipy.integrate.dblquad(f, 0, 0.5, g, h)  
# print(i)

# #Task 3:SciPy Interpolation

# x = np.linspace(0, 5, 10)  
# y = np.cos(x**2/3+4) 
# plt.scatter(x,y,c='r')  
# plt.show()  
# fun1 =interp1d(x, y,kind='linear')  
# fun2 =interp1d(x, y, kind ='cubic')  
# xnew =np.linspace(0, 4,30)  
# plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
# plt.legend(['data', 'linear', 'cubic','nearest'], loc ='best')  
# plt.show()
# fun1 =interp1d(x, y,kind='linear')  
# fun2 =interp1d(x, y, kind ='cubic')  
# xnew=np.linspace(3, 5,30)  
# plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
# plt.legend(['data', 'linear', 'cubic','nearest'], loc ='best')  
# plt.show()  


# #Task 4: Equations solving/Determinant
# a =np.array([[1, 2, -3], [2, -5, 4], [5, 4, -1]])   
# b =np.array([[-3], [13], [5]])   
# x =linalg.solve(a, b)   
# print(x)   
# print("\n Checking results,must be zeros")  
# print(a.dot(x) -b)  
# A =np.array([[1,2,9],[3,4,8],[7,8,4]])
# x =linalg.det(A)
# print('Determinant of \n{} \n is {}'.format(A,x))
# A =np.array([[2,1,-2],[1,0,0],[0,1,0]])
# values, vectors =linalg.eig(A)
# print(values)
# print(vectors)

#Task 5: Image Processing
face =scipy.misc.face()
plt.imshow(face)
plt.show()

#Crop image
face =scipy.misc.face()
lx,ly,channels=face.shape
crop_face=face[int(lx/4):int(-lx/4), int(ly/4):int(-ly/4)]
plt.imshow(crop_face)
plt.show()

#Rotate Image
face =misc.face()
rotate_face=ndimage.rotate(face, 180)
plt.imshow(rotate_face)
plt.show()

#Blurring or Smoothing  Images 
face = scipy.misc.face(gray=True)
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.imshow(very_blurred, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(blurred_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
                    left=0.01, right=0.99)
plt.show()

#Sharpening images
f =scipy.misc.face(gray=True).astype(float)
blurred_f=ndimage.gaussian_filter(f, 3)
filter_blurred_f=ndimage.gaussian_filter(blurred_f, 1)
alpha =30
sharpened =blurred_f+alpha *(blurred_f-filter_blurred_f)
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(f, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.imshow(blurred_f, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(sharpened, cmap=plt.cm.gray)
plt.axis('off')
plt.tight_layout()
plt.show()

#Edge detection

im=np.zeros((256, 256))
im[64:-64, 64:-64] =1
im=ndimage.rotate(im, 15, mode='constant')
im=ndimage.gaussian_filter(im, 8)
sx=ndimage.sobel(im, axis=0, mode='constant')
sy=ndimage.sobel(im, axis=1, mode='constant')
sob =np.hypot(sx, sy) 
plt.figure(figsize=(9,5))
plt.subplot(141)
plt.imshow(im)
plt.axis('off')
plt.title('square', fontsize=20)
plt.subplot(142)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel filter', fontsize=20)
plt.show()
