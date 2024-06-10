poll_results = {}

while True:
  place = input("If you could visit one place in the world, where would you go? (or 'quit' to finish): ")
  if place.lower() == 'quit':
    break

  # Check if place was already entered and increment count if so
  if place in poll_results:
    poll_results[place] += 1
  else:
    poll_results[place] = 1

print("\nDream Vacation Poll Results:")
for place, votes in poll_results.items():
  print(f"\t{place.title()}: {votes} votes")
