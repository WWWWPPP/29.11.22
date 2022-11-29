class Shape:
    def __init__(self):
        self._position=None
        self._scale=0
        self._color=''
        
    def set_position(self,position):
        self._position=position
    def get_position(self):
        return self._position
    def set_scale(self,scale):
        self._scale=scale
    def get_scale(self):
        return self._scale
    def set_color(self,color):
        self._color=color
    def get_color(self):
        return self._color
    
    def info(self):
        print('Position - ',self._position,'\nScale - ',self._scale,'\nColor - ',self._color)
        
    def area(self):
        print('Plocshad figyriy')
        
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self._side1=0
        self._side2=0
        
    def set_side1(self,side1):
        self._side1=side1
    def get_side1(self):
        return self._side1
    def set_side2(self,side2):
        self._side2=side2
    def get_side2(self):
        return self._side2
    
    def info(self):
        super().info()
        print('Side1 -',self._side1,'\nSide2 -', self._side2)
    
    def area(self):
        print ('Rectangle')
        super().area()
        print (self._side1*self._side2)
        

class Trapezoid(Shape):
    def __init__(self):
        super().__init__()
        self._side1=0
        self._side2=0
        self._h=0
        
    def set_side1(self,side1):
        self._side1=side1
    def get_side1(self):
        return self._side1
    def set_side2(self,side2):
        self._side2=side2
    def get_side2(self):
        return self._side2
    def set_h(self,h):
        self._h=h
    def get_h(self):
        return self._h
    
    def info(self):
        super().info()
        print('Side1 -',self._side1,'\nSide2 -', self._side2,'\nViysota -', self._h)
    def area(self):
        print ('Trapezoid')
        super().area()
        print ((self._side1+self._side2)*self._h/2)
    
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self._radius=0
        
    def set_radius(self,radius):
        self._radius=radius
    def get_radius(self):
        return self._radius
    
    def info(self):
        super().info()
        print(self._radius)
        
    def area(self):
        print('Radius')
        super().area()
        print ('Circle ',3.14*(self._radius**2))

fp=Rectangle()
ft=Trapezoid()
fc=Circle()

fp.set_color('Black')
fp.set_position({'x':2,
                 'y':-3})
fp.set_scale(5)#Что это?
fp.set_side1(5)
fp.set_side2(3)

ft.set_color('Black')
ft.set_position({'x':9,
                 'y':-32})
ft.set_scale(5)#Что это?
ft.set_side2(5)
ft.set_side1(8)
ft.set_h(6)

fc.set_color('Black')
fc.set_position({'x':9,
                 'y':-32})
fc.set_scale(5)#Что это?
fc.set_radius(15)

fp.info()
fp.area()
print('')
ft.info()
ft.area()
print('')
fc.info()
fc.area()