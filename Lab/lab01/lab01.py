def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    s=str(n);#转化字符串
    if k<len(s):
        return int(s[-(k+1)])#python允许数组索引从-1开始减小，用来表示末位元素及其之前的元素.
    else:
        return 0


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    
    max_num=max(a,b,c)
    min_num=min(a,b,c)

    if a!=max_num and a!= min_num:
        return a
    elif b!=max_num and b!= min_num:
        return b
    else: 
        return c


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    
    if k==0:
        return 1
    else:
        return n*falling(n-1,k-1)


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    num=0
    i=k
    while(i<=n):
        if i%k==0:
            num+=1
            print(i)
        i+=1
    return num


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    
    total=0
    s=str(y)
    for i in range(len(s)):
        total+=int(s[i])
    return total


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

    flag=0#当为1时。前一位是8，为0时前一位不是8
    s=str(n)
    for i in range(len(s)):
        if s[i]=='8' and flag==1:
            print("True")
            return 
        elif s[i]=='8':
            flag=1
        else:flag=0
    print("False")