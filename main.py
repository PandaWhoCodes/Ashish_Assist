import apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
from multiprocessing import Process
from run import capture_video
sched = BackgroundScheduler()
sched.start()
from comics import GetComics
from brightness import setBrightness
from bacha import getage
from getOUT import showAlert
from run import brightness

sched.add_job(brightness, 'interval', seconds=30)
sched.add_job(showAlert, 'interval', seconds=7200)
sched.add_job(GetComics, 'interval', seconds=10)

if __name__ == '__main__':
    p = Process(capture_video())
    p.start()
