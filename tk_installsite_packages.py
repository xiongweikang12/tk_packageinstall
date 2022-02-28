#TODO 配置虚拟环境时，导入想要的第三方库


import random
import time
import tkinter as tk
import pathlib
import pathlib as plib
from tkinter import messagebox
import re
import shutil
import logging as logg
import pyautogui
import pyperclip


#TODO 定义主函数tk 窗口

window=tk.Tk()
window.title('导入第三库')
window.geometry('400x200')
entry_install=tk.StringVar
entry_project=tk.StringVar
l_top=tk.Label(window,text='第三方库',height=1,width=20,bg='red')
l_top.place(x=138,y=10)
tk.Label(window,text='第三方库库名 :',height=1,width=15).place(x=10,y=45)
tk.Label(window,text='环境项目名称 :',height=1,width=15).place(x=10,y=75)
e_install=tk.Entry(window)
e_install.place(x=140,y=45)
e_project=tk.Entry(window)
e_project.place(x=140,y=75)

#TODO 设置logging

logg.basicConfig(level=logg.DEBUG,format='%(asctime)s -%(filename)s[line:%(lineno)d]-%(levelname)s -%(message)s')
logg.basicConfig(level=logg.INFO,format='%(asctime)s -%(filename)s[line:%(lineno)d]-%(levelname)s -%(message)s')





def copied_to_newproject():
    global path_sitepackage_install
    path_sitepackage_install=None

    p=plib.Path(r'D:\lib\site-packages') #pip 安装的目录
    p_par=plib.Path(r'D:\python\pythonProject1\venv\Lib\site-packages') #另一个第三方库获取路径
    p_par_list=[p for p in list(p_par.glob('*')) if p.is_dir()]
    p_list=list(p.glob('*'))
    p_dirname=[i for i in p_list if i.is_dir()] #通过列表推导式获取p路径下是文件夹的路径
    p_python=plib.Path.cwd().parent.parent #设置环境的目录 D:\python
    p_list_project=list(p_python.glob('*'))
    p_list_project=[str(a) for a in p_list_project if a.is_dir()] #获取环境项目路径，转换成string

    # TODO 检测
    def Exist_Install_path():
        global check_install
        global path_sitepackage_install
        global entry_install
        check_install=0
        entry_install=e_install.get()
        for name_ in p_dirname:
            if bool(re.search('%s$'%(entry_install),name_.name)):#通过entry输入内容，遍历搜索库名
                #将该文件夹复制到环境的site_packages
                path_sitepackage_install=name_ #得到库的路径
                logg.info('pip安装路径的现有库路径 (起始): %s '%(path_sitepackage_install))
                break
            else:
                check_install+=1
                continue
        if check_install==len(p_dirname):
            return True
        else:
            return False




    # TODO 检测目的路径的存在性
    def Button_CmdTo_Install():
        global path_sitepackage
        global check_project
        global entry_project
        flag_project = len(p_list_project)
        check_project = 0
        entry_project = e_project.get()
        for path_project in p_list_project:
            if bool((re.search('%s$' % (entry_project), path_project))):
                path_sitepackage = pathlib.Path(path_project) / pathlib.Path(
                    'Lib/site-packages') / pathlib.Path(entry_install)
                logg.info('代导入库的路径（目的） :' + str(path_sitepackage))
                break
            else:
                check_project += 1
                continue
        if check_project == flag_project:
            messagebox.showerror(title='information', message='on find out the project')
            quit()



    if Exist_Install_path():
        if messagebox.askyesnocancel(title='information',message="       can't find out the package \n                  if try other"):
            check_install_project1=0
            for project1_name in p_par_list:
                if bool(re.search('%s$'%(entry_install),project1_name.name)):
                    path_sitepackage_install=project1_name
                    #log
                    break
                else:
                    check_install_project1+=1
                    continue

            if check_install_project1==len(p_par_list):
                if messagebox.askyesnocancel(title='choice',message='    to install  %s  package'%(entry_install)):

                    var2=tk.StringVar()
                    window_install=tk.Toplevel(window)
                    window_install.title('installing by the mrrio url')
                    window_install.geometry('400x400')
                    l_window_install=tk.Label(window_install,text='第三方库名',height=1,width=20,bg='red')
                    l_window_install.pack()
                    var2.set(('pypi.douban', 'pypi.mirrors.ustc.edu.cn', 'pypi.tuna.tsinghua.edu.cn'))
                    listbox_url=tk.Listbox(window_install,listvariable=var2)
                    listbox_url.pack()







                    # TODO 通过pyautogui cmd install packages
                    def Auto_Install():

                        pyautogui.keyDown('winleft')
                        pyautogui.keyDown('r')
                        pyautogui.keyUp('r')
                        pyautogui.keyUp('winleft')
                        pyautogui.keyDown('enter')
                        pyautogui.keyUp('enter')
                        install_url = listbox_url.get(listbox_url.curselection())
                        copyToCmd = 'pip install %s-i http://%s.com/simple --trusted-host pypi.douban.com' % (
                        entry_install, install_url)
                        pyperclip.copy(copyToCmd)
                        pyautogui.keyDown('ctrl')
                        pyautogui.keyDown('v')
                        pyautogui.keyUp('v')
                        pyautogui.keyUp('ctrl')
                        pyautogui.keyDown('enter')
                        pyautogui.keyUp('enter')
                        time.sleep(5)
                        Exist_Install_path()




                    button_window_install=tk.Button(window_install,text='test',command=Button_CmdTo_Install,height=1,width=10)
                    button_window_Autoinstall=tk.Button(window_install,text='install',command=Auto_Install,height=1,width=10)
                    button_window_install.pack()
                    button_window_Autoinstall.pack()




                        # os.mkdir(path_sitepackage)
                        # break















                else:
                    quit()
        else:
            quit()
    else:
        Button_CmdTo_Install()



    # flag_project=len(p_list_project)
    # check_project=0
    # entry_project = e_project.get()
    # for path_project in p_list_project:
    #     if bool((re.search('%s$' % (entry_project), path_project))):
    #         path_sitepackage = pathlib.Path(path_project) / pathlib.Path('Lib/site-packages')/pathlib.Path(entry_install)
    #         print(path_sitepackage)
    #         break
    #     else:
    #         check_project+=1
    #         continue
    # if check_project==flag_project:
    #     messagebox.showerror(title='information',message='on find out the project')
    #     quit()

            # os.mkdir(path_sitepackage)
            # break

    #TODO 判断是否输入正常，第三方库是否重复安装
    if path_sitepackage_install:
        shutil.copytree(path_sitepackage_install,path_sitepackage)
        messagebox.showinfo(title='information',message='pasckage have installed ')
        time.sleep(random.randint(2,5))
        quit()




button_ml=tk.Button(window,text='启动',height=1,width=10,command=copied_to_newproject)
button_ml.place(x=180,y=110)
button_quit=tk.Button(window,text='退出',height=1,width=10,command=quit)
button_quit.place(x=180,y=145)

if __name__=='__main__':
    window.mainloop()

