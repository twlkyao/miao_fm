#! /usr/bin/env python
#coding=utf-8
import datetime
import traceback
from apscheduler.scheduler import Scheduler
from music.get_music_tag import update_the_tag
from status.model import gen_status, gc
from music.recommendations import user_get_music


def update_all():
    print '[update_all] start', datetime.datetime.now()
    try:
        print '[gc] start', datetime.datetime.now()
        gc()
        print '[gc] finish', datetime.datetime.now()
    except:
        print '[gc] error!', datetime.datetime.now()
        traceback.print_exc()

    try:
        print '[update_the_tag] start', datetime.datetime.now()
        update_the_tag()
        print '[update_the_tag] finish', datetime.datetime.now()
    except:
        print '[update_the_tag] error!', datetime.datetime.now()
        traceback.print_exc()

    try:
        print '[user_get_music] start', datetime.datetime.now()
        user_get_music()
        print '[user_get_music] finish', datetime.datetime.now()
    except:
        print '[user_get_music] error!', datetime.datetime.now()
        traceback.print_exc()

    try:
        print '[gen_status] start', datetime.datetime.now()
        gen_status()
        print '[gen_status] finish', datetime.datetime.now()
    except:
        print '[gen_status] error!', datetime.datetime.now()
        traceback.print_exc()

    print '[update_all] finish', datetime.datetime.now()


def update_5_min():
    try:
        print '[gen_status] start', datetime.datetime.now()
        gen_status()
        print '[gen_status] finish', datetime.datetime.now()
    except:
        print '[gen_status] error!', datetime.datetime.now()
        traceback.print_exc()

if __name__ == '__main__':
    sched = Scheduler(standalone=True)
    sched.add_cron_job(update_all, hour=2)
    sched.add_interval_job(update_5_min, minutes=5)
    sched.start()
