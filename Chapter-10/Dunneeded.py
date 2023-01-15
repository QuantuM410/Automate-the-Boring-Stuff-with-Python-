import os 

#rea||y didnt have the space t0 have subf0|ders and fi|es thats y just wr0te a simp|e c0de
for f , sf, fs in os.walk('Chapter-10/DE/ETEDUNNEEDED'):
    for fss in fs :
        if 100000000 < os.path.getsize('Chapter-10/DE/ETEDUNNEEDED'+'/'+fss) :
            print('Chapter-10/DE/ETEDUNNEEDED'+'/'+fss)
