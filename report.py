try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

def plot_top_words(top_words):

    if (HAS_MATPLOTLIB):
        plt.rc('font', family='serif', weight='bold')
        plt.rc('axes', linewidth=2)

        fig = plt.figure(figsize=(10,6))

        ax = fig.add_subplot(1,1,1)

        ax.tick_params(axis='both',which='both',labelsize=20)
        ax.yaxis.set_tick_params(labelsize=20)
        ax.set_title('10 most frequent words',fontsize=25,weight='bold')
        ax.xaxis.set_tick_params(rotation=30)
        ax.set_xlabel('Frequency',fontsize=20,weight='bold')

        word = [x[0] for x in top_words]
        freq = [x[1] for x in top_words]

        ax.barh(range(len(word)),freq,height=0.5,edgecolor='k')
        plt.yticks(range(len(word)),word)
            
        plt.gca().invert_yaxis()
        fig.savefig('report.pdf',bbox_inches='tight')

    print('----------------------')
    print('10 most frequent words')
    print('----------------------')
    for w in top_words:
        print(w[0] , w[1])
    print('----------------------')
        
