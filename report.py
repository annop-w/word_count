try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

def plot_top_words(top_words):

    if (HAS_MATPLOTLIB):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif', weight='bold')
        plt.rc('axes', linewidth=2)

        fig = plt.figure(figsize=(8,6))

        ax = fig.add_subplot(1,1,1)

        ax.tick_params(axis='both',which='both',labelsize=20)
        ax.yaxis.set_tick_params(labelsize=20)
        ax.set_xlabel(r'Frequency',fontsize=20)
        ax.set_title(r'10 most frequent words',fontsize=25)

        word = [x[0] for x in top_words]
        freq = [x[1] for x in top_words]
        ax.barh(word, freq, height=0.35)

        plt.gca().invert_yaxis()
        fig.savefig('report.pdf',bbox_inches='tight')

    print('10 most frequent words')
    for w in top_words:
        print(w[0] , w[1])
        
