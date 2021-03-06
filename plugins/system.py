# -*- coding: utf-8 -*-

from config import *
import platform, psutil, subprocess

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rotation.py importado.{/cyan}'))

@bot.message_handler(commands=['system'])
def command_system(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        uptime = subprocess.getoutput('uptime')
        running = '\n*Running on*:\n'
        running += '\tSystem: {0}\n'.format(subprocess.getoutput('head -n1 /etc/issue | cut -d " " -f -3'))
        running += '\tKernel: {0}\n'.format(subprocess.getoutput('uname -rs'))
        running += '\tProcessor: {0}\n'.format(subprocess.getoutput('cat /proc/cpuinfo | grep "model name" | tr -s " " | cut -d " " -f 3-'))
        running += '\tRAM: {0}MB ({1}% used)\n'.format(int(psutil.virtual_memory()[0] / 1000 / 1000), psutil.virtual_memory()[2])
        running += '\tPython: {0} ({1})\n'.format(str(platform.python_version()), str(platform.python_compiler()))
        running += '\tServer time: {0}\n'.format(time.strftime("%c"))
        running += '\tUptime: Server up for {0} d, {1} h, {2} m\n'.format(uptime.split()[2], uptime.split(':')[0], uptime.split(':')[1])
        bot.send_message( cid, running, parse_mode="Markdown")
