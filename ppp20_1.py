#객체 지향 프로그램
#(삼각형,샂각형,육각형)을 객체 (Shape)으로 묶어주기 시도
from turtle import Shape  # 파이참이 이거 해야한다고 도와줬어요 turtle 프로그램에서 shape 변수 가져온건가..
import math # 정육각형 넓이 구할 떄 쓰기 위해서
# 클래스 속성은 클래스와 인스턴스 전체 공유 가능
class Rectriangle(Shape):
    def __init__(self,one_bottom):
        self.one_bottom= one_bottom   # 이거 인스턴트 정리  인스턴스.속성 =값

    def area(self):
        dulrea= self.one_bottom * 3 #dulrea 는 둘레 입니다
        nurbee= self.one_bottom * math.sqrt(3) /2  # nurbee 는 넓이 입니다.
        return (dulrea, nurbee)

class Rectangle(Shape):
    def __init__(self,one_bottom):
        self.one_bottom=one_bottom
    def area(self):
        dulrea=self.one_bottom * 4
        nurbee=self.one_bottom **2
        return (dulrea,nurbee)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        # return (f"원의 넓이는,{self.radius**2*3.14}")
        dulrea= self.radius * 3.14
        nurbee= (self.radius**2) * 3.14
        return (dulrea, nurbee)


class RegularHexagon(Shape):
    def __init__(self,one_bottom):
        """one_bottom은 6개의 변중에 1개의 변을 가르킵니다. """
        self.one_bottom=one_bottom

    def area(self):
        dulrea =self.one_bottom * 6
        nurbee= self.one_bottom * math.sqrt(3) /3
        return dulrea, nurbee


def main():
    #도형의 둘레와 면적을 출력하세요
    Rectriangle_1= Rectriangle(8)
    Rectangle_1 = Rectangle(8)
    Circle_1 =Circle(2)
    RegularHexagon_1 = RegularHexagon(5)




    #정삼각형 둘레, 넓이
    print(f"정삼각형의 둘레는 {Rectriangle_1.area()[0]}입니다.")
    print(f"정삼각형의 넓이는 {Rectriangle_1.area()[1]:.0f}입니다.")

    #정사각형 둘레, 넓이
    print(f"정사각형의 둘레는 {Rectangle_1.area()[0]}입니다.")
    print(f"정사각형의 넓이는 {Rectangle_1.area()[1]}입니다.")

    #원 둘레 넓이
    print(f"원의 둘레는 {Circle_1.area()[0]:.2f}")
    print(f"원의 넓이는 {Circle_1.area()[1]:.2f}")

    #정육각형 둘레, 넓이
    print(f"정육각형의 둘레는 {RegularHexagon_1.area()[0]:.2f}")
    print(f"정육각형의 넓이는 {RegularHexagon_1.area()[1]:.2f}")



if __name__=="__main__":
    main()