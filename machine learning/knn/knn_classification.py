# 基于 欧式距离(或者其它距离计算方式)计算 测试集 和 每个训练集之间的距离, 然后根据距离升序排列, 找到最近的K个样本.
# 基于K个样本投票, 票数多的就作为最终预测结果 -> 分类问题.
# 基于K个样本计算平均值, 作为最终预测结果 -> 回归问题.

from sklearn.neighbors import KNeighborsClassifier

x_train = [[0], [1], [2], [3]]  # 特征可能有多个，所以是二维数组
y_train = [0, 0, 1, 1]
x_test = [[5]]

estimator = KNeighborsClassifier(n_neighbors=3)  # KNN 默认使用欧氏距离
estimator.fit(x_train, y_train)

y_pred = estimator.predict(x_test)

print(f"y pred: {y_pred}")

# y pred: [1]