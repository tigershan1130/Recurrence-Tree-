class TsTree(object):
    def __init__(self, Parent, data, depth = 0):
        self.root = Parent
        self.childs = []
        self.data = data       
        self.depth = depth
        
    def AddChildren(self, dataVal):
        TreeObj = TsTree(self, dataVal, self.depth+1)    
        self.childs.append(TreeObj)
        return TreeObj

    # recursively push our children to hash
    def PushTreeDataToHash(self, hash):

        # this will print the tree recursively using its depth
        # we can traverse through tree using BFS and push it to a hash, then print the hash       

        if(self.depth in hash):            
            hash[self.depth].append(self.data)
        else:
            hash[self.depth] = []
            hash[self.depth].append(self.data)


        if(len(self.childs) <= 0):
            return

        for i in range (len(self.childs)):
            self.childs[i].PushTreeDataToHash(hash)

        return
    

