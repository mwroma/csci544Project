import pickle
import os

def tf_idf():
    pass

def word2vec():
    pass

def word_bag():
    return load_data('bags')

def vec_to_category(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            return i
    return len(arr)

def load_data(rootDir):
    result = {'X':[], 'Y':[]}
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            file_path = os.path.join(root, f)
            with open(file_path, 'rb') as fp:
                data = pickle.load(fp)
                result['X'].append(data['word_bag'])
                result['Y'].append(vec_to_category(data['label1']))
    with open('train_data.bat', 'wb+') as fp:
        pickle.dump(result, fp, protocol=pickle.HIGHEST_PROTOCOL)
    return result

if __name__ == "__main__":
    word_bag()
