PIN=18
echo $PIN > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio18/direction

while true
do
	echo "1" > /sys/class/gpio/gpio18/value
	sleep 1
	echo "0" > /sys/class/gpio/gpio18/value
	sleep 1
done

	
