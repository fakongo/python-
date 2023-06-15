class myDeque:
    def __init__(self,iterable=None,maxlen=10):
        if iterable==None:
            self._content=[]
            self._current=0
        else:
             self._content=list(iterable)
             self._current=len(iterable)
        self._size=maxlen
        if self._size<self._current:
            self._size=len(iterable)

    def __del__(self):
        del self._content

