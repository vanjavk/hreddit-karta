asdf="""Zastava bjelovarsko bilogorske zupanije.gif Bjelovar-Bilogora	4,105	4,550	5,108	5,135	5,510	5,848	6,634	6,691	8,255	7,677	7,059	7,062	6,879	6,838	7,012	7,342	7,792	8,272	8,831
Flag of Brod-Posavina County.svg Brod-Posavina	3,260	3,633	3,955	4,065	4,452	4,487	4,972	5,345	6,183	5,606	5,852	5,882	5,853	5,858	5,661	5,962	6,544	7,098	7,746
Flag of Dubrovnik-Neretva County.png Dubrovnik-Neretva	4,679	5,146	5,456	5,990	7,059	7,719	8,482	10,042	10,601	9,990	10,265	9,807	9,861	9,969	10,177	10,717	11,342	11,831	12,415
Zastava Istarske županije.svg Istria	6,828	7,728	8,597	9,275	10,192	10,628	11,377	12,463	13,195	12,810	13,298	12,991	12,677	12,711	12,724	13,225	13,853	14,352	15,003
Flag of Karlovac county.svg Karlovac	4,124	5,054	5,581	5,408	5,580	6,125	6,923	7,825	8,451	7,634	7,539	7,709	7,621	7,763	7,629	8,007	8,782	9,582	10,158
Flag of Koprivnica-Križevci County.png Koprivnica-Križevci	5,487	5,894	5,406	6,441	6,620	7,157	8,386	9,142	9,730	9,371	9,108	8,524	9,156	8,768	8,564	8,791	9,342	9,992	10,583
Flag of Krapina-Zagorje-County.svg Krapina-Zagorje	3,995	4,639	4,843	5,001	5,161	5,993	6,345	7,144	7,377	6,576	6,174	6,300	6,246	6,380	6,541	6,887	7,388	7,892	8,531
Flag of Lika-Senj County.png Lika-Senj	4,478	4,822	5,941	7,249	9,892	7,603	8,074	8,039	9,725	8,707	8,243	8,081	7,764	7,841	7,822	8,155	8,621	9,131	9,831
Medjimurje-flag.gif Međimurje	4,397	4,855	5,494	5,535	5,855	6,125	7,074	7,581	8,960	8,349	8,353	8,459	8,436	8,481	8,686	9,029	9,542	10,111	10,847
Zastava Osječko-baranjske županije.png Osijek-Baranja	4,147	4,537	5,149	5,199	5,750	6,127	6,757	7,875	8,871	8,112	8,246	8,271	8,093	8,121	8,045	8,413	9,142	10,001	10,641
Flag of Požega-Slavonia County.png Požega-Slavonia	3,934	4,320	4,610	5,020	5,383	5,605	5,786	6,505	6,750	6,229	6,404	6,281	6,101	6,102	5,827	6,061	6,459	7,141	7,874
Flag of Primorje-Gorski Kotar County.png Primorje-Gorski Kotar	6,682	6,765	7,155	7,997	8,474	9,674	10,560	11,177	12,680	12,305	12,515	12,724	13,110	12,930	12,548	12,770	13,377	13,835	14,139
Flag of Sisak-Moslavina County.png Sisak-Moslavina	4,949	5,067	5,274	5,349	5,654	6,331	7,391	8,401	9,312	9,141	9,241	9,512	9,412	9,612	9,884	10,134	10,874	11,721	12,538
Flag of Split-Dalmatia County.svg Split-Dalmatia	4,097	4,468	4,840	5,192	5,935	6,298	6,932	8,003	8,422	7,952	8,340	8,072	7,875	7,849	7,808	8,186	8,709	9,543	10,412
Flag of Šibenik-Knin County.png Šibenik-Knin	3,710	3,953	4,466	5,019	5,691	6,513	6,575	7,799	8,156	7,239	7,848	7,930	7,869	8,051	8,068	8,291	8,548	9,048	9,664
Flag of Varaždin County.png Varaždin	4,852	5,422	6,198	6,338	6,305	6,711	7,552	8,223	9,404	8,834	8,338	8,285	8,300	8,415	8,448	8,871	9,372	10,041	10,583
Flag of Virovitica-Podravina County.png Virovitica-Podravina	4,045	4,654	5,016	5,176	5,410	5,485	6,497	6,923	7,485	6,399	6,179	6,333	6,199	6,043	5,655	5,852	6,300	6,992	7,641
Flag of Vukovar-Syrmia County.svg Vukovar-Srijem	3,184	3,528	3,903	4,127	4,414	4,807	5,501	5,756	6,647	5,974	6,123	6,217	5,996	6,025	5,897	6,235	6,873	7,599	8,003
Flag of Zadar County.png Zadar	3,872	4,497	5,027	5,806	6,198	6,731	6,918	7,980	9,051	8,388	8,460	8,302	8,169	8,173	8,197	8,604	8,983	9,592	10,148
Zagreb County.png Zagreb County	4,236	4,166	5,111	5,249	5,731	6,368	6,458	7,360	8,036	7,803	7,755	7,786	7,791	7,781	7,897	8,265	8,742	9,512	10,358
Flag of Zagreb.svg City of Zagreb	8,532	9,674	10,529	11,527	12,701	14,216	15,567	16,766	18,554	17,814	19,211	18,503	18,506	18,132	17,908	18,579	19,631	20,884	22,125"""
lik=asdf.split("\n")
zupanije={}
for i in lik:
    j=i.split()
    zupanije[i[i.find(".")+5:i.find(",",i.find(".")+5)-2]]=int(j[-1].replace(',',''))

g=list()
gdp=list()
gdpcolor=list()
for w in sorted(zupanije, key=zupanije.get, reverse=True):
    g.append(w)
    gdp.append(zupanije[w])
for i in gdp:
    gdpcolor.append(round(1-(i-min(gdp))/(max(gdp)-min(gdp))*0.9,3))
for i in range(len(g)):
    print (gdpcolor[i]*100,g[i])


