# change all the names in folder 'source' to ids.png
import os
import cv2
from tqdm import tqdm

# id = 0
# for filename in os.listdir('source'):
#     os.rename('source/' + filename, 'source/' + str(id) + '.png')
#     id += 1

# crop the image from 1920x1080 to 1920x720 from the center, and save it to the folder 'cropped'
for filename in tqdm(os.listdir('source')):
    if filename.endswith('.png'):
        img = cv2.imread('source/' + filename)
        img = img[166:838, 340:1699]
        cv2.imwrite('cropped/' + filename, img)
        # print(filename)

# # delete all images without labels in the folder 'cropped'
# for filename in os.listdir('cropped'):
#     if filename.endswith('.png'):
#         if filename[:-4]+ '.xml' not in os.listdir('cropped/'):
#             os.remove('cropped/' + filename)

# re-number all images (id.png) in the folder 'cropped'
id = 1000
for filename in os.listdir('cropped'):
    if filename.endswith('.png') and len(filename) > 10:
        os.rename('cropped/' + filename, 'cropped/' + str(id) + '.png')
        id += 1

# # replace all text 'special' and 'human' with 'normal' in the folder 'cropped'
# for filename in os.listdir('cropped'):
#     if filename.endswith('.xml'):
#         with open('cropped/' + filename, 'r') as f:
#             lines = f.readlines()
#         with open('cropped/' + filename, 'w') as f:
#             for line in lines:
#                 if 'special' in line:
#                     line = line.replace('special', 'normal')
#                 if 'human' in line:
#                     line = line.replace('human', 'normal')
#                 f.write(line)
#         print(filename)
