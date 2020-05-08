# *               @ANDROIDEV
# *                 2020
# * _____________________________________________________________
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
def addField(currJson, newField): 

    f = open(currJson)
    data = json.load(f)
    data[newField] = []
    writeJson(currJson, data)

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
                print("Amount : ", numField)
                return True
    return False

# *------------------ DELETE FIELD-------------------------------(Array of object)
def delField(currJson, field):  


    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

    for element in data:
        if element == field:

            print(element)
            del data[element]
            break

    writeJson(currJson, data)
# ? _______________________________________________________________________________

# *------------------ ADD ITEM-------------------------------(Object in an Array)


# TODO modelo de datos definitivo
def addItem(currJson, dic, item, nameObject: bool = None, name: str = 'DefaultName'):
    if nameObject:
        return addItemNamed(currJson, dic, item, nameObject, name)
    else:
        print('add item')
        f = open(currJson)
        data = json.load(f)
        if findField(currJson, dic):
            data[dic].append(item)
            writeJson(currJson, data)
            return True
        else:
            print('no existe la libreria, debe crearla')
            return False


def addItemNamed(currJson, dic, item, nameObject: bool = None, name: str = 'DefaultName'):
        print('add item named')
        f = open(currJson)
        data = json.load(f)
        if findField(currJson, dic):
            data[dic].append({
                name:item
            })
            writeJson(currJson, data)
            return True
        else:
            print('no existe la libreria, debe crearla')
            return False
# *------------------ DELETE ITEM-------------------------------(Object in an Array)


def delItem(currJson, itemListDel: str = None, itemValueDel: str = None, itemDict: dict = None):

    if itemDict:
        print('del by dict')  # !<-----
    if itemValueDel:
        return delValueItem(currJson, itemValueDel)
    if itemListDel:
        return delListItem(currJson, itemListDel)

    return False
# *------------------ DELETE ITEM by value-------------------------------(Object in an Array)
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
                            writeJson(currJson, data)
                            return True

    return False

# *------------------ DELETE ITEM by list name-------------------------------(Object in an Array)
def delListItem(currJson, itemDel):
    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):

                if itemDel in data[element][i]:

                    print(data[element][i][itemDel],' Was deleted')
                    del data[element][i]
                    writeJson(currJson,data)
                    return True

    return False




# *------------------ FIND ITEM-------------------------------
def findItem(currJson, itemList: str = None, itemValue: str = None, itemDict: dict = None):
    if itemDict: 
        return findDictItem(currJson, itemDict)
    if itemValue:
        return findValueItem(currJson, itemValue)
    if itemList:
        return findListItem(currJson, itemList)

    return False

# *------------------ FIND ITEM by value-------------------------------
def findValueItem(currJson, item): 
    print('find list by value')
    numItems = 0

    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):
                values = data[element][i]
                for value in values.values():
                    if value == item:
                        numItems = numItems + 1
                        print("Item was found, it's : ", value)
                        
                        

        if numItems > 0:
            print("Amount : ", numItems)
            return True
    print('no se encontro!')
    return False

# *------------------ FIND ITEM by list name-------------------------------
def findListItem(currJson, item):
    numItems = 0

    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for i in range(len(data[element])):
                if item in data[element][i]:
                    numItems = numItems + 1
                    print("Item was found, it's : ", data[element][i])
                    print("Amount : " , numItems)

        if numItems > 0:
            print("Amount : ", numItems)
            return True
    print('no se encontro!')
    return False


def findDictItem(currJson, item):
    numItems = 0

    with open(currJson, 'r') as data_file:
        data = json.load(data_file)

        for element in data:
            for dics in data[element]:
                if item == dics:
                    numItems = numItems +1
        if numItems >0:
            print('amount: ',numItems)
            return True
    return False


