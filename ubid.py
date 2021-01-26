
fast-gpio set-output $LED_PIN


while [ 1 ]
do

 dht-sensor 3 DHT11 > sensors.txt

 INPUT=sensors.txt
 OLDIFS=$IFS
 IFS=': '
 [ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }

 while read col1 col2
  do

    if [ $col1 == "temperature" ]
     then
      temp=$col2
     fi

    if [ $col1 == "humidity" ]
     then
       hum=$col2
     fi

  done < $INPUT
  IFS=$OLDIFS
  echo "Temperature: $temp"
  echo "Humidity: $hum"
  
  fast-gpio set $LED_PIN 1
  sleep 1
  fast-gpio set $LED_PIN 0





  if [ $temp != "-255.000000" ] && [ $hum != "-255.000000" ]
   then

     TOKEN="BBFF-74YX4td32Qyxj3lqV7jnv24jYHi9by"
     DEVICE="oo_label"

     ubidots -t $TOKEN -d $DEVICE set "{\"humidity\":\"$hum\",\"temperature\":\"$temp\"}"
     sleep 5s
   fi

done





