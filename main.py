import os
import pyautogui as p
import sys
from flask import Flask

app = Flask(__name__)


def find(img):
	currentDir = os.path.realpath(__file__).split('\\')
	currentDir.pop()
	drivePng = "\\".join(currentDir)+'\\png\\{}'.format(img).replace('\\\\','\\')
	return p.center(p.locateOnScreen(drivePng, confidence=0.8))
	
def click(img):
	p.rightClick(find(img))

def press(key, how=1):
		p.press(key, presses=int(how))

def quality(q):
		#q = 360, 720
		click('setting_drive_video.png')
		click('quality_drive_video.png')
		click('q_{}.png'.format(q))

def speed(s):
		# s = 1, 1.25, 1.5
		click('setting_drive_video.png')
		click('speed_drive_video.png')
		p.sleep(0.5)
		p.vscroll(-400)
		p.sleep(0.5)
		click('s_{}.png'.format(s))
		click('setting_off_drive_video.png')

def pause_play():
		press('space')

def mute_loud():
		press('m')

def full_wide():
		press('f')

def sort():
		click('sort.png')

def r_sort():
		click('r_sort.png')

def list_view():
		click('list_view.png')

def grid_view():
		click('grid_view.png')

def next_page(how):
		p.vscroll(-1*int(how))

def prev_page(how):
		p.vscroll(int(how))

def up(how):
		press('up', how)

def down(how):
		press('down', how)

def left(how):
		press('left', how)

def right(how):
		press('right', how)

def back():
		press('backspace')

def enter():
		press('enter')

def esc():
		press('esc')



@app.route('/<f>/<how>/')
def index(f, how):
	if(f=='list'):
		list_view()
	
	elif(f=='grid'):
		grid_view()
	
	elif(f=='up'):
		up(how)
	
	elif(f=='down'):
		down(how)
	
	elif(f=='mute'):
		mute_loud()
	
	elif(f=='fullscreen'):
		full_wide()
	
	elif(f=='left'):
		left(how)
	
	elif(f=='right'):
		right(how)
	
	elif(f=='sort'):
		sort()
	
	elif(f=='r_sort'):
		r_sort()
	
	elif(f=='play'):
		pause_play()
	
	elif(f=='back'):
		back()
	
	elif(f=='speed'):
		d = {"1":"1","2":"1.25","3":"1.5"}
		speed(d[how])
	
	elif(f=='enter'):
		enter()
	
	elif(f=='esc'):
		esc()
	
	elif(f=='q'):
		d = {"1":"360", "2":"720"}
		quality(d[how])

		

	print(f)
	print(how)

	
	return '<h1>{} {}</h1>'.format(f, how)


if __name__=='__main__':
	app.run()


