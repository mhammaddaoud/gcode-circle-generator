import math
import numpy as np
import time
import cv2

#    x = r × cos( θ )
#    y = r × sin( θ )

#gives radius, center, angles

def to_radians(angle):
    return angle * (math.pi/180)

def circle_generator(radius = 3.0, center_x = 0.0, center_y = 0.0, iterations = 360):
    #   the MATH:
    #   x = r × cos( θ )
    #   y = r × sin( θ )

    circle_coordinates = []
    angle = 0
    angle_increment = 360 / iterations
    for i in range(iterations):
        x = (radius * math.cos(to_radians(angle))) + center_x

        # takes 3 numbers after the decimal (grbl doesnt like more than 3 numbers)
        x_str = str(x)
        x_decimal = x_str.find(".")
        x_coor_str = x_str[0:x_decimal+4]

        y = (radius * math.sin(to_radians(angle))) + center_y  # float number

        # takes 3 numbers after the decimal (grbl doesnt like more than 3 numbers)
        y_str = str(y)
        y_decimal = y_str.find(".")
        y_coor_str = y_str[0:y_decimal+4]

        circle_coordinates.append([x_coor_str, y_coor_str])
        angle = angle + angle_increment
        print(angle)

    return circle_coordinates

if __name__ == "__main__" :
    x=[]
    y=[]

    print("init done")

    height = 640
    width = 480
    blank_image = np.zeros((height,width,3), np.uint8)

    start = time.time()

    coor = circle_generator(100, width/2, height/2, 360)
    for i in range(len(coor)):
        #g1 xcoor[i][0] ycoor[i][1]
        x_str = str(coor[i][0])
        x_decimal = x_str.find(".")
        x_coor_str = x_str[0:x_decimal+4]
        
        y_str = str(coor[i][1])
        y_decimal = y_str.find(".")
        y_coor_str = y_str[0:y_decimal+4]

        #everything below is for testing only (see the generated circle on an image and check the values and execution time)
        gcode_message = "G1 X"+ str(coor[i][0]) + " Y"+ str(coor[i][1]) + " F2000 \n" 
        print(gcode_message) # value checking
        cv2.circle(blank_image, (int(float(coor[i][0])), int(float(coor[i][1]))), 3, (255,255,255), 2) # generated circle on image

    print("--- %s seconds ---" % (time.time() - start)) #execution time

    #display the circle
    while True:
        cv2.imshow("img", blank_image)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
    
    cv2.destroyAllWindows()

    

    


