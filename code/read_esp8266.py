import serial
import urllib3
import time
from timeit import default_timer as timer


arduino = serial.Serial('COM4', 9600)
arduino.flushInput()  # Vacia buffer

user_API_key = 'YTP7PWZGO0G2RU00'
url = 'https://api.thingspeak.com/update?api_key=' + user_API_key
temperatureStr = ''
humidityStr = ''
Tr = 20
dataReady = False
dataRaw = 0
end = 0
elapsed = 21

start = timer()


while True:
    time.sleep(2)

    # Lectura de Arduino a Python
    if arduino.inWaiting() > 6:
        # Leo el dato en crudo del Arduino
        dataRaw = arduino.readline()
        print(f'Dato en bruto: {dataRaw}')
        dataReady = True
        print(f'Tiempo inicial: {start}')
    else:
        arduino.close()

    if elapsed > Tr and dataReady:
        start = timer()
        # Elimino caracteres y convierto en lista para obtener los valores de temperatura y humedad
        dataString = str(dataRaw)
        dataMod = dataString.strip("b'\\rn ")
        dataList = dataMod.split(",")
        print(dataList)
        # Adquiero valores de la lista por separados
        temperature = dataList[0]
        humidity = dataList[1]
        temperatureStr = str(temperature)
        humidityStr = str(humidity)
        print(f' La temperatura es: {temperature}')
        print(f'La humedad es: {humidity}')
        # Programacion para Thingspeak
        data = '&field' + str(1) + '=' + temperatureStr + '&field' + str(2) + 
               '=' + humidityStr
        http = urllib3.PoolManager()
        conn = http.request('GET', url + data)
        conn.close()
        print('Dato enviado a Thingspeak')
    end = timer()
    # Obtención del tiempo transcurrido
    print(f'Tiempo final: {end}')
    elapsed = end - start
    print(f'Tiempo transcurrido: {elapsed}')
    print(' ')
    dataReady = False
