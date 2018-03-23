import argparse
import subprocess
from time import sleep
from uuid import uuid4
from telepot import Bot,glance
from telepot.loop import MessageLoop

def newredirect(email):
    redirectmail = '{}@{}'.format(uuid4().hex,domain)
    open(virtualaliasfile,'a').write('{}\t{}\n'.format(redirectmail,email))
    subprocess.check_output('postmap {}'.format(virtualaliasfile).split())
    subprocess.check_output('service postfix reload'.split())
    return redirectmail

def deleteredirect(email):
    lines = [line for line in open(virtualaliasfile) if not email in line]
    open(virtualaliasfile,'w').write(''.join(lines))
    subprocess.check_output('postmap {}'.format(virtualaliasfile).split())
    subprocess.check_output('service postfix reload'.split())

def listredirects():
    redirects = [line for line in open(virtualaliasfile)]
    return redirects

def actions(msg,chat_id):
    msg = msg.split()
    if '/new' in msg[0] and len(msg) == 2:
        redirectmail = newredirect(msg[1])
        bot.sendMessage(chat_id,'{} to email {}'.format(msg[1],redirectmail))

    elif '/delete' in msg[0] and len(msg) == 2:
        deleteredirect(msg[1])
        bot.sendMessage(chat_id,'All redirects to email {} were deleted'.format(msg[1]))

    elif '/list' in msg[0]:
        redirects = listredirects()
        for redirect in redirects:
            redirect,email = redirect.replace('\n','').split('\t')
            bot.sendMessage(chat_id,'{} to {}'.format(redirect,email)) 

def handle(msg):
    content_type, chat_type, chat_id = glance(msg)
    if str(chat_id) in users and chat_type == 'private' and content_type == 'text':
        actions(msg['text'],chat_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-t',
        '--token-telegram',
        metavar='telegram-token-goes-here',
        help='Insert your telegram token',
        required=True)
    required.add_argument('-d',
        '--domain',
        metavar='domain.no-ip.org',
        help='Your domain goes here',
        required=True)
    required.add_argument('-i',
        '--id-telegram',
        metavar='Telegram user ID',
        help='Insert one or more Telegram IDs separeted by ,',
        required=True)
    args = parser.parse_args()

    bot = Bot(args.token_telegram)
    users = args.id_telegram.split(',')
    domain = args.domain
    virtualaliasfile = '/data/virtual'
    subprocess.check_output('/etc/init.d/postfix restart'.split())
    MessageLoop(bot, handle).run_as_thread()
    while 1:
        sleep(1)

