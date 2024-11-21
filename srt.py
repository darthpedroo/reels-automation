import pysrt

subs = pysrt.open('homero.srt')
print(len(subs))

for sub in subs:
    print("--------")
    print(sub.start)
    print("[--------]")
    print(sub.text)
    print("[--------]")
    print(sub.end)
    print("end")