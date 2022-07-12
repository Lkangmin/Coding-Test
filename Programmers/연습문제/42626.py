import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        
        new_ = fir + (sec * 2)
        
        heapq.heappush(scoville, new_)
        answer += 1 
    
    return answer