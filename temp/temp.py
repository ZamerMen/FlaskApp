from app import app
from models import db
db.create_all()
from models import Plat
p = Plat(title='fp', body='its body post')
db.session.add(p)#хранит все монипуляции над базой
db.session.commit()



class Rectangle:
	def __init__(self,lenght, width):
		self.lenght = lenght
		self.width = width

	def __str__(self):
		return f'работает функция str длина равна={self.lenght} а аширина ={self.width}'

class Square(Rectangle):


	def m2(self):
		return self.lenght*self.width

class Square1(Rectangle):
	def __init__(self, lenght, width):
		super().__init__(lenght,width)

	def m2(self):
		return self.lenght*self.width


ob = Square(20,20)
print(ob.m2())


ob1 = Square1(10,20)
print(ob1.m2())
print(str(ob1))
print(repr(ob1))