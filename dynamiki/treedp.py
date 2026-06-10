class Node:
    def __init__(self, val) -> None:
        self.left = None 
        self.right = None 
        self.val = val


def solve(root):

    global_max = float("-inf")

    def dfs(node):
        global global_max

        if node is None:
            return 0

        if node.left: 
            ans_left = dfs(node.left)
        else:
            ans_left = 0
        if node.right:
            ans_right = dfs(node.right)
        
        else: ans_right = 0

        akt = max(ans_right, 0)+ max(ans_left,0) + node.val 
        global_max = max(global_max,akt)

        score = max(node.val+max(0,ans_right),node.val+max(0,ans_left))
        
        return score
    
    dfs(root)

    return global_max