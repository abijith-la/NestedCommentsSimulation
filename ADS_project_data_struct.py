import sys
sys.setrecursionlimit(1000000)

from timeit import default_timer as timer
from datetime import timedelta

#test_data
post_content = "Python is a great language to start your programming journey with...\nPython is a high-level, \
interpreted, interactive and object-oriented scripting language.\nPython is designed to be highly readable.\nIt \
uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."


class Post:
    def __init__(self, pno = 1, pcontent = "NO CONTENT"):
        self.pno = pno
        self.pcontent = pcontent
    def print_post(self):
        print("POST {}:".format(self.pno))
        print(self.pcontent)
        print("\nCOMMENTS:\n")


class Comment_Tree:
    def __init__(self,content,author,indent):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.content = content
        self.author = author
        self.indent = indent
    def reply_iter(self,ptr):
       if ptr.right is not None:
           ptr = ptr.right
           self.iter(ptr)
       else:
            return 0

    def iter(self,ptr):
        self.printer(ptr)
        self.reply_iter(ptr)
        if ptr.down is not None:
            ptr = ptr.down
            self.iter(ptr)
        else:
            return 0
        

    def display(self):
        ptr = self
        self.iter(ptr)


    def printer(self, ptr):
        print(ptr.indent*'\t',ptr.content,"-{}".format(ptr.author))      
    



start = timer()

P = Post(1,post_content)
tree = Comment_Tree("This post was really fun to read.","Abijith",0)

tree.right = Comment_Tree("I would also agree.","Dinesh",1)
tree.right.left = tree

tree.right.right = Comment_Tree("Thank you for your compliments.","Author",2)
tree.right.right.left = tree.right

tree.down = Comment_Tree("You could improve this post by also providing the links of your sources.","Ash",0)
tree.down.up = tree

tree.down.right = Comment_Tree("I'll add it in immediately","Author",1)
tree.down.right.left = tree.down.right

def down(tree,i):
    if i > 0:
        tree.down = Comment_Tree("This is a test comment","me",0)
        i = i-1
        tree.down.up = tree
        down(tree.down,i)
    return tree

P.print_post()
tree.display()


end = timer()
print("\nTime Taken: ",timedelta(seconds=end-start))
