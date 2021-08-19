import os
import glob
from PIL import Image
from time import sleep


    AX
def image_grid(imgs, rows, cols):

    print("\n\n-------Generating Grid-------\n")


    folderName = "Result"

    # getting current working directory
    current_directory = os.getcwd()
    path = os.path.join(current_directory, folderName)

    # creating a new folder for storing the results
    try : 
        os.mkdir(path)
    except:
        pass

    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    #creting a new image as Grid with size of cols and rows
    grid = Image.new('RGB', size=(cols*w, rows*h))

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))

    grid.save("{}/grid.jpg".format(folderName))

    sleep(1)
    print("""\nImage Grid will be available at "{}"\n\n
---------Task-Completed---------\n\n""".format(path))



if __name__ == "__main__":

    img_list=[]

    for filename in glob.glob('Data/*.jpg'):
        img = Image.open(filename) 
        img_list.append(img)

    length=len(img_list)
    while True:
        rows=int(input("\n\nEnter the no. of rows : "))
        cols=int(input("Enter the no. of cols : "))
        if length != rows*cols:
            print("\nCan't create an image grid!\n")
            sleep(2)
            print("Tip : The product of rows and cols should be equal to total number of images (here, {})".format(length))
            sleep(4)
            print("\nRetry...")
        else:
            break

    image_grid(img_list, rows, cols)
    


