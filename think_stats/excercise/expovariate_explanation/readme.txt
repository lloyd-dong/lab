python random.expovariate(lam) 生成一系列 x。 

1. x 分布的特点是 max(x) <4.5,  80%的 x < 1.0. 这一点可以通过生成 逆函数 -ln(1-random())/am 的分布来对比验证。
2. 用这个 x list, 套用 指数分布的 CDF 公式 CDF = 1 - exp(-lam * x), 就可以得到 CDF 从 [0.0, 1.0) 的均匀随机分布。举例，用expovaiate(2.0) 得到 [x],从[0.0, 4) 按照公式生成的cdf，按步长为一分成10组 (bin_cdf_by_rand_x)，pmf分布很均匀, 每个bin 都在 10% 左右.

然而，如果用其他方法随便生成 x 系列， 按照lam 公式得到到CDF 不会在 [0.0, 1.0)均匀分布。

例如：随机生成 [x] [0.0, 10), 按照公式生成的cdf，按步长为一分成10组 (bin_cdf_by_rand_x2)，pmf分布很不均匀， 有85% 的 cdf 值在 >9这个分组，也就是说绝大多数点都集中在cdf曲线右上侧
