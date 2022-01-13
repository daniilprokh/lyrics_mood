#!/usr/bin/env python
# coding: utf-8

# In[4]:


from ui_api_widget import Ui_ApiWidget
from api import Api


# In[5]:


from PySide2 import QtCore, QtGui, QtWidgets


# In[6]:


class ApiWidget(QtWidgets.QWidget):
    def __init__(self):
        super(ApiWidget, self).__init__()
        
        self.d_ui = Ui_ApiWidget()
        self.d_ui.setupUi(self)
        
        self.d_ui.pb_ok.clicked.connect(self.accept)
        self.d_ui.pb_cancel.clicked.connect(self.cancel)
        
        self.api_list = [Api.IBM_WATSON, Api.PARALLEL_DOTS]
    
    @QtCore.Slot()
    def accept(self):
        api_list = []
        if self.d_ui.cb_ibm_watson.isChecked():
            api_list.append(Api.IBM_WATSON)
        if self.d_ui.cb_parallel_dots.isChecked():
            api_list.append(Api.PARALLEL_DOTS)
        if self.d_ui.cb_twinword.isChecked():
            api_list.append(Api.TWINWORD)
        if self.d_ui.cb_prompt.isChecked():
            api_list.append(Api.PROMPT)
        self.api_list = api_list
        if api_list:
            self.close()
    
    @QtCore.Slot()
    def cancel(self):
        if Api.IBM_WATSON in self.api_list:
            self.d_ui.cb_ibm_watson.setChecked(True)
        else:
            self.d_ui.cb_ibm_watson.setChecked(False)
        if Api.PARALLEL_DOTS in self.api_list:
            self.d_ui.cb_parallel_dots.setChecked(True)
        else:
            self.d_ui.cb_parallel_dots.setChecked(False)
        if Api.TWINWORD in self.api_list:
            self.d_ui.cb_twinword.setChecked(True)
        else:
            self.d_ui.cb_twinword.setChecked(False)
        if Api.PROMPT in self.api_list:
            self.d_ui.cb_prompt.setChecked(True)
        else:
            self.d_ui.cb_prompt.setChecked(False)
        self.close()


# In[ ]:




