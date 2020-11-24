import json
with open("edges.json", "r", encoding='utf8') as fp:
    roads = json.load(fp) #type(sroad) = list
    roads = roads['features'] #type(sroad) = list
    s_road = []
    for i in roads:
        if 'G' in i['properties']['ref']:
            #将匹配到的数据写入列表
            s_road.append(i)
    s_road = {"type":"FeatureCollection", "features":s_road}
    with open("guodao.json", 'w', encoding='utf8') as f:
        json.dump(s_road,f,ensure_ascii=False)


