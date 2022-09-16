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


class Comments:
    def __init__(self,  indent = -1, content = None, author = None):
        self.author = author
        self.content = content
        self.indent = indent
        self.replies = []
    def add_reply(self, content = "This is a test comment", author = "me"):
        new_obj = Comments((self.indent+1), content, author)
        self.replies.append(new_obj)
    def display_comments(self, obj_list):
        for i in obj_list:
            self.printer(i)
            if i.replies is not False:
                self.display_comments(i.replies)
            else:
                continue
    def printer(self, ptr):
        print(ptr.indent*'\t',ptr.content,"-{}".format(ptr.author))


start = timer()

P = Post(1,post_content)
C = Comments()

C.add_reply(content = "This post was really fun to read.", author = "Abijith")
C.replies[0].add_reply(content = "I would also agree.", author = "Dinesh")
C.replies[0].replies[0].add_reply(content = "Thank you for your compliments.", author = "Author")
C.add_reply(content = "You could improve this post by also providing the links of your sources.", author = "Ash")
C.replies[1].add_reply(content = "I'll add it in immediately",author = "Author")

P.print_post()
C.display_comments(C.replies)

end = timer()
print("\nTime Taken: ",timedelta(seconds=end-start))
