from picamera import PiCamera
from time import sleep

def photo():
    path = '/home/pi/Documents/smartbin2/smartbin2-master/images'
    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)
    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    lastfile = sorted_filename_list[-1]
    ending = lastfile[6:]
    string = ending[:-4]
    number = int(float(string))
    imagename = "-image"+str(number+1)+".jpg"
    print(imagename)
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Documents/smartbin2/smartbin2-master/images/'+imagename)
    camera.stop_preview()
