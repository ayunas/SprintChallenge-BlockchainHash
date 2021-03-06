#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,LinkedPair, hash_table_insert,hash_table_remove,hash_table_retrieve,
                        hash_table_resize)
from time import time
from random import randint

 # lp = LinkedPair('hello','world')
    # print(lp)
'''Store each weight as a key, and the value is the limit - key.
and then for each weight, if the hash_table['key'] == weight, we have a valid tuple
'''

start = time()

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i,w in enumerate(weights):
        hash_table_insert(ht,w,i)
    
    for i,w in enumerate(weights):
        # value = limit - prev_w   v = limit - w
        w2 = (limit - w)
        # print('w1', w)
        # print('w2', w2)
        print('possible addition', w,w2)
        j = hash_table_retrieve(ht,w2)
        # print('i',i)
        if j:
            print('j', j, f'{weights[j]} + {w}')
        if not j:
            continue
        else: return (i,j) if i > j else (j,i)
    return None

    # for w1 in weights:
    #     for w2 in weights:
    #         if w1 + w2 == limit:
    #             return (w1,w2)

    # return None

# x = get_indices_of_item_weights([12,0,23,34,5,23,12,22,34,12,22,2,22,2,12,100],16,44)

arr = [randint(1,100) for i in range(500)]

iw = get_indices_of_item_weights(arr,len(arr),150)
print(iw)

# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")
end = time()

print('processing time: ', end - start)
