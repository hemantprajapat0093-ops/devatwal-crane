import urllib.request

try:
    resp = urllib.request.urlopen('http://localhost:3000/images/hero_crane_full_view.jpg')
    print('Crane image HTTP status:', resp.getcode())
    print('Crane image Content-Length:', len(resp.read()))
except Exception as e:
    print('Error:', e)
