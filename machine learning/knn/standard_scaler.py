# 特征预处理之 标准化介绍:
#     目的:
#         防止因为量纲(单位)问题, 导致特征列的方差值相差较大, 影响模型的最终结果.
#         所以通过公式把 各列的值 映射到 均值为0, 标准差为1的 正态分布序列.
#     公式:
#         x'  = (当前值 - 该列平均值) / 该列的标准差

#     应用场景:
#         适用于 大数据集 的处理.

#     结论:
#         无论是归一化, 还是标准化, 目的都是为了解决因为量纲(单位)问题, 导致模型评估较低等问题.


from sklearn.preprocessing import StandardScaler

x_train = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]

transfer = StandardScaler()

x_train_scaler = transfer.fit_transform(x_train)

print(f"x_train_scaler:\n {x_train_scaler}")
print(f"mean: {transfer.mean_}")
print(f"var: {transfer.var_}")
print(f"scale: {transfer.scale_}")

# x_train_scaler:
#  [[ 1.22474487 -1.22474487 -1.29777137 -1.3970014 ]
#  [-1.22474487  1.22474487  1.13554995  0.50800051]
#  [ 0.          0.          0.16222142  0.88900089]]
# mean: [75.          3.         12.66666667 43.66666667]
# var: [150.           0.66666667   4.22222222   6.88888889]
# scale: [12.24744871  0.81649658  2.05480467  2.62466929]