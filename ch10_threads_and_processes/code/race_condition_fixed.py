import threading
import random

counter = dict(cats=0, dogs=0)
counter_lock = threading.Lock()


def plus_many_cats(number=100_000):
    numbers = [1 for _ in range(10)]
    for _ in range(number):
        with counter_lock:
            counter['cats'] += random.choice(numbers)


print('start')
threads = [
    threading.Thread(target=plus_many_cats)
    for _ in range(5)
]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)
# Expected: 5 * 100,000 = 500,000
# Output:
# {'cats': 500000, 'dogs': 0}
