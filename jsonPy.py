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
    if os.path.splitext(name) != '.json':
        name = name + '.json'

    if findJson(name):
        print('there is a existing file with that name')
        return False
    else:
        try:
            # Create target Directory
            os.mkdir('data')
            print("Directory ", 'data',  " Created ")


        except FileExistsError:
            print("Directory ", 'data',  " already exists")
    print('crating a new file Json')
    with open(name, 'w'):
        pass
    data={

    }
    writeJson(name,data)
    return True
# *------------------ JSON IS EMPTY-------------------------------
def isEmptyJson(currJson):
    numItems = 0
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            print('There are ',len(data),' fields')
            if len(data) == 0 :True
            else: False


# *------------------ DEL A JSON-------------------------------
def delJson(name):
    if findJson(name):
        os.remove(name)
    else:
        print('there is a existing file with that name')


# *------------------ FIND A JSON-------------------------------
def findJson(name):
    print(name)
    path = os.getcwd()
    dir_list= os.listdir(path)
    print("List of directories and files before creation:")
    print(dir_list)
    if name in dir_list:
        return True
    else:
            return False
    return False


# *------------------ WRITE JSON -------------------------------
def writeJson(currJson, data):

    with open(currJson, 'w') as jsonFileOut:
        json.dump(data, jsonFileOut, indent=4)


# ? _______________________________________________________________________________

# *------------------ ADD FIELD-------------------------------(Array of object)
def addField(currJson, newField): 
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
        f = open(currJson)
        data = json.load(f)
        data[newField] = []
        writeJson(currJson, data)
        return True
    else:
        print('json not foud')
        return False


# *------------------ FIND FIELD-------------------------------(Array of object)
def findField(currJson, field):
    if '.json' in currJson:print('lets find it')# TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    numField = 0
    if findJson(currJson):

        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            if isEmptyJson(currJson):
                return False   # TODO apli
            else:
                for element in data:
                    if field == element:
                        numField = numField + 1
                        return True
        return False
    else:
        print('json not foud')
        return False


# *------------------ DELETE FIELD-------------------------------(Array of object)
def delField(currJson, field):  
    if os.path.splitext(currJson) != '.json':
        currJson = currJson + '.json'
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)

        for element in data:
            if element == field:

                print(element)
                del data[element]
                break

        writeJson(currJson, data)
    else:
        print('json not foud')
        return False
# ? _______________________________________________________________________________

# *------------------ ADD ITEM-------------------------------(Object in an Array)

def addItem(currJson, dic, item, nameObject: bool = None, name: str = 'DefaultName'):
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
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
    else:
        print('json not foud')
        return False



# *------------------ ADD ITEM with Name list-------------------------------(Object in an Array)
def addItemNamed(currJson, dic, item: dict, nameObject: bool = None, name: str = 'DefaultName'):
    if '.json' in currJson: print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
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
    else:
        print('json not foud')
        return False


# *------------------ DELETE ITEM-------------------------------(Object in an Array)
def delItem(currJson, itemListDel: str = None, itemValueDel: str = None, itemDict: dict = None):
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
        if itemDict:
            print('del by dict')  # !<-----
        if itemValueDel:
            return delValueItem(currJson, itemValueDel)
        if itemListDel:
            return delListItem(currJson, itemListDel)

        return False
    else:
        print('json not foud')
        return False


# *------------------ DELETE ITEM by value-------------------------------(Object in an Array)
def delValueItem(currJson,itemDel):
    if findJson(currJson):

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
    else:
        print('json not foud')
        return False


# *------------------ DELETE ITEM by list name-------------------------------(Object in an Array)
def delListItem(currJson, itemDel):
    if findJson(currJson):
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
    else:
        print('json not foud')
        return False


# *------------------ FIND ITEM-------------------------------
def findItem(currJson, itemList: str = None, itemValue: str = None, itemDict: dict = None):
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
        if itemDict: 
            return findDictItem(currJson, itemDict)
        if itemValue:
            return findValueItem(currJson, itemValue)
        if itemList:
            return findListItem(currJson, itemList)
        return False
    else:
        print('json not foud')
        return False


# *------------------ FIND ITEM by value------------------------------ -
def findValueItem(currJson, item):  

    print('find list by value')
    numItems = 0
    if findJson(currJson):
        print(os.getcwd())
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            for element in data:
                for i in range(len(data[element])):
                    values = data[element][i]
                    for value in values.values():
                        if value == item:
                            numItems = numItems + 1
                            
                            print("Item was found, it's : ", value)
                            return values
                            

            if numItems > 0:
                print("Amount : ", numItems)
                return True
        print('no se encontro!')
        return None
    else:
        print('json not foud')
        return None


# *------------------ FIND ITEM by list name-------------------------------
def findListItem(currJson, item):
    numItems = 0
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            if isEmptyJson(currJson): return False
            else:
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
    else:
        print('json not foud')
        return False


# *------------------ FIND ITEM by dict-----------------------------
def findDictItem(currJson, item):
    numItems = 0
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)

            for element in data:
                for dics in data[element]:
                    if item == dics:
                        print('el item es :',dics)
                        numItems = numItems +1
            if numItems >0:
                print('amount: ',numItems)
                return True
        return False
    else:
        print('json not foud')
        return False

os.chdir('data')


