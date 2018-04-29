#-------------------------------------------------------------------
# @author  Anil Kumar Nayak
# @copyright (C) 2018, 
# @doc
#
# @end
# Created : 29. Apr 2018 12:58 AM
#-------------------------------------------------------------------

import numpy as np
import cv2


class Sample():
    def __init__(self):
        self.scrambled_image = cv2.imread("mystery_number_scrambled.jpg")
        self.scrambled_image_gray = self.scrambled_image[:,:,0]
        shape = np.shape(self.scrambled_image_gray)
        print("Shape of Scrambled Image ", shape)

        self.Y = np.asarray(self.scrambled_image_gray).flatten()
        self.Z = np.zeros(np.shape(self.Y)) * -1
        self.pixels = np.shape(self.Y)[0]
        print("Shape of Flatten Scrambled Image Y ", np.shape(self.Y)[0])
        print("Shape of Flatten Scrambled Image Z ", np.shape(self.Z)[0])

        print("Total Pixels", str(shape[0]*shape[1]))
        self.indices = []
        with open('shuffle_indecies.txt', 'r') as csvfile:
            lines = csvfile.readlines()
            for line in lines:
                self.indices.append(int(line.rstrip()))
        print("Shuffled Number of Indices ", len(self.indices))
        if len(self.indices) == shape[0]*shape[1]:
            print("Data is correct to proceed")
            self.process()
            image = np.reshape(self.Z, (shape[0], shape[1]))
            cv2.imshow("Window", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Data provided is not correct form")

    def process(self):
        for ind in range(self.pixels):
            index = self.indices[ind]
            value = self.Y[ind]
            self.Z[index] = value



if __name__ == '__main__':
    Sample()