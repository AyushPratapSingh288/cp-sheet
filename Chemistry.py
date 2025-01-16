from collections import defaultdict

def main():
    n, k = map(int, input().split())
    s = input()
    
    # Initialize a defaultdict for counting character frequencies
    char_count = defaultdict(int)
    for char in s:
        char_count[char] += 1
    
    cnt = 0  # Count of characters that can be paired
    for char, freq in char_count.items():
        if cnt % 2 == 0:
            cnt += freq
        else:
            if freq % 2 == 0:
                cnt += freq
            else:
                cnt +=freq-1
           
    if n - cnt <= k:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input()) 
    for _ in range(t):
        main()
