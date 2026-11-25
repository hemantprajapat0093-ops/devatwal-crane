import urllib.request

html = urllib.request.urlopen('http://127.0.0.1:3000/').read().decode('utf-8')
print('Vishnudat present:', 'Vishnudat' in html)
print('Dharminder count:', html.count('Dharminder'))
print('8003721244 count:', html.count('8003721244'))
print('9982842357 count:', html.count('9982842357'))
print('9414333328 count:', html.count('9414333328'))
print('9950233073 count:', html.count('9950233073'))
print('corner-dock-btn-maps present:', 'corner-dock-btn-maps' in html)
print('Clickable RIICO box present:', 'Click to Open Google Maps' in html)
