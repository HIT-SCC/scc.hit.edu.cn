# 并行计算基础

## 什么是并行计算

![image-20240809154342495](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\image-20240809154342495.png)

## 应用领域

计算气动声学、流体力学、电磁学；生物基因领域；机器学习；数字媒体；气象领域；天文物理；油气模拟等。

## 并行计算机体系结构

![image-20240809155102575](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\image-20240809155102575.png)

## 并行程序设计基础

### 串行算法并行化

#### 例1.求和方法进行数值积分

$$
\int f(x) \approx \sum_{i=0}^{N-1} \left(b-a\right) f\left(\frac{i(b-a)}{N} + a + 0.5\right),
$$

![image-20240809161552338](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\image-20240809161552338.png)

#### 例2.Floyd并行算法

分块思想，参考[求最短路径Floyd算法的并行化（解APSP问题）-CSDN博客](https://blog.csdn.net/kissgoodbye2012/article/details/107499354)

