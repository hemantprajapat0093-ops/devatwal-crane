import subprocess

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate(input='protocol=https\nhost=github.com\nusername=hemantprajapat0093-ops\n\n')
print("STDOUT:", out)
print("STDERR:", err)
