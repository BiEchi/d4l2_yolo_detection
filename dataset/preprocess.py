# change all the names in folder 'source' to ids.png
import os
import cv2

# id = 0
# for filename in os.listdir('source'):
#     os.rename('source/' + filename, 'source/' + str(id) + '.png')
#     id += 1

# # # crop the image from 1920x1080 to 1920x720 from the center, and save it to the folder 'cropped'
# for filename in os.listdir('source'):
#     img = cv2.imread('source/' + filename)
#     img = img[130:930, 0:1920]
#     cv2.imwrite('cropped/' + filename, img)

# delete all images without labels in the folder 'cropped'
for filename in os.listdir('cropped'):
    if filename.endswith('.png'):
        if filename[:-4]+ '.xml' not in os.listdir('cropped/'):
            os.remove('cropped/' + filename)

