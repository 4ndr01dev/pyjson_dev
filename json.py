import json  # librery
from sympy.polys.domains import field
import os
# * _____________________________________________________________
# *                FUNCTIONS
# * _____________________________________________________________

# *------------------ CREATE A NEW JSON-------------------------------
def addNewJson(name): 
    if findJson(name):
        print('there is a existing file with that name')
    else:
        print('crating a new file Json')
        with open(name, 'w'):
            pass
    

# *------------------ DEL A JSON-------------------------------
def delJson(name):
    if findJson(name):
        os.remove(name)
    else:
        print('there is a existing file with that name')


# *------------------ FIND A JSON-------------------------------
def findJson(name):
    path = os.getcwd()
    dir_list = os.listdir(path)

    print("List of directories and files before creation:")
    print(dir_list)
    if name in dir_list:
        return True
    else:
        return False

# *------------------ ADD ITEM-------------------------------
def addItem(dic, item):  # ! en que fichero busco ?

    f = open('words.json')
    data = json.load(f)
    if findField(dic):
        data[dic].append({
            'item': item
        })
        writeJson(data)
    else:
        print('no existe la libreria, quiere crear una ?') 
        #! pedir crear una nueva libreria 


# *------------------ ADD FIELD-------------------------------
def addField(newField):  # ! en que fichero busco ?

    f = open('words.json')
    data = json.load(f)
    data[newField] = []
    writeJson(data)


# *------------------ DELETE FIELD-------------------------------
def delField(field):  # ! en que fichero busco ?


    with open('words.json', 'r') as data_file:
        data = json.load(data_file)

    for element in data:
        if element == field:

            print(element)
            del data[element]
            break

    writeJson(data)


# *------------------ DELETE ITEM-------------------------------
def delItem(itemDel):  # ! en que fichero busco ?

    with open('words.json', 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):

                if itemDel in data[element][i]:

                    print(data[element][i][itemDel]+' Was deleted')
                    del data[element][i]
                    break

    writeJson(data)


# *------------------ FIND ITEM-------------------------------
def findItem(item):  # ! just add a parameters for diferent values and return; deside how to operate 
    numItems = 0

    with open('words.json', 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):
                if item in data[element][i]:
                    numItems = numItems + 1
                    print("Item was found, it's : ", data[element][i])
                    print("Contains : " + data[element][i][item])
                    print("Amount : " , numItems)
                    return True

        if numItems > 1:
            print('eliminar redundancias')
    return False


# *------------------ FIND field-------------------------------
def findField(field):  # ! just add a parameters for diferent values and return; deside how to operate
    numField = 0

    with open('words.json', 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            if field == element:
                numField = numField + 1
                print("Field was found, it's : ", element)
                print("Contains : " , data[element])
                print("Amount : ", numField)
                return True
    return False


# *------------------ WRITE JSON -------------------------------
def writeJson(data):

    with open('words.json', 'w') as jsonFileOut:
        json.dump(data, jsonFileOut, indent=4)


# *------------------ ADD JSON -------------------------------
def addJson(data):

    with open('words.json', 'a') as jsonFileOut:
        json.dump(data, jsonFileOut, indent=4)


# * _____________________________________________________________
        # *      MAIN # 
# * _____________________________________________________________
 # ! ahora evaluar como hago una funcion para esta wea
amountJsonFiles = 0
path = os.getcwd()
for file in os.listdir(path):
    if file.endswith(".json"):
        print(os.path.join(file))
        amountJsonFiles=amountJsonFiles+1
if amountJsonFiles == 1:
    currJson = file
    print('currJson : ',currJson)
else:
    dir_list = os.listdir(path)
    if amountJsonFiles == 0:
        addNewJson('default.json')
        if 'default.json' in dir_list:
            currJson= 'default.json'
            print('currJson : ', currJson)
    if amountJsonFiles == 2 :
        if 'default.json' in dir_list:
            currJson= 'default.json'
            print('currJson : ', currJson)
        #! else: si no esta entonces preguntar al usuario cual quiere setear como el current

# addItem('wenardo',item)
# addField('Hola')
# delField('Hola')
# delItem('word')
# findItem('item')
# findField('Hola')
# addNewJson('pico.json')
# delJson('pico.json')
