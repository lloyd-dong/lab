
# coding: utf-8

# In[2]:

class P:
    def _internal_method(self,number):
        return ">0" if number >0 else "<=0"
            
    def main_method(self):
        print "in main_method"
        print "num is {}".format(self._internal_method(13))

    @staticmethod
    def s_method():
        print "static method"

