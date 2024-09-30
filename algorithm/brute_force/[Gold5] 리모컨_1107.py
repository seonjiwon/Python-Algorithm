import sys

def is_valid_channel(channel, broken_buttons):
  for digit in str(channel):
    if int(digit) in broken_buttons:
      return False
  return True

def min_presses(target_channel, broken_buttons = []):
  current_channel = 100
  if target_channel == current_channel:
    return 0
  min_presses = abs(target_channel - current_channel)

  for channel in range(1000001):
    if is_valid_channel(channel, broken_buttons):
      pressses = len(str(channel)) + abs(channel - target_channel)
      min_presses = min(pressses, min_presses)
  return min_presses


if __name__ == "__main__":
  target_channel = int(sys.stdin.readline())
  num_broken_buttons = int(sys.stdin.readline())
  if num_broken_buttons > 0:
    broken_button = list(map(int, sys.stdin.readline().strip().split()))
    print(min_presses(target_channel, broken_button))
  else:
    print(min_presses(target_channel))
