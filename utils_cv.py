import numpy as np
import cv2

def load_and_display(adresse_image):
	img = cv2.IMREAD_COLOR(adresse_image)
	cv2.imshow('image', img)
	return


