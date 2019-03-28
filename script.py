import csv
import mysql.connector
from datetime import datetime
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="vol"
)

mycursor = mydb.cursor()
mycursor2 = mydb.cursor(buffered=True)
# data to timezone
# mycursor.execute("SELECT DISTINCT(airports1.tzone),airports1.tz FROM airports1")
# myresult = mycursor.fetchall()
# for x in myresult:
#     i=1;
#     for y in x:
#         if i==1 :
#             tzone=y
#         else:
#             tz=y
#         i+=1
#     print(tzone," : ", tz)
#     val=(tzone,tz)
#     mycursor.execute("INSERT INTO timezone (tzone,tz) values (%s,%s)",val)
#

# data to airports
# mycursor.execute("SELECT * from airports1")
#
# airports = mycursor.fetchall()
# mycursor.execute("select * from timezone")
# tz=mycursor.fetchall()
#
# for a in airports:
#      for t in tz:
#         print(t[1],a[8])
#         if t[1]==a[8] and a[7]==t[2]:
#             print("ici")
#             val= (a[1],a[2],a[3],a[4],a[5],a[6],t[0])
#             print(val)
#             mycursor.execute("insert into airports2 (dst, FAA,name, lat,lon, alt,id_tz) values (%s,%s,%s,%s,%s,%s,%s)",val)
#
# data to model
#
mycursor.execute("SELECT distinct(model),manufacturer,engine,engines,speed,seats,type   from planes1")
planes= mycursor.fetchall()
mycursor.execute("SELECT * from engine")
engines= mycursor.fetchall()
mycursor.execute("SELECT * from manufacturer")
manufacturer= mycursor.fetchall()
mycursor.execute("SELECT * from type")
type= mycursor.fetchall()
print(type)
#
# id_eng=0
# id_type=0
# id_manuf=0


#
# for p in planes:
#     print(p[2])
#     for e in engines:
#         if e[1] == p[2]:
#             id_eng=e[0]
#     for t in type:
#         print(t[1])
#         if t[1] == p[6]:
#             print(t[1])
#             id_type=t[0]
#     for m in manufacturer:
#         if m[1] == p[1]:
#             id_manuf=m[0]
#     val=p[0],id_manuf,id_type,id_eng,p[5],p[4],p[3]
#     print(val)
#     mycursor.execute("insert into model (model,id_manufacturer,id_type,id_engine,seats,speed,engines) values (%s,%s,%s,%s,%s,%s,%s)",val)
#
#     # resolution d'un problème: des avions qui n'aparaissent pas dans planes, on dois leur préparer un model vide.
#     mycursor.execute("insert into model (model,id_manufacturer,id_type,id_engine,seats,speed,engines) values (null,null,null,null,null,null,null)")
#

# miam miam pour plane
# mycursor.execute("SELECT tailnum,model,year from planes1")
# planes= mycursor.fetchall()
# mycursor.execute("SELECT * from model")
# model= mycursor.fetchall()
# id_model=0
# for p in planes:
#     for m in model:
#         if m[1] == p[1]:
#             id_model=m[0]
#             val=p[0],p[2],id_model
#     print(p[0],id_model)
#     mycursor.execute("Insert into planes2 (tailnum, year, id_model) values (%s,%s,%s)",val)
# print("debut commit")
# mydb.commit()
# print("finit")
#


# manque des tailnums dans planes, on va les chercher dans fligts
mycursor.execute("SELECT DISTINCT(tailnum) FROM flights1 WHERE tailnum NOT IN (SELECT tailnum FROM planes1)")
tailnum=mycursor.fetchall()
mycursor.execute("Select id_model from model where model like null ")
idModelNull=mycursor.fetchall()

for t in tailnum:
    val=[]
    val = t[0],"NULL",idModelNull
    print(val)
    mycursor.execute("Insert into planes2 (tailnum, year, id_model) values (%s,%s,%s)",val)


# table airlines2

# mycursor.execute("select * from airlines1")
# airlines = mycursor.fetchall()
# val=[]
# for a in airlines:
#     val= a[1],a[2]
#     print(val)
#     mycursor.execute("insert into airlines2 (carrier, name) value (%s,%s)",val)
#
# mydb.commit()







# miam pour flights
# #
# mycursor.execute("select count(*) from flights1")
# nb= mycursor.fetchall()
# for n in nb:
#     nombre=n[0]
#     print(nombre)
#
# mycursor2.execute("select * from flights1")
# i=0
# while i < nombre:
#     i+=1
#     plane=mycursor2.next()
#     print(plane)
#     print(i)
#     j=0
#     val=[]
#     while j <= 18:
#         j+=1
#         val.append(plane[j])
#     print(val)
#     mycursor.execute("INSERT into flights2 (year, month, day, dep_time, shed_dep_time, dep_delay, arr_time, shed_arr_time, arr_delay, carrier, flight, tailnum, origin, dest, air_time, distance, hour, minute, timehour) "
#                      "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE month=month", val)






# script datetime

#
# mycursor2.execute("Select count(*) from flights2")
# nb = mycursor2.fetchall()
# mycursor2.execute("select * from flights2")
# for n in nb:
#     nombre=n[0]
# i=0
# while i < nombre:
#      i+=1
#      plane=mycursor2.next()
#      print(i)
#      print(plane)
#      timehour=datetime(year=plane[0],month=plane[1],day=plane[2],hour=plane[16],minute=plane[17])
#      # stringDate="datetime.datetime"+"("+str(plane[0])+","+str(plane[1])+","+str(plane[2])+","+str(plane[16])+","+str(plane[17])+")"
#      # timehour.strftime('%Y-%m-%d %H:%M:%S')
#      print(timehour)
#      # print(stringDate)
#
#      val=timehour,plane[0],plane[1],plane[2],plane[16],plane[10]
#      mycursor.execute("UPDATE flights2 set timehour = (%s) where flights2.year =(%s) and flights2.month=(%s) and flights2.day=(%s) and flights2.hour=(%s) and flights2.flight= (%s)", val)





mycursor2.execute("")


print("debut commit")
mydb.commit()
print("finit")
