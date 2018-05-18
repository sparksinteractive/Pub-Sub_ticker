# Pub/Sub ticker
Pub/sub lightshow runs on two separate Raspberry pis.
This repo is for the second pi which takes care of one main function:
 Read serial and display content on the ticker

### Building
Clone this repo into your raspberry pi.
In the root folder and run the following commands in terminal

```
$ sudo apt-get update && sudo apt-get install python2.7-dev python-pillow -y
$ sudo python install setup.py
```
That should take care of all the required dependencies.

### Running
The RGB LED matrix uses a HAT from Adafruit to make things easier to run.
The RGB LED matrix uses command line flags to address some of the required parameters.
The script run_showmessages.py takes care of the command line flags for you.

Go into the folder scripts and run the folloeing command after you run main.py on the lightshow pi.

```
$ sudo python run_showmessages.py
```

Once all the hardware is wired up, Make sure there is a conncetion between the Tx pin on the lightshow pi and the ticker pi. Make a connection between GND  on both Pis as well.

This should establish the physical serial connection that will show total messages or messages/sec on the ticker.

### References
Incase you run into issues, please refer to the following links.

* RGB LED matrix: https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python