import os

dataDir = ['Kitchen', 'LivingRoom', 'Mall', 'GroceryStore', 'Supermarket', 'Mueseum', 'Autorickshaw']

def clean(descriptor):
    try:
        os.system('rm -rf ./Dataset/' + descriptor +'/*')
    except Exception as e:
        print(e)

def cleanGB_LBP():
    for i in dataDir:
        try:
            path0 = './Dataset/Gabor/' + i + '/Horizontal'
            path1 = './Dataset/Gabor/' + i + '/Vertical'

            try:
                for j in os.listdir(path0):
                    os.remove(path0 + '/' + j)
                for j in os.listdir(path1):
                    os.remove(path1 + '/' + j)
            except Exception as e:
                print(e)
                continue

            try:
                os.remove('./Dataset/LBP/' + i + '/gabor_v.csv')
                os.remove('./Dataset/LBP/' + i + '/gabor_h.csv')
            except:
                continue

        except Exception as ee:
            continue


