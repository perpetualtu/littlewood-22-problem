# Littlewood 第 22 问：下界提升的六智能体路线图

日期：2026-08-27  
结果类别：**rigorous partial result（严格部分结果）**。本轮得到两个可立即写成定理的分支与若干精确候选引理，但没有得到强于 Bedert 的新统一下界。

## 1. 研究契约

对有限集 \(A\subset\mathbb Z_{\ge0}\)，令

\[
F_A(x)=\sum_{a\in A}\cos(ax),\qquad |A|=N,
\]

并令 \(Z(F_A)\) 为 \([0,2\pi)\) 上不同实零点的数目，

\[
Z(N)=\min_{|A|=N}Z(F_A).
\]

截至本轮文献核对，公开纪录下界仍是

\[
B(N):=\frac{\log\log N}{\log\log\log N}
\ll Z(N),
\]

更准确地写作 \(Z(N)\ge(\log\log N)^{1-o(1)}\)。完整的“下界提升”必须对每个 \(A\) 给出 \(\omega(N)B(N)\) 型下界，其中 \(\omega(N)\to\infty\)。特例、有限枚举、条件引理、结构子集的零点结论都不构成统一提升。

主要基准：

- [Bedert, *An improved lower bound for a problem of Littlewood on the zeros of cosine polynomials*](https://arxiv.org/abs/2407.16075)
- [Bloom--Green, *Remarks on the inverse Littlewood conjecture*](https://arxiv.org/abs/2602.16482)
- [Reiher--Schoen, *Note on the Theorem of Balog, Szemerédi, and Gowers*](https://arxiv.org/abs/2308.10245)

## 2. 六个独立子任务

| 子智能体 | 独立机制 | 核心返回 |
|---|---|---|
| 1 | 加性能量与逆结构 | 能量纪录提升阈值；区间并分支；结构子集到完整和的非遗传障碍 |
| 2 | 跳点、Hankel、Prony | 跳点指数和的精确秩；根处原函数逐点界的反例；全局交错和候选 |
| 3 | 卷积幂等核、Toeplitz | 普通 BV 只能给常数；交换子恒等式；逆 Littlewood 的高能子集桥 |
| 4 | Bedert 参数链 | \(P,K,L^1\) 三类损失的统一反演；确定最小可见改进 |
| 5 | 局部根几何与复分析 | 固定环带根质量；固定相位层通量；排除净绕数/Mahler 终局 |
| 6 | 计算性恶意审计 | 1474 样本的统一特征面板；反射、膨胀、切触根压力测试与判废阈值 |

## 3. 本轮得到的两个严格分支

### 3.1 固定阶高阶能量阈值

对固定 \(k\ge2\)，令

\[
E_k(A)=\#\{a_1+\cdots+a_k=b_1+\cdots+b_k\}.
\]

已有高阶能量下界

\[
Z(F_A)\ge c_k
\frac{N^{(3k-1)/(k-1)}}{E_k(A)^{2/(k-1)}}.
\]

因此，对任意 \(\omega(N)\to\infty\)，若

\[
\boxed{
E_k(A)\le c_k
N^{(3k-1)/2}
[\omega(N)B(N)]^{-(k-1)/2},
}
\]

则

\[
Z(F_A)\gg_k\omega(N)B(N),
\]

严格超过当前统一纪录。特别地，\(k=2\) 时只需

\[
E(A)\le c\frac{N^{5/2}}{\sqrt{\omega(N)B(N)}}.
\]

这把统一问题压缩到高能量区域，但高能量本身不预测零点数；反射集合保持全部 \(E_k\)，零点数却可相差一个数量级。

### 3.2 少整数区间分块分支

令 \(q(A)\) 为把 \(A\setminus\{0\}\) 写成互不交整数区间之并所需的最少区间数。则

\[
\boxed{
Z(F_A)\ge c\frac{\log N}{q(A)}.
}
\]

证明如下。令 \(\sigma=\operatorname{sgn}F_A\)，其变号跳点为 \(\theta_j\)，跳幅 \(J_j\in\{\pm2\}\)，总数为 \(r\le Z(F_A)\)。对

\[
H_A(t)=\sum_{\substack{a\in A\\a>0}}\frac{\sin(at)}a
\]

分布积分分部给出

\[
\|F_A\|_1
=\mathbf1_{0\in A}\widehat\sigma(0)
-\frac1{2\pi}\sum_jJ_jH_A(\theta_j).
\]

经典 Dirichlet--Abel 估计给

\[
\sup_{m,t}\left|\sum_{n=1}^m\frac{\sin(nt)}n\right|<\infty.
\]

所以每个整数区间对 \(H_A(t)\) 的贡献一致为 \(O(1)\)，从而

\[
\|F_A\|_1\le1+Crq(A).
\]

再用 Littlewood \(L^1\) 下界 \(\|F_A\|_1\gg\log N\) 即得结论。于是当

\[
q(A)\le\frac{\log N}{\omega(N)B(N)}
\]

时，这一分支也严格超过 Bedert；若 \(q(A)=O((\log N)^{1-\varepsilon})\)，则 \(Z(F_A)\gg(\log N)^\varepsilon\)。

高能量或小 doubling 不会推出小 \(q(A)\)：随机稠密子集可同时具有 \(E(A)\asymp N^3\) 与 \(q(A)\asymp N\)。

## 4. 统一问题的核心断点

四种表述指向同一个障碍：

\[
\boxed{
\text{结构子集或局部根数据的振荡，如何稳健地传递给完整的 }F_A？
}
\]

具体地说：

1. BSG 可从高能量中抽出小 doubling 子集，但补集可以抹掉该子和的全部载波零点。
2. 跳点 Hankel 低秩与卷积递推逐节点只重述 \(F_A(\theta_j)=0\)，不自动产生跨根抵消。
3. 单个根处的原函数不小。取
   \[
   A_N=\{1,5,\ldots,4N-3\},\qquad \theta=\pi/2,
   \]
   则 \(\theta\) 是真变号根，但
   \[
   H_A(\theta)=\sum_{k<N}\frac1{4k+1}=\frac14\log N+O(1).
   \]
4. 净绕数、单位圆内根数和 Mahler 测度被
   \[
   P_n(z)=1+z+z^3+\cdots+z^{2n-1}
   \]
   击穿；其净绕数很小，但边界辐角有大量往返。

因此下一步不能证明“每个根收费 \(O(1)\)”或“结构子集自动贡献零点”，而要证明**所有根的交错抵消**或**每个零自由弧的容量上界**。

## 5. 候选路线登记

| ID | 机制与最小目标 | 若成立导出的量级 | 第一缺口 | 状态/优先级 |
|---|---|---|---|---|
| R1 | 全局交错原函数：\(\left|\sum_jJ_jH_A(\theta_j)\right|\le e^{Cr}\) | \(Z(N)\gg\log\log N\) | 逐根界为假；必须利用跳点交错与全部根约束 | active，高 |
| R1+ | 更强地控制为 \(Cr\log(r+2)\) | \(Z(N)\gg\log N/\log\log N\) | 可能存在极少根承载几乎全部 \(L^1\) | active，高风险高收益 |
| R2 | 环带根容量：\(A_{1/4}(P)\le\exp(C(Z+1)\log(Z+2))\) | \(Z(N)\gg\log N/\log\log N\) | 需用 \(0/1\) 系数控制零自由弧背后的 Carleson box；一般解析函数为假 | active，高风险高收益 |
| R3 | Bedert 稀疏乘积项 \(q\) 的指数由 \(d\log d\) 降到 \(d\log\log d\) | \(Z(N)\gg\log\log N/\log\log\log\log N\) | 改善 Cor.4.3/Prop.4.4 的 support 数；单改 period 无收益 | active，最高可操作性 |
| R4 | 对 Bedert 特殊分块证明 \(\|\widetilde g\|_1\ll dM\log\log(K+3)\) | 同 R3 | 一般端点的 \(\log K\) 很可能临界，必须使用 support-gap 谱系 | active，中高 |
| R5 | Bloom--Green 高能大子集 + 稳健振荡传递 | 未闭合；目标至少 \(\log\log N\) | 子集零点不遗传；需控制补集在结构载波点的幅值 | active，中高 |
| R6 | 热门差分给不交对并提取 \(\cos(dx/2)\) 载波 | 未闭合 | 仅能提取次线性配对，余项可在全部载波零点占优 | active，中 |
| R7 | 自洽 Toeplitz 交换子/幂等核水平集复杂度 | 目标 \(\log N/\log\log N\) | 任意阶梯函数版本为假；必须利用 \(\sigma=\operatorname{sgn}(G-\lambda)\) | active，中 |
| R8 | 固定相位层通量的下界和 \(Z\)-only 上界 | 目标 \(\log N/\log\log N\) | Jensen 不能把通量固定到虚轴层；擦边临界点缺少 \(Z\)-only 控制 | active，中低 |

### 5.1 R2 的严格输入

把 \(P_A\) 除去 \(z^{\min A}\)，则常数项和首项均为 \(1\)。若根为 \(\alpha_j\)，定义

\[
A_\delta(P)=\#\{j:|\log|\alpha_j||\le\delta\}.
\]

由根模乘积为 \(1\) 以及

\[
\log M(P)\le\log\|P\|_2=\frac12\log N,
\]

严格得到

\[
\sum_j|\log|\alpha_j||=2\log M(P)\le\log N,
\]

从而

\[
\boxed{
A_\delta(P)\ge\deg P-\frac{\log N}{\delta}
\ge N-1-\frac{\log N}{\delta}.
}
\]

所以几乎所有根都落在固定厚度单位圆环带内。R2 只缺把环带根数用实部零点数控制的上界。

### 5.2 R3/R4 的精确参数反演

令

\[
H=\log\frac{|g(0)|}{M},\qquad X=\log H,
\qquad p(d)=\log P,quad k(d)=\log\log K.
\]

Bedert Proposition 3.1 给

\[
H\ll dMP^2\log(KP),
\]

所以

\[
X\le2p(d)+\max\{k(d),\log p(d)\}+O(\log(dM)).
\]

当前 \(p(d)=O(d\log\log d)\)、\(k(d)=O(d\log d)\)，故 \(d\gg X/\log X\)。参数结论是：

- 单独把 \(P\) 改为 \(e^{O(d)}\) 甚至常数，不改变最终量级，因为 \(K\) 仍主导。
- 把 \(K\) 改为 \(\exp\exp(O(d\log\log d))\)，即可得到 R3 的四重对数分母。
- 若同时令 \(k(d)=O(d)\) 且 \(p(d)=O(d)\)，才得到 \(Z(N)\gg\log\log N\)。
- 若结构化 \(L^1\) 的相对损失最终能压到 \(d^{O(1)}\)，才会质变为 \((\log N)^c\) 下界。

## 6. 低秩与幂等核的严格账本

若 \(\sigma\) 有跳点 \(\theta_j\)，则

\[
in\widehat\sigma(n)=\frac1{2\pi}\sum_jJ_je^{-in\theta_j}.
\]

因此 \(u_n=n\widehat\sigma(n)\) 是 \(r\) 项指数和，而且无限 Hankel 秩恰为 \(r\)：

\[
\det[u_{p+q}]_{p,q=0}^{r-1}
=\left(\prod_j\frac{J_j}{2\pi i}\right)
\prod_{j<k}(e^{-i\theta_k}-e^{-i\theta_j})^2\ne0.
\]

但跳点聚簇会使 Vandermonde 极度病态，精确秩不等于稳定有效秩。

对 \(S=A\cup(-A)\)、\(G_A=\sum_{n\in S}e^{inx}\)，有

\[
G_A*G_A=G_A.
\]

若 \(P_S\) 是 Fourier 投影，则

\[
\|[P_S,M_\sigma]\|_{HS}^2
=2\sum_{k\in\mathbb Z}|S\setminus(S+k)|\,|\widehat\sigma(k)|^2.
\]

该式精确显示普通幂等性不足：右侧依赖 \(S\) 的加法边界分布，并不只依赖 \(|S|\) 与跳点数。任意阶梯函数的小反号弧还会使交换子能量趋零，因此需要自洽符号条件。

## 7. 计算审计：只做一个实验时做什么

现有精确样本数是

\[
\sum_{n=2}^6\binom{11}{n}=1474;
\]

十个 \(\{0,m\}\) 已包含其中，不应重复记为 1484。

建立统一特征面板，并加入三类压力测试：

1. 反射集合；
2. \(q=2,3,4\) 的频率膨胀；
3. 低零点脊柱 \(\{0,1,3,\ldots,2N-3\}\)，\(N\le20\)。

每个样本记录：

\[
Z,\ r,\ \|F\|_1,\
\sum J_jH_A(\theta_j),\
E_2,\ldots,E_6,\ q(A),\
\eta_{\rm jump},\
\text{Hankel 奇异值},\
\text{Toeplitz 交换子谱}.
\]

计算规范：零点继续用有理 Sturm 链；\(L^1\) 与 \(\widehat\sigma\) 用认证根区间分段积分；Hankel/Toeplitz 用 80 位精度和双截断窗口。

硬判废阈值：

- 同一候选不变量组内 \(Z\) 比达到 \(8\)，淘汰“只依赖该不变量”的版本；现有反射对已经达到 \(9\)。
- 候选控制量在 \(Z\le4\) 样本上跨越 \(10\) 倍，淘汰其 \(Z\)-only 版本。
- Hankel 最小/最大奇异值比低于 \(10^{-10}\) 且 80 位复算稳定，淘汰稳定有效秩假设。
- Toeplitz 截断窗口扩大后变化超过 \(5\%\)，不把数值现象当证据。
- 任何只数变号根的实验必须单列 \(\{0,m\}\) 的偶重切触根。

## 8. 建议执行顺序

### 第一阶段：低成本判别与可发表分支

1. 把第 3.2 节的少区间并定理写成独立、逐行可审计的命题。
2. 建立第 7 节统一特征面板，优先搜索 R1/R1+ 的反例。
3. 对 Bedert Corollary 4.3 中非零系数数目 \(q\) 的 \(d\log d\) 来源逐项重做，目标先降为 \(d\log\log d\)。

### 第二阶段：两条主攻线

4. 主攻 R1：先证明较弱的 \(e^{Cr}\) 全局交错和，再尝试 \(Cr\log r\)。禁止退回逐根估计。
5. 并行主攻 R2：建立单个零自由弧对应的 Carleson box 根容量定理；先处理根径向分离或跳点间距有下界的特例。

### 第三阶段：高能量桥

6. 用 Bloom--Green 得到的大高能量子集，寻找“在多数真实跳点上补集不能同时抵消”的稳健传递引理。
7. 若该桥失败，再转向 R7 的自洽 Toeplitz 交换子，而不是普通 BV 或任意阶梯函数不确定性。

## 9. 最终判定

本轮没有新的统一下界，不能声称解决或刷新纪录。最强的严格推进是：

1. 明确了所有固定阶能量下的纪录提升阈值；
2. 得到 \(Z(F_A)\gg\log N/q(A)\) 的少整数区间分支；
3. 把统一问题的共同缺口压缩为“全局交错抵消/零自由弧容量/结构子集到完整和的稳健传递”；
4. 给出一条最小可见的 Bedert 参数改进，目标为四重对数分母；
5. 给出能一次性判废六类朴素路线的统一计算实验。

