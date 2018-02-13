from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob


def damped_vibrations(t, A, b, w):
    return A * exp(-b * t) * cos(w * t)


def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution + 1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, u)
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))
    abspath = os.path.abspath(os.path.dirname(__file__))
    static_dir = os.path.join(abspath, 'static')
    temp_file_dir = os.path.join(static_dir, 'temp_file')
    if not os.path.isdir(static_dir):
        os.mkdir(static_dir)
    if not os.path.isdir(temp_file_dir):
        os.mkdir(temp_file_dir)
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join(temp_file_dir, '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join(temp_file_dir, str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile


if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))
