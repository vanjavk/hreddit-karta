bottom=42.392423
top=46.554968
right=19.447751
left=13.490044
t=4
b=301
r=310
l=5
#xin,yin=list(map(float,input().split(", ")))
yin,xin=list(map(float,"43.784, 16.337".split(", ")))
y=(yin-top)/(bottom-top)*(b-t)+t

x=(xin-left)/(right-left)*(r-l)+l
print("top: "+str(y)+"px;\n  left: "+str(x)+"px;")
