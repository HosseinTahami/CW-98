import pickle

def pickeling(obj_list):
    
    pickle_file = open("list.pickle","wb")
    pickle.dump(obj_list,pickle_file)
    pickle_file.close()

def unpickeling(pickle_list_file):
    
    pickle_file = open(pickle_list_file,"rb")
    obj_list = pickle.load(pickle_file)
    pickle_file.close()
    return(obj_list)