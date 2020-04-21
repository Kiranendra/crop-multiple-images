from cv2 import imread, imwrite
from os import listdir

source_path = "G:\\Pictures\\MCA Family(PP)\\Farewell\\"
save_path = "G:\\Pictures\\MCA Family(PP)\\Farewell_Cropped_Images\\"
log_file_path = "G:\\Pictures\\MCA Family(PP)\\Farewell_Cropped_Images\\logs\\"
images = [f for f in listdir(source_path)]
i = 1

for image in images:
    try:
        img = imread(source_path + image)
        height, width = img.shape[:2]
        start_row, start_col = int(height*.01), int(width*.01)
        end_row, end_col = int(height*.99), int(width*.99)
        cropped_img = img[start_row:end_row, start_col:end_col]
        imwrite(save_path + str(i) + ".jpg", cropped_img)
        log = open(log_file_path + "logs.txt", "a+")
        log.write(str("Current Image: " + image + "\t" + "Saved as: " + str(i) + ".jpg" + "\n"))
        log.close()
        i += 1

    except Exception as e:
        print("Failed to crop Image: " + str(e))
        break


print('Cropping all images is successfully done')
