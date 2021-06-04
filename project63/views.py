import subprocess
from threading import Thread

import roslaunch
import rospy
from django.shortcuts import render


def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test.html', context)
def formation(request):
    rospy.init_node('test_formation', disable_signals=True)
    run()
    return render(request,'test.html')

def run():
    cmd = "roslaunch president run.launch"
    # cmd = 'ping 127.0.0.1'
    print(cmd)
    mytask = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)