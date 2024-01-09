from picamera import PiCamera
from guizero import App, PushButton, Picture,Box
import datetime
from picamera.array import PiRGBArray

camera = PiCamera()
camera.resolution = (1280, 675)
camera.hflip = True
camera.vflip = True

app = App("Camera GUI", width=1280, height=720) 
preview_picture = Picture(app, image=None, width=1275, height=620)

def start_preview():
    global preview_picture
    camera.start_preview(fullscreen=False, window=(1, 1, 1280, 675))
    preview_picture.image = None

def stop_preview():
    global preview_picture
    camera.stop_preview()
    preview_picture.image = None  

def take_picture():
    global preview_picture,preview_button,stop_preview_button,shutter_button
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'/home/fujikura/Desktop/Capture/image_{current_datetime}.jpg'
    camera.capture(filename, use_video_port=True)
    preview_picture.image = filename
    preview_picture.x = 10
    preview_picture.y = 10
    preview_picture.width = 1275
    preview_picture.height = 620
    camera.stop_preview()
    
def exit_app():
    app.destroy()
    stop_preview()
    
def change_text_color(button):
    button.text_color = "blue"
    
def reset_text_color(button):
    button.text_color = None 
    
def Create_Gui():  
    global app
    buttons_box = Box(app, width="fill", align="bottom")
    exit_button = PushButton(buttons_box, command=exit_app, text="Exit", align="right")
    stop_preview_button = PushButton(buttons_box, command=stop_preview, text="Stop Preview", align="right")    
    preview_button = PushButton(buttons_box, command=start_preview, text="Start Preview", align="right")
    shutter_button = PushButton(buttons_box, command=take_picture, text="Take Picture", align="right")
    
    global zoom_20x_button,zoom_30x_button, zoom_40x_button, zoom_50x_button,zoom_60x_button, zoom_70x_button, zoom_80x_button, zoom_90x_button, zoom_100x_button
    zoom_20x_button = PushButton(buttons_box, command=zoom_20x, text="20x", align="left")
    zoom_30x_button = PushButton(buttons_box, command=zoom_30x, text="30x", align="left")
    zoom_40x_button = PushButton(buttons_box, command=zoom_40x, text="40x", align="left")
    zoom_50x_button = PushButton(buttons_box, command=zoom_50x, text="50x", align="left")
    zoom_60x_button = PushButton(buttons_box, command=zoom_60x, text="60x", align="left")
    zoom_70x_button = PushButton(buttons_box, command=zoom_70x, text="70x", align="left")
    zoom_80x_button = PushButton(buttons_box, command=zoom_80x, text="80x", align="left")
    zoom_90x_button = PushButton(buttons_box, command=zoom_90x, text="90x", align="left")
    zoom_100x_button = PushButton(buttons_box, command=zoom_100x, text="100x", align="left")

def zoom_20x():
    camera.zoom = (0.0, 0.0, 1.0, 1.0)  
    change_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_30x():
    camera.zoom = (0.1, 0.1, 0.71, 0.71)  
    change_text_color(zoom_30x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_40x():
    camera.zoom = (0.2, 0.2, 0.53, 0.53)
    change_text_color(zoom_40x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_50x():
    camera.zoom = (0.3, 0.3, 0.43, 0.43)
    change_text_color(zoom_50x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_60x():
    camera.zoom = (0.4, 0.4, 0.35, 0.35)
    change_text_color(zoom_60x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_70x():
    camera.zoom = (0.5, 0.5, 0.3, 0.3)
    change_text_color(zoom_70x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_80x():
    camera.zoom = (0.6, 0.6, 0.26, 0.26)
    change_text_color(zoom_80x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_90x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_90x():
    camera.zoom = (0.7, 0.7, 0.24, 0.24)
    change_text_color(zoom_90x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_100x_button)
    
def zoom_100x():
    camera.zoom = (0.77, 0.77, 0.21, 0.21)
    change_text_color(zoom_100x_button)
    reset_text_color(zoom_20x_button)
    reset_text_color(zoom_30x_button)
    reset_text_color(zoom_40x_button)
    reset_text_color(zoom_50x_button)
    reset_text_color(zoom_60x_button)
    reset_text_color(zoom_70x_button)
    reset_text_color(zoom_80x_button)
    reset_text_color(zoom_90x_button)
    
Create_Gui()
start_preview()
change_text_color(zoom_20x_button)
app.display()

