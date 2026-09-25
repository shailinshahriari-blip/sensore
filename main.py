import pandas as pd
from sklearn.model_selection import train_test_split





data = pd.read_csv("data.csv")
data


data.columns



x=data[['Temperature', 'Humidity', 'Light', 'CO2', 'HR']]
y=data['Occupancy']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)



data_train=pd.concat([x_train,y_train],axis=1)
data_test=pd.concat([x_test,y_test],axis=1)
data_test.to_csv("test.csv")


data_1=data_train[data_train["Occupancy"]==1]
del data_1["Occupancy"]
data_1
data_1.to_csv("data_train_1.csv", index=False)





data_0=data_train[data_train["Occupancy"]==0]
del data_0["Occupancy"]
data_0
data_0.to_csv("data_train_0.csv", index=False)




data_0=data[data["Occupancy"]==0]
del data_0["Occupancy"]
data_0





data_1=data_test[data_test["Occupancy"]==1]
del data_1["Occupancy"]
data_1.to_csv("data_test_1.csv",index=False)
data_1





data_1=data_test[data_test["Occupancy"]==0]
del data_1["Occupancy"]
data_1.to_csv("data_test_0.csv",index=False)
data_1





data_0.to_csv("data_label_0.csv", index=False)






from mlforkidsnumbers import MLforKidsNumbers





project = MLforKidsNumbers(
    modelurl="https://mlforkids-newnumbers.1re3wh44gzos.eu-de.codeengine.appdomain.cloud/saved-models/auth0|6a253bf63c6de0b92c8093c2-2/status"
)





testvalue = {
    "Temperature" : 0,
    "Humidity" : 0,
    "Light" : 0,
    "CO2" : 0,
    "HR" : 0,
}

response = project.classify(testvalue)
top_match = response[0]

label = top_match["class_name"]
confidence = top_match["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))





import pandas as pd




data=pd.read_csv("data_test_0.csv")
data



data["truth"]=0
data






p=[]
for i in range(0,348):
  testvalue = {
     "Temperature" : data["Temperature"][i],
      "Humidity" : data["Humidity"][i],
     "Light" : data["Light"][i],
     "CO2" :  data["CO2"][i],
      "HR" : data["HR"][i],
     }

  response = project.classify(testvalue)
  top_match = response[0]

  label = int(top_match["class_name"])
  p.append(label)