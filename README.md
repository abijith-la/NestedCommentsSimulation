# nested-comments-simulation
Developed custom data structures that simulate the storage and retrieval of nested comments as seen on various social media platforms using Python and analyzed their time complexity to compare their effectiveness. 

TWO-DIMENSIONAL TREE

In this approach we use a two-dimensional tree to store all our comments in. Each comment node is connected in 4 directions. Up and Down for comments of the same level. Left and Right to access replies and parent comments. The comments are rendered using two functions that call each other recursively.

NESTED LIST

In this approach each comment object has a list member in it. This list contains all the children of the comment. These children are also the same type of objects and have their own list of children/replies.

DICTIONARY TABLE AND ORDERED LIST

In this approach we assign a unique (uuid) to each and every comment object. These IDs and comment object pairs are stored in a dictionary. The IDs alone are also stored in an ordered list. The order of this list ensures that all the comments are rendered in the correct hierarchical order. Each comment object stores its parent ID as a class member.

![alt name](https://user-images.githubusercontent.com/87352664/190663704-95c9f101-6fcf-472e-b78f-91cf3d0f17bf.png)
