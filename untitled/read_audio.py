import librosa
import numpy as np


def wav2mfcc(file_path,max_length=1500):
    wave, sr = librosa.load(file_path, mono=True,sr=20000,)
    mfcc = librosa.feature.mfcc(wave, sr=sr,n_mfcc=40)
    mfcc = np.pad(mfcc, ((0,0), (0, max_length-len(mfcc[0]))), mode='constant', constant_values=0)
    return mfcc