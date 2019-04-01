# -*- coding: UTF-8 -*-  
#廖沩健
#自动化65
#2160504124

from __future__ import print_function, division
import numpy as np
import cv2
import math

def load_file(file):
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    return img

def dft(img):
    fimg = np.fft.fft2(img)
    fshiftimg = np.fft.fftshift(fimg)
    return fshiftimg

def idft(img):
    img = np.fft.ifftshift(img)
    img = np.abs(np.fft.ifft2(img))
    return img

def extract_from_padded(img, m, n):
    return img[:m, :n]

def form_padded_img(img):
    return np.pad(img, (0,img.shape[0]), 'constant')

def filtering(img, kernel):
    return np.multiply(img, kernel)

def center_distance_matrix(img):
    centerX = img.shape[0] / 2
    centerY = img.shape[1] / 2
    cdm = np.zeros_like(img, dtype=np.float)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            cdm[i,j] = np.sqrt((i - centerX) ** 2 + (j - centerY) ** 2)
    return cdm

def butterworth_kernel(cdm, n, D0, type='LOW'):
    d = cdm.astype(np.complex)
    h = 1 / ((d / D0) ** (2*n) + 1)
    if type == 'LOW':
        return h
    else:
        return 1 - h

def gaussian_kernel(cdm, sigma, type='LOW'):
    d = cdm.astype(np.complex)
    h = np.exp(-d**2 / (2*sigma))
    if type == 'LOW':
        return h
    else:
        return 1 - h

def laplace_kernel(cdm):
    d = cdm.astype(np.complex)
    return 1 + 4 * (math.pi ** 2) * (d ** 2)

def unmask_sharpen(kernel, k=1):
    return 1 + k * kernel

def power_spectrum(x):
    ps = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            realX = np.real(x[i,j])
            imagX = np.imag(x[i,j])
            ps += realX ** 2 + imagX ** 2
    return ps

def main(name, method, *args):
    img = load_file(name)
    h, w = img.shape
    F = dft(form_padded_img(img))
    cdm = center_distance_matrix(F)
    print('method:{}===========\n'.format(method))
    if method == 'butterworth':
        H = butterworth_kernel(cdm, args[0], args[1], type=args[2])
        print('n:{}, D0:{}, type:{}'.format(args[0], args[1], args[2]))
        img_name = name+str('_')+method+str(args[1])

    elif method == 'gaussian':
        H = gaussian_kernel(cdm, args[0], type=args[1])
        print('sigma:{}, type:{}'.format(args[0], args[1]))
        img_name = name+str('_')+method+str(args[0])

    elif method == 'laplace':
        H = laplace_kernel(cdm)
        img_name = name+str('_')+method

    elif method == 'unmask_sharpen':
        H = laplace_kernel(cdm)
        H = unmask_sharpen(H)
        print('kernel: {}'.format('laplace'))
        img_name = name+str('_')+method

    G = filtering(F, H)
    res = extract_from_padded(idft(G), h, w)
    #uncomment the following tow line  when playing laplace
    # res = (res - np.min(res)) / (np.max(res) - np.min(res)) * 255
    # G = dft(form_padded_img(res))
    ratio = power_spectrum(G) / power_spectrum(F)

    cv2.imwrite('./res/{}.bmp'.format(img_name+'_'+str(ratio)), res)
    print('finish {}\n'.format(name))

if __name__ == '__main__':
    main('test1.pgm', 'butterworth', 2, 300, 'LOW')
    main('test1.pgm', 'butterworth', 2, 30, 'LOW')
    main('test1.pgm', 'gaussian', 300, 'LOW')
    main('test1.pgm', 'gaussian', 30, 'LOW')

    main('test2.tif', 'butterworth', 2, 300, 'LOW')
    main('test2.tif', 'butterworth', 2, 30, 'LOW')
    main('test2.tif', 'gaussian', 300, 'LOW')
    main('test2.tif', 'gaussian', 30, 'LOW')

    main('test3_corrupt.pgm', 'butterworth', 2, 5, 'HIGH')
    main('test3_corrupt.pgm', 'butterworth', 2, 20, 'HIGH')
    main('test3_corrupt.pgm', 'gaussian', 5, 'HIGH')
    main('test3_corrupt.pgm', 'gaussian', 100, 'HIGH')

    main('test4.tif', 'butterworth', 2, 5, 'HIGH')
    main('test4.tif', 'butterworth', 2, 25, 'HIGH')
    main('test4.tif', 'gaussian', 5, 'HIGH')
    main('test4.tif', 'gaussian', 100, 'HIGH')

    # main('test3_corrupt.pgm', 'laplace')
    # main('test3_corrupt.pgm', 'unmask_sharpen')

    # main('test4.tif', 'laplace')
    # main('test4.tif', 'unmask_sharpen')



    
    






