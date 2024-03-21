n, k, m = map(int, input().split())
if m > k and abs(k - n - 1) < (m - k - 1):
    print(m - k - 1)
elif abs(k - n - 1) > (k - m - 1) and m < k:
    print(abs(k - n - 1))
