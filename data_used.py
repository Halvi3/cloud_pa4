import sys

used_twt_count = 0

for i in range(1,len(sys.argv)):
    with open(sys.argv[i]) as f:
        lines = f.readlines()
        for line in lines:
            day, count = line.split('\t',1)
            used_twt_count += int(count)
    f.close()

percent = float(used_twt_count)/52303.0 * 100.0
print("Used {twts} tweets, or {pr}%".format(twts=used_twt_count,pr=percent))

