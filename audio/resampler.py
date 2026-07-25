import numpy as np


TARGET_RATE = 48000


def resample(data, fs):

    if fs == TARGET_RATE:

        return data


    duracion = len(data) / fs

    muestras = int(
        duracion * TARGET_RATE
    )


    viejo = np.linspace(
        0,
        1,
        len(data)
    )


    nuevo = np.linspace(
        0,
        1,
        muestras
    )


    if data.ndim == 1:

        return np.interp(
            nuevo,
            viejo,
            data
        ).astype(np.float32)


    canales = []

    for c in range(data.shape[1]):

        canales.append(

            np.interp(
                nuevo,
                viejo,
                data[:, c]
            )

        )

    return np.stack(
        canales,
        axis=1
    ).astype(np.float32)