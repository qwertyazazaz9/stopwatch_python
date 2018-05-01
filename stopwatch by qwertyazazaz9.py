from tkinter import *
import math

#окошко
root = Tk()
root.title('Секундомер')

#делаем холст
canvas = Canvas(root, width = 400, height = 400)
canvas.pack()
canvas.create_oval(7, 7, 393, 393, fill = 'lightgray')
canvas.create_text(200, 180, text = '.', font = ('Arial', 50))

#изначальные значения переменных
sec = 0
after_id = ''
m = 0
line_sec = canvas.create_line(200, 200, 200, 50, fill = 'red', width = 2)
x1 = 200
y1 = 50
line_m = canvas.create_line(200, 200, 200, 55, width = 3)
xm = 200
ym = 55

#счётчик цикла для рисочек
i = 0
#делаем рисочки
while i < 60:
    i = i + 1
    canvas.create_line(200 + 170 * math.cos(-i * 6 * math.pi/180 + math.pi/2),
                       200 - 170 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                       200 + 190 * math.cos(-6 * i * math.pi/180 + math.pi/2),
                       200 - 190 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                       width = 2)
    if i % 5 == 0:
        canvas.create_line(200 + 165 * math.cos(-i * 6 * math.pi/180 + math.pi/2),
                           200 - 165 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                           200 + 190 * math.cos(-6 * i * math.pi/180 + math.pi/2),
                           200 - 190 * math.sin(-6 * i * math.pi/180 + math.pi/2),
                           width = 4)

#функция секундомера
def tick():
    global sec, m, x1, y1, after_id, line_sec, line_m
    after_id = root.after(1000, tick)
    #стрелки
    canvas.delete(line_sec)
    x1 = 200 - 150 * math.cos(sec * 6 * math.pi/180 + math.pi/2)
    y1 = 200 - 150 * math.sin(sec * 6 * math.pi/180 + math.pi/2)
    line_sec = canvas.create_line(200, 200, x1, y1, fill = 'red', width = 2)
    canvas.delete(line_m)
    xm = 200 - 145 * math.cos(m * 6 * math.pi/180 + math.pi/2)
    ym = 200 - 145 * math.sin(m * 6 * math.pi/180 + math.pi/2)
    line_m = canvas.create_line(200, 200, xm, ym, width = 3)
    #выравнивание времени по формату ММ:СС
    if m<10 and sec<10:
        label1.configure(text='0'+str(m)+':0'+str(sec))
    elif m>=10 and sec<10:
        label1.configure(text=str(m)+':0'+str(sec))
    elif m<10 and sec>=10:
        label1.configure(text='0'+str(m)+':'+str(sec))
    else:
        label1.configure(text=str(m)+':'+str(sec))
    sec += 1
    if sec == 59:
        sec = 0
        x1 = 200
        y1 = 50
        m += 1
    
#старт
def start():
    btn1.pack_forget()
    btn2.pack()
    tick()

#стоп
def stop():
    btn2.pack_forget()
    btn3.pack()
    btn4.pack()
    root.after_cancel(after_id)

#продолжить
def continue_sec():
    btn3.pack_forget()
    btn4.pack_forget()
    btn2.pack()
    tick()

#сброс
def reset():
    global sec, m, line_m, line_sec
    sec = 0
    m = 0
    #сброс времени на дисплейчике
    label1.configure(text='00:00')
    #сброс на часах
    canvas.delete(line_m)
    canvas.delete(line_sec)
    line_sec = canvas.create_line(200, 200, 200, 50, fill = 'red', width = 2)
    x1 = 200
    y1 = 50
    line_m = canvas.create_line(200, 200, 200, 55, width = 3)
    xm = 200
    ym = 55
    btn3.pack_forget()
    btn4.pack_forget()
    btn1.pack()

#дисплейчик
label1 = Label(root, width=7, text='00:00', font=('Arial', 50))
label1.pack()

#кнопки
btn1 = Button(root, text = 'Старт', font=('Arial', 15), command = start)
btn2 = Button(root, text='Стоп', font=('Arial', 15), command=stop)
btn3 = Button(root, text='Продолжить', font=('Arial', 15), command=continue_sec)
btn4 = Button(root, text='Сброс', font=('Arial', 15), command=reset)

btn1.pack()


root.mainloop()
