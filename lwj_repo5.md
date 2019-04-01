# 第五次作业

廖沩健

自动化65

2160504124

提交日期:  2019年4月1日

摘要:

这次作业聚焦于频域高低通滤波处理，低通滤波器选用了ButterWorth滤波器和高斯滤波器，二者的半径都设为了300和30进行比较。发现在同样的半径下,高斯滤波器的低通特性更佳.高通滤波同样选择了二者，前者半径取了5和20两个值,后者取了5和100两个值,相反地,ButterWorth在同样半径下高通特性更佳。高通滤波器还选择了laplace和unmask_sharpen.效果较为不错。其中所有的算法除快速傅里叶变换外都是用python从头实现的，使用到的库主要有numpy,cv2等。大部分参考的都是课本与ppt的内容。对于所有处理结果的讨论，都展示在下面的对应的部分。



在以下的代码实现过程，不同于书上的过程，我首先对源图像padding，做FFT，然后是在频域做的中心化操作，而课本中是在空域做的。
## 频域低通滤波
### ButterWorth滤波

#### test1
#### 半径:30
#### 功率谱比：0.9444


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.pgm_butterworth30_0.944390390105.bmp)


#### test2
#### 半径:30
#### 功率谱比：0.9603

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.tif_butterworth30_0.960310027477.bmp)




#### test1
#### 半径:300
##### 功率谱比：0.9990


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.pgm_butterworth300_0.998965793875.bmp)


#### test2
#### 半径:300
##### 功率谱比：0.9956

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.tif_butterworth300_0.995627975903.bmp)



### Gaussian滤波

#### test1
#### 半径:30
#### 功率谱比：0.7550


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.pgm_gaussian30_0.754951915127.bmp)


#### test2
#### 半径:30
#### 功率谱比：0.8417

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.tif_gaussian30_0.841682319425.bmp)




#### test1
#### 半径:300
##### 功率谱比：0.8927


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.pgm_gaussian300_0.892724715286.bmp)


#### test2
#### 半径:300
##### 功率谱比：0.9311

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.tif_gaussian300_0.931147093254.bmp)


由以上结果，可以发现，随着半径增大，功率谱逐渐接近1,图像变得越来越模糊；在同样的半径下，高斯滤波器的低通效果更加显著，并且，对于背景中＂白点＂的消除效果也更好。

## 空域高通滤波
### ButterWorth滤波

#### test3
#### 半径:5
#### 功率谱比：0.1789


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3_corrupt.pgm_butterworth5_0.178922591317.bmp)


#### test4
#### 半径:5
#### 功率谱比：0.1393

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.tif_butterworth5_0.13934563406.bmp)




#### test3
#### 半径:20
##### 功率谱比：0.0257


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3_corrupt.pgm_butterworth20_0.0257001792117.bmp)


#### test4
#### 半径:25
##### 功率谱比：0.0335

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.tif_butterworth25_0.0334853577091.bmp)

### Gaussian滤波

#### test3
#### 半径:5
#### 功率谱比：0.3982


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3_corrupt.pgm_gaussian5_0.398181815677.bmp)


#### test4
#### 半径:5
#### 功率谱比：0.2403

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.tif_gaussian5_0.24030288771.bmp)


#### test3
#### 半径:100
##### 功率谱比：0.0633


![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3_corrupt.pgm_gaussian100_0.063324547816.bmp)


#### test4
#### 半径:100
##### 功率谱比：0.0708

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.tif_gaussian100_0.070787175512.bmp)

由以上结果可知，随着半径的增大，功率谱比越来越小，图像的轮廓会越来越清晰，但同时由于滤除的频率分量过多，会使图像变得越来越暗；在同样的半径条件下，Butterworth的滤波效果更好。
### Laplace滤波
#### test3
##### 功率谱比:0.0516

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3_corrupt.pgm_laplace_384170528.941.bmp)

#### test4
##### 功率谱比:0.0045

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.tif_laplace_65781111892.8.bmp)

### Unmask_sharpen
#### test3
##### 功率谱比:0.0516

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3_corrupt.pgm_unmask_sharpen_384176478.733.bmp)

#### test4
##### 功率谱比:0.0045

![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.tif_unmask_sharpen_65781147722.6.bmp)

由以上结果，我们可以看到，laplace的滤波效果是不错的，特别是在房子的那张图中，比较准确地提取出了轮廓，而没有附带中间的图像信息。这里还需要说明的一点是，由于通过laplace做出的结果会使得图像数据变得非常大，为了仍然能使用8-bit表示，我对卷积后的结果做了max-min的归一化处理，然后scale到0-255的范围。


## 讨论空域低通高通滤波（Project3）与频域低通和高通的关系:
空间域和频域滤波间的纽带是卷积定理。空间域中的滤波定义为滤波函数h(x,y)与输入图像f(x,y)进行卷积；频率域中的滤波定义为滤波函数H(u,v)与输入图像的傅里叶变换F(u,v)进行相乘。空间域的滤波器和频率域的滤波器互为傅里叶变换。
频域增强技术与空域增强技术有密切的联系。一方面，许多空域增强技术可借助频域概念来分析和帮助设计；另一方面，许多空域增强技术可转化到频域实现，而许多频域增强技术可转化到空域实现。空域滤波主要包括平滑滤波和锐化滤波。平滑滤波是要滤除不规则的噪声或干扰的影响，从频域的角度看，不规则的噪声具有较高的频率，所以可用具有低通能力的频域滤波器来滤除。由此可见空域的平滑滤波对应频域的低通滤波。锐化滤波是要增强边缘和轮廓处的强度，从频域的角度看，边缘和轮廓处都具有较高的频率，所以可用具有高通能力的频域滤波器来增强。由此可见，空域的锐化滤波对应频域的高通滤波。频域里低通滤波器的转移函数应该对应空域里平滑滤波器的模板函数的傅里叶变换。频域里高通滤波器的转移函数应该对应空域里锐化滤波器的模板函数的傅里叶变换。即空域和频域的滤波器组成傅里叶变换对。给定一个域内的滤波器，通过傅里叶变换或反变换得到在另一个域内对应的滤波器。 空域的锐化滤波或频域的高通滤波可用两个空域的平滑滤波器或两个频域的低通滤波器实现。在频域中分析图像的频率成分与图像的视觉效果间的对应关系比较直观。空域滤波在具体实现上和硬件设计上有一定优点。区别：例如，空域技术中无论使用点操作还是模板操作，每次都只是基于部分像素的性质，而频域技术每次都利用图像中所有像素的数据，具有全局性，有可能更好地体现图像的整体特性，如整体对比度和平均灰度值等。