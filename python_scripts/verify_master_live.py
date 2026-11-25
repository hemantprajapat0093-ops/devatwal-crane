import urllib.request

try:
    resp = urllib.request.urlopen('http://localhost:3000/api/health')
    print('Health status:', resp.getcode(), resp.read().decode())
    
    resp_img = urllib.request.urlopen('http://localhost:3000/images/hero_exact_master_banner.jpg')
    print('Master banner 1x HTTP status:', resp_img.getcode(), 'length:', len(resp_img.read()))

    resp_img2 = urllib.request.urlopen('http://localhost:3000/images/hero_exact_master_banner_2x.jpg')
    print('Master banner 2x HTTP status:', resp_img2.getcode(), 'length:', len(resp_img2.read()))

    resp_html = urllib.request.urlopen('http://localhost:3000/')
    html = resp_html.read().decode('utf-8')
    print('HTML length:', len(html))
    print('Contains hero_exact_master_banner.jpg:', 'hero_exact_master_banner.jpg' in html)
    print('Contains hero-btn-hotspot-booking:', 'hero-btn-hotspot-booking' in html)
    print('Contains hero-btn-hotspot-quote:', 'hero-btn-hotspot-quote' in html)
except Exception as e:
    print('Error:', e)
