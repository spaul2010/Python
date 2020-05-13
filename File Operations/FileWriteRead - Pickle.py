# ------------------------------------------------------------------------------
#    Binary File Operations - Use Pickle
# ------------------------------------------------------------------------------

import pickle

# ------------------------------------------------------------------------------
#       pickle.dump(data_item, File)                          ---> Write to File
# ------------------------------------------------------------------------------
# sample dictionary to write/dump to file
tesData = {'Fname': 'Sukumar',
           'Lname': 'Paul',
           'Phone': '555-55555',
           'Address': 'Oxford Road'}

with open("PickleTestFile","wb") as pwf:
    pickle.dump(tesData, pwf)


# ------------------------------------------------------------------------------
#       pickle.load(file)                                    ---> Read from File
# ------------------------------------------------------------------------------
# Now read back the dictionary from the file
with open("PickleTestFile","rb") as prf:
    testData2 = pickle.load(prf)

print(testData2)
