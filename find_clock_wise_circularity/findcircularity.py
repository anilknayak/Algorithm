# -------------------------------------------------------------------
# @author Anil KUmar Nayak
# @copyright (C) 2018,
# @doc
#
# @end
# Created : 27. Apr 2018 4:41 PM
# -------------------------------------------------------------------

import numpy as np
import csv

class Sample():
    def __init__(self):
        with open('circle.csv', 'r') as csvfile:
            # read the csv file
            rows = csv.reader(csvfile, delimiter=',')
            # used to ignore the first line
            r = 0
            # holds all the positions of each data point
            point_id = []
            # Hold all the data points
            coordinates = []
            self.anti_clock_wise = []
            # Preparing data
            for row in rows:
                if r == 0:
                    r += 1
                else:
                    point_id.append(int(row[0]))
                    coordinates.append([float(row[1]), float(row[2])])

            for pos in range(len(coordinates)):
                self.points = coordinates[pos: pos + 3]
                self.ids = point_id[pos: pos + 3]

                # Preparing 3 point window for validation
                self.p0 = np.asarray(self.points[0])
                self.p1 = np.asarray(self.points[1])
                self.p2 = np.asarray(self.points[2])

                # Stop when the last window of validation reached
                if pos+3 >= len(coordinates):
                    break

                # Find the change
                # 1. Change in gradient in same coordinate quadrant
                # 2. Change in gradient from one coordinate quadrant to another coordinate quadrant
                self.find_first_derivative_of_change()

                # Validating for 2 windows to confirm that same point is rotating anti clock wise
                if len(self.anti_clock_wise) == 2:
                    w1 = self.anti_clock_wise[0][2]
                    w2 = self.anti_clock_wise[1][1]
                    if w1==w2:
                        print("Anti Clock Wise Point is ", w2)
                    break

    def find_first_derivative_of_change(self):
        # find the neumerator to find the gradient
        self.find_numerator()
        # find the denominator to find the gradient
        self.find_denominator()

        # find the gradient
        self.change_point_1 = np.divide(self.sign_d1,self.sign_p1)
        self.change_point_2 = np.divide(self.sign_d2,self.sign_p2)

        # if np.array_equal(self.sign_d1, self.sign_d2):
        #     print("Close Wise >>>>>>>", self.ids)
        if np.array_equal(self.sign_d1, self.sign_d2 * -1):
            # print("Anti Clock Wise >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", self.ids)
            # Validating for 2 windows to confirm that same point has been
            # found in first and second check has same point which is rotating anti clock wise
            self.anti_clock_wise.append(self.ids)
        # elif np.array_equal(self.sign_p1, self.sign_p2):
        #     # print("Close Wise >>>>>>>", self.ids)



    def find_denominator(self):
        # This is to Handle the change in coordinate system
        self.sign_p1 = np.sign(self.p1)
        self.sign_p2 = np.sign(self.p2)

        if self.sign_p1[0] == 0:
            self.sign_p1[0] = self.sign_p1[1]
        if self.sign_p1[1] == 0:
            self.sign_p1[1] = self.sign_p1[0]
        if self.sign_p2[0] == 0:
            self.sign_p2[0] = self.sign_p2[1]
        if self.sign_p2[1] == 0:
            self.sign_p2[1] = self.sign_p2[0]

    def find_numerator(self):
        # this is to check the change in the distance
        self.d1 = self.p1 - self.p0
        self.d2 = self.p2 - self.p1
        self.sign_d1 = np.sign(self.d1)
        self.sign_d2 = np.sign(self.d2)



if __name__ == '__main__':
    Sample()
