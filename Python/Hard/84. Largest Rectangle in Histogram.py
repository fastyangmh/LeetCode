# import
from src.parameters import Options
import torch
import librosa
from os.path import isfile, join
import pandas as pd
from scipy.signal import butter, lfilter
import numpy as np
from librosa.display import specshow
import matplotlib.pyplot as plt
from glob import glob
from tqdm import tqdm

# def


def load_wav(file_path, sr):
    """Load wav from the file path, if exist the wav time label, will load it then use time label to segment the wav.

    Args:
        file_path (str): the file path.
        sr (int): the sample rate of the wav data.

    Returns:
        list: the wav data.
    """
    y, _ = librosa.load(path=file_path, sr=sr)
    if isfile(file_path[:-3]+'txt'):
        df = pd.read_csv(file_path[:-3]+'txt', sep='\t',
                         names=['start', 'end', 'none'])
        new_y = []
        for v in df.iloc[::2].values:
            st = int(sr*float(v[0]))
            ed = int(sr*float(v[1]))
            new_y.append(y[st:ed])
        y = new_y
    y = y if type(y) is list else [y]
    return y


def butter_filter(y, sr, btype, freqcut, order=5):
    """The butter filter which has different filters according to the btype.

    Args:
        y (numpy array): the wav data which wanted to be filtered.
        sr (int): the sample rate of the wav data.
        btype (str): the type of filter which has high, low, band.
        freqcut (list or int): the cutoff frequency.
        order (int, optional): the order of the filter. Defaults to 5.

    Returns:
        numpy array: the filterd wav data.
    """
    nyq = 0.5*sr
    freqcut = [v/nyq for v in freqcut]
    b, a = butter(N=order, Wn=freqcut, btype=btype)
    y = lfilter(b, a, y).astype(np.float32)
    return y


def wav2stft(y, sr, n_fft, framesize, overlap):
    """Convert the wav data to short-time Fourier transform.

    Args:
        y (numpy array): the wav data.
        sr (int): the sample rate of the wav data.
        n_fft (int): the FFT length.
        framesize (float or int): the frame size.
        overlap (float or int): the overlap in each frame.

    Returns:
        tuple: the tuple contains stft.
    """
    if type(framesize) == float and type(overlap) == float:
        framesize = int(sr*framesize)
        overlap = int(sr*overlap)
    step = framesize-overlap
    # the stft dimension is (1+n_fft/2, n_frames)
    stft = np.abs(librosa.stft(y=y, n_fft=n_fft,
                               hop_length=step, win_length=framesize))
    stft = librosa.amplitude_to_db(S=stft, ref=1)
    return stft


def stft2image(file_path, stft, sr, step):
    """Save the stft feature to image based on each frame.

    Args:
        file_path (str): the file path.
        stft (numpy array): the short-time Fourier transform feature.
        sr (int): the sample rate of the wav data.
        step (float or int): the hop length.
    """
    if type(step) == float:
        step = int(sr*step)
    for idx in range(stft.shape[-1]):
        specshow(stft[:, idx].reshape(-1, 1), sr=sr, hop_length=step)
        plt.axis('off')
        img_path = file_path[:-4]+'_{0:05d}.png'.format(idx+1)
        plt.savefig(img_path, pad_inches=0, bbox_inches='tight')
        plt.close()


def wav2image(typ, data_path, sr, btype, freqcut, n_fft, framesize, overlap):
    """This function will get data from the data path and save as an image.

    Args:
        typ (dict): the dictionary contains each class and label.
        data_path (str): the data path.
        sr (int): the sample rate of the wav data.
        btype (str): the type of filter which has high, low, band.
        freqcut (list): the cutoff frequency.
        n_fft (int): the FFT length.
        framesize (float or int): the frame size.
        overlap (float or int): the overlap in each frame.
    """
    for ty, v in typ.items():
        files = sorted(glob(join(data_path, ty+'/*.wav')))
        # if there are no files, will pass this type
        if not len(files):
            continue
        wav_list, stft_list = [], []
        print('Load {} data'.format(ty))
        for file_path in tqdm(files):
            if len(glob(file_path[:-4]+'_*.png')):
                continue
            for y in load_wav(file_path=file_path, sr=sr):
                y = butter_filter(y=y, sr=sr, btype=btype,
                                  freqcut=freqcut)
                stft = wav2stft(y=y, sr=sr, n_fft=n_fft,
                                framesize=framesize, overlap=overlap)
                stft2image(file_path=file_path, stft=stft,
                           sr=sr, step=framesize-overlap)


if __name__ == "__main__":
    # parameters
    typ = ['normal', 'crackle', 'wheeze', 'rhonchi']
    typ = {k: v for v, k in enumerate(typ)}
    opt = Options().parse()
    data_path = opt.datapath
    sr = opt.sr
    btype = opt.filter
    freqcut = opt.freqcut
    n_fft = opt.nfft
    framesize = opt.framesize
    overlap = opt.overlap
    batchsize = opt.batchsize
    use_cuda = torch.cuda.is_available() and not opt.nocuda

    # test
    wav2image(typ=typ, data_path=data_path, sr=sr, btype=btype,
              freqcut=freqcut, n_fft=n_fft, framesize=framesize, overlap=overlap)