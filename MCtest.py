from sklearn import tree # creates training data in lines below
features = [[140,1],[130,1],[150,0],[170,0]] # 0 for bumpy 1 for smooth
labels = ["apple","apple","orange","orange"] # 0 for apple, 1 for orange 
clf= tree.DecisionTreeClassifier()
clf=clf.fit(features, labels) #trains classifier
print clf.predict([[160,0]])
