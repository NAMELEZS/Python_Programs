### 03/28/2021
### Norman Lowery II
### Using the pop() method, used for removing something from a list but still want to have it there

subscribers = ['norman@example.com', 'john@example.com', 'mary@example.com']
print(subscribers)

popped_subscriber = subscribers.pop()

print(subscribers)

print(popped_subscriber)

subscribers = ['norman@example.com', 'john@example.com', 'mary@example.com']
first_subscriber = subscribers.pop(0)

print("Your first subscriber was " + first_subscriber + ".")

subscribers = ['norman@example.com', 'john@example.com', 'mary@example.com']
print(subscribers)

subscribers.remove('john@example.com')

print(subscribers)

subscribers = ['norman@example.com', 'john@example.com', 'mary@example.com']
subscribed_by_mistake = 'norman@example.com'
subscribers.remove(subscribed_by_mistake)

print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up.")