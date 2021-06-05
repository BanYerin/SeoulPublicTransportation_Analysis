import json
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

#subway mongoDB에 저장
myclient=MongoClient('mongodb://127.0.0.1:27017/')
projectDb = myclient["project"]
subwayCol = projectDb["subway"]

#한글 폰트 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#subway 역이름 승차 평균인원 시각화
avg_ride_pipelines=[{ "$project": {"sub_sta_nm":1,  "four_ride_num":1, "five_ride_num":1, "six_ride_num":1, "seven_ride_num":1, "eight_ride_num":1,
                                   "nine_ride_num":1, "ten_ride_num":1, "eleven_ride_num":1, "twelve_ride_num":1, "thirteen_ride_num":1, "fourteen_ride_num":1,
                                   "fifteen_ride_num":1, "sixteen_ride_num":1, "seventeen_ride_num":1, "eighteen_ride_num":1, "nineteen_ride_num":1,
                                   "twenty_ride_num":1, "twenty_one_ride_num":1, "twenty_two_ride_num":1, "twenty_three_ride_num":1, "midnight_ride_num":1,
                                   "one_ride_num":1, "two_ride_num":1, "three_ride_num":1} },
                    { "$addFields": { "totalRide": { "$sum": [ "$four_ride_num", "$five_ride_num", "$six_ride_num", "$seven_ride_num", "$eight_ride_num",
                                                               "$nine_ride_num", "$ten_ride_num", "$eleven_ride_num", "$twelve_ride_num", "$thirteen_ride_num",
                                                               "$fourteen_ride_num", "$fifteen_ride_num", "$sixteen_ride_num", "$seventeen_ride_num",
                                                               "$eighteen_ride_num", "$nineteen_ride_num", "$twenty_ride_num", "$twenty_one_ride_num",
                                                               "$twenty_two_ride_num", "$twenty_three_ride_num", "$midnight_ride_num", "$one_ride_num",
                                                               "$two_ride_num", "$three_ride_num" ] } } },
                    { "$group": { "_id": "$sub_sta_nm", "avgRide": { "$avg": "$totalRide" } } },
                    { "$sort": { "avgRide":-1} },{ "$limit":5 },{ "$project": { "_id":1, "avgRide":1} }]

avg_ride_results=subwayCol.aggregate(avg_ride_pipelines)

avg_ride_x=list()
avg_ride_y=list()
max_val=0

for doc in avg_ride_results:
    avg_ride_x.append(doc['_id'])
    avg_ride_y.append(round(doc['avgRide'], 2))

    if max_val<doc['avgRide']:
        max_val=doc['avgRide']

    print(doc)

a = np.arange(5)

plt.subplot(1,2,1)
plt.bar(a, avg_ride_y)
plt.title('역이름별 지하철 승차 평균인원')
plt.ylabel('지하철 인원 (단위: 1e6명)', fontsize=14)
plt.xticks(a, avg_ride_x, fontsize=12)
plt.yticks(fontsize=12)

#subway 역이름 하차 평균인원 시각화
avg_alight_pipelines=[{ "$project": {"sub_sta_nm":1,  "four_alight_num":1, "five_alight_num":1, "six_alight_num":1, "seven_alight_num":1,
                                     "eight_alight_num":1,"nine_alight_num":1, "ten_alight_num":1, "eleven_alight_num":1, "twelve_alight_num":1,
                                     "thirteen_alight_num":1, "fourteen_alight_num":1,"fifteen_alight_num":1, "sixteen_alight_num":1,
                                     "seventeen_alight_num":1, "eighteen_alight_num":1, "nineteen_alight_num":1,"twenty_alight_num":1,
                                     "twenty_one_alight_num":1, "twenty_two_alight_num":1, "twenty_three_alight_num":1, "midnight_alight_num":1,
                                     "one_alight_num":1, "two_alight_num":1, "three_alight_num":1} },
                      { "$addFields": { "totalAlight": { "$sum": [ "$four_alight_num", "$five_alight_num", "$six_alight_num", "$seven_alight_num",
                                                                   "$eight_alight_num","$nine_alight_num", "$ten_alight_num", "$eleven_alight_num",
                                                                   "$twelve_alight_num", "$thirteen_alight_num","$fourteen_alight_num", "$fifteen_alight_num",
                                                                   "$sixteen_alight_num", "$seventeen_alight_num","$eighteen_alight_num", "$nineteen_alight_num",
                                                                   "$twenty_alight_num", "$twenty_one_alight_num","$twenty_two_alight_num",
                                                                   "$twenty_three_alight_num", "$midnight_alight_num", "$one_alight_num","$two_alight_num",
                                                                   "$three_alight_num" ] } } },
                      { "$group": { "_id": "$sub_sta_nm", "avgAlight": { "$avg": "$totalAlight" } } },
                      { "$sort": { "avgAlight":-1} },{ "$limit":5 },
                      { "$project": { "_id":1, "avgAlight":1} }]


avg_alight_results=subwayCol.aggregate(avg_alight_pipelines)

avg_alight_x=list()
avg_alight_y=list()

print("subway 역이름 하차 평균인원 시각화")

for doc in avg_alight_results:
    avg_alight_x.append(doc['_id'])
    avg_alight_y.append(doc['avgAlight'])

    if max_val<doc['avgAlight']:
        max_val=doc['avgAlight']+50000

    print(doc)

plt.subplot(1,2,2)
plt.bar(a, avg_alight_y)
plt.title('역이름별 지하철 하차 평균인원')
plt.xticks(a, avg_alight_x, fontsize=12)
plt.yticks([])
plt.ylim(0, max_val)
plt.show()


#subway 호선별 승차 평균인원 시각화
line_avg_ride_pipelines=[{ "$project": {"line_num":1,  "four_ride_num":1, "five_ride_num":1, "six_ride_num":1, "seven_ride_num":1, "eight_ride_num":1,
                                   "nine_ride_num":1, "ten_ride_num":1, "eleven_ride_num":1, "twelve_ride_num":1, "thirteen_ride_num":1, "fourteen_ride_num":1,
                                   "fifteen_ride_num":1, "sixteen_ride_num":1, "seventeen_ride_num":1, "eighteen_ride_num":1, "nineteen_ride_num":1,
                                   "twenty_ride_num":1, "twenty_one_ride_num":1, "twenty_two_ride_num":1, "twenty_three_ride_num":1, "midnight_ride_num":1,
                                   "one_ride_num":1, "two_ride_num":1, "three_ride_num":1} },
                    { "$addFields": { "totalRide": { "$sum": [ "$four_ride_num", "$five_ride_num", "$six_ride_num", "$seven_ride_num", "$eight_ride_num",
                                                               "$nine_ride_num", "$ten_ride_num", "$eleven_ride_num", "$twelve_ride_num", "$thirteen_ride_num",
                                                               "$fourteen_ride_num", "$fifteen_ride_num", "$sixteen_ride_num", "$seventeen_ride_num",
                                                               "$eighteen_ride_num", "$nineteen_ride_num", "$twenty_ride_num", "$twenty_one_ride_num",
                                                               "$twenty_two_ride_num", "$twenty_three_ride_num", "$midnight_ride_num", "$one_ride_num",
                                                               "$two_ride_num", "$three_ride_num" ] } } },
                    { "$group": { "_id": "$line_num", "avgRide": { "$avg": "$totalRide" } } },
                    { "$sort": { "avgRide":-1} },{ "$limit":5 },{ "$project": { "_id":1, "avgRide":1} }]

line_avg_ride_results=subwayCol.aggregate(line_avg_ride_pipelines)

line_avg_ride_x=list()
line_avg_ride_y=list()
max_val=0

for doc in line_avg_ride_results:
    line_avg_ride_x.append(doc['_id'])
    line_avg_ride_y.append(round(doc['avgRide'], 2))

    if max_val<doc['avgRide']:
        max_val=doc['avgRide']

    print(doc)

a = np.arange(5)

plt.subplot(1,2,1)
plt.bar(a, line_avg_ride_y)
plt.title('호선별 지하철 승차 평균인원')
plt.ylabel('지하철 인원 (단위: 명)', fontsize=14)
plt.xticks(a, line_avg_ride_x, fontsize=12)
plt.yticks(fontsize=12)

#subway 호선별 하차 평균인원 시각화
line_avg_alight_pipelines=[{ "$project": {"line_num":1,  "four_alight_num":1, "five_alight_num":1, "six_alight_num":1, "seven_alight_num":1,
                                     "eight_alight_num":1,"nine_alight_num":1, "ten_alight_num":1, "eleven_alight_num":1, "twelve_alight_num":1,
                                     "thirteen_alight_num":1, "fourteen_alight_num":1,"fifteen_alight_num":1, "sixteen_alight_num":1,
                                     "seventeen_alight_num":1, "eighteen_alight_num":1, "nineteen_alight_num":1,"twenty_alight_num":1,
                                     "twenty_one_alight_num":1, "twenty_two_alight_num":1, "twenty_three_alight_num":1, "midnight_alight_num":1,
                                     "one_alight_num":1, "two_alight_num":1, "three_alight_num":1} },
                      { "$addFields": { "totalAlight": { "$sum": [ "$four_alight_num", "$five_alight_num", "$six_alight_num", "$seven_alight_num",
                                                                   "$eight_alight_num","$nine_alight_num", "$ten_alight_num", "$eleven_alight_num",
                                                                   "$twelve_alight_num", "$thirteen_alight_num","$fourteen_alight_num", "$fifteen_alight_num",
                                                                   "$sixteen_alight_num", "$seventeen_alight_num","$eighteen_alight_num", "$nineteen_alight_num",
                                                                   "$twenty_alight_num", "$twenty_one_alight_num","$twenty_two_alight_num",
                                                                   "$twenty_three_alight_num", "$midnight_alight_num", "$one_alight_num","$two_alight_num",
                                                                   "$three_alight_num" ] } } },
                      { "$group": { "_id": "$line_num", "avgAlight": { "$avg": "$totalAlight" } } },
                      { "$sort": { "avgAlight":-1} },{ "$limit":5 },
                      { "$project": { "_id":1, "avgAlight":1} }]


line_avg_alight_results=subwayCol.aggregate(line_avg_alight_pipelines)

line_avg_alight_x=list()
line_avg_alight_y=list()

print("subway 호선별 하차 평균인원 시각화")

for doc in line_avg_alight_results:
    line_avg_alight_x.append(doc['_id'])
    line_avg_alight_y.append(doc['avgAlight'])

    if max_val<doc['avgAlight']:
        max_val=doc['avgAlight']+50000

    print(doc)

plt.subplot(1,2,2)
plt.bar(a, line_avg_alight_y)
plt.title('호선별 지하철 하차 평균인원')
plt.xticks(a, line_avg_alight_x, fontsize=12)
plt.yticks([])
plt.ylim(0, max_val)
plt.show()


myclient.close()