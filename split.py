import os
import glob
import time
import random


def create_folder(foldername):
    try:
        os.mkdir('./' + str(foldername))
    except:
        print('{} has been created'.format(foldername))
    
def split(one_per_x_ratio, annot_ext):
     for i, xml_filename in enumerate(sorted(glob.glob(annot_ext))):
        try:
            filename = xml_filename.split('.xml')[0]
            jpg_filename = filename + '.jpg'
            

            if i % one_per_x_ratio == 0 :
                os.rename('./' + jpg_filename, './val/' + jpg_filename)
                os.rename('./' + xml_filename, './val/' + xml_filename)
                print('move '+ jpg_filename + 'to ' + 'val')
            else:
                os.rename('./' + jpg_filename, './train/' + jpg_filename)
                os.rename('./' + xml_filename, './train/' + xml_filename)
                print('move '+ jpg_filename + 'to ' + 'train')
        except:
            pass

def split_random(one_per_x_ratio, annot_ext):
    list_data = glob.glob(annot_ext)
    random.shuffle(list_data)
    for i, xml_filename in enumerate(list_data):
        try:
            filename = xml_filename.split('.xml')[0]
            jpg_filename = filename + '.jpg'
            
            if i % one_per_x_ratio == 0 :
                os.rename('./' + jpg_filename, './val/' + jpg_filename)
                os.rename('./' + xml_filename, './val/' + xml_filename)
                print('move '+ jpg_filename + 'to ' + 'val')
            else:
                os.rename('./' + jpg_filename, './train/' + jpg_filename)
                os.rename('./' + xml_filename, './train/' + xml_filename)
                print('move '+ jpg_filename + 'to ' + 'train')
        except:
            pass
    

if __name__ == '__main__':
    one_per_x_ratio = 3
    annot_ext = '*.xml'
    flag_random = True
    
    create_folder('train')
    create_folder('val')
    
    if flag_random:
        split_random(one_per_x_ratio, annot_ext)
    else:
        split(one_per_x_ratio, annot_ext)
    
   
        
    
    