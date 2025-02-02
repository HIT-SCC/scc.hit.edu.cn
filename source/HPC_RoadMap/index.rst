=====================
高性能计算学习路线
=====================

**学习路线**
--------------------------------


**并行编程**
~~~~~~~~~~~~~~~~~~
- **课程简介** 

这门课程将带你深入理解现代并行计算的模型和方法。课程涵盖科学应用中的并行性概述，以及线性代数、粒子计算、网格计算、排序、FFT、图算法和机器学习等领域的并行算法研究。同时，课程还将介绍各种并行计算机及其结构，包括共享内存和分布式内存的并行计算机、GPU 和云平台。你将学习并行编程语言、编译器、库和工具箱的使用，数据分区技术以及同步和负载平衡的技巧。课程还会对中型应用程序进行详细研究和算法/程序开发。

总的来讲是对并行算法和并行编程比较全面的介绍。

- **课程资源**

`cs267-UCB(C/C++) <https://www2.eecs.berkeley.edu/Courses/CSC267/>`_

`CMU15-418(C++) <https://www.cs.cmu.edu/~15418/schedule.html>`_

**并发编程**
~~~~~~~~~~~~~~~~~~

- **课程简介**

这门课程专注于并行和并发编程的理论与实践，解决在大规模并行系统中出现的挑战。随着Dennard scaling和Moore's Law的终结，提升计算机性能越来越依赖于专用化和并行化。

并行计算中的核心难题是如何有效管理共享可变状态，这是多核同步与并发控制的关键。本课程将探讨共享可变状态理论的最新进展，并将这些理论应用于实际系统设计与实现。

课程目标是帮助学生掌握并发编程的动机、设计模式及在现实系统中的应用。

**前置要求**:rust语言(可参照以下链接)

`Rust语言圣经(Rust Course) <https://course.rs/about-book.html>`_

- **课程资源**

`cs431-kaist(Rust) <https://github.com/kaist-cp/cs431>`_


**系统优化**
~~~~~~~~~~~~~~~~~~
- **课程简介** 

本课程专注于构建高性能和可扩展软件系统，涵盖了多项与性能优化相关的关键技术，包括性能分析、高性能算法设计、指令级优化、缓存优化和并行编程。

同时本课程将学习如何通过深入分析代码性能，找到瓶颈并应用优化技术来提升程序效率。课程还涉及构建大规模可扩展系统的挑战和解决方法，帮助掌握处理复杂软件系统的能力。

- **课程资源**

`MIT6.172(C) <https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/>`_


**开源项目（copy from Hongyu Zhang）**
~~~~~~~~~~~~~~

算法导论的习题解答：https://github.com/walkccc/CLRS

CSAPP的习题解答：https://github.com/DreamAndDead/CSAPP-3e-Solutions

数值分析算法的实现：https://github.com/lonelyprince7/NumericalAnalysis

Nvidia的CUDA优化官方样例：https://github.com/NVIDIA/cuda-samples

MIT 6.828的Lab：https://github.com/SmallPond/MIT6.828_OS

CMU 15-213的Lab：https://github.com/JonnyKong/CMU-15-213-Intro-to-Computer-Systems

2020年的CPC决赛赛题－基于太湖之光平台的通用型网格计算方法：https://github.com/lonelyprince7/Grid-Computing

2020年的CPC初赛赛题－基于太湖之光超算平台与MPI集群的的分布式图BFS算法：https://github.com/lonelyprince7/DistributedBFS

2019年的CPC初赛赛题－基于神威·太湖之光超算平台的模板卷积运算优化：https://github.com/lonelyprince7/Stencil

CUDA矩阵乘法的优秀开源实现：https://github.com/NVIDIA/cutlass

CUDA矩阵分解算法的优秀开源实现：https://github.com/cuMF/cumf_als

基于C++的迷你深度学习框架实现：https://github.com/E1eveNn/xshinnosuke_cpp

基于Intel平台的深度学习算子优化：https://github.com/PasaLab/dolphin

OpenMP实现的一个异步坐标更新算法，想优化深度学习底层架构的同学可以看看：https://github.com/ZhiminPeng/ARock

和上面一样，也是一个分布式优化算法项目：https://github.com/uclaopt/TMAC


学术社区
~~~~~~~~~~~~~~~~~~
- MICRO、ISCA、ASPLOS和HPCA等四个CCF A类会议并称计算机体系结构领域的四大国际学术会议。MICRO是四大会议中历史最悠久的。自1968年创办以来，55届MICRO会议总共收录论文1900余篇。
- 历史上，中国大陆机构仅有两次获得四大会议的最佳论文奖（十年前），分别是ASPLOS 2014（DianNao）和MICRO 2014（DaDianNao），都是由中科院计算所智能处理器团队获得。
- 相信后人的智慧（）
- 注意：
- 更新，在2024年内地北京大学与香港科技大学(广州)分别获得2024 ASPLOS最佳论文奖，本次会议共收录文章170篇，录取率为18.4%，共评出6篇最佳论文（占录取论文的3.5%）。


**本文作者：** ycy

**联系方式：** chenyuy001@gmail.com

**版权声明：** 欢迎对文章内容进行转载，但请注明出处