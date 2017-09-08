#ifndef DARKNET_API
#define DARKNET_API
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include "meta.h"

#ifdef GPU
    #include "cuda_runtime.h"
    #include "curand.h"
    #include "cublas_v2.h"

    #ifdef CUDNN
    #include "cudnn.h"
    #endif
#endif

#ifndef __cplusplus
    #ifdef OPENCV
    #include "opencv2/highgui/highgui_c.h"
    #include "opencv2/imgproc/imgproc_c.h"
    #include "opencv2/core/version.hpp"
    #if CV_MAJOR_VERSION == 3
    #include "opencv2/videoio/videoio_c.h"
    #endif
    #endif
#endif

#ifdef CUDNN
typedef struct layercudnn {
    cudnnTensorDescriptor_t srcTensorDesc, dstTensorDesc;
    cudnnTensorDescriptor_t dsrcTensorDesc, ddstTensorDesc;
    cudnnTensorDescriptor_t normTensorDesc;
    cudnnFilterDescriptor_t weightDesc;
    cudnnFilterDescriptor_t dweightDesc;
    cudnnConvolutionDescriptor_t convDesc;
    cudnnConvolutionFwdAlgo_t fw_algo;
    cudnnConvolutionBwdDataAlgo_t bd_algo;
    cudnnConvolutionBwdFilterAlgo_t bf_algo;
} layercudnn;
#endif

#endif
