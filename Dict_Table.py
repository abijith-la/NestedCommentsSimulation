
from timeit import default_timer as timer
from datetime import timedelta
from uuid import uuid4 as uid
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


class Comment_Table:
    def __init__(self):
        self.table = {}
        self.order = []

    def add_reply(self, content = "This is a test comment", author = "me", reply_to = -1):
        if reply_to == -1:
            new_comment = Comment_Node(content = content, author = author)
            self.table[new_comment.id] = new_comment
            self.order.append(new_comment.id)
        else:
            reply_to = reply_to - 1
            parent_id = self.order[reply_to]
            indent = self.table[parent_id].indent + 1
            new_comment = Comment_Node(content, author, parent_id, indent)
            self.table[new_comment.id] = new_comment
            for i, v in enumerate(self.order): #getting index of parent id
                if v == new_comment.parent_id:
                    insert_at = i
            insert_at+=1
            if insert_at == len(self.order):
                self.order.append(new_comment.id)
            else:
                temp = insert_at
                for i in range (temp, len(self.order)): #checking for children after parent index
                    if self.table[self.order[i]].parent_id == new_comment.parent_id: #checking if parent_id of the nodes = new comment parent_id
                        insert_at +=1
                    else:
                        self.order.insert(insert_at,new_comment.id)
                        break 
                 

    def display_comments(self):
        for i in self.order:
            self.printer(self.table[i])

    def printer(self, ptr):
        print(ptr.indent*'\t',ptr.content,"-{}".format(ptr.author))


class Comment_Node:
    def __init__(self, content, author, parent_id = str(uid()), indent = 0):
        self.content = content
        self.author = author
        self.indent = indent
        self.parent_id = parent_id
        self.id = str(uid())

start = timer()

P = Post(1,post_content)
CT = Comment_Table()

CT.add_reply(content = "This post was really fun to read.", author = "Abijith")
CT.add_reply(content = "You could improve this post by also providing the links of your sources.", author = "Ash")
CT.add_reply(content = "I would also agree.", author = "Dinesh",reply_to = 1)
CT.add_reply(content = "Thank you for your compliments.", author = "Author",reply_to = 2)
CT.add_reply(content = "I'll add it in immediately",author = "Author",reply_to = 4)

P.print_post()
CT.display_comments()

end = timer()

print("\nTime Taken: ",timedelta(seconds=end-start))
