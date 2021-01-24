import requests, json, uuid, random, os

current_hwid = uuid.getnode()
r = random.randint(1, 25)
cmd = ['61757468', '73656367726f7570', '737461747573', '757365726e616d65']
stats = ['76616c6964', '73756363657373']

def zoneauth():
    authkey = ''
    if os.path.isfile('key.dat'):
        keyfile = open('key.dat', 'r')
        authkey = keyfile.read()
        keyfile.close()
    else:
        authkey = str(input('Insert Your Auth Key: '))
    data = {
        'type': dec(cmd[0]),
        'key': str(authkey),
        'hwid': str(current_hwid)
    }
    print('Please wait...')
    print('Connecting to InfectedZone Server #', r, sep='')
    try:
        with requests.Session() as sess:
            checkauth = sess.post('http://localhost/zone/auth.php', data=data)
            response = checkauth.json()
            print(response)
            if response[dec(cmd[0])] == dec(stats[1]):
                if response[dec(cmd[1])] == dec(stats[0]):
                    keyfile = open('key.dat', 'w')
                    keyfile.write(authkey)
                    keyfile.close()
                    print('Welcome: ' + response[dec(cmd[3])] + ', enjoy your exclusive infected-zone.com tool!')
                else:
                    print('You need to be Premium+ to use this tool sir.')
                    exit()
            else:
                print('Error: ' + response[dec(cmd[2])])
                if os.path.isfile('key.dat'):
                    os.remove('key.dat')
                exit()
    except Exception as ex:
        print('Failed to do something: ' + str(ex))
        exit()

def dec(data):
    return bytes.fromhex(data).decode('utf-8')