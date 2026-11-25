import urllib.request

try:
    resp = urllib.request.urlopen('http://localhost:3000/api/health')
    print('Health status:', resp.getcode(), resp.read().decode())
    resp2 = urllib.request.urlopen('http://localhost:3000/')
    html = resp2.read().decode('utf-8')
    print('Index length:', len(html))
    print('Contains hero_crane_full_view.jpg:', 'hero_crane_full_view.jpg' in html)
    print('Contains lg:col-span-5:', 'lg:col-span-5' in html)
    print('Contains Devatwal Crane Service:', 'Devatwal Crane Service' in html)
    print('Contains Lift Higher:', 'Lift Higher' in html)
except Exception as e:
    print('Error:', e)
