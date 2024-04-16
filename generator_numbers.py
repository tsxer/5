import re

def generator_numbers(text) :
  pattern = r"(\s+\d+\.\d+)+\s*"
  matches = re.findall(pattern, text)
  for match in matches:
    yield float(match.strip())

def sum_profit(text, func):
  nums = func(text)
  profit = 0 
  for num in nums:
    profit += num
  return profit
   
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

