 #!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import serial

ser = serial.Serial(port='/dev/ttyS0',baudrate = 38400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
oldMessage = 0
message = "standby..."
class RunText(SampleBase):

    def run(self):
        global oldMessage
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../fonts/7x13.bdf")
        textColor = graphics.Color(100, 100, 100)
        pos = 2

        while True:
            message = ser.readline()
#            message = "test: 012345gfjvghgvmh"
            print 'printing: ',message
            my_text = message
            if not message:
                print "skip render"
                continue
            else:
                offscreen_canvas.Clear()
                len = graphics.DrawText(offscreen_canvas, font, pos, 12, textColor, my_text)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            oldMessage = message

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

