import cv2
import numpy as np
import foodClassifier as fc
import glob

def getPicture():
	paths = glob.glob("C:/Users/VIAO2/Desktop/Codigo/Self/Concursos/HackMty/sources/*.jpg")
	img = cv2.imread(paths[len(paths)-1])
	return img



if __name__ == "__main__":
	# for path in glob.glob("C:/Users/VIAO2/Desktop/Codigo/Self/Concursos/HackMty/Images/todo/*.jpg"):
		#Acces de picture
		# img = cv2.imread(path)#getPicture()
		img = getPicture()
		img = cv2.resize(img,(640,480))

		#Classify the picture, and put classification in boolean array
		classification = fc.classification(img.copy())

		# display classification result and calories
		height = img.shape[0]
		separation = height*.25

		

		texts = ["C - 443","M - 350","H - 360","S - 339"]

		for i in range(len(classification)):
			if classification[i]:
				cv2.putText(img,texts[i],(10,int(separation*i)+50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,70,0),4)

		cv2.imshow("MyCalories",img)

		k = cv2.waitKey(0)

		# if k == 27:
		# 	break






