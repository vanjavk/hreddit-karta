import json
from tinycss2 import *
import re
from xml.dom import minidom
from pprint import pprint
from colormath.color_objects import CMYKColor, sRGBColor
from colormath.color_conversions import convert_color
from PIL import Image, ImageFilter, ImageOps
def calccoords(xinyin):

	yin,xin=xinyin

	bottom=42.392423
	top=46.554968
	right=19.447751
	left=13.491044
	#t=4
	t=5
	#b=301
	b=307
	r=310
	#l=5
	l=1
	y=(yin-top)/(bottom-top)*(b-t)+t
	x=(xin-left)/(right-left)*(r-l)+l
	return(x-10,y-10)

precss=open("oldpre.css", "r", encoding="utf8").read()
premarkdown=open("oldpre.txt", "r", encoding="utf8").read()
postcss=open("oldpost.css", "r", encoding="utf8").read()
postcsscro=open("oldpostcro.css", "r", encoding="utf8").read()
postmarkdown=open("oldpost.txt", "r", encoding="utf8").read()
css=precss
markdown=premarkdown
data=json.loads(open("data.json", "r", encoding="utf8").read())
width=20
height=20
grboviim=Image.new("RGBA",(width,42*height),(0,0,0,0))
brojalo=0


svg_file=open("hreddit.svg","r+", encoding="utf8")
try:
	doc = minidom.parse(svg_file)
except:
	print("error")
  # parseString also exists
#print(doc.getElementById('HR0_Hrvatska').getElementsByTagName("g"))

zupanije = [path for path
                in doc.getElementsByTagName("g")+doc.getElementsByTagName("path") if "HR0" in path.getAttribute('id') and all(x not in path.getAttribute('id') for x in ["HR0_","HR03_","HR04_"])]
style = doc.getElementsByTagName("style")
#for i in zupanije:
#	print (i.getAttribute('id'),i.getAttribute('class'))
#stylecss=str(style[0].firstChild.nodeValue)
sthrk = {i.getAttribute('class'):i.getAttribute('id') for i in zupanije}
#pprint(sthrk)
stylecss=parse_stylesheet(style[0].firstChild.nodeValue,skip_whitespace=True)
#pprint(stylecss)
#pprint(stylecss[1])
#pprint(stylecss[1].prelude)
#pprint(stylecss[1].content)
#pprint(stylecss[1].content[-2].value)

zupss={i:data["zupanije"][i]["gdpp"] for i in data["zupanije"]}
#for i in lik:
#    j=i.split()
#    zupss[i[i.find(".")+5:i.find(",",i.find(".")+5)-2]]=int(j[-1].replace(',',''))
#pprint(zupss)
g=list()
gdp=list()
gdpcolor=list()
zupssmod=zupss
zupssmod['Grad Zagreb']=17000
for w in sorted(zupssmod, key=zupssmod.get, reverse=True):
    g.append(w)
    gdp.append(zupssmod[w])

for i in gdp:
    gdpcolor.append(round((i-min(gdp))/(max(gdp)-min(gdp))*0.70,3))
#for i in range(len(g)):
#    print (gdpcolor[i]*100,g[i])
zupssgdpp={data["zupanije"][g[i]]["code"]:gdpcolor[i] for i in range(len(g))}


#pprint(zupssgdpp)


for i in range(len(stylecss)):

	#if stylecss[i].prelude[0].value in sthrk:
		#stylecss[i].prelude[0].value=sthrk[stylecss[i].prelude[0].value]
	#print(stylecss[i].content[10])
	if "HR03" in stylecss[i].prelude[0].value:
		cmik=CMYKColor(1,0.5,0,1*zupssgdpp[stylecss[i].prelude[0].value[0:5]])
		hexana=convert_color(cmik,sRGBColor).get_rgb_hex().upper().replace("#","")
		stylecss[i].content[10].value=hexana
		#0080FF
	if "HR04" in stylecss[i].prelude[0].value:
		cmik=CMYKColor(0,0.5,1,1*zupssgdpp[stylecss[i].prelude[0].value[0:5]])
		hexana=convert_color(cmik,sRGBColor).get_rgb_hex().upper().replace("#","")
		stylecss[i].content[10].value=hexana
		#FF8000
	#print(i)


#for i in range(len(stylecss)):
#	print(stylecss[i].prelude[1].value)


doc.getElementsByTagName("style")[0].firstChild.nodeValue=serialize(stylecss)
newsvg= open("hredditnew.svg","w", encoding="utf8")
doc.writexml(newsvg)

#for i in zupanije:
	#print (i.getAttribute('id'),i.getAttribute('class'))
#	style[0].firstChild.nodeValue=style[0].firstChild.nodeValue.replace("."+i.getAttribute('class'),"#"+i.getAttribute('id'))

	

#for i in [m.start() for m in re.finditer('fill:#', style[0].firstChild.nodeValue)]:
#	style[0].firstChild.nodeValue=style[0].firstChild.nodeValue.replace(style[0].firstChild.nodeValue[i+6:i+12],"ee42f4")


#pprint(style[0].firstChild.nodeValue)

#print(path_strings)
#doc.unlink()
#with open("file_out.txt", "w", encoding="utf8") as fout:
#    pprint(xmltodict.parse(svg_file)['svg'],fout)
#pprint(xmltodict.parse(svg_file))

print  (calccoords((43.783333, 16.333333)))#cavoglave
for j in data:
	for i in data[j]:
		if j in ["gradovi","np","pp"]:
			markdown+="* ["+i+"]("+data[j][i]["web"]+' "'
			if j=="gradovi":
				markdown+=i
			elif j=="np":
				markdown+="NP "+i
			elif j=="pp":
				markdown+="PP "+i
			markdown+='")\n'

		if j in ["gradovi","np","pp"]:
			x,y=calccoords(data[j][i]["loc"])
			css+='\ndiv.side .md>ul a[href="'+data[j][i]["web"]+'"]{\n'
			css+='  top: '+str(y)+"px;\n  left: "+str(x)+"px;"#kordinate

			
			css+='\n  background-position: 0px -'+str((brojalo)*height)+'px;'
			if j in ['np','pp']:
				if data[j][i]["visits"]>1000000:
					uvecanje=1
				elif data[j][i]["visits"]>100000:
					uvecanje=0.75
				else:
					uvecanje=0.5
				css+='\n transform: scale('+str(0.33*uvecanje)+');'

			css+="\n}\n"
			if j in ['np','pp']:
				css+='div.side .md:hover a[href="'+data[j][i]["web"]+'"]{\n'
				if data[j][i]["visits"]>1000000:
					uvecanje=1
				elif data[j][i]["visits"]>100000:
					uvecanje=0.75
				else:
					uvecanje=0.5
				css+='\n transform: scale('+str(0.4*uvecanje)+');'	
				css+="\n}\n"

			css+='\ndiv.side .md>ul a[href="'+data[j][i]["web"]+'"]::before{\n'
			

			if j=="gradovi":
				if data[j][i]['code']=='BIH' or data[j][i]['code']=='SI' or data[j][i]['code']=='ME':
					css+='  background: #ffcc00;'
				else:
					css+='  background: #ffff00;'#kordinate
			elif j=="np":
				css+='  background: #00af00;'#008400;'#kordinate
			elif j=="pp":
				css+='  background: #00ff00;'#kordinate

			css+="\n}\n"

		if j=="np" or j=="pp":
			css+='\ndiv.side .md>ul a[href="'+data[j][i]["web"]+'"]:hover{\n'
			css+='transform: scale(1);\n'
			css+='box-shadow: 0px 0px 4px 1px rgba(255,255,255,0.3);'


			css+="\n}\n"


		
		

		if j in ["gradovi","np","pp"]:
			try:
				im = Image.open("grbovi/"+data[j][i]["code"]+".gif")
			except:
				im = Image.open("grbovi/"+data[j][i]["code"]+".png")
			im = im.convert(mode="RGBA")
			im.thumbnail(size=(height,width), resample=Image.LANCZOS)
			#im = im.resize(size=(height,width), resample=Image.LANCZOS)
			addw = width - im.size[0]
			addh = height - im.size[1]
			grboviim.paste(im, ((width-im.size[0])//2, brojalo*height))
			im.save("grbovi/mini/"+data[j][i]["code"]+".png")
			brojalo+=1

		
		print (i, "generated.")
grboviim.save("grbovi/mini/"+"grbovi"+".png")




css+=postcss
markdown+=postmarkdown
print("gotovo")
open("oldfinal.css", "w", encoding="utf8").write(postcsscro+css)
open("oldfinal.txt", "w", encoding="utf8").write(markdown)