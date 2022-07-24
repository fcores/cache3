from cachetools import cached,TTLCache
from time import time

cache = TTLCache(maxsize=100,ttl=86400)


inicio_1=time()
for i in range(0,100000):
    pass
fin_1=time()-inicio_1


@cached(cache)
def prueba():
    for i in range(0,100000):
        pass
inicio_2=time()
prueba()
fin_2=time()-inicio_2

print(fin_1)
print(fin_2)

