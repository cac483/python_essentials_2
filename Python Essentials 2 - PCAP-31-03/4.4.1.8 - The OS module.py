import os

def find(path = '', dir = ''):
    if path != '' and dir != '':
        try:
            os.chdir(os.getcwd() + '/' + path)
            # print(os.getcwd())

            for item in os.listdir():
                # print("Curr item: " + path + '/' + item)
                if item == dir:
                    print(os.getcwd() + '/' + item)
                if os.path.isdir(os.getcwd() + '/' + item):
                    find(item, dir)
                    os.chdir('..')
                
        except OSError as oe:
            print('Error when starting search in ' + path + ': ' + str(oe))
    else:
        return ''

find('./tree','python')