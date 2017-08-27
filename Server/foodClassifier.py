import cv2
import numpy as np

img = []

Chilaquiles = cv2.CascadeClassifier('Cascades/chilaquiles2.xml')
Molletes = cv2.CascadeClassifier('Cascades/molletes.xml')
Hamburguesa = cv2.CascadeClassifier('Cascades/hamburguesa.xml')
Sandwich = cv2.CascadeClassifier('Cascades/sandwich.xml')


def checkChilaquiles(im):
	global img
	chilaquiles = Chilaquiles.detectMultiScale(im, 1.3, 1000) #1.3,3000
	if not(chilaquiles is ()):
		for (x,y,w,h) in chilaquiles:	        
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		return True
	return False

def checkMolletes(im):
	global img
	molletes = Molletes.detectMultiScale(im, 1.3, 4000)
	if not(molletes is ()):
		for (x,y,w,h) in molletes:	      
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		return True
	return False

def checkHamburguesa(im):
	global img
	hamburguesa = Hamburguesa.detectMultiScale(im, 1.3, 2000)
	if not(hamburguesa is ()):
		for (x,y,w,h) in hamburguesa:	        
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		return True
	return False

def checkSandwich(im):
	global img
	sandwich = Sandwich.detectMultiScale(im, 1.3, 4000)
	if not(sandwich is ()):
		for (x,y,w,h) in sandwich:	        
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,180,180),2)
		return True
	return False

def classification(im):
	global img
	detectados = []
	img = cv2.resize(im,(200,200))

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	isChilaquiles = checkChilaquiles(gray)
	isMolletes = checkMolletes(gray)
	isHamburguesa = checkHamburguesa(gray)
	isSandwich = checkSandwich(gray)

	detectados.append(isChilaquiles)
	detectados.append(isMolletes)
	detectados.append(isHamburguesa)
	detectados.append(isSandwich)

	cv2.imshow('img',img)

	return detectados
