# Chapter 11 : Image and Audio Processing

In this chapter, we will cover the following topics:

* [11.1. Manipulating the exposure of an image](01_exposure.md)
* [11.2. Applying filters on an image](02_filters.md)
* [11.3. Segmenting an image](03_segmentation.md)
* [11.4. Finding points of interest in an image](04_interest.md)
* [11.5. Detecting faces in an image with OpenCV](05_faces.md) *
* [11.6. Applying digital filters to speech sounds](06_speech.md)
* [11.7. Creating a sound synthesizer in the Notebook](07_synth.md)

In the previous chapter, we covered signal processing techniques for one-dimensional, time-dependent signals. In this chapter, we will see signal processing techniques for images and sounds.

Generic signal processing techniques can be applied to images and sounds, but many image or audio processing tasks require specialized algorithms. For example, we will see algorithms for segmenting images, detecting points of interest in an image, or detecting faces. We will also hear the effect of linear filters on speech sounds.

**scikit-image** is one of the main image processing packages in Python. We will use it in most of the image processing recipes in this chapter. For more on scikit-image, refer to http://scikit-image.org.

We will also use **OpenCV** (http://opencv.org), a computer vision library in C++ that has a Python wrapper.

In this introduction, we will discuss the particularities of images and sounds from a signal processing point of view.

## Images

A **grayscale image** is a bidimensional signal represented by a function, $f$, that maps each pixel to an **intensity**. For example, the intensity could be a real value between 0 (dark) and 1 (light). In a colored image, this function maps each pixel to a triplet of intensities, generally, the **red, green, and blue (RGB) components**.

On a computer, images are digitally sampled. The intensities are not real values, but integers or floating point numbers. On one hand, the mathematical formulation of continuous functions allows us to apply analytical tools such as derivatives and integrals. On the other hand, we need to take into account the digital nature of the images we deal with.

## Sounds

From a signal processing perspective, a sound is a time-dependent signal that has sufficient power in the hearing frequency range (about 20 Hz to 20 kHz). Then, according to the Nyquist-Shannon theorem (introduced in *Chapter 10, Signal Processing*), the sampling rate of a digital sound signal needs to be at least 40 kHz. A sampling rate of 44100 Hz is frequently chosen.

## References

Here are a few references:

* Image processing on Wikipedia, available at https://en.wikipedia.org/wiki/Image_processing
* Numerical Tours, advanced image processing algorithms available at http://www.numerical-tours.com/python/
* Audio signal processing on Wikipedia, available at https://en.wikipedia.org/wiki/Audio_signal_processing
* Particularities of the 44100 Hz sampling rate explained at https://en.wikipedia.org/wiki/44,100_Hz
