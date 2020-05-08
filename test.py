
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
#! lo que deveria hacer es eliminar nomas y despues cachar que metodo usar dependiendo del tipo de dato
#!probar todos los add del y find
item = {'word': 'pepinillo'}
currDict = 'dic'
currJson = 'words.json'

# if addItem(currJson,currDict, item, True) :
#     print(item,' agregado')
# else:
#     print(item.values(), ' no agregado')

# if delItem(currJson, itemDict = item ):
#     print(item, ' eliminado')
# else:
#     print(item.values(), ' no eliminado')

# if delItem(currJson, itemListDel='DefaultName'):
#     print(item, ' eliminado')
# else:
#     print(item, ' no eliminado')

# if delItem(currJson, itemValueDel='pepinillo'):
#     print(item, ' eliminado')
# else:
#     print(item.values(), ' no eliminado')


if findItem(currJson, itemValue='pepinillo'):
    print(item, ' encontrado')
else:
    print(item.values(), ' no lencontrado')

if findItem(currJson, itemList='DefaultName'):
    print(item, ' encontrado')
else:
    print(item.values(), ' no lencontrado')

if findItem(currJson, itemDict=item):
    print(item, ' encontrado')
else:
    print(item, ' no lencontrado')
