from graphics import *




winny = GraphWin("superCool", 3000, 400)
winny.setBackground("black")
#draw(winny)
 # pause for click in window

iNumbers = []

text_file = open("data.txt")
file_content = text_file.readlines()
#rData = file_content.split('\n')
for results in file_content:
    iNumbers.append(int(results))
        
text_file.close()

p = []
#40-50
third = [] 
#50-60
second = []
#60-70
first = []
#70+

Xpos1 = -50
Xpos2 = 0
Ypos1 = 200
Ypos2 = 200

for everyNumber in iNumbers:
    if (everyNumber < 50):
        p.append(everyNumber)
    if (everyNumber <= 60) and (everyNumber > 50):
        third.append(everyNumber)
    if (everyNumber < 70) and (everyNumber > 60):
        second.append(everyNumber)
    if (everyNumber >= 70):
        first.append(everyNumber)
        
for everyNumber in iNumbers:
    Xpos1 = Xpos1 + 50
    Xpos2 = Xpos2 + 50
    if (everyNumber in p):
        Ypos2 = Ypos2 + 20
        line = Line(Point(Xpos1,Ypos1),Point(Xpos2,Ypos2))
        Ypos1 = Ypos1 + 20
        line.setFill(color_rgb(255,255,0))
        line.setWidth(4)
        line.draw(winny)
    if (everyNumber in third):
        Ypos2 = Ypos2 + 10
        line = Line(Point(Xpos1,Ypos1),Point(Xpos2,Ypos2))
        Ypos1 = Ypos1 + 10
        line.setFill(color_rgb(255,255,0))
        line.setWidth(4)
        line.draw(winny)
    if (everyNumber in second):
        Ypos2 = Ypos2 - 10
        line = Line(Point(Xpos1,Ypos1),Point(Xpos2,Ypos2))
        Ypos1 = Ypos1 - 10
        line.setFill(color_rgb(255,255,0))
        line.setWidth(4)
        line.draw(winny)  
    if (everyNumber in first):
        Ypos2 = Ypos2 - 20
        line = Line(Point(Xpos1,Ypos1),Point(Xpos2,Ypos2))
        Ypos1 = Ypos1 - 20
        line.setFill(color_rgb(255,255,0))
        line.setWidth(4)
        line.draw(winny)    


#----------------------------------------------------------------------------------------------------        
        
#line = Line(Point(200,200),Point(250,p[0]))
#line.setFill(color_rgb(255,255,p[0]))
#line.setWidth(4)
#line.draw(winny)        
#
#line = Line(Point(200,200),Point(250,p[1]+50))
#line.setFill(color_rgb(255,255,p[1]))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,p[2]+100))
#line.setFill(color_rgb(255,255,p[2]))
#line.setWidth(4)
#line.draw(winny) 
#
#line = Line(Point(200,200),Point(250,p[3]+150))
#line.setFill(color_rgb(255,255,p[3]))
#line.setWidth(4)
#line.draw(winny) 
#
#line = Line(Point(200,200),Point(250,p[4]+200))
#line.setFill(color_rgb(255,255,p[4]))
#line.setWidth(4)
#line.draw(winny) 
#
#line = Line(Point(200,200),Point(250,p[5]+250))
#line.setFill(color_rgb(255,255,p[5]))
#line.setWidth(4)
#line.draw(winny) 
#
#line = Line(Point(200,200),Point(250,p[6]+300))
#line.setFill(color_rgb(255,255,p[6]))
#line.setWidth(4)
#line.draw(winny) 
#
#line = Line(Point(200,200),Point(250,p[7]+350))
#line.setFill(color_rgb(255,255,p[7]))
#line.setWidth(4)
#line.draw(winny) 
#
#line = Line(Point(200,200),Point(250,p[8]+400))
#line.setFill(color_rgb(255,255,p[8]))
#line.setWidth(4)
#line.draw(winny) 
#
##---------------------------------------------------------------------------------------------------------------------
#
#line = Line(Point(200,200),Point(250,third[0]+ 100))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)  
#
#line = Line(Point(200,200),Point(250,third[0]+ 150))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 200))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 250))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 300))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 350))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 400))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 450))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 500))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 550))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 600))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 650))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 700))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)
#
#line = Line(Point(200,200),Point(250,third[0]+ 750))
#line.setFill(color_rgb(255,third[0],255))
#line.setWidth(4)
#line.draw(winny)



#ball = Circle(Point(100,100), second[0])
#ball.setFill(color_rgb(second [0],second [0],second [0]))
#ball.draw(winny)
    
#example = Text(Point(200,550),third)
#example.setFill(color_rgb(66,172,95))
#example.draw(winny)
    
        
winny.getMouse()

