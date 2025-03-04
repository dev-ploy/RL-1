import matplotlib.pyplot as plt
from IPython import display
import numpy as np

plt.ion()
def plot(scores, mean_scores):
    display.clear_output(wait=True)
    plt.close()
    fig,ax=plt.subplots(figsize=(10,5))
    plt.figure(figsize=(10, 5))
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Scores')
    plt.plot(scores, label='Score')
    plt.plot(mean_scores, label='Mean Score')
    
    # Adding a moving average for smoother visualization
    if len(scores) > 10:
        moving_avg = np.convolve(scores, np.ones(10)/10, mode='valid')
        ax.plot(range(9, len(scores)), moving_avg, label='Moving Average (10 games)')
    
    ax.set_ylim(ymin=0)
    ax.text(len(scores)-1, scores[-1], str(scores[-1]))
    ax.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    ax.legend()
    ax.grid(True)
    plt.show()
    display.display(fig)