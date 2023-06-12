from PIL import Image as img
import os


def main():
   

    Source=img.open(r'/Users/antoniolansang/Downloads/TestFolder/20230531_115032(1).jpg')
    Source.save(r'/Users/antoniolansang/Downloads/TestFolder/test.png')




if __name__ == '__main__':
    main()
