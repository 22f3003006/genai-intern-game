class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Game:
    def __init__(self):
        self.head=None
        self.tail=None
        self.words=set()
        self.score=0
    def add_word(self,word):
        if word in self.words:
            return False
        node=ListNode(word)
        self.words.add(word)
        self.score+=1
        if not self.head:
            self.head=self.tail=node
        else:
            self.tail.next=node
        return True
    def history(self):
        result=[]
        current=self.head
        while current:
            result.append(current.val)
            current=current.next
        return result
