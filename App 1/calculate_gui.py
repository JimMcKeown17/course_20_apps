import FreeSimpleGUI as sg
from calculate import convert

sg.theme("black")

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

covert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

feet = 0
inches = 0
result = sg.Text(convert(feet, inches), key="result")
window = sg.Window("File Compresser",
                   layout=[[label1, input1],
                           [label2, input2],
                           [covert_button, result],
                           [exit_button]])
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Convert":
        try:
            feet = float(values["feet"])
            inches = float(values["inches"])
            conversion_result = convert(feet, inches)
            # result = sg.Text(convert(feet, inches))
            window['result'].update(conversion_result)
        except ValueError:
            window['result'].update("Please enter a valid number")
    if event == "Exit":
        break

window.close()