import dash_bootstrap_components as dbc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, ctx
import pandas as pd
import plotly.express as px
from urllib.parse import quote

from controls.indicators import WorkCount, Workload
import get_rest

df = pd.read_csv('gapminder2007.csv')
app = Dash()

def get_department():
    return [f"name{name}" for name in range(20)]

departments=get_department()

inform_row=html.Div([
    html.Div(f"по состоянию на {12} (номер недели :{49})",
             className='header_info_line'),
    html.Div(f"номер текущей недели :{4}",className='header_info_line'),
    dbc.ListGroupItem(
        "I. Производственная загрузка подразделений филиала (чел.-час)",
        color="dark"),
])

indicators_row=dbc.Row(id='indicators',children=[])

controls = dbc.Card(
    [
        dbc.CardHeader("Подразделение"),
        dcc.Dropdown(departments,value=departments,id='demo-dropdown',
                      multi=True,),
    ],
    body=False,
)

data_row = dbc.Row(
    [
        html.Br(),
        dbc.Col(controls,width={"size": 2, "order": 1},
        ),
        dbc.Col(
            dbc.Card(
            [
                dbc.Label("Тип диаграммы:"),
                dcc.RadioItems(['area', 'histogram'], 'area', 
                               id='controls-type-graph',inline=True),
                dcc.Graph(figure={}, id='controls-and-graph'),
            ],
                    body=True),
                width={"size": 10, "order": 2}),

            
    ],
)

app.layout = html.Div( [
    html.Div(
             children=[
    html.Img(src=r'assets/img/app_logo.jpg',width="100", height="50",
             style={'margin':'0 10px'}),
    dbc.Col([html.H5(children=[
        '''РЕСУРСНЫЙ ПЛАН ПРОИЗВОДСТВЕННЫХ ПОДРАЗДЕЛЕНИЙ ''',html.Br(),
        '''САРАТОВСКОГО ФИЛИАЛА (ПО БЮДЖЕТАМ ПРОЕКТОВ И РАЗБИВКАМ)'''],
        className='header_caption',
    )]),
    ], style={'display': 'flex'}),
    inform_row,
    html.Br(),
    indicators_row,
    html.Br(),
    # controls,
    html.Br(),
    data_row,
    html.Br(),
    html.Div(id="output"),
],style={"padding": "10px"})

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    [
        Input(component_id='controls-type-graph', component_property='value'),
        Input(component_id='demo-dropdown', component_property='value'),
    ]
)
def update_graph(type_graph,value):
    button_id = ctx.triggered_id
    print(button_id)
    global graph_data
    if button_id != 'controls-type-graph':
        s= value if value == None else quote(','.join([item for item in value]))
        error,df=get_rest.get_LabourCost(s)
        graph_data=df

    if type_graph=='area':
        fig = px.area(graph_data, x='week_num', y='labor_costs')
    else:
        fig=px.histogram(graph_data,x='week_num', y='labor_costs',histfunc='avg')
    
    fig.update_xaxes(title_text='Неделя')
    fig.update_yaxes(title_text='Трудозатраты')

    red_line_lost = 0 if len(graph_data['labor_costs'])<=0 else graph_data['labor_costs'].max()+3
    fig.add_hline(y=red_line_lost, line_color='red')

    return fig


@app.callback(Output("output", "children"), [Input("demo-dropdown", "value")])
def display_value(value):
    s='' if value == None else quote(','.join([item for item in value]))
    return f"Selected value: {s}"

@app.callback(
        Output('indicators',component_property='children'),
        Input("demo-dropdown", "value"))
def update_indicators(value):
    year=2025
    pre_year=year-1
    worker_count=291
    # return dbc.Col([Workload(2024,86,None),],width={"size": 2, "order": 1},)
    return [
        dbc.Col([Workload(year,86,None),],width={"size": 2, "order": 1},),
        dbc.Col([Workload(pre_year,40,-45),],width={"size": 2, "order": 2},),
        dbc.Col([WorkCount(worker_count)],width={"size": 2, "order": 3},),
    ]
    

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=False, host='0.0.0.0', port=8050)
