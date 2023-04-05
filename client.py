from datetime import datetime

import rides_pb2 as pb


# print(pb.POOL)
# print(pb.RideType.Name(pb.POOL))
# print(pb.RideType.Value('REGULAR'))


# loc = pb.Location(
#     lat = 32.548764,
#     lang = 34.45456,
# )

# print(loc)



request = pb.StartRequest(
    car_id = 87,
    driver_id = "hoseinlycan",
    passenger_ids = ['p1', 'p2', 'p3'],
    type = pb.POOL,
    location = pb.Location(
        lat=32.4344334,
        lang=34.567575,

    ),
)



time = datetime(2023, 2, 13, 14, 39, 42)
request.time.FromDatetime(time)
print(request)


time2 = request.time.ToDatetime()
print(type(time2), time2)


from google.protobuf.timestamp_pb2 import Timestamp

now = Timestamp()
now.GetCurrentTime()
print(now)




#region json
from google.protobuf.json_format import MessageToJson

data = MessageToJson(request)
print(data)



# region size 
print('encode size')
print('_ json :', len(data))
print('_ protobuf:', len(request.SerializeToString()))



# print(request)
# print('lat: ',request.location.lat)


# data = request.SerializeToString()
# print('type: ', type(data))
# print('size: ', len(data))



# request2 = pb.StartRequest()
# request2.ParseFromString(data)
# print(request2)