import pandas as pd

import matplotlib.pyplot as plt

def plot_yearly_data(data: pd.DataFrame, label_delta_x: int, label_delta_y: float, discharge=False):
    x_max = data.idxmax()
    y_max = data[x_max]
    label = label = f"Año: {x_max}\n"
    if discharge:
        label += f"Q: {y_max:.0f} m$^3$/s"
    else:
        label += f"P: {y_max:.0f} mm"

    fig, ax = plt.subplots()
    ax.plot(data.index, data, marker="o")
    ax.annotate(
        text=label,
        xy=(x_max, y_max),
        xytext=(x_max + label_delta_x, y_max + label_delta_y),
        arrowprops={"arrowstyle": "<|-"},
        bbox={"boxstyle": "round", "facecolor": "white", "edgecolor": "black"},
    )
    ax.grid(ls="--", alpha=0.50)
    ax.set_xlabel("Año")
    if discharge:
        ax.set_ylabel("Caudal Máx. Anual en 24 h (m$^3$/s)")
    else:
        ax.set_ylabel("Precip. Máx. Anual en 24 h (mm)")
    return fig, ax
