import time
import json
import datetime
from grovepi import *
from grove_rgb_lcd import *
import requests 
from requests import post
from requests.exceptions import HTTPError, RequestException, SSLError
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SubjectAltNameWarning)

hu_tem = 6


time.sleep(1)
i = 0
rooturl = 'https://raspberrypimads.local'
pem ='/home/pi/Downloads/raspberrypimads.local.pem'
temp = 0.01
hum = 0.01

count =1;


while True:
    try:
        print(' ')
        setRGB(255,255,255)  
        print("New line")
        [ temp,hum ] = dht(hu_tem,1)
        DT = datetime.datetime.now()
        Temp_Alarm ='False';
        Humid_Alarm ='False';
        
        h = str(hum);
        t = str(temp);
        WorkHours = "WorkHoures Error";
        Wjson = "Wjson Error";
        Data_Temperatur_PointsGet = "Data_Temperatur_PointsGet Error";
        DTPp = "DTPp Error";
        Data_Humidity_PointsGet = "Data_Humidity_PointsGet Error";
        DHPp = "DHPp Error";
        #setText("Temp :" + t + "C      " + "Humidity :" + h + "%")
        try:
            
            WorkHours = requests.get(url = rooturl + '/WorkHours/GetAll',verify=pem)
            Wjson = WorkHours.json()
        
            Data_Temperatur_PointsGet = requests.get(url = rooturl + '/Data_Temperatur_Points/GetAll',verify=pem)
            DTPp = Data_Temperatur_PointsGet.json()
                
            Data_Humidity_PointsGet = requests.get(url = rooturl + '/Data_Humidity_Points/GetAll',verify=pem)
            DHPp = Data_Humidity_PointsGet.json()
            #print(DHPp)
            Data_Alarm_TypeGet = requests.get(url = rooturl + '/Data_Alarm_Type/GetAll',verify=pem)
            DATg = Data_Alarm_TypeGet.json()
            setRGB(255,255,255) 
        except:
            setRGB(255,0,255);
          #x = requests.get(url = rooturl + '/Location/GetAll',
                        #verify='/home/pi/Downloads/raspberrypimads.local.pem')
        
        print("H = " + str(hum))
        print("T = " + str(temp)+'C')
        #print(WorkHours.text)
        
        
        #print(json.dumps(Wjson, indent=4, sort_keys=True))
        
        description="description Error";
        work_Start_Time="work_Start_Time Error";
        work_End_Time="work_End_Time Error";
        Temp_Max ="Temp_Max Error";
        Temp_Min="Temp_Min Error";
        Humidity_Max="Humidity_Max Error";
        Humidity_Min="Humidity_Min Error";
        data_Alarm_TypeIdTemp="data_Alarm_TypeIdTemp Error";
        data_Alarm_TypeNameTemp ="data_Alarm_TypeNameTemp Error";
        data_Alarm_TypeIdHumi="data_Alarm_TypeIdHumi Error";
        data_Alarm_TypeNameHumi="data_Alarm_TypeNameHumi Error";
        
        try:
            description = Wjson[0]['description']
            work_Start_Time = Wjson[0]['work_Start_Time']
            work_End_Time = Wjson[0]['work_End_Time']
            #print(description)
            #print(work_Start_Time)
            #print(work_End_Time)        
            Temp_Max = DTPp[0]['temperatur_High_Point']
            Temp_Min = DTPp[0]['temperatur_Low_Point']
        
            Humidity_Max = DHPp[0]['humidity_High_Point']
            Humidity_Min = DHPp[0]['humidity_Low_Point']
         
            data_Alarm_TypeIdTemp = DATg[0]['data_Alarm_TypeId']
            data_Alarm_TypeNameTemp = DATg[0]['data_Alarm_TypeName']
        
            data_Alarm_TypeIdHumi = DATg[2]['data_Alarm_TypeId']
            data_Alarm_TypeNameHumi = DATg[2]['data_Alarm_TypeName']
        
        except:
            setRGB(255,0,255);
            
            
        #print(Temp_Max)
        if(temp > Temp_Max):
            Temp_Alarm ='True';
            #setRGB(255,0,0);
            print('RGB Changed Hot');
        elif(temp < Temp_Min):
            Temp_Alarm ='True';
            #setRGB(0,0,255);
            print('RGB Changed Cold');
        else:
            setRGB(0,255,0);
            print('RGB Not Changed');
          #  
        if(hum > Humidity_Max):
            Humid_Alarm ='True';
            #setRGB(255,0,0);
            print('RGB Changed Hot');
        elif(hum < Humidity_Max):
            Humid_Alarm ='True';
            #setRGB(0,0,255);
            print('RGB Changed Cold');
        else:
            #setRGB(0,255,0);
            print('RGB Not Changed');  
        #print(datetime.datetime.now())
        Temperatur = temp;
        Temperatur = str(Temperatur);
        Humidity = hum;
        Humidity = str(Humidity);
        TemperaurTime = datetime.datetime.now();
        TemperaurTime = str(TemperaurTime);
        HumidityTime = datetime.datetime.now();
        HumidityTime = str(HumidityTime);
        EnhedId = 1;
        EnhedId = str(EnhedId);
        Data_Temperatur_PointsId = 1
        Data_Temperatur_PointsId = str(Data_Temperatur_PointsId);
        Data_Humidity_PointsId = 1;
        Data_Humidity_PointsId = str(Data_Humidity_PointsId);
        Alarm_On_OfT = Temp_Alarm
        Alarm_On_OfT = str(Alarm_On_OfT);
        Alarm_On_OfH =Humid_Alarm
        Alarm_On_OfH = str(Alarm_On_OfH);
        h = str(hum);
        t = str(temp);
        print(TemperaurTime);
        print("test1");

        #setText('Temp :' + temp + 'C      ' + 'Humidity :' + hum + '%')
        data ="Send Data To Api";
        setText(data);
        setRGB(0,0,255);
        time.sleep(1);
        print("Test2");
        
        Data_TemperaturPut = "Data_TemperaturPut Error";
        Data_HumidityPut= "Data_HumidityPut Error";
        try:
        #print('/Data_Temperatur/Create/' + Temperatur +','+ TemperaurTime +',' + EnhedId + ',' + Data_Temperatur_PointsId + ',' + Alarm_On_Of) 
            TemperaturPutUrl = '/Data_Temperatur/Create/' + Temperatur +','+ TemperaurTime +',' + EnhedId + ',' + Data_Temperatur_PointsId + ',' + Alarm_On_OfT;
            Data_TemperaturPut = requests.put(url = rooturl + TemperaturPutUrl ,verify=pem)
            print(TemperaturPutUrl);
            print('Tempratur status code: '+ str(Data_TemperaturPut.status_code))
        
        
            Humidityputurl = '/Data_Humidity/Create/' + Humidity +','+ HumidityTime +',' + EnhedId + ',' + Data_Humidity_PointsId + ',' + Alarm_On_OfH;
            Data_HumidityPut = requests.put(url = rooturl + Humidityputurl , verify=pem)    
            print('Humidity status code: '+ str(Data_HumidityPut.status_code))
        
        except:
            setRGB(255,0,255);
        
        
        #/Data_Alarm/Create/{Alarm},{EnhedId},{Data_Alarm_TypeId}
        Data_AlarmUrl = '/Data_Alarm/Create/';
        #Data_HumidityPut = requests.put(url = rooturl + Data_AlarmUrl , verify=pem)    
        #print('Humidity status code: '+ str(Data_HumidityPut.status_code))
        if(Alarm_On_OfT == 'True'):            
            Data_AlarmTPut = requests.put(url = rooturl + Data_AlarmUrl + 'Tempratur,'+ '1,'+'1', verify=pem);    
            print('Alarm Temp status code: '+ str(Data_AlarmTPut.status_code));
        if(Alarm_On_OfH == 'True'):
            Data_AlarmHPut = requests.put(url = rooturl + Data_AlarmUrl + 'Humidity,'+ '1,'+'1', verify=pem);    
            print('Alarm Humi status code: '+ str(Data_AlarmHPut.status_code));
        #print('/Data_Temperatur/Create/' + Temperatur +','+ TemperaurTime +',' + EnhedId + ',' + Data_Temperatur_PointsId + ',' + Alarm_On_Of) 
        
        #if(Alarm_On_OfT = 'True'):
            #;
        #elif(Alarm_On_OfT = 'True'):
            #;
        
        
        
        print('SC: T :' + str(Data_TemperaturPut.status_code)+ '/H:' + str(Data_HumidityPut.status_code)+'/AT:'+ str(Data_AlarmTPut.status_code)+'/AH:'+str(Data_AlarmHPut.status_code))
        statuscode = str("SC: T :" + str(Data_TemperaturPut.status_code)+ "/H:" + str(Data_HumidityPut.status_code)+"/AT:"+ str(Data_AlarmTPut.status_code)+"/AH:"+str(Data_AlarmHPut.status_code))
        
        setText(statuscode)
        
        if(str(Data_TemperaturPut.status_code)=='200' and str(Data_HumidityPut.status_code)=='200' and str(Data_AlarmTPut.status_code) =='200' and str(Data_AlarmHPut.status_code)=='200'):
            setRGB(0,255,0);
        else:
            setRGB(255,0,0);
        #setRGB(0,255,0)
        time.sleep(5)
        
        
        setText('Temp :' + t + 'C     ' + 'Humidity :' + h + '%')
        
        
        print('Count : ' + str(count));
        count = count+1;
        print('End Of The Line')        
        time.sleep(600)

    except IOError:
        print("Error Temp SC : " + str(Data_TemperaturPut.status_code))
        print("Error Humi SC : " + str(Data_AlarmHPut.status_code))
        print('Error Alarm Temp SC : '+ str(Data_AlarmTPut.status_code));
        print('Error Alarm Humi SC : '+ str(Data_AlarmHPut.status_code));
        