def solution(list_of_nums):
    for i in list_of_nums:
        if i%2 == 0:
            d1['EVEN']=d1['EVEN'] + 1
        else:
            d1['ODD'] = d1['ODD'] + 1
    return d1


list_of_nums = []
d1 = {'ODD': 0, 'EVEN': 0}
solution(list_of_nums)
