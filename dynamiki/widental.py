class Node:
    def __init__(self) -> None:
        self.left = None 
        self.right = None 
        self.parent = None



def solve(root):

    nodes = []

    def dfs(node,depth):
        if node is None: return 

        children = 0
        if node.left:
            children+=1
            dfs(node.left, depth+1)
        
        if node.right:
            children+=1
            dfs(node.right, depth+1)
        
        node.append((depth, children))

    
    dfs(root,0)

    m = max(d for _, d in nodes)
    best = float('inf')
    for h in range(0,m+1):
        cuts = 0

        for depth, children in nodes:
            if depth==h:
                cuts+=children
            if depth<h and children==0:
                cuts+=1
        best = min(best,cuts)
    return best