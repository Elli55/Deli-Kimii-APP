import sys
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.ticker import FuncFormatter
from . import finance
from . import doing
from pathlib import Path





if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent.parent

def set_data_dir_gr(new_base):
    global EXPENSE_DIR, INCOME_DIR, DEBIT_DIR

    doing.DATA_DIR = Path(new_base)
    EXPENSE_DIR = doing.DATA_DIR/ 'expenses.csv'
    INCOME_DIR = doing.DATA_DIR / 'income.csv'
    DEBIT_DIR = doing.DATA_DIR/ 'debt.csv'

    

def get_exp_graph_datas():
    total_cotegory = {}
    if finance.EXPENSE_DIR.exists():

        with open(finance.EXPENSE_DIR, 'r', newline='', encoding='utf-8') as f:

            reader = csv.DictReader(f)
            for line in reader:

                cat = line.get(finance._category)
                amount = line.get(finance._amount)
                if cat in total_cotegory:
                    total_cotegory[cat] += float(amount)
                else:    
                    total_cotegory[cat] = float(amount)

        
    return list(total_cotegory.keys()), list(total_cotegory.values())






def create_exp_bar_chart_widget(categories, values):
    if not categories or not values:
        return None

    fig = Figure(figsize=(8, 4), dpi=100)
    fig.patch.set_facecolor('#0b2b1b')
    canvas = FigureCanvasQTAgg(fig)

    ax = fig.add_subplot(111)
    ax.set_facecolor('#041e10')
    ax.tick_params(colors='#d8e6df')
    ax.yaxis.label.set_color('#d8e6df')
    ax.xaxis.label.set_color('#d8e6df')
    ax.title.set_color('#ffffff')

    bars = ax.bar(
        categories,
        values,
        color='#795100',
        width=0.6
    )

    ax.set_ylabel('Məbləğ (AZN)', fontsize=11)
    ax.set_xlabel('Kateqoriya', fontsize=11)
    ax.set_title('Xərclərin kateqoriyalar üzrə bölgüsü', fontsize=13, pad=12)

    ax.tick_params(axis='x', rotation=45, labelsize=9)
    ax.tick_params(axis='y', labelsize=9)

    ax.grid(axis='y', linestyle='--', alpha=0.3)

    ax.yaxis.set_major_formatter(
        FuncFormatter(lambda x, _: f'{int(x):,} AZN')
    )

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f'{height:.0f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    fig.tight_layout()
    return canvas



def get_vvindovvs1_graph_datas():
       
    total_works_hour = {}
    if doing.VVINDOVVS1_DIR.exists():

        with open(doing.VVINDOVVS1_DIR, 'r', newline='', encoding='utf-8')  as f:
            reader = csv.DictReader(f)

            for line in reader:
                if not line:
                    continue
                

                mod = line.get(doing._theme)
                time = line.get(doing._usedtime)
                time_count = int(time) / 60

                if mod in total_works_hour:
                    total_works_hour[mod] += time_count
                else:
                    total_works_hour[mod] = time_count
            return list(total_works_hour.keys()), list(total_works_hour.values())





def create_vvindovvs1_pie_widget(labels, values):
    if not labels or not values:
        return None

    fig = Figure(figsize=(5, 5), dpi=100)
    fig.patch.set_facecolor('#0b2b1b') 
    canvas = FigureCanvasQTAgg(fig)

    ax = fig.add_subplot(111)
    ax.set_facecolor('#041e10')
    ax.tick_params(colors='#d8e6df')
    ax.yaxis.label.set_color('#d8e6df')
    ax.xaxis.label.set_color('#d8e6df')
    ax.title.set_color('#ffffff')


    ax.pie(
        values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 9, 'color': 'white'} 
    )

    ax.set_title(
        'İş vaxtının mövzular üzrə bölgüsü',
        fontsize=12,
        pad=10,
        color='white'  
    )

    fig.tight_layout()
    return canvas










 
