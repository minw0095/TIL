# def make(n):
#     for a in range(n):
#         total = list(str(a))
#         for b in range(len(total)):
#             total[b] = int(total[b])
#     for a in range(n):
#         if a + sum(total) == n:
#             return True

# for a in range(9990,10001):
#     if not make(a):
#         print(a)

nums = set(range(1,10001))
news = set()

for a in range(1,100001):
    t = list(str(a))
    for b in range(len(t)):
        t[b] = int(t[b])
    news.add(a+sum(t))

for a in sorted(nums-news):
    print(a)

