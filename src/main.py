
import PySimpleGUI as sg

# layout
sg.theme('dark grey 9')

functionLayout = [
    [
        sg.Button(
            key='-INIT-',
            button_text='Iniciar',
            size=(10, 1),
            font='Any 12 bold',
            button_color=('#FFFFFB', '#6FBA26')
        )
    ],
    [
        sg.Button(
            key='-NEWTURN-',
            button_text='Novo turno',
            size=(10, 1),
            font='Any 12 bold',
            button_color=('#FFFFFB', '#FF5200')
        )
    ],
    [
        sg.Button(
            key='-OPTIONS-',
            button_text='Opções',
            size=(10, 1),
            font='Any 12 bold',
            button_color=('#FFFFFB', '#007FC7')
        )
    ]
]

viewLayout = [
    [
        sg.Text('ROUND:', font='Any 12 bold'),
        sg.Text(key='-ROUND-', text='1', font='Any 11 bold'),
        sg.Text(
            key='-ROUND-',
            text='50',
            visible=False,
            background_color='red',
            font='Any 11 bold'
        )
    ],
    [
        sg.Text(
            key='-VIEW-',
            text='3',
            size=(20, 1),
            justification='center',
            background_color='#232629',
            font='Any 50 bold'
        )
    ]
]

countLayout = [
    [
        sg.Button(
            key='-MORE1-',
            button_text='+1',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#B5179E')
        ),
        sg.Button(
            key='-MORE2-',
            button_text='+2',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#B5179E')
        ),
        sg.Button(
            key='-MORE3-',
            button_text='+3',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#B5179E')
        ),
        sg.Button(
            key='-MORE4-',
            button_text='+4',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#B5179E')
        )
    ],
    [
        sg.Button(
            key='-LESS1-',
            button_text='-1',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#7209B7')
        ),
        sg.Button(
            key='-LESS2-',
            button_text='-2',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#7209B7')
        ),
        sg.Button(
            key='-LESS3-',
            button_text='-3',
            border_width=3, pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#7209B7')
        ),
        sg.Button(
            key='-LESS4-',
            button_text='-4',
            border_width=3,
            pad=(1, 2),
            size=(5, 1),
            font='Any 15 bold',
            button_color=('#FFFFFB', '#7209B7')
        )
    ]
]

homeLayout = [
    [
        sg.Column(functionLayout),
        sg.VSeperator(),
        sg.Column(viewLayout),
    ],

    [sg.HSeparator()],
    [sg.Column(countLayout)]
]

# window
window = sg.Window('AxieCount', layout=homeLayout, size=(320, 250))


# events
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break

window.close()
