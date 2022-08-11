import turtle
turtle.register_shape('BP.gif')
turtle.register_shape('BL.gif')
turtle.register_shape('BN.gif')
turtle.register_shape('BB.gif')
turtle.register_shape('BQ.gif')
turtle.register_shape('BK.gif')
turtle.register_shape('WP.gif')
turtle.register_shape('WL.gif')
turtle.register_shape('WN.gif')
turtle.register_shape('WB.gif')
turtle.register_shape('WQ.gif')
turtle.register_shape('WK.gif')
board=turtle.Screen()
board.setup(400,400)
board.bgpic('Chess_Board.gif')
##클래스 상속 만들기
##기물의 정보
#1: 어떤 기물인가-색상,기물,등
#2:기물이 움직이는 규칙은 무엇인가
#3:기물이 어디에 있는가
#4:기물이 몇번 움직였는가
#5:기물이 공격 받고있는가
#6:기물의 점수는 몇점인가.
#여기서 3,4는 공통이다.
#기물을 설정해주고, 
class Pawn(turtle.Turtle):
    #폰에게 필요한 정보
    #값 설정
    #색상/색상에 따른 이동 정보
    #모양 만들어주기
    def init(self):
        self.speed(0)
        self.penup()
class Rook(turtle.Pawn):
    #룩의 이동관련 함수를 만들어야 한다.
    #룩에게 필요한 정보
    #룩 색깔
    #룩 위치
    #전에 터치가 된적이 있는지(캐슬링을 위해서)
    #룩 이동 법
        #룩 이동법에는 뭐가 필요할까 
        #일단 룩 값을 입력 받기(이건 메인에서 해도 될듯) input
        #입력 받은 값이 옮길 수 있는 부분인가 확인하기 move_checker
        #옮기기rook move==> goto

    def rook_move(self,x,y):
        if self.move_checker==0:
            print("you can not take that move")
            return 0
        else:
            self.goto(x,y)
            return 1
        
    def move_checker(self,x,y):
        #위치를 찾는다. 
        #위치 기반 갈 수 있는 곳 찾아보기
        #입력 받은 위치가 갈 수 있는 곳인지 확인하기
        return 0
        
class Knight(turtle.Pawn):
    #나이트 이동 함수
    def knight_move(self,x,y):
        return 0
        
        
    def move_checker(self):
        return 0
class Bishop(turtle.Pawn):
    # 비숏 이동 함수
    def bishop_move(self,x,y):
        return 0
        
        
    def move_checker(self):
        return 0
class Queen(turtle.Pawn):
    #퀸 이동 함수
    def queen_move(self,x,y):
        return 0
        
        
    def move_checker(self):
        return 0
class King(turtle.Pawn):
    #깅 이동 함수
    def king_move(self,x,y):
        return 0
        
        
    def move_checker(self):
        return 0


if __name__ =="__main__":
    idk=0
    