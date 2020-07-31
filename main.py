from animal import dog # animal 패키지에서 dog 라는 모듈을 가져와줘
from animal import cat # animal 패키지에서 cog 라는 모듈을 가져와줘

from animal import * # animal 패키지가 갖고 있는 모듈을 다 불러와줘

d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()

a = Dog()
b = Cat()
a.hi()
b.hi()