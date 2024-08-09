.. _header-n0:

并行计算基础
============

.. _header-n2:

什么是并行计算
--------------

.. image:: /images/mod_yuhy/pcam/image-20240809154342495.png
   :align: center

.. _header-n4:

应用领域
--------

计算气动声学、流体力学、电磁学；生物基因领域；机器学习；数字媒体；气象领域；天文物理；油气模拟等。

.. _header-n6:

并行计算机体系结构
------------------

|image2|

.. _header-n8:

并行程序设计基础
----------------

.. _header-n9:

串行算法并行化
~~~~~~~~~~~~~~

.. _header-n10:

例1.求和方法进行数值积分
^^^^^^^^^^^^^^^^^^^^^^^^

.. math:: \int f(x) \approx \sum_{i=0}^{N-1} \left(b-a\right) f\left(\frac{i(b-a)}{N} + a + 0.5\right),

|image3|

.. _header-n13:

例2.Floyd并行算法
^^^^^^^^^^^^^^^^^

分块思想，参考\ `求最短路径Floyd算法的并行化（解APSP问题）-CSDN博客 <https://blog.csdn.net/kissgoodbye2012/article/details/107499354>`__

.. _header-n27:

从问题描述开始设计并行算法
~~~~~~~~~~~~~~~~~~~~~~~~~~

|image4|

.. _header-n40:

借用已有算法求解新问题
~~~~~~~~~~~~~~~~~~~~~~

|image5|

.. _header-n45:

并行程序性能评价
----------------

.. _header-n47:

加速比
~~~~~~

|image6|

.. _header-n49:

Amdahl定律
~~~~~~~~~~

|  Amdahl定律定义了串行程序并行化后加速比计
| 算公式与理论上限。

f 表示程序中不可以被并行化的部分所占的比例。

|image7|

.. _header-n58:

Gustafson定律
~~~~~~~~~~~~~

|  研究在给定的时间内用不同数目的处理器能够完
| 成多大的计算量是并行计算中一个很实际的问题。

|image8|

.. _header-n69:

时间复杂度
~~~~~~~~~~

|image9|

.. _header-n71:

示例
^^^^

|image10|

.. |image1| image:: /images/mod_yuhy/pcam/image-20240809154342495.png
.. |image2| image:: /images/mod_yuhy/pcam/image-20240809155102575.png
.. |image3| image:: /images/mod_yuhy/pcam/image-20240809161552338.png
.. |image4| image:: /images/mod_yuhy/pcam/image-20240809192512773.png
.. |image5| image:: /images/mod_yuhy/pcam/image-20240809193553135.png
.. |image6| image:: /images/mod_yuhy/pcam/image-20240809194543692.png
.. |image7| image:: /images/mod_yuhy/pcam/image-20240809194628969.png
.. |image8| image:: /images/mod_yuhy/pcam/image-20240809195002246.png
.. |image9| image:: /images/mod_yuhy/pcam/image-20240809195209755.png
.. |image10| image:: /images/mod_yuhy/pcam/image-20240809195232456.png
