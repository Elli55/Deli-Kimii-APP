import sys
import traceback
import datetime
import csv
from PySide6 import QtWidgets, QtCore, QtGui


def exception_hook(exctype, value, tb):
    print("\n UNCAUGHT EXCEPTION ")
    traceback.print_exception(exctype, value, tb)
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = exception_hook

from build import Ui_Main
import moduls
from Dialogs import dialogexp, dialoginc, dialogop, dialogprogressbar, dialogexpco, dialogincco


MESSAGE_XETA = 'XƏTA'


app = QtWidgets.QApplication(sys.argv)

class MainVvindovvs(QtWidgets.QMainWindow):

   
    def __init__(self, parent = None):
        super().__init__(parent)
        #sistem əməliyyatları
        self.ui = Ui_Main()
        self.ui.setupUi(self)

    

       
        self.statusBar = QtWidgets.QStatusBar()  
        self.setStatusBar(self.statusBar)

        self.dialog_xrc = DialogXrc(self)
        self.dialog_glr = DialogGlr(self)
        self.dialog_op = DialogOp(self)
        self.dialog_progress = DialogProg(self)
        self.dialog_exp_co = DialogExpCo(self)
        self.dialog_inc_co = DialogIncCo(self)

        #Maliyyə düymələri
       
        self.ui.SaveIncomeButton.clicked.connect(self.click_on_vvrite_inc)
        self.ui.SaveExpButton.clicked.connect(self.click_on_vvrite_exp)
        self.ui.SaveDebitButton.clicked.connect(self.click_on_vvrite_debit)
        self.ui.RemoveDebitButton.clicked.connect(self.click_on_pay_debit)



        #Operativ düymələr

        self.ui.Vvindovvs1AcceptButton.clicked.connect(self.click_on_vvindovvs_1_accept)

        self.ui.RiyaziyyatYazButton.clicked.connect(self.click_on_rizayizzat_qeyd)

        self.ui.TryButton.clicked.connect(self.on_click_problem_tap)

        self.ui.SaveButtonForVVindovs1.clicked.connect(self.click_on_save_file)

        self.ui.ButtonForCalendarVVindovvs3.clicked.connect(self.click_on_calendar_button_vvindovvs_3)

        

         #Menular 
        self.setup_xerc_tool_menu()
        self.setup_gelir_tool_button()
        self.ui.ToolButtonForOp.clicked.connect(self.set_up_op_tool_button)


        
        #grafikləşdirmə və yansıtma
        self.setup_vvallet()
        self.setup_total_debit()

        self.ui.ProgressBarButton.clicked.connect(self.setup_progressbar)

        self.exp_graph = self.setup_graph_exp()
        self.ui.verticalLayout_3.addWidget(self.exp_graph)


        self.pie_widget = self.setup_vvindovv1_pie_chart()
        self.ui.Graph_layout_for_vvindovvs_1.addWidget(self.pie_widget) 


       

    

        

        

    #grafik funksiyaları
    def setup_progressbar(self):
        
        self.dialog_progress.show()
        self.dialog_progress.raise_()


    def setup_graph_exp(self):
        cats, sums = moduls.get_exp_graph_datas()

        widget = moduls.create_exp_bar_chart_widget(cats, sums)

        if widget is None:
            empty_label = QtWidgets.QLabel("Hələ heç bir xərc qeyd edilməyib")
            empty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            empty_label.setStyleSheet("color: #795100; font-size: 14px;")
            return empty_label

        return widget

    
    def setup_vvindovv1_pie_chart(self):
        if moduls.doing.VVINDOVVS1_DIR.exists():

            mod, pros = moduls.get_vvindovvs1_graph_datas()
            widget = moduls.create_vvindovvs1_pie_widget(mod, pros) 
            return widget
        else:

    
        
            empty_label = QtWidgets.QLabel("Hələ heç bir məlumat yoxdur")
            empty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            empty_label.setStyleSheet("color: #795100; font-size: 14px;")
            return empty_label
        
         
        
    def setup_vvallet(self):
        balance = moduls.calculate_wallet()

        self.ui.SumVvallet.display(balance)


    def setup_total_debit(self):

        debits = moduls.calculate_total_debits()

        self.ui.TotalDebit.display(debits)    

        

            


    # Menular üçün funksiyalar
    def set_up_op_tool_button(self):
        self.dialog_op.show()
        self.dialog_op.raise_()

    def click_on_liested_expenses(self):
        
        self.dialog_xrc.listed_expenses()
        self.dialog_xrc.show()
        self.dialog_xrc.raise_()

    def click_on_add_category_exp(self):

        self.dialog_exp_co.show()   

    def click_on_add_category_inc(self):

        self.dialog_inc_co.show()     

    def setup_xerc_tool_menu(self):

        
        

        act_pop_last = QtGui.QAction('Sonuncu yazılanı sil', self)
        act_listed = QtGui.QAction('Xərcləri siyahıla və sil', self)
        act_inport_category = QtGui.QAction('Kateqoriya əlavə et.', self)

        act_pop_last.triggered.connect(self.dialog_xrc.click_on_pop_last_expens)
        act_listed.triggered.connect(self.click_on_liested_expenses)
        act_inport_category.triggered.connect(self.click_on_add_category_exp)
            

        menu_exp = QtWidgets.QMenu(self)
        menu_exp.addAction(act_pop_last)
        menu_exp.addSeparator()
        menu_exp.addAction(act_listed)
        menu_exp.addSeparator()
        menu_exp.addAction(act_inport_category)


        self.ui.ToolButtonXerc.setMenu(menu_exp)
        self.ui.ToolButtonXerc.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)

    def setup_gelir_tool_button(self):
        act_pop_last = QtGui.QAction('Sonuncu yazılanı sil.', self)
        act_listed_inc = QtGui.QAction('Gəlirləri siyahıla və sil', self)
        act_inport_category = QtGui.QAction('Kateqoriyaları təyin et.', self)

        

        act_pop_last.triggered.connect(self.dialog_glr.pop_last_income)
        act_listed_inc.triggered.connect(self.clicked_on_listed_income)
        act_inport_category.triggered.connect(self.click_on_add_category_inc)

        

        menu_inc = QtWidgets.QMenu(self)
        menu_inc.addAction(act_pop_last)
        menu_inc.addSeparator()
        menu_inc.addAction(act_listed_inc)
        menu_inc.addSeparator()
        menu_inc.addAction(act_inport_category)

        


        
        self.ui.ToolButtonGelir.setMenu(menu_inc)
        self.ui.ToolButtonGelir.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)

    def clicked_on_listed_income(self):
        
        self.dialog_glr.listed_income()
        self.dialog_glr.show()
        self.dialog_glr.raise_()
   

    
   

        


    
    


        

        
    #mesjaları daha asan əldə etməkçün
    def warning_mesagge(self, mesage):
        QtWidgets.QMessageBox.warning(self, MESSAGE_XETA, mesage)

    def status_bar_message(self,mesage):
        self.statusBar.showMessage(mesage, 5000)    
        

    #maliyyə funksiyaları
    def click_on_vvrite_inc(self):
        print("Gəlir yaz düyməsi işləyir")

        name_of_inc = self.ui.VvriteIncNmae.text()
        source_of_in = self.ui.ChoosCategoryForInc.currentText()
        date_of_inc = self.ui.DateOfInc.date().toString('yyyy-MM-dd')
        amount_of_inc = self.ui.AmounOfInc.value()

        if not name_of_inc:
            self.warning_mesagge('Gəlirin adını qeyd et !!!')
            return


        if amount_of_inc <= 0:
            self.warning_mesagge('Gəlirin məbləğini təyin et !!!')  
            return       

        moduls.write_income(name_of_inc, date_of_inc, amount_of_inc, source_of_in)

        self.status_bar_message(f"{name_of_inc} üçün {source_of_in}'dən {amount_of_inc} əlavə edildi ")

        self.ui.VvriteIncNmae.clear()
        self.ui.ChoosCategoryForInc.setCurrentIndex(0)
        self.ui.DateOfInc.setDate(QtCore.QDate.currentDate())
        self.ui.AmounOfInc.setValue(0)
        self.setup_vvallet()
    
                
    def click_on_vvrite_exp(self):


        name_of_exp = self.ui.VvriteExpName.text()
        category_of_exp = self.ui.ChooisCategoryOfExp.currentText()
        date_of_ex = self.ui.DateOfExp.date().toString('yyyy-MM-dd')
        amoun_of_exp = self.ui.AmountOfEcp.value()

        if not name_of_exp:
            self.warning_mesagge('Xərcin adını qeyd elə !!!')
            return

        if amoun_of_exp <= 0:
            self.warning_mesagge('Xərcin məbləğini qeyd et !!!')
            return

        moduls.write_expenses(name_of_exp,date_of_ex, amoun_of_exp,category_of_exp )

        self.status_bar_message(f'{name_of_exp} üçün {amoun_of_exp} AZN xərc əlavə edildi !!! ')
        
        self.ui.VvriteExpName.clear()
        self.ui.DateOfExp.setDate(QtCore.QDate.currentDate())
        self.ui.AmountOfEcp.setValue(0)
        self.setup_vvallet()


        while self.ui.verticalLayout_3.count():
            item = self.ui.verticalLayout_3.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.exp_graph = self.setup_graph_exp()
        self.ui.verticalLayout_3.addWidget(self.exp_graph)




    def click_on_vvrite_debit(self):
        print('Borcyaz düyməsi işləyir')

        name_of_debit = self.ui.VVriteDebitsName.text()
        amount_of_debit = self.ui.VVriteDebitAmaount.value()
        category_of_debit = self.ui.ChoosCategoryOfDebit.text()
        deadline_of_debit = self.ui.VVriteDebitDate.date().toString('yyyy-MM-dd')

        if not name_of_debit:
            self.warning_mesagge('Borcun adını qedy et !!!')
            return
        
        if amount_of_debit <= 0:
            self.warning_mesagge('Borcun məbləğini də qeyd et !!! ')
            return
        
        
        moduls.write_debit(name_of_debit, amount_of_debit,category_of_debit,deadline_of_debit)
        self.status_bar_message(f'{amount_of_debit} AZN ödəniş {name_of_debit} üçün əlavə edildi')

        
        self.ui.VVriteDebitDate.setDate(QtCore.QDate.currentDate())
        self.ui.VVriteDebitsName.clear()
        self.ui.VVriteDebitAmaount.setValue(0)
        self.setup_vvallet()
        self.setup_total_debit()

        self.ui.ListOfDebits.clear()
        self.ui.ListOfDebits.addItems(moduls.get_debits_list())
        print('Conbo boxa borcları yaza bildi.')



    def click_on_pay_debit(self):
        print('Borc sil düyməsi işləyir.')

        payed_debit = self.ui.ListOfDebits.currentText()
        category_of_this_debit = None

        with open(moduls.finance.DEBIT_DIR, 'r', newline='', encoding='utf-8') as f:
            reader =csv.DictReader(f)
            for line in reader:
                if line.get(moduls.finance._name) == payed_debit:

                    category_of_this_debit = line.get(moduls.finance._category)

        while self.ui.verticalLayout_3.count():
            item = self.ui.verticalLayout_3.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.exp_graph = self.setup_graph_exp()
        self.ui.verticalLayout_3.addWidget(self.exp_graph)            






        moduls.pay_debit(payed_debit,category_of_this_debit)
        self.ui.ListOfDebits.clear()
        self.ui.ListOfDebits.addItems(moduls.get_debits_list())
        self.setup_vvallet()
        self.setup_total_debit()
        self.ui.verticalLayout_3.addWidget(self.exp_graph)








    #Operativ funksiyaları
    def click_on_vvindovvs_1_accept(self):

        vvindovv1_theme = self.ui.Vvindovvs1Cat.currentText()
        vvindovv1_date = self.ui.Vvvindovvs1Date.date().toString('yyyy-MM-dd')
        vvindovvs1_hours = self.ui.Vvvindovvs1Hours.time()
        total_vvindovvs1_hours = vvindovvs1_hours.hour() * 60 + vvindovvs1_hours.minute()
        vvindovv1_note= self.ui.Vvindovs1Noten.toPlainText()


        if total_vvindovvs1_hours <= 0:
            self.warning_mesagge('İşlədiyin saatı qeyd et !!!')
            return


        moduls.write_vvindovvs1_progress(vvindovv1_date, vvindovv1_theme, total_vvindovvs1_hours, vvindovv1_note)

        self.status_bar_message(f'Bu gün {vvindovv1_theme} üzrə {vvindovvs1_hours} işlədin. ')

        self.ui.Vvvindovvs1Date.setDate(QtCore.QDate.currentDate())
        self.ui.Vvvindovvs1Hours.setTime(QtCore.QTime(0,0))
        self.ui.Vvindovs1Noten.setPlainText(f'Sonuncu dəfə  {vvindovv1_theme} üzrə  {total_vvindovvs1_hours} dəqiqə işləyibsən ')
        
        while self.ui.Graph_layout_for_vvindovvs_1.count():
            item = self.ui.Graph_layout_for_vvindovvs_1.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.pie_widget = self.setup_vvindovv1_pie_chart()
        self.ui.Graph_layout_for_vvindovvs_1.addWidget(self.pie_widget)    



    def click_on_save_file(self):

        name = self.ui.toolBox.itemText(0)

        doc = moduls.export_word_file(name)

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Word file', 'Qeydler.docx', 'Word Files (*.docx)'  )

        if file_path:
            if file_path.endswith('.docx'):
                file_path += '.docx'
            doc.save(file_path)
        


    def click_on_rizayizzat_qeyd(self):
        print('Riyaziyyat qeyd et düyməsi işləyir')

        riyaziyyat_tarix = self.ui.RiyaziyyatTarix.date().toString('yyyy-MM-dd')
        riyaziyyat_saat = self.ui.RiyaziyyatSaat.time()
        total_riyaziyyat_saat = riyaziyyat_saat.hour() * 60 + riyaziyyat_saat.minute()
        riyaziyyat_movzu = self.ui.RiyaziyyatMvzu.text()
        riyaziyyat_not = self.ui.RiyaziyyatProblemYaz.toPlainText()

        if not riyaziyyat_movzu:
            self.warning_mesagge('Mövzunu qeyd et !!! ')
            return

        if total_riyaziyyat_saat <= 0:
            self.warning_mesagge('İşlədiyin saatı qeyd et !!! ')
            return

        moduls.write_math_progress(riyaziyyat_tarix, riyaziyyat_movzu, total_riyaziyyat_saat, riyaziyyat_not, 'Open')

        self.ui.RiyaziyyatTarix.setDate(QtCore.QDate.currentDate())
        self.ui.RiyaziyyatSaat.setTime(QtCore.QTime(0,0))
        self.ui.RiyaziyyatMvzu.clear()
        self.ui.RiyaziyyatProblemYaz.setPlainText('Araşdırılmalı olan problem. ')


    def on_click_problem_tap(self):
       
       topic, problem =  moduls.find_random_math_problem()

       if not problem:
           self.warning_mesagge('Sistemdə riyazi problem qalmayıb')
           return

       moduls.done_topic_math(problem)

       self.ui.RiyaziyyatProblemGoster.setPlainText(f'{topic} - \n {problem}')



    def click_on_calendar_button_vvindovvs_3(self):
        date = self.ui.Vvindovvs_3_calendar.selectedDate()
        
        current_format = self.ui.Vvindovvs_3_calendar.dateTextFormat(date)
        current_color = current_format.background().color()
        
        forma = QtGui.QTextCharFormat()
        
        # Əgər artıq yaşıldırsa, default rəngə qaytar
        if current_color == QtGui.QColor('green'):
            forma.setBackground(QtGui.QColor())  # Boş = default rəng
        else:
            forma.setBackground(QtGui.QColor('green'))
        
        self.ui.Vvindovvs_3_calendar.setDateTextFormat(date, forma)

    


    


class DialogXrc(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = dialogexp.Ui_DialogXercSil()
        self.ui.setupUi(self)


        self.ui.BaglaButtonDialogExp.clicked.connect(self.close)
        self.ui.SilButtonDialogExp.clicked.connect(self.click_on_remove_selected)




    

    def listed_expenses(self):
        
        self.ui.XrcList.clear()
            
        with open(moduls.finance.EXPENSE_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                exp_text = f'{line[1]}  | {line[3]} 💵 | {line[4]} | {line[2]}'
                item = QtWidgets.QListWidgetItem(exp_text)
                item.setData(QtCore.Qt.ItemDataRole.UserRole, line[0])

                self.ui.XrcList.addItem(item) 

            

    def  click_on_remove_selected(self):
        row = self.ui.XrcList.currentItem()
        if not row:
            return

        idd = row.data(QtCore.Qt.ItemDataRole.UserRole)

        cleaned = []

        with open(moduls.finance.EXPENSE_DIR, 'r', encoding='utf-8' , newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0] == idd:
                    continue
                else:
                    cleaned.append(line)

        with open(moduls.finance.EXPENSE_DIR, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerows(cleaned)
        
        row_index = self.ui.XrcList.currentRow()
        self.ui.XrcList.takeItem(row_index)

    
    def click_on_pop_last_expens(self):

       

        expenses = []

        with open(moduls.finance.EXPENSE_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                expenses.append(line)

        if len(expenses) >1:
            deleted_expenses = expenses.pop()
            headd = expenses[0]
            body = expenses[1:]

            with open(moduls.finance.EXPENSE_DIR, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headd)
                writer.writerows(body)
            self.parent().warning_mesagge(f'{deleted_expenses[1]} silindi')    

               
        else:
            self.parent().status_bar_message('Silinəcək xərc yoxdur')


    
class DialogGlr(QtWidgets.QDialog):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.ui = dialoginc.Ui_DialogGlr()
        self.ui.setupUi(self)

        self.ui.DialogIncCloseButton.clicked.connect(self.close)
        self.ui.DialogIncSilButton.clicked.connect(self.click_on_remove_selected)


   
    
    def  listed_income(self):

        self.ui.GlrList.clear()

        with open(moduls.finance.INCOME_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                glr_text = f'{line[1]} | {line[3]} 💵 | {line[4]} | {line[2]}'
                glr_item = QtWidgets.QListWidgetItem(glr_text)
                glr_item.setData(QtCore.Qt.ItemDataRole.UserRole, line[0])

                self.ui.GlrList.addItem(glr_item)

    

    def click_on_remove_selected(self):

        line = self.ui.GlrList.currentItem()    
        if not line:
            return
        
        idd = line.data(QtCore.Qt.ItemDataRole.UserRole)


        cleaned = []

        with open(moduls.finance.INCOME_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0] == idd:
                    continue
                else:
                    cleaned.append(line)

        with open(moduls.finance.INCOME_DIR, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(cleaned)


        line_index = self.ui.GlrList.currentRow()
        self.ui.GlrList.takeItem(line_index)



    def pop_last_income(self):

        inc_rows = []

        with open(moduls.finance.INCOME_DIR, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line  in reader:
                    inc_rows.append(line)

        if len(inc_rows) > 1:
            deleted_row = inc_rows.pop()
            last_list = inc_rows

            with open(moduls.finance.INCOME_DIR, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(last_list)

                self.parent().warning_mesagge(f'{deleted_row} silindi !!!')




class DialogOp(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = dialogop.Ui_Dialog()
        self.ui.setupUi(self)




        self.ui.AcceptButtonVVindovvs1.clicked.connect(self.click_on_accept_1)
        self.ui.AcceptButtonVVindovvs_2.clicked.connect(self.click_on_accept_2)
        self.ui.AcceptButtonVVindovvs_3.clicked.connect(self.click_on_accept_3)




    
    def click_on_accept_1(self):


        titel = self.ui.TitelForVVindovvs1.text()
        category_text = self.ui.ItemsForConboboxVvindovs1.toPlainText()
        category_lines = []
        
        if not category_text:
            
            self.parent().warning_mesagge('Bölmə adlarını qeyd edin.')
        else:
            self.parent().ui.Vvindovvs1Cat.clear()

            for line in category_text.split('\n'):
                category_lines.append(line.strip())
            
            for li in category_lines:
               
                self.parent().ui.Vvindovvs1Cat.addItem(li)


        self.parent().ui.toolBox.setItemText(0, titel)

    def click_on_accept_2(self):

        titel = self.ui.TitelForVvindovvs_2.text()

        
        self.parent().ui.toolBox.setItemText(1, titel)


    def click_on_accept_3(self):

        titel = self.ui.TitttelForVvindovvs_3.text()

        
        self.parent().ui.toolBox.setItemText(2, titel) 




class DialogProg(QtWidgets.QDialog):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.ui = dialogprogressbar.Ui_DialogProgressBar()
        self.ui.setupUi(self)

        

        

        self.ui.ProgressBarAcceptButton.clicked.connect(self.click_on_set)

    def get_dates(self):
        date_for_start = self.ui.ProgressBarDateForStart.date().toPython()
        date_for_end = self.ui.ProgressBarDateForEnd.date().toPython()
        titel_for_prog = self.ui.TitelInput.text()

        return date_for_start,  date_for_end, titel_for_prog
    

    def calculate_time_for_progresbar(self):
        start_date, end_date, _ = self.get_dates()

        now_date = datetime.datetime.now().date()    

        if now_date < start_date:
            return 0
        elif end_date < now_date:
            return 100
        else:
            total_time = (end_date - start_date).days
            past_days =   (now_date - start_date).days

            return int((past_days / total_time) * 100)  
        
    def click_on_set(self):
       _, _, dir = self.get_dates()

       moduls.doing.set_data_dir_do(dir)
       moduls.finance.set_data_dir_fi(dir)
       moduls.graphics.set_data_dir_gr(dir)

       self.parent().ui.TitelVVidget.setText(dir)          

       self.parent().ui.DateOfProject.setValue(self.calculate_time_for_progresbar()) 
        


class DialogExpCo(QtWidgets.QDialog):

    def __init__(self,  parent = None):
        super().__init__(parent)

        self.ui = dialogexpco.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.AcceptCategory.clicked.connect(self.click_on_accept)


    def click_on_accept(self):

        category_text = self.ui.CategoryText.toPlainText()
        if not category_text:
            self.parent().warning_mesagge('Kateqoriya adlarını qeyd edin.')

        else:
            self.parent().ui.ChooisCategoryOfExp.clear()
            for cat in category_text.split('\n'):
                
                self.parent().ui.ChooisCategoryOfExp.addItem(cat)  
    

class DialogIncCo(QtWidgets.QDialog):
    def __init__(self, parent =None):
        super().__init__(parent)

        self.ui = dialogincco.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.AcceptCategory.clicked.connect(self.click_on_accept)


        
    def click_on_accept(self):

        category_text = self.ui.CategoryText.toPlainText()
        if not category_text:
            self.parent().warning_mesagge('Kateqoriya adlarını qeyd edin.')

        else:
            self.parent().ui.ChoosCategoryForInc.clear()
            for cat in category_text.split('\n'):
                
                self.parent().ui.ChoosCategoryForInc.addItem(cat)  

                
              





        

    



    
         
      
    



window = MainVvindovvs()

window.show()

sys.exit(app.exec())

