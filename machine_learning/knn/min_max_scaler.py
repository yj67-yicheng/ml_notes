# 特征预处理之 归一化介绍:
#     目的:
#         防止因为量纲(单位)问题, 导致特征列的方差值相差较大, 影响模型的最终结果.
#         所以通过公式把 各列的值 映射到 [0, 1] 区间.
#     公式:
#         x'  = (当前值 - 该列最小值) / (该列最大值 - 该列最小值)
#         x'' = x' * (mx - mi) + mi
#     公式解释:
#         x' ->  基于公式算出来的 结果
#         x'' -> 最终的 结果.
#         mx ->  区间的最大值
#         mi ->  区间的最小值
#     弊端:
#         容易受到最大值 和 最小值的影响, 所以它一般用于处理 小数据集.

from sklearn.preprocessing import MinMaxScaler

x_train = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]

transfer = MinMaxScaler(feature_range=(3, 5))
x_train_scaler = transfer.fit_transform(x_train)

print(f"x_train_scaler:\n {x_train_scaler}")

# x_train_scaler:
#  [[5.         3.         3.         3.        ]
#  [3.         5.         5.         4.66666667]
#  [4.         4.         4.2        5.        ]]
