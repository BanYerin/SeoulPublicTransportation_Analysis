"""

<작성자 및 담당 부분>
*2017038023 반예린
-시간대별 버스 승차 쿼리 및 시각화
-시간대별 버스 하차 쿼리 및 시각화
-시간대별 지하철 승차 쿼리 및 시각화
-시간대별 지하철 하차 쿼리 및 시각화
-정류장별 버스 승차 쿼리 및 시각화
-정류장별 버스 하차 쿼리 및 시각화
-노선 번호별 버스 승차 쿼리 및 시각화
-노선 번호별 버스 하차 쿼리 및 시각화

*2015023025 배나영
-역별 지하철 승차 쿼리 및 시각화
-역별 지하철 하차 쿼리 및 시각화
-호선별 지하철 승차 쿼리 및 시각화
-호선별 지하철 하차 쿼리 및 시각화

"""


import pymongo
import matplotlib.pyplot as plt
import numpy as np

#한글 폰트 사용을 위한 설정
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)



myclient = pymongo.MongoClient("mongodb://localhost:27017/") #MongoDB 연결

projectDb = myclient["project"] #db
subwayCol = projectDb["subway"] #서울 지하철 컬렉션
busCol = projectDb["bus"] #서울 버스 컬렉션


#시간대별 승차 인원 구하는 쿼리
timeRide_query = [
    {"$project": {"_id": 0, "midnight_ride_num": 1, "one_ride_num": 1, "two_ride_num": 1, "three_ride_num": 1,
                  "four_ride_num": 1, "five_ride_num": 1, "six_ride_num": 1, "seven_ride_num": 1,
                  "eight_ride_num": 1, "nine_ride_num": 1, "ten_ride_num": 1, "eleven_ride_num": 1,
                  "twelve_ride_num": 1, "thirteen_ride_num": 1, "fourteen_ride_num": 1, "fifteen_ride_num": 1,
                  "sixteen_ride_num": 1, "seventeen_ride_num": 1, "eighteen_ride_num": 1, "nineteen_ride_num": 1,
                  "twenty_ride_num": 1, "twenty_one_ride_num": 1, "twenty_two_ride_num": 1, "twenty_three_ride_num": 1}},
    {"$group":
             {
                 "_id": "null",
                 "midnight_ride_num": {"$avg": "$midnight_ride_num"},
                 "one_ride_num": {"$avg": "$one_ride_num"},
                 "two_ride_num": {"$avg": "$two_ride_num"},
                 "three_ride_num": {"$avg": "$three_ride_num"},
                 "four_ride_num": {"$avg": "$four_ride_num"},
                 "five_ride_num": {"$avg": "$five_ride_num"},
                 "six_ride_num": {"$avg": "$six_ride_num"},
                 "seven_ride_num": {"$avg": "$seven_ride_num"},
                 "eight_ride_num": {"$avg": "$eight_ride_num"},
                 "nine_ride_num": {"$avg": "$nine_ride_num"},
                 "ten_ride_num": {"$avg": "$ten_ride_num"},
                 "eleven_ride_num": {"$avg": "$eleven_ride_num"},
                 "twelve_ride_num": {"$avg": "$twelve_ride_num"},
                 "thirteen_ride_num": {"$avg": "$thirteen_ride_num"},
                 "fourteen_ride_num": {"$avg": "$fourteen_ride_num"},
                 "fifteen_ride_num": {"$avg": "$fifteen_ride_num"},
                 "sixteen_ride_num": {"$avg": "$sixteen_ride_num"},
                 "seventeen_ride_num": {"$avg": "$seventeen_ride_num"},
                 "eighteen_ride_num": {"$avg": "$eighteen_ride_num"},
                 "nineteen_ride_num": {"$avg": "$nineteen_ride_num"},
                 "twenty_ride_num": {"$avg": "$twenty_ride_num"},
                 "twenty_one_ride_num": {"$avg": "$twenty_one_ride_num"},
                 "twenty_two_ride_num": {"$avg": "$twenty_two_ride_num"},
                 "twenty_three_ride_num": {"$avg": "$twenty_three_ridet_num"}
             }
    }
]

#시간대별 하차 인원 구하는 쿼리
timeAlight_query = [
    {"$project": {"_id": 0, "midnight_alight_num": 1, "one_alight_num": 1, "two_alight_num": 1, "three_alight_num": 1,
                  "four_alight_num": 1, "five_alight_num": 1, "six_alight_num": 1, "seven_alight_num": 1,
                  "eight_alight_num": 1, "nine_alight_num": 1, "ten_alight_num": 1, "eleven_alight_num": 1,
                  "twelve_alight_num": 1, "thirteen_alight_num": 1, "fourteen_alight_num": 1, "fifteen_alight_num": 1,
                  "sixteen_alight_num": 1, "seventeen_alight_num": 1, "eighteen_alight_num": 1, "nineteen_alight_num": 1,
                  "twenty_alight_num": 1, "twenty_one_alight_num": 1, "twenty_two_alight_num": 1, "twenty_three_alight_num": 1}},
    {"$group":
             {
                 "_id": "null",
                 "midnight_alight_num": {"$avg": "$midnight_alight_num"},
                 "one_alight_num": {"$avg": "$one_alight_num"},
                 "two_alight_num": {"$avg": "$two_alight_num"},
                 "three_alight_num": {"$avg": "$three_alight_num"},
                 "four_alight_num": {"$avg": "$four_alight_num"},
                 "five_alight_num": {"$avg": "$five_alight_num"},
                 "six_alight_num": {"$avg": "$six_alight_num"},
                 "seven_alight_num": {"$avg": "$seven_alight_num"},
                 "eight_alight_num": {"$avg": "$eight_alight_num"},
                 "nine_alight_num": {"$avg": "$nine_alight_num"},
                 "ten_alight_num": {"$avg": "$ten_alight_num"},
                 "eleven_alight_num": {"$avg": "$eleven_alight_num"},
                 "twelve_alight_num": {"$avg": "$twelve_alight_num"},
                 "thirteen_alight_num": {"$avg": "$thirteen_alight_num"},
                 "fourteen_alight_num": {"$avg": "$fourteen_alight_num"},
                 "fifteen_alight_num": {"$avg": "$fifteen_alight_num"},
                 "sixteen_alight_num": {"$avg": "$sixteen_alight_num"},
                 "seventeen_alight_num": {"$avg": "$seventeen_alight_num"},
                 "eighteen_alight_num": {"$avg": "$eighteen_alight_num"},
                 "nineteen_alight_num": {"$avg": "$nineteen_alight_num"},
                 "twenty_alight_num": {"$avg": "$twenty_alight_num"},
                 "twenty_one_alight_num": {"$avg": "$twenty_one_alight_num"},
                 "twenty_two_alight_num": {"$avg": "$twenty_two_alight_num"},
                 "twenty_three_alight_num": {"$avg": "$twenty_three_alight_num"}
             }
    }
]

#버스 정류장별 승차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리
busStaRide_query = [
    {"$group":
             {
                 "_id": "$bus_sta_nm",
                 "midnight_ride_num": {"$avg": "$midnight_ride_num"},
                 "one_ride_num": {"$avg": "$one_ride_num"},
                 "two_ride_num": {"$avg": "$two_ride_num"},
                 "three_ride_num": {"$avg": "$three_ride_num"},
                 "four_ride_num": {"$avg": "$four_ride_num"},
                 "five_ride_num": {"$avg": "$five_ride_num"},
                 "six_ride_num": {"$avg": "$six_ride_num"},
                 "seven_ride_num": {"$avg": "$seven_ride_num"},
                 "eight_ride_num": {"$avg": "$eight_ride_num"},
                 "nine_ride_num": {"$avg": "$nine_ride_num"},
                 "ten_ride_num": {"$avg": "$ten_ride_num"},
                 "eleven_ride_num": {"$avg": "$eleven_ride_num"},
                 "twelve_ride_num": {"$avg": "$twelve_ride_num"},
                 "thirteen_ride_num": {"$avg": "$thirteen_ride_num"},
                 "fourteen_ride_num": {"$avg": "$fourteen_ride_num"},
                 "fifteen_ride_num": {"$avg": "$fifteen_ride_num"},
                 "sixteen_ride_num": {"$avg": "$sixteen_ride_num"},
                 "seventeen_ride_num": {"$avg": "$seventeen_ride_num"},
                 "eighteen_ride_num": {"$avg": "$eighteen_ride_num"},
                 "nineteen_ride_num": {"$avg": "$nineteen_ride_num"},
                 "twenty_ride_num": {"$avg": "$twenty_ride_num"},
                 "twenty_one_ride_num": {"$avg": "$twenty_one_ride_num"},
                 "twenty_two_ride_num": {"$avg": "$twenty_two_ride_num"},
                 "twenty_three_ride_num": {"$avg": "$twenty_three_ride_num"}
             }
    },
    {"$project": {"_id": 1,
                  "rideNum": {"$add": ["$midnight_ride_num", "$one_ride_num", "$two_ride_num", "$three_ride_num",
                                      "$four_ride_num", "$five_ride_num", "$six_ride_num", "$seven_ride_num",
                                      "$eight_ride_num", "$nine_ride_num", "$ten_ride_num", "$eleven_ride_num",
                                      "$twelve_ride_num", "$thirteen_ride_num", "$fourteen_ride_num",
                                      "$fifteen_ride_num", "$sixteen_ride_num", "$seventeen_ride_num",
                                      "$eighteen_ride_num", "$nineteen_ride_num", "$twenty_ride_num",
                                      "$twenty_one_ride_num", "$twenty_two_ride_num", "$twenty_three_ride_num"]}}},
    {"$sort": {"rideNum": -1}},
    {"$limit": 5}

]

#버스 정류장별 하차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리
busStaAlight_query = [
    {"$group":
             {
                 "_id": "$bus_sta_nm",
                 "midnight_alight_num": {"$avg": "$midnight_alight_num"},
                 "one_alight_num": {"$avg": "$one_alight_num"},
                 "two_alight_num": {"$avg": "$two_alight_num"},
                 "three_alight_num": {"$avg": "$three_alight_num"},
                 "four_alight_num": {"$avg": "$four_alight_num"},
                 "five_alight_num": {"$avg": "$five_alight_num"},
                 "six_alight_num": {"$avg": "$six_alight_num"},
                 "seven_alight_num": {"$avg": "$seven_alight_num"},
                 "eight_alight_num": {"$avg": "$eight_alight_num"},
                 "nine_alight_num": {"$avg": "$nine_alight_num"},
                 "ten_alight_num": {"$avg": "$ten_alight_num"},
                 "eleven_alight_num": {"$avg": "$eleven_alight_num"},
                 "twelve_alight_num": {"$avg": "$twelve_alight_num"},
                 "thirteen_alight_num": {"$avg": "$thirteen_alight_num"},
                 "fourteen_alight_num": {"$avg": "$fourteen_alight_num"},
                 "fifteen_alight_num": {"$avg": "$fifteen_alight_num"},
                 "sixteen_alight_num": {"$avg": "$sixteen_alight_num"},
                 "seventeen_alight_num": {"$avg": "$seventeen_alight_num"},
                 "eighteen_alight_num": {"$avg": "$eighteen_alight_num"},
                 "nineteen_alight_num": {"$avg": "$nineteen_alight_num"},
                 "twenty_alight_num": {"$avg": "$twenty_alight_num"},
                 "twenty_one_alight_num": {"$avg": "$twenty_one_alight_num"},
                 "twenty_two_alight_num": {"$avg": "$twenty_two_alight_num"},
                 "twenty_three_alight_num": {"$avg": "$twenty_three_alight_num"}
             }
    },
    {"$project": {"_id": 1,
                  "alightNum": {"$add": ["$midnight_alight_num", "$one_alight_num", "$two_alight_num", "$three_alight_num",
                                      "$four_alight_num", "$five_alight_num", "$six_alight_num", "$seven_alight_num",
                                      "$eight_alight_num", "$nine_alight_num", "$ten_alight_num", "$eleven_alight_num",
                                      "$twelve_alight_num", "$thirteen_alight_num", "$fourteen_alight_num",
                                      "$fifteen_alight_num", "$sixteen_alight_num", "$seventeen_alight_num",
                                      "$eighteen_alight_num", "$nineteen_alight_num", "$twenty_alight_num",
                                      "$twenty_one_alight_num", "$twenty_two_alight_num", "$twenty_three_alight_num"]}}},
    {"$sort": {"alightNum": -1}},
    {"$limit": 5}

]

#버스 노선 번호별 승차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리
busRouteRide_query = [
    {"$group":
             {
                 "_id": "$bus_route_no",
                 "midnight_ride_num": {"$avg": "$midnight_ride_num"},
                 "one_ride_num": {"$avg": "$one_ride_num"},
                 "two_ride_num": {"$avg": "$two_ride_num"},
                 "three_ride_num": {"$avg": "$three_ride_num"},
                 "four_ride_num": {"$avg": "$four_ride_num"},
                 "five_ride_num": {"$avg": "$five_ride_num"},
                 "six_ride_num": {"$avg": "$six_ride_num"},
                 "seven_ride_num": {"$avg": "$seven_ride_num"},
                 "eight_ride_num": {"$avg": "$eight_ride_num"},
                 "nine_ride_num": {"$avg": "$nine_ride_num"},
                 "ten_ride_num": {"$avg": "$ten_ride_num"},
                 "eleven_ride_num": {"$avg": "$eleven_ride_num"},
                 "twelve_ride_num": {"$avg": "$twelve_ride_num"},
                 "thirteen_ride_num": {"$avg": "$thirteen_ride_num"},
                 "fourteen_ride_num": {"$avg": "$fourteen_ride_num"},
                 "fifteen_ride_num": {"$avg": "$fifteen_ride_num"},
                 "sixteen_ride_num": {"$avg": "$sixteen_ride_num"},
                 "seventeen_ride_num": {"$avg": "$seventeen_ride_num"},
                 "eighteen_ride_num": {"$avg": "$eighteen_ride_num"},
                 "nineteen_ride_num": {"$avg": "$nineteen_ride_num"},
                 "twenty_ride_num": {"$avg": "$twenty_ride_num"},
                 "twenty_one_ride_num": {"$avg": "$twenty_one_ride_num"},
                 "twenty_two_ride_num": {"$avg": "$twenty_two_ride_num"},
                 "twenty_three_ride_num": {"$avg": "$twenty_three_ride_num"}
             }
    },
    {"$project": {"_id": 1,
                  "rideNum": {"$add": ["$midnight_ride_num", "$one_ride_num", "$two_ride_num", "$three_ride_num",
                                      "$four_ride_num", "$five_ride_num", "$six_ride_num", "$seven_ride_num",
                                      "$eight_ride_num", "$nine_ride_num", "$ten_ride_num", "$eleven_ride_num",
                                      "$twelve_ride_num", "$thirteen_ride_num", "$fourteen_ride_num",
                                      "$fifteen_ride_num", "$sixteen_ride_num", "$seventeen_ride_num",
                                      "$eighteen_ride_num", "$nineteen_ride_num", "$twenty_ride_num",
                                      "$twenty_one_ride_num", "$twenty_two_ride_num", "$twenty_three_ride_num"]}}},
    {"$sort": {"rideNum": -1}},
    {"$limit": 5}

]

#버스 노선 번호별 하차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리
busRouteAlight_query = [
    {"$group":
             {
                 "_id": "$bus_route_no",
                 "midnight_alight_num": {"$avg": "$midnight_alight_num"},
                 "one_alight_num": {"$avg": "$one_alight_num"},
                 "two_alight_num": {"$avg": "$two_alight_num"},
                 "three_alight_num": {"$avg": "$three_alight_num"},
                 "four_alight_num": {"$avg": "$four_alight_num"},
                 "five_alight_num": {"$avg": "$five_alight_num"},
                 "six_alight_num": {"$avg": "$six_alight_num"},
                 "seven_alight_num": {"$avg": "$seven_alight_num"},
                 "eight_alight_num": {"$avg": "$eight_alight_num"},
                 "nine_alight_num": {"$avg": "$nine_alight_num"},
                 "ten_alight_num": {"$avg": "$ten_alight_num"},
                 "eleven_alight_num": {"$avg": "$eleven_alight_num"},
                 "twelve_alight_num": {"$avg": "$twelve_alight_num"},
                 "thirteen_alight_num": {"$avg": "$thirteen_alight_num"},
                 "fourteen_alight_num": {"$avg": "$fourteen_alight_num"},
                 "fifteen_alight_num": {"$avg": "$fifteen_alight_num"},
                 "sixteen_alight_num": {"$avg": "$sixteen_alight_num"},
                 "seventeen_alight_num": {"$avg": "$seventeen_alight_num"},
                 "eighteen_alight_num": {"$avg": "$eighteen_alight_num"},
                 "nineteen_alight_num": {"$avg": "$nineteen_alight_num"},
                 "twenty_alight_num": {"$avg": "$twenty_alight_num"},
                 "twenty_one_alight_num": {"$avg": "$twenty_one_alight_num"},
                 "twenty_two_alight_num": {"$avg": "$twenty_two_alight_num"},
                 "twenty_three_alight_num": {"$avg": "$twenty_three_alight_num"}
             }
    },
    {"$project": {"_id": 1,
                  "alightNum": {"$add": ["$midnight_alight_num", "$one_alight_num", "$two_alight_num", "$three_alight_num",
                                      "$four_alight_num", "$five_alight_num", "$six_alight_num", "$seven_alight_num",
                                      "$eight_alight_num", "$nine_alight_num", "$ten_alight_num", "$eleven_alight_num",
                                      "$twelve_alight_num", "$thirteen_alight_num", "$fourteen_alight_num",
                                      "$fifteen_alight_num", "$sixteen_alight_num", "$seventeen_alight_num",
                                      "$eighteen_alight_num", "$nineteen_alight_num", "$twenty_alight_num",
                                      "$twenty_one_alight_num", "$twenty_two_alight_num", "$twenty_three_alight_num"]}}},
    {"$sort": {"alightNum": -1}},
    {"$limit": 5}

]



####################### 시간대별 버스 승차 인원
busTimeRideList = [] #시간대별 버스 승차 인원수 결과 배열
busTimeRideDoc = busCol.aggregate(timeRide_query) #시간대별 버스 승차 인원 구하는 쿼리 수행

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in busTimeRideDoc:
    busTimeRideList.append(item['midnight_ride_num'])
    busTimeRideList.append(item['one_ride_num'])
    busTimeRideList.append(item['two_ride_num'])
    busTimeRideList.append(item['three_ride_num'])
    busTimeRideList.append(item['four_ride_num'])
    busTimeRideList.append(item['five_ride_num'])
    busTimeRideList.append(item['six_ride_num'])
    busTimeRideList.append(item['seven_ride_num'])
    busTimeRideList.append(item['eight_ride_num'])
    busTimeRideList.append(item['nine_ride_num'])
    busTimeRideList.append(item['ten_ride_num'])
    busTimeRideList.append(item['eleven_ride_num'])
    busTimeRideList.append(item['twelve_ride_num'])
    busTimeRideList.append(item['thirteen_ride_num'])
    busTimeRideList.append(item['fourteen_ride_num'])
    busTimeRideList.append(item['fifteen_ride_num'])
    busTimeRideList.append(item['sixteen_ride_num'])
    busTimeRideList.append(item['seventeen_ride_num'])
    busTimeRideList.append(item['eighteen_ride_num'])
    busTimeRideList.append(item['nineteen_ride_num'])
    busTimeRideList.append(item['twenty_ride_num'])
    busTimeRideList.append(item['twenty_one_ride_num'])
    busTimeRideList.append(item['twenty_two_ride_num'])
    busTimeRideList.append(item['twenty_three_ride_num'])


print('시간대별 버스 승차 인원: ', busTimeRideList) #배열 내용 확인

plt.plot(busTimeRideList, color='green', marker='o')
plt.xticks(np.arange(0, 24)) #x축: 시각(0시~23시)
plt.xlabel('시각')
plt.ylabel('버스 승차 인원 (단위: 명)')
plt.title('시간대별 버스 승차 인원')
plt.show() #결과 그래프 출력



####################### 시간대별 버스 하차 인원
busTimeAlightList = [] #시간대별 버스 하차 인원수 결과 배열
busTimeAlightDoc = busCol.aggregate(timeAlight_query) #시간대별 버스 하차 인원 구하는 쿼리 수행

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in busTimeAlightDoc:
    busTimeAlightList.append(item['midnight_alight_num'])
    busTimeAlightList.append(item['one_alight_num'])
    busTimeAlightList.append(item['two_alight_num'])
    busTimeAlightList.append(item['three_alight_num'])
    busTimeAlightList.append(item['four_alight_num'])
    busTimeAlightList.append(item['five_alight_num'])
    busTimeAlightList.append(item['six_alight_num'])
    busTimeAlightList.append(item['seven_alight_num'])
    busTimeAlightList.append(item['eight_alight_num'])
    busTimeAlightList.append(item['nine_alight_num'])
    busTimeAlightList.append(item['ten_alight_num'])
    busTimeAlightList.append(item['eleven_alight_num'])
    busTimeAlightList.append(item['twelve_alight_num'])
    busTimeAlightList.append(item['thirteen_alight_num'])
    busTimeAlightList.append(item['fourteen_alight_num'])
    busTimeAlightList.append(item['fifteen_alight_num'])
    busTimeAlightList.append(item['sixteen_alight_num'])
    busTimeAlightList.append(item['seventeen_alight_num'])
    busTimeAlightList.append(item['eighteen_alight_num'])
    busTimeAlightList.append(item['nineteen_alight_num'])
    busTimeAlightList.append(item['twenty_alight_num'])
    busTimeAlightList.append(item['twenty_one_alight_num'])
    busTimeAlightList.append(item['twenty_two_alight_num'])
    busTimeAlightList.append(item['twenty_three_alight_num'])


print('시간대별 버스 하차 인원: ', busTimeAlightList) #배열 내용 확인

plt.plot(busTimeAlightList, color='green', marker='o')
plt.xticks(np.arange(0, 24)) #x축: 시각(0시~23시)
plt.xlabel('시각')
plt.ylabel('버스 하차 인원 (단위: 명)')
plt.title('시간대별 버스 하차 인원')
plt.show() #결과 그래프 출력



####################### 시간대별 지하철 승차 인원
subwayTimeRideList = [] #시간대별 지하철 승차 인원수 결과 배열
subwayTimeRideDoc = subwayCol.aggregate(timeRide_query) #시간대별 지하철 승차 인원 구하는 쿼리 수행

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in subwayTimeRideDoc:
    subwayTimeRideList.append(item['midnight_ride_num'])
    subwayTimeRideList.append(item['one_ride_num'])
    subwayTimeRideList.append(item['two_ride_num'])
    subwayTimeRideList.append(item['three_ride_num'])
    subwayTimeRideList.append(item['four_ride_num'])
    subwayTimeRideList.append(item['five_ride_num'])
    subwayTimeRideList.append(item['six_ride_num'])
    subwayTimeRideList.append(item['seven_ride_num'])
    subwayTimeRideList.append(item['eight_ride_num'])
    subwayTimeRideList.append(item['nine_ride_num'])
    subwayTimeRideList.append(item['ten_ride_num'])
    subwayTimeRideList.append(item['eleven_ride_num'])
    subwayTimeRideList.append(item['twelve_ride_num'])
    subwayTimeRideList.append(item['thirteen_ride_num'])
    subwayTimeRideList.append(item['fourteen_ride_num'])
    subwayTimeRideList.append(item['fifteen_ride_num'])
    subwayTimeRideList.append(item['sixteen_ride_num'])
    subwayTimeRideList.append(item['seventeen_ride_num'])
    subwayTimeRideList.append(item['eighteen_ride_num'])
    subwayTimeRideList.append(item['nineteen_ride_num'])
    subwayTimeRideList.append(item['twenty_ride_num'])
    subwayTimeRideList.append(item['twenty_one_ride_num'])
    subwayTimeRideList.append(item['twenty_two_ride_num'])
    subwayTimeRideList.append(item['twenty_three_ride_num'])


print('시간대별 지하철 승차 인원: ', subwayTimeRideList) #배열 내용 확인


plt.plot(subwayTimeRideList, color='green', marker='o')
plt.xticks(np.arange(0, 24)) #x축: 시각(0시~23시)
plt.xlabel('시각')
plt.ylabel('지하철 승차 인원 (단위: 명)')
plt.title('시간대별 지하철 승차 인원')
plt.show() #결과 그래프 출력



####################### 시간대별 지하철 하차 인원
subwayTimeAlightList = [] #시간대별 지하철 하차 인원수 결과 배열
subwayTimeAlightDoc = subwayCol.aggregate(timeAlight_query) #시간대별 지하철 하차 인원 구하는 쿼리 수행

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in subwayTimeAlightDoc:
    subwayTimeAlightList.append(item['midnight_alight_num'])
    subwayTimeAlightList.append(item['one_alight_num'])
    subwayTimeAlightList.append(item['two_alight_num'])
    subwayTimeAlightList.append(item['three_alight_num'])
    subwayTimeAlightList.append(item['four_alight_num'])
    subwayTimeAlightList.append(item['five_alight_num'])
    subwayTimeAlightList.append(item['six_alight_num'])
    subwayTimeAlightList.append(item['seven_alight_num'])
    subwayTimeAlightList.append(item['eight_alight_num'])
    subwayTimeAlightList.append(item['nine_alight_num'])
    subwayTimeAlightList.append(item['ten_alight_num'])
    subwayTimeAlightList.append(item['eleven_alight_num'])
    subwayTimeAlightList.append(item['twelve_alight_num'])
    subwayTimeAlightList.append(item['thirteen_alight_num'])
    subwayTimeAlightList.append(item['fourteen_alight_num'])
    subwayTimeAlightList.append(item['fifteen_alight_num'])
    subwayTimeAlightList.append(item['sixteen_alight_num'])
    subwayTimeAlightList.append(item['seventeen_alight_num'])
    subwayTimeAlightList.append(item['eighteen_alight_num'])
    subwayTimeAlightList.append(item['nineteen_alight_num'])
    subwayTimeAlightList.append(item['twenty_alight_num'])
    subwayTimeAlightList.append(item['twenty_one_alight_num'])
    subwayTimeAlightList.append(item['twenty_two_alight_num'])
    subwayTimeAlightList.append(item['twenty_three_alight_num'])


print('시간대별 지하철 하차 인원: ', subwayTimeAlightList) #배열 내용 확인

plt.plot(subwayTimeAlightList, color='green', marker='o')
plt.xticks(np.arange(0, 24)) #x축: 시각(0시~23시)
plt.xlabel('시각')
plt.ylabel('지하철 하차 인원 (단위: 명)')
plt.title('시간대별 지하철 하차 인원')
plt.show() #결과 그래프 출력



####################### 정류장별 버스 승차 인원
busStaList = [] #버스 정류장 이름 배열
busStaRideList = [] #정류장별 버스 승차 인원수 결과 배열
busStaRideDoc = busCol.aggregate(busStaRide_query) #버스 정류장별 승차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in busStaRideDoc:
    busStaList.append(item['_id'])
    busStaRideList.append(item['rideNum'])


#배열 내용 확인
print('top5 버스 정류장 리스트: ', busStaList)
print('top5 정류장별 버스 승차 인원: ', busStaRideList)

plt.hist(busStaList, bins=None, density=None, weights=busStaRideList, cumulative=False) #x축: 버스 정류장 이름, y축: 버스 승차 인원
plt.xlabel('버스 정류장 이름')
plt.ylabel('버스 승차 인원 (단위: 명)')
plt.title('정류장별 버스 승차 인원(인원 많은 상위 5개)')
plt.show() #결과 그래프 출력



####################### 정류장별 버스 하차 인원
busStaList = [] #버스 정류장 이름 배열
busStaAlightList = [] #정류장별 버스 하차 인원수 결과 배열
busStaAlightDoc = busCol.aggregate(busStaAlight_query) #버스 정류장별 하차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in busStaAlightDoc:
    busStaList.append(item['_id'])
    busStaAlightList.append(item['alightNum'])


#배열 내용 확인
print('top5 버스 정류장 리스트: ', busStaList)
print('top5 정류장별 버스 하차 인원: ', busStaAlightList)

plt.hist(busStaList, bins=None, density=None, weights=busStaAlightList, cumulative=False) #x축: 버스 정류장 이름, y축: 버스 하차 인원
plt.xlabel('버스 정류장 이름')
plt.ylabel('버스 하차 인원 (단위: 명)')
plt.title('정류장별 버스 하차 인원(인원 많은 상위 5개)')
plt.show() #결과 그래프 출력



####################### 노선 번호별 버스 승차 인원
busRouteList = [] #버스 노선 번호 배열
busRouteRideList = [] #노선 번호별 버스 승차 인원수 결과 배열
busRouteRideDoc = busCol.aggregate(busRouteRide_query) #버스 노선 번호별 승차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리 수행

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in busRouteRideDoc:
    busRouteList.append(item['_id'])
    busRouteRideList.append(item['rideNum'])


#배열 내용 확인
print('top5 버스 노선번호 리스트: ', busRouteList)
print('top5 노선 번호별 버스 승차 인원: ', busRouteRideList)

plt.hist(busRouteList, bins=None, density=None, weights=busRouteRideList, cumulative=False) #x축: 버스 노선 번호, y축: 버스 승차 인원
plt.xlabel('버스 노선 번호')
plt.ylabel('버스 승차 인원 (단위: 명)')
plt.title('노선 번호별 버스 승차 인원(인원 많은 상위 5개)')
plt.show() #결과 그래프 출력



####################### 노선 번호별 버스 하차 인원
busRouteList = [] #버스 노선 번호 배열
busRouteAlightList = [] #노선 번호별 버스 하차 인원수 결과 배열
busRouteAlightDoc = busCol.aggregate(busRouteAlight_query) #버스 노선 번호별 하차 인원이 많은 상위 5개의 도큐먼트를 구하는 쿼리 수행

#어그리게이션 결과로 나온 도큐먼트의 각 필드 값을 배열에 넣음
for item in busRouteAlightDoc:
    busRouteList.append(item['_id'])
    busRouteAlightList.append(item['alightNum'])


#배열 내용 확인
print('top5 버스 노선번호 리스트: ', busRouteList)
print('top5 노선 번호별 버스 하차 인원: ', busRouteAlightList)

plt.hist(busRouteList, bins=None, density=None, weights=busRouteAlightList, cumulative=False) #x축: 버스 노선 번호, y축: 버스 하차 인원
plt.xlabel('버스 노선 번호')
plt.ylabel('버스 하차 인원 (단위: 명)')
plt.title('노선 번호별 버스 하차 인원(인원 많은 상위 5개)')
plt.show() #결과 그래프 출력




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#역이름별 지하철 승차 평균인원 시각화
sta_avg_ride_pipelines=[{ "$project": {"sub_sta_nm":1,  "four_ride_num":1, "five_ride_num":1, "six_ride_num":1, "seven_ride_num":1, "eight_ride_num":1,
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

avg_ride_results=subwayCol.aggregate(sta_avg_ride_pipelines)

avg_ride_x=list()
avg_ride_y=list()
max_val=0

print("역이름별 지하철 승차 평균인원")
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

#역이름별 지하철 하차 평균인원 시각화
sta_avg_alight_pipelines=[{ "$project": {"sub_sta_nm":1,  "four_alight_num":1, "five_alight_num":1, "six_alight_num":1, "seven_alight_num":1,
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


avg_alight_results=subwayCol.aggregate(sta_avg_alight_pipelines)

avg_alight_x=list()
avg_alight_y=list()

print("역이름별 지하철 하차 평균인원")
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


#호선별 지하철 승차 평균인원 시각화
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

print("호선별 지하철 승차 평균인원")
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

#호선별 지하철 하차 평균인원 시각화
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

print("호선별 지하철 하차 평균인원")
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

