import urllib.request

try:
    resp = urllib.request.urlopen('http://localhost:3000/api/health')
    print('Health status:', resp.getcode(), resp.read().decode())
    
    resp_img = urllib.request.urlopen('http://localhost:3000/images/hero_exact_master_banner.jpg')
    print('Banner 1x size:', len(resp_img.read()))

    resp_img2 = urllib.request.urlopen('http://localhost:3000/images/hero_exact_master_banner_2x.jpg')
    print('Banner 2x size:', len(resp_img2.read()))

    resp_insp = urllib.request.urlopen('http://localhost:3000/images/verify_hindi_crane_service.jpg')
    print('Inspection crop size:', len(resp_insp.read()))
    print("All live assets verified successfully!")
except Exception as e:
    print('Error:', e)
