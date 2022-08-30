from sklearn import tree

print("Welcome to the 'Body Health Program'. It will tell, depending of you habits, how your healthy you'll be in 30 years!\n")

healthy= '1'
normal = '2'
unhealthy = '3'

daily = '1'
usually = '2'
rarely = '3'

training = [[10, 30, daily, daily, daily], [5, 15, usually, usually, usually], [5, 7, rarely, rarely, rarely]]
health = [healthy, normal, unhealthy]

test=tree.DecisionTreeClassifier()
testr=test.fit(training, health)

activity = input("Time percentage of fisical activity: ")
sleep = input("Time percentage of sleep: ")
fruit = input("Please select from: 1 - Daily, 2 - Usually, 3 - Rarely.\nFrequency that you eat fruits: ").lower()
meals = input("Please select from: 1- Daily, 2 - Usually, 3 - Rarely.\nFrequency that you eat meals: ").lower()
sunlight = input("Please select from: 1- Daily, 2 - Usually, 3 - Rarely.\nFrequency that you're exposed to sunlight: ").lower()

result = test.predict([[activity, sleep, fruit, meals, sunlight]])

if result == "1":
    print("You'll be healthy in 30 years!")
elif result == "2":
    print("You'll be on average in 30 years!")
elif result == "3":
    print("You'll be unhealthy in 30 years!")
else:
    print("ops")
