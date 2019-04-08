import json
def calccoords(xinyin):

	yin,xin=xinyin

	bottom=42.392423
	top=46.554968
	right=19.447751
	left=13.490044
	t=4
	b=301
	r=310
	l=5
	y=(yin-top)/(bottom-top)*(b-t)+t
	x=(xin-left)/(right-left)*(r-l)+l
	return(x-7.5,y-7.5)

precss=open("pre.css", "r", encoding="utf8").read()
premarkdown=open("pre.txt", "r", encoding="utf8").read()
postcss=open("post.css", "r", encoding="utf8").read()
postmarkdown=open("post.txt", "r", encoding="utf8").read()
css=precss
markdown=premarkdown
data=json.loads(open("data.json", "r", encoding="utf8").read())



for j in data:
	for i in data[j]:
		markdown+="["+i+"]("+data[j][i]["web"]+' "'+i+'")'
		x,y=calccoords(data[j][i]["loc"])
		css+='\na[href="'+data[j][i]["web"]+'"]{\n'
		css+='  top: '+str(y)+"px;\n  left: "+str(x)+"px;"#kordinate

		if "UNESCO" in data[j][i]:
			"\n  box-shadow: 0px 0px 3px 1.5px rgba(91,146,229,0.8);"

		css+="\n}\n"

		if "UNESCO" in data[j][i]:
			css+='\na[href="'+data[j][i]["web"]+'"]:hover{\n'

			css+="box-shadow: 0px 0px 4px 1px rgba(91,146,229,0.8);"

			css+="\n}\n"



		css+='\na[href="'+data[j][i]["web"]+'"]::before{\n'

		if j=="gradovi":
			css+='  background: #ffff00;'#kordinate
		elif j=="np":
			css+='  background: #00ff00;'#kordinate

		css+="\n}\n"
		print (i, "generated.")



css+=postcss
markdown+=postmarkdown
print("gotovo")
open("final.css", "w", encoding="utf8").write(css)
open("final.txt", "w", encoding="utf8").write(markdown)