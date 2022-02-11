def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      print(item)
      if  max(d)[0] > item[0]:
          d.append(item)
          print(d)
      else:
          print(item)
          answer += 1
          if item[1] == location:
              break
  return answer

priorities = [2, 1, 3, 2]
location = 0

print(solution(priorities, location))
