import matplotlib.pyplot as plt

def create_scatter_plot(linkedlist_timings, staticarray_timings):
    indices = list(range(len(linkedlist_timings)))
    plt.scatter(indices, linkedlist_timings, color='blue', label='Linked List')
    plt.scatter(indices, staticarray_timings, color='red', label='Static Array')
    plt.xlabel('Call Number')
    plt.ylabel('Execution Time (ms)')
    plt.ylim(bottom=0,top=1)
    plt.title('Scatter Plot')
    plt.legend()
    plt.show()