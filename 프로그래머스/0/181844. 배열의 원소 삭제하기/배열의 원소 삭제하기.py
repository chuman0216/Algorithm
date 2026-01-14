def solution(arr, delete_list):
    answer = arr.copy()
    
    for i in arr:
        if i in delete_list:
            answer.remove(i)
    
    return answer