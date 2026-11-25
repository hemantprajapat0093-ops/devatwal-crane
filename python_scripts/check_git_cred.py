import subprocess

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate(input='protocol=https\nhost=github.com\n\n')
print("STDOUT:")
for line in out.splitlines():
    if line.startswith('username='):
        print(line)
    elif line.startswith('password='):
        print("password is set (len:", len(line.split('=', 1)[1]), ")")
print("STDERR:", err)
