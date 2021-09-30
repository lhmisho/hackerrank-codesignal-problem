# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def count_pair(n, ar):
    return sum([ar.count(i)//2 for i in set(ar)])

if __name__ == "__main__":
    socks_list = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = count_pair(len(socks_list), socks_list)
    print(result)