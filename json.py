import json  # librery
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

# *------------------ WRITE JSON -------------------------------
def writeJson(currJson, data):

    with open(currJson, 'w') as jsonFileOut:
        json.dump(data, jsonFileOut, indent=4)
# ? _______________________________________________________________________________

# *------------------ ADD FIELD-------------------------------(Array of object)
def addField(newField):  # ! en que fichero busco ?

    f = open(currJson)
    data = json.load(f)
    data[newField] = []
    writeJson(data)

# *------------------ FIND FIELD-------------------------------(Array of object)
# ! just add a parameters for diferent values and return; deside how to operate
def findField(currJson, field):
    numField = 0

    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            if field == element:
                numField = numField + 1
                print("Field was found, it's : ", element)
                print("Contains : ", data[element])
                print("Amount : ", numField)
                return True
    return False

# *------------------ DELETE FIELD-------------------------------(Array of object)
def delField(field):  # ! en que fichero busco ?


    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

    for element in data:
        if element == field:

            print(element)
            del data[element]
            break

    writeJson(data)
# ? _______________________________________________________________________________

# *------------------ ADD ITEM-------------------------------(Object in an Array)
def addItem(currJson, dic, item):  # TODO modelo de datos definitivo

    f = open(currJson)
    data = json.load(f)
    if findField(currJson, dic):
        data[dic].append(item)
        writeJson(currJson, data)
    else:
        print('no existe la libreria, quiere crear una ?')
        #! pedir crear una nueva libreria

# *------------------ DELETE ITEM-------------------------------(Object in an Array)
def delValueItem(currJson,itemDel):

    deleted= False
    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):
                    values = data[element][i]
                    for value in values.values():
                        if value == itemDel:
                            del data[element][i]
                            print(value + ' Was deleted')
                            deleted== True
                    if deleted == True:
                        break


    writeJson(currJson,data)

# *------------------ DELETE ITEM-------------------------------(Object in an Array)
def delItem(currJson,itemDel):  

    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):
                print(data[element][i].value())
                if itemDel in data[element][i]:#!arreglar esta wea

                    print(data[element][i][itemDel]+' Was deleted')
                    del data[element][i]
                    break

    writeJson(currJson,data)

# *------------------ FIND ITEM-------------------------------
def findItem(currJson,item):  # ! just add a parameters for diferent values and return; deside how to operate 
    numItems = 0

    with open(currJson, 'r') as data_file:
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





# * _____________________________________________________________
        # *      MAIN # 
# * _____________________________________________________________
#  # ! ahora evaluar como hago una funcion para esta wea
# amountJsonFiles = 0
# path = os.getcwd()
# for file in os.listdir(path):
#     if file.endswith(".json"):
#         print(os.path.join(file))
#         amountJsonFiles=amountJsonFiles+1
# if amountJsonFiles == 1:
#     currJson = file
#     print('currJson : ',currJson)
# else:
#     dir_list = os.listdir(path)
#     if amountJsonFiles == 0:
#         addNewJson('default.json')
#         if 'default.json' in dir_list:
#             currJson= 'default.json'
#             print('currJson : ', currJson)
#     if amountJsonFiles == 2 :
#         if 'default.json' in dir_list:
#             currJson= 'default.json'
#             print('currJson : ', currJson)
#         #! else: si no esta entonces preguntar al usuario cual quiere setear como el current
#addItem('words.json','dic',pepinillo)
# addField('Hola')
# delField('Hola')
#delValueItem('words.json','pepinillo')#!funciona buscar la palabra pero no por la palabra que busco
# findItem('item')
# findField('Hola')
# addNewJson('pico.json')
# delJson('pico.json')
