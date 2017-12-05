from sklearn import tree # creates training data in lines below
features = [[4,3],[5,4],[9,8],[7,9]] # Happiness 0-10, hours of sleep
labels = ["Computer Science Major","Computer Science Major","LAS Major","LAS Major"] 
clf= tree.DecisionTreeClassifier()
clf=clf.fit(features, labels) #trains classifier
print clf.predict([[2,2]])
