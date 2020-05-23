# *               0ANDROIDEV
# *                 2020
# * _____________________________________________________________
'''                                                  
                                #                   
                               ###                  
                              #####                 
                             #######                
                            ###### ##               
                           ###### ####              
                          ##### #######             
                         ####     ######            
                        ####        #####           
                       ###           #####          
                      ###              ####         
                     ##                  ###        
                    #                      ##       
                   #                         #      
'''
import json  # librery
import os
import string
import random
# * _____________________________________________________________
# *                FUNCTIONS
# * _____________________________________________________________


def generateId():
    return''.join(random.choices(string.ascii_uppercase + string.digits, k=8))



# *------------------ CREATE A NEW JSON-------------------------------

def addNewJson(name): 
    """Add a new Json file in the current directiry
    
    """
    if os.path.splitext(name) != '.json':
        name = name + '.json'

    if findJson(name):
        print('there is a existing file with that name')
        return False
    else:
        try:
            # Create target Directory
            print("Directory data must to be created")


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
    """Find if the json is empty

    """
    numItems = 0
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            print('There are ',len(data),' fields')
            if len(data) == 0 :True
            else: False

# *------------------ JSON GET DATA-------------------------------
def getData(currJson):
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            return data
    else: return None

# *------------------ DEL A JSON-------------------------------
def delJson(name):
    """Delete a Json in a current directory

    """
    if findJson(name):
        os.remove(name)
    else:
        print('there is a existing file with that name')


# *------------------ FIND A JSON-------------------------------
def findJson(name):
    """Find a Json file in a current directory
    """
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
    """Write the data in the current Json File
        ---------------------------------------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED data -> Data to add

        ---------------------------------------------------
    """
    with open(currJson, 'w') as jsonFileOut:
        json.dump(data, jsonFileOut, indent=4)

# ? _______________________________________________________________________________

# *------------------ ADD FIELD-------------------------------(Array of object)


def addField(currJson: str, newField: str):
    """Add a dictionary
    ---------------------------------------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED newFile:str -> Dic name to add it. DEFAULT VALUE = 'default'

        ---------------------------------------------------
    RETURN:
        TRUE -> correctly added

        FALSE -> it have an issue

    """
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
def findField(currJson:str, field:str):
    """find a dictionary
    ---------------------------------------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED file:str -> Dic name to add it. DEFAULT VALUE = 'default'

        ---------------------------------------------------
    RETURN:
        TRUE -> found

        FALSE -> not found

    """
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
    """delete a dictionary
    ---------------------------------------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED file:str -> Dic name to add it. DEFAULT VALUE = 'default'

        ---------------------------------------------------
    RETURN:
        TRUE -> deleted

        FALSE -> not deleted

    """
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

def addItem(currJson, dic='default', item: dict= None, name:str = None):
    """Add a new item  to a determinate dictionary
    ---------------------------------------------------

    REQUIRED currJson--> current Json File. 

    dic='default' -> Dic name to add item in it. DEFAULT VALUE = 'default'

    REQUIRED item: dict= None --> The item to add, it must be a dictionary.

    name:str = None --> The name that you want to asing to your item

        ---------------------------------------------------
    RETURN:
        TRUE -> correctly added

        FALSE -> it have an issue

    """
    nameObject= False
    if name != None:
        nameObject = True
    idFound = False
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    id = generateId()
    while idFound == False:
        if findItem(currJson,dic,itemValue= id) :
            print('there is a value with that id')
            id = generateId()
        else: 
            idFound = True
    item['ID']= id 
    if findJson(currJson):
        if nameObject:
            if findItem(currJson, itemList=name):
                print('this list allredy exists')
                return False
            else:
                return __addItemNamed(currJson, dic, item, name)
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
def __addItemNamed(currJson, dic, item: dict, name: str = 'DefaultName'):
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
    """Delete a item  to a determinate dictionary
    ---------------------------------------------------

        REQUIRED currJson--> current Json File.

        dic='default' -> Dic name to add it. DEFAULT VALUE = 'default'

    REQUIRED  some of this options:
    
        itemListDel: str = None --> delete a item by name of the list that contains
        a particular dictionary
        
        itemValueDel: str = None --> delete a item that contains
        a particular value in it .
        
        itemDict: dict = None --> delete the itemDict if it´s in the Field.


        ---------------------------------------------------
    RETURN:

        TRUE -> correctly deleted

        FALSE -> it have an issue

    """
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
        if itemDict:
            print('del by dict')  # !<-----
        if itemValueDel:
            return __delValueItem(currJson, itemValueDel)
        if itemListDel:
            return __delListItem(currJson, itemListDel)

        return False
    else:
        print('json not foud')
        return False


# *------------------ DELETE ITEM by value-------------------------------(Object in an Array)
def __delValueItem(currJson,itemDel):
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
def __delListItem(currJson, itemDel):
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
    """Find a item  to a determinate Json
    ---------------------------------------------------

        REQUIRED currJson--> current Json File.

    REQUIRED  some of this options:
    
        itemListDel: str = None --> find a item by name of the list that contains
        a particular dictionary
        
        itemValueDel: str = None --> find a item that contains
        a particular value in it .
        
        itemDict: dict = None --> find the itemDict if it´s in the Field.

        ---------------------------------------------------
    RETURN:

        TRUE -> correctly deleted

        FALSE -> it have an issue

    """
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    if findJson(currJson):
        if itemDict: 
            return __findDictItem(currJson, itemDict)
        if itemValue:
            return __findValueItem(currJson, itemValue)
        if itemList:
            return __findListItem(currJson, itemList)
        return False
    else:
        print('json not foud')
        return False


# *------------------ FIND ITEM by value------------------------------ -
def __findValueItem(currJson, item):  

    print('find list by value')
    numItems = 0
    if findJson(currJson):
        print(os.getcwd())
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            for element in data:
                for i in range(len(data[element])):
                    values = data[element][i]
                    print('--------------------------values', values)
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
def __findListItem(currJson: str, item):
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
def __findDictItem(currJson:str, item):
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

# *------------------ EDIT ITEM-------------------------------
def editItem(currJson: str,dic:str='default', item:dict={}):
    if '.json' in currJson:
        print('lets find it')  # TODO apli
    else:
        currJson = currJson+'.json'  # TODO apli
    print(currJson)
    if findJson(currJson):
        if findItem(currJson, itemValue= item['ID']):
            if delItem(currJson, itemValueDel=item['ID']):
                print('Item with ', item['ID'] , ' was deleted')
            else:
                print('error')
                return False
            if addItem(currJson,dic,item):
                print('Item with ', item['ID'], ' was remplaced')
                return True
            else:
                print('error')
                return False
    else:
        print('json not foud')
        return False

if 'data' in os.listdir(os.getcwd()):
    os.chdir('data')
else:
    os.mkdir('data')
    os.chdir('data')
currDict = 'dic'
currJson = 'words.json'
data = getData(currJson)
for field in data:

    print(field)
    for item in data[field]:
        print(item)
