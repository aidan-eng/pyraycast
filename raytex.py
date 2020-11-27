import turtle
from math import *

t=turtle.Turtle()
turtle.speed(0)
turtle.bgcolor("black")
loc=turtle.Turtle()
tig=turtle.Turtle()
tig.goto(0,0)
tig.pu()
tig.ht()
sw=int(240)
sh=int(40)
fov=float(0.070)
fd=float(10)
turtle.setworldcoordinates(-300,200,-72,0)
t.speed(0)
t.color('red')
t.pu()
t.pensize(4)
t.goto(-300,200)
t.right(90)
#t.pd()
#t.pendown()
#turtle.tracer(0)
h=float(0)
loc.goto(5.5,5.5)
loc.penup()
loc.ht()
tig.left(90)
from math import *
def trig(angle, side_length, side_respective_to_angle, unknown):
    sohcahtoa = [
        ['opposite', 'hypotenuse', 'adjacent'],
        [None, math.sin, math.tan],
        [math.sin, None, math.cos],
        [math.tan, math.cos, None]
    ]
    index1 = sohcahtoa[0].index(side_respective_to_angle)
    index2 = sohcahtoa[0].index(unknown)
    function = sohcahtoa[index1 + 1][index2]
    return (side_length / function(math.radians(angle))
        if side_respective_to_angle == 'opposite' or (side_respective_to_angle == 'adjacent' and unknown == 'hypotenuse')
        else function(math.radians(angle) * side_length))
# constant
pi_180=(22/7)/180

tex=[['1111111111'],['0001000010'],['0001000010'],['0001000010'],['0001111110'],['0000010010'],['0000010010'],['1111110011'],['1111110011'],['1111111111']]
             

# use multiline string define to make the map easier to
# see/adjust
map = '''
xxxxrxrxrxrxrxrx
x..............r
x..............x
x.........gggggx
x..............r
x..............x
xxx............r
xx.............x
x.........r...rx
x.........r....r
x.........r....x
x..............r
x..............x
x..............r
x..............x
xrxrxrxrxrxrxrxx
'''.strip()
# strip just removes any whitespace at the beginning and end

# generate ma1, note this could easily be extended
# to auto-detect width and height.
ma1 = []
for row in map.splitlines():
  ma1.extend(row) # strip the neewline from the map
mx = my = int(sqrt(len(ma1))) # autodetect map square

turtle.tracer(0)

# keyboard
is_up = False
is_down = False
is_left = False
is_right = False

def press_up():
    global is_up
    is_up = True

def release_up():
    global is_up
    is_up = False

def press_down():
    global is_down
    is_down = True

def release_down():
    global is_down
    is_down = False

def press_left():
    global is_left
    is_left = True

def release_left():
    global is_left
    is_left = False

def press_right():
    global is_right
    is_right = True

def release_right():
    global is_right
    is_right = False

def exit_prog():
    exit()

turtle.onkeypress(press_up, "w")
turtle.onkeyrelease(release_up, "w")
turtle.onkeypress(press_down, "s")
turtle.onkeyrelease(release_down, "s")
turtle.onkeypress(press_left, "a")
turtle.onkeyrelease(release_left, "a")
turtle.onkeypress(press_right, "d")
turtle.onkeyrelease(release_right, "d")
turtle.onkey(exit_prog, "q")
turtle.listen()

def position():
    dirty = False
    if is_left:
        dirty = True
        loc.right(5)
    if is_right:
        dirty = True
        loc.left(5)
    if is_down:
        dirty = True
        loc.backward(0.1)
        if (ma1[int(loc.ycor()-0.1) * mx + int(loc.xcor()-0.1)] == 'x'):
            loc.backward(-0.1)
    if is_up:
        dirty = True
        loc.forward(0.1)
        if (ma1[int(loc.ycor()-0.1) * mx + int(loc.xcor()-0.1)] == 'x'):
            loc.forward(-0.1)
    if dirty:
        turtle.tracer(0)
        t.clear()
        draw_rays()
        turtle.update()
        turtle.listen()
    turtle.ontimer(position,1)

def do_color(c, dis):
    shade = int(255-(dis*1.2*12.75))
    dark=shade
    if c == "1":
        return dark,dark,dark
    if c == "0":
        return 0,0,shade
    return 0,0,255

def draw_rays():
    py = float()
    px = float()
    pa = float()
    hit = False
    ty = 0
    tx = 0
    spot = 'r'

    # Rays are cast in vertical slices
    for i in range (int(sw)):
          hit = False
          ra=float(((pa-fov/2)+(i)/(mx)*fov))
          #print(ra-pa)
          ex=float(sin(ra))
          ey=float(cos(ra))
          dis=float(0)
          while hit ==False and dis< fd:
              dis=dis+0.05
              urtx=(px+ex*dis)
              urty=(py+ey*dis)
              tx=int(urtx)
              ty=int(urty)
              
              hyp=abs((px-urtx)**2)
              opp=abs((py-urty)**2)
              adj=sqrt(opp+hyp)
              if tx<0 or tx>=mx or ty<0 or ty>= my:
                  hit=True
              else:
                  spot = ma1[(tx*mx+ty)]
                  if(spot!='.'):
                      hit=True
                      #print(str(round(urtx,1))[-1],str(round(urty,1))[-1])
          if dis>= fd:
              hit=True
          if hit:
              tdis=dis

              if int(str(round(urtx,1))[-1])==0:
                  collum=int(str(round(urty,1))[-1])
                  
              if int(str(round(urty,1))[-1])==0:
                  collum=int(str(round(urtx,1))[-1])              

              
              h=40-(tdis*4)
              t.forward((((40-h)/2)*5))
              turtle.colormode(255)
              t.pd()
              # further back = darker red
              t.pencolor(*do_color(spot,dis))
              h=(h*5)/10
              for dr in range (10):
                  
                  spot=str(int(tex[collum][0][dr]))
                  t.pencolor(*do_color(spot,tdis))
                      
                  
                  t.fd(h)

             

              
              #t.color("black")
              #t.fd((((40-h)/2))*5)
              t.pu()
              t.goto((-300)+i,200)
              #t.pd()
              dis=0
              px=loc.ycor()
              py=loc.xcor()
              radian = (loc.heading()-40)*(pi_180)
              pa=radian

#initial state
draw_rays()
turtle.update()
turtle.ontimer(position,1)
# run
turtle.mainloop()
