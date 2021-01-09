def nearest_square(n):
    if n>0:
        for i in range(n):
            if i*i<=n:
                nearSq=i*i
        return nearSq
    return 0
