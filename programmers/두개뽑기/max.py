def solution(numbers):
  answer = []

  for i in range(0, len(numbers) - 1):
    for n in numbers[i + 1:]:
      s = numbers[i] + n
      if not s in answer:
        answer.append(s)

  answer.sort()
  return answer