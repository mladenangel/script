# delwin

class SortedList:
    def __init__(self,sequence=None,key=None):
        self.__key=key or _identity
        assert hasattr(self.__key,'__call__')
        if sequence is None:
            self.__list=[]
        elif (isinstance(sequence,SortedList) and sequence.key == self.__key):
            self.__list = sequence.__list[:]
        else:
            self.__list = sorted(list(sequence), key=self.__key)


class SortedDict(dict):

    def __init__(self,dictionary=None,key=None,**kwargs):
        dictionary = dictionary or {}
        super().__init__(dictionary)
        if kwargs:
            super().update(kwargs)
        self.__key=SortedList(super().keys(),key)


d=SortedDict(dict(S=1,A=2,Y=6,c=0,e=10,w=3),str.lower)

print(d)
