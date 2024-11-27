import numpy as np

type GraphicType = tuple[
    int,
    tuple[int, int, int, int],
    tuple[int, int, int, int],
]

graphic_dtype = np.dtype(
    [
        ("ch", np.intc),
        ("fg", "(4,)u1"),
        ("bg", "(4,)u1"),
    ],
)
