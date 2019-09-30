class point:
     def __init__(self, dim, data):
         self.dim=dim
         self.data=[]
         for i in range(dim):
             self.data.append(float(data[i]))
     def __repr__(self):
         output=""
         for i in self.data:
             output+=str(i)+" "
         return output
     def scale(self, x):
         for i in range(self.dim):
             self.data[i]*=x
     def add(self, apoint):
          alist= []
          p1 = []
          p3 = [0]
          for i in range(self.dim):
             p3 =self.data[i]+apoint.data[i]
             alist.append(p3)
             self.data[i] = alist[i]
          return p1
     
     def sqmag(self):
          p4=[0]
          blist =[]
          for i in range(self.dim):
               p4=self.data[i]*self.data[i]
               blist.append(p4)
               self.data[i] = blist[i]
          return blist
