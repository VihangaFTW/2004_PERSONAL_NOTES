class Node:
    def __init__(self, data=None|str, size = 27, level: int=0) -> None: # 27 for lowercase letter mapping (53 if uppercase included)
        # data payload
        self.data = data
        #* index 0 is for the terminal node. ASCII value of char maps to the array indices[1-26].
        #? we store the data in the terminal node
        #! the array index corresponds to the "link" aka a character in the trie
        self.link: list = [None] * size
        self.level = level


class Trie:
    '''
    Trie is a type of k-ary search tree used for storing and searching a specific (string) key from a set. 
    Using Trie, search complexities can be brought to optimal worst case: O (N) where N is the length of key. O(1) best case when first char not in trie
    '''

    def __init__(self):
        self.root: Node = Node()


    def insert(self, key: str, data= None):
        
        current_node = self.root
        count_level = 1
        for char in key:
            index = ord(char) - ord('a') + 1
            if current_node.link[index] is not None:
                current_node = current_node.link[index]
            else:
                current_node.link[index] = Node(level= count_level)
                current_node = current_node.link[index]
            count_level += 1
        
        # check for terminal node (terminal node is represented by a Node object at index 0)
        if current_node.link[0] is not None:
            current_node = current_node.link[0]
        else:
            current_node.link[0] = Node(level= count_level)
            current_node = current_node.link[0]

        # add the payload
        #* data is stored in the terminal node
        current_node.data = data
        
    def search(self, key: str):
        '''
        : returns the data associated with the given key if it exists,
          otherwise, raises an Exception
        :time complexity:   best:- O(1) the first character does not exist
                            worst:- O(N) where N is the length of the key

        '''
        
        current_node = self.root

        for char in key:
            index = ord(char) - ord('a') + 1
            if current_node.link[index] is not None:
                current_node = current_node.link[index]
            else:
                raise Exception(f"Key '{key}' does not exist")
        
        # check for terminal symbol (terminal symbol is represented by a Node object at index 0)
        if current_node.link[0] is not None:
            current_node = current_node.link[0]
            return f'Key: {key}, Value: {current_node.data}, Node level: {current_node.level}'
        else:
            raise Exception(f"Key '{key}' does not exist")

#! ==================================== recursive insert and search methods =========================================
        
    def insert_recur_2(self,key, data ):
        self.insert_recur_2_aux(current_node= self.root,key= key, level=1,data=data)
    
    def insert_recur_2_aux(self, current_node,key,level,data):
        if not key:
            if current_node.link[0] is not None:
                raise Exception(f"Key already exists!")
            current_node.link[0] = Node(level=level)
            #* store data in the terminal node
            current_node.link[0].data = data
            print(f"inserted value {data} in level {level} node")
            return
        
        index = ord(key[0]) -ord('a') + 1
        if current_node.link[index] is None:
            current_node.link[index] = Node(level=level)
        self.insert_recur_2_aux(current_node.link[index],key[1:],level+1,data)


    def search_recur(self, key):
        return self.search_recur_aux(self.root,key)
    

    def search_recur_aux(self, current_node, key):
        if not key:
            # current node is now the terminal node.
            if current_node.link[0] is None:
                raise Exception("Key does not exist!")
            return current_node.link[0].data

        index = ord(key[0]) - ord('a') + 1
        if current_node.link[index] is None:
            raise Exception("Key does not exist!")
        return self.search_recur_aux(current_node.link[index], key[1:])
    
#! ==================================================================================================================

    def generate_suffix_array(self):
        '''
        This function performs an in-order traversal of the trie and returns the data associated with each key as elements in a list
        in lexicographical order aka alphabetical order.
        #!:prerequisite: The Trie must only contain all the suffixes of a word as keys. The data associated with each key must be the corresponding key's suffix id.
        :return a list of integers where each integer represents a suffix id.
        :raises Exception if Trie is empty
        : time complexity
        '''
        count = 0
        for i in range(len(self.root.link)): 
            if self.root.link[i] is not None:
                count += 1
        if count == 0:
            raise Exception("Trie is empty!")
        
        suffix_arr = []
        return self._generate_suffix_arr_aux(self.root,suffix_arr)

    def _generate_suffix_arr_aux(self, current_node: Node, suffix_arr: list[int]):
        node_arr =current_node.link
        
        for i in range(len(node_arr)):
            # node array contains a node
            if node_arr[i] is not None:
                # terminal node is found
                if i == 0:
                    suffix_arr.append(node_arr[i].data)
                # go down the trie until terminal node is found
                self._generate_suffix_arr_aux(node_arr[i], suffix_arr)
        
        return suffix_arr

    def predecessor_query(self, key):
        pass


if __name__ == "__main__":
    # blah = Trie()
    # blah.insert_recur_2("lol", [1,2,3,4,5])
    # blah.insert_recur_2("lolly", "2")
    # blah.insert_recur_2("lola", "3")
    # blah.insert_recur_2("loby", "4")
    # print(blah.traverse())
    # print(blah.search_recur("lol"))
    # print(blah.search_recur("lolly"))
    # print(blah.search_recur("lola"))
    # print(blah.search_recur("loby"))
    #print(blah.search_recur("loll")) # should give error

    test_trie = Trie()
    # inserting all the suffixes of "apples"
    test_trie.insert("apples",0)
    test_trie.insert('pples', 1)
    test_trie.insert("ples",2)
    test_trie.insert('les', 3)
    test_trie.insert("es",4)
    test_trie.insert('s', 5)
    test_trie.insert("",6)
    new_trie = Trie()
    print(new_trie.generate_suffix_array())
















