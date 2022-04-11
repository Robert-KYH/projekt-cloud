
from matplotlib import pyplot as plot
import boto3

# anslut till dynamodbn

dynamodb = boto3.resource("dynamodb",
                          aws_access_key_id="---",
                          aws_secret_access_key="---",
                          region_name="eu-north-1")

# läs in all data från tabellen

tab = dynamodb.Table("sensordata")
data = tab.scan()["Items"]

inne_x, inne_y = [], []
ute_x, ute_y = [], []
t1 = t2 = 0

# skapa en datapunkt för varje inlägg i tabellen, rätta temperaturen från tiondelar
# och hoppa 10 sekunder mellan varje datapunkt

for d in data:
  # lägg till en datapunkt i inside-kurvan
  if "inside" in d:
    tid = t1
    temp = float(d["inside"])/10
    inne_x.append(tid)
    inne_y.append(temp)
    t1 += 10

  # lägg till en datapunkt i outside-kurvan
  else:
    tid = t2
    temp = float(d["outside"])/10
    ute_x.append(tid)
    ute_y.append(temp)
    t2 += 10

# plotta kurvorna

plot.figure()
plot.xlabel("Tid")
plot.ylabel("Grader Celsius")
plot.plot(ute_x, ute_y, label="Utomhus")
plot.plot(inne_x, inne_y, label="Inomhus")
plot.legend()
plot.show()
