import json
import re
from xml.dom import minidom
from pprint import pprint
from colormath.color_objects import CMYKColor, sRGBColor
from colormath.color_conversions import convert_color
from PIL import Image, ImageFilter, ImageOps

KARTA_SIZE = 312


def calccoords(xinyin):
    yin, xin = xinyin

    bottom = 42.392423
    top = 46.554968
    right = 19.447751
    left = 13.491044
    # t=4
    t = 5
    # b=301
    b = 307
    r = 310
    # l=5
    l = 1
    y = (yin - top) / (bottom - top) * (b - t) + t
    x = (xin - left) / (right - left) * (r - l) + l
    return (x - 10, y - 10)


precss = open("pre.css", "r", encoding="utf8").read()
premarkdown = open("pre.txt", "r", encoding="utf8").read()
postcss = open("post.css", "r", encoding="utf8").read()
postmarkdown = open("post.txt", "r", encoding="utf8").read()
css = precss
markdown = premarkdown
data = json.loads(open("data.json", "r", encoding="utf8").read())

svg_file = open("karta/hreddit.svg", "r+", encoding="utf8")
# svg_file = open("karta/hredditmodified.svg", "r+", encoding="utf8") #moram modifirati jer ima neki bug u parseru da kada convertam value koji pocinje sa slovom npr FFFFFF u 000000 on mi dodaje neke escapeove "/30 " pa modificiram boje da sve pocinju brojem jer onda mogu promijeniti u broj i nece biti buga????
try:
    doc = minidom.parse(svg_file)
except:
    print("error")
# parseString also exists
# print(doc.getElementById('HR0_Hrvatska').getElementsByTagName("g"))

zupanije = [path for path
            in doc.getElementsByTagName("g") + doc.getElementsByTagName("path") if
            "HR0" in path.getAttribute('id') and all(
                x not in path.getAttribute('id') for x in ["HR0_", "HR03_", "HR04_"])]
style = doc.getElementsByTagName("style")
# for i in zupanije:
#	print (i.getAttribute('id'),i.getAttribute('class'))
# stylecss=str(style[0].firstChild.nodeValue)
sthrk = {i.getAttribute('class'): i.getAttribute('id') for i in zupanije}
# pprint(sthrk)


import cssutils

stylecss = cssutils.parseString(style[0].firstChild.nodeValue)

zupss = {i: data["zupanije"][i]["gdpp"] for i in data["zupanije"]}
# for i in lik:
#    j=i.split()
#    zupss[i[i.find(".")+5:i.find(",",i.find(".")+5)-2]]=int(j[-1].replace(',',''))
# pprint(zupss)
g = list()
gdp = list()
gdpcolor = list()
zupssmod = zupss
zupssmod['Grad Zagreb'] = 17000
for w in sorted(zupssmod, key=zupssmod.get, reverse=True):
    g.append(w)
    gdp.append(zupssmod[w])

for i in gdp:
    gdpcolor.append(round((i - min(gdp)) / (max(gdp) - min(gdp)) * 0.70, 3))
# for i in range(len(g)):
#    print (gdpcolor[i]*100,g[i])
zupssgdpp = {data["zupanije"][g[i]]["code"]: gdpcolor[i] for i in range(len(g))}

# pprint(zupssgdpp)

for i in stylecss:

    if "HR03" in i.selectorText:

        cmik = CMYKColor(1, 0.5, 0, 1 * zupssgdpp[i.selectorText[1:6]])
        hexana = convert_color(cmik, sRGBColor).get_rgb_hex().upper()  # .replace("#", "")

        i.style['fill'] = hexana

    elif "HR04" in i.selectorText:

        cmik = CMYKColor(0, 0.5, 1, 1 * zupssgdpp[i.selectorText[1:6]])
        hexana = convert_color(cmik, sRGBColor).get_rgb_hex().upper()  # .replace("#", "")

        i.style['fill'] = hexana

doc.getElementsByTagName("style")[0].firstChild.nodeValue = stylecss.cssText.decode('utf-8')
with open("karta/hredditnew.svg", "w", encoding="utf8") as newsvg:
    doc.writexml(newsvg)

# a = -1
# for i in stylecss:
#     a += 1
#     if a == 1:
#         i.style['fill'] = "#24A0ED"  # 'st1'
#
#         i.style['opacity'] = "0.5"
#     if a == 2:
#         i.style['fill'] = "#1A1A1B"
#     if a == 4:
#         i.style['fill'] = "#1A1A1B"
# a = -1
# for i in stylecss:
#     a += 1
#     if a < 6:
#         continue
#     i.style['stroke'] = "#000000"
#     if a == 26:
#         break
# doc.getElementsByTagName("style")[0].firstChild.nodeValue = stylecss.cssText.decode('utf-8')
#
# with open("karta/hredditnewdark.svg", "w", encoding="utf8") as newsvg:
#     doc.writexml(writer=newsvg)

### GENERIRANJE GRBOVA
width = 20
height = 20
grboviim = Image.new("RGBA", (width, 42 * height), (0, 0, 0, 0))
brojalo = 0
for j in data:
    for i in data[j]:
        if j in ["gradovi", "np", "pp"]:
            markdown += "[" + i + "](" + data[j][i]["web"] + ' "'
            if j == "gradovi":
                markdown += i
            elif j == "np":
                markdown += "NP " + i
            elif j == "pp":
                markdown += "PP " + i
            markdown += '")'

        if j in ["gradovi", "np", "pp"]:
            x, y = calccoords(data[j][i]["loc"])
            css += '\na[href="' + data[j][i]["web"] + '"]{\n'
            css += '  top: ' + str(y) + "px;\n  left: " + str(x) + "px;"  # kordinate

            css += '\n  background-position: 0px -' + str((brojalo) * height) + 'px;'
            if j in ['np', 'pp']:
                if data[j][i]["visits"] > 1000000:
                    uvecanje = 1
                elif data[j][i]["visits"] > 100000:
                    uvecanje = 0.75
                else:
                    uvecanje = 0.5
                css += '\n transform: scale(' + str(0.33 * uvecanje) + ');'

            css += "\n}\n"
            if j in ['np', 'pp']:
                css += 'body:hover a[href="' + data[j][i]["web"] + '"]{\n'
                if data[j][i]["visits"] > 1000000:
                    uvecanje = 1
                elif data[j][i]["visits"] > 100000:
                    uvecanje = 0.75
                else:
                    uvecanje = 0.5
                css += '\n transform: scale(' + str(0.4 * uvecanje) + ');'
                css += "\n}\n"

            css += '\na[href="' + data[j][i]["web"] + '"]::before{\n'

            if j == "gradovi":
                if data[j][i]['code'] == 'BIH' or data[j][i]['code'] == 'SI' or data[j][i]['code'] == 'ME':
                    css += '  background: #ffcc00;'
                else:
                    css += '  background: #ffff00;'  # kordinate
            elif j == "np":
                css += '  background: #00af00;'  # 008400;'#kordinate
            elif j == "pp":
                css += '  background: #00ff00;'  # kordinate

            css += "\n}\n"

        if j == "np" or j == "pp":
            css += '\nbody a[href="' + data[j][i]["web"] + '"]:hover{\n'
            css += 'transform: scale(1);\n'
            css += 'box-shadow: 0px 0px 4px 1px rgba(255,255,255,0.3);'

            css += "\n}\n"

        if j in ["gradovi", "np", "pp"]:
            try:
                im = Image.open("grbovi/" + data[j][i]["code"] + ".gif")
            except:
                im = Image.open("grbovi/" + data[j][i]["code"] + ".png")
            im = im.convert(mode="RGBA")
            im.thumbnail(size=(height, width), resample=Image.LANCZOS)
            # im = im.resize(size=(height,width), resample=Image.LANCZOS)
            addw = width - im.size[0]
            addh = height - im.size[1]
            grboviim.paste(im, ((width - im.size[0]) // 2, brojalo * height))
            im.save("grbovi/mini/" + data[j][i]["code"] + ".png")
            brojalo += 1

        # print(i, "generated.")
grboviim.save("grbovi/mini/" + "grbovi" + ".png")
print("grbovi generated.")

css += postcss
markdown += postmarkdown
print("gotovo")
open("final.css", "w", encoding="utf8").write(css)
open("final.txt", "w", encoding="utf8").write(markdown)

from cairosvg import svg2png

with open(file="karta/hredditnew.svg", mode="r", encoding="utf-8") as myfile:
    svg2png(bytestring=myfile.read().encode('utf-8'), write_to='karta/hredditnew.png')
    print("hredditnew.png done")
# with open(file="karta/hredditnewdark.svg", mode="r", encoding="utf-8") as myfile:
#     svg2png(bytestring=myfile.read().encode('utf-8'), write_to='karta/hredditnewdark.png')
#     print("hredditnewdark.png done")

### STACKANJE 2 IMAGEA
# karteim = Image.new("RGBA", (KARTA_SIZE, 2 * KARTA_SIZE), (0, 0, 0, 0))
# im1 = Image.open("karta/hredditnew.png")
# im2 = Image.open("karta/hredditnewdark.png")
# im1 = im1.resize(size=(KARTA_SIZE,KARTA_SIZE), resample=Image.LANCZOS)
# im2 = im2.resize(size=(KARTA_SIZE,KARTA_SIZE), resample=Image.LANCZOS)
# # im1 = im1.convert(mode="RGBA")
# # im2 = im2.convert(mode="RGBA")
# # im.thumbnail(size=(height, width), resample=Image.LANCZOS)
# # im = im.resize(size=(height,width), resample=Image.LANCZOS)
# # addw = width - im.size[0]
# # addh = height - im.size[1]
# karteim.paste(im1, (0, 0))
# karteim.paste(im2, (0, KARTA_SIZE))
# # im.save("karta/hreddit" + data[j][i]["code"] + ".png")
#
#
# # print(i, "generated.")
# karteim.save("karta/background.png")
