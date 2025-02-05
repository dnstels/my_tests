from datetime import date, datetime, timedelta
import dash
import flask
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Output, Input, ctx
import plotly.graph_objects as go

from controls.indicators import WorkCount, Workload
import get_rest

cookie_department="dash departments"
cookie_multi_department="dash multi_departments"
cookie_period_type="dash period_type"

app = Dash()

def update_text_error(errors):
    errors=[""]+errors
    err_body='\n- '.join(errors)
    txt=f"""
### Ошибка сервера данных:
{err_body}
    """
    return len(errors)>1,dcc.Markdown(txt)

def get_department():
    errors=[]
    error,df=get_rest.get_departments()
    if error!=None:
        errors.append(error)
        departments=[]
    else:
        departments=[name for name in df['departmentCode']]
    err_is_open,err_body=update_text_error(errors)
    return err_is_open,err_body,departments

err_is_open,err_body,departments=get_department()

today=date.today()
yesterday = today - timedelta(days=1)

inform_row=html.Div([
    html.Div(f"по состоянию на {yesterday} (номер недели :{yesterday.isocalendar()[1]})",
             className='header_info_line'),
    html.Div(f"номер текущей недели :{today.isocalendar()[1]}",className='header_info_line'),
    dbc.ListGroupItem(
        "I. Производственная загрузка подразделений филиала (чел.-дн)",
        color="dark"),
])

controls = dbc.Card(
    [
        dbc.CardHeader(html.Div(["Подразделение",
            dbc.Checklist(id="mode-department-dropdown",
                options=[
                    {"label": "Несколько", "value": 1},
                ],style={"display": "inline-block", "margin": "0px 5px"},value=[1]),
                        ])),
        dbc.CardBody([dcc.Dropdown(options=departments,value=[],id='department-dropdown',
                      placeholder="Выбрать подразделение",multi=True,),
                      ],
                    )
    ],style={"padding":"0px"},
    body=False,
)

data_row = dbc.Row(
    [
        html.Br(),
        dbc.Col(
            [
                dbc.Row(
                    [dbc.Card(
                        [
                            dbc.CardHeader("Тип среза:"),
                            dbc.CardBody(
                                [dcc.Dropdown(
                                id="control-period-type",
                                options=[{"label": "Неделя", "value": 0}, 
                                {"label": "Месяц", "value": 1}],
                                value=0,
                                clearable=False
                                )]
                                )
                        ],style={
                            "margin": "0px 0px 20px 0px",
                            'padding':'0px'
                            },
                    ),
                     controls
                    ],
                ),
            ], 
            width={"size": 2, "order": 1}
        ),
        dbc.Col(
            dbc.Card(
            [
                dcc.Graph(figure={}, id='controls-and-graph',config={'displaylogo': False}),
            ],
            body=True),
        width={"size": 10, "order": 2}),
    ],style={"padding": "10px"}
)

app.layout = html.Div( [
    html.Div(
             children=[
    html.Img(src=r'assets/img/app_logo.png',width="100", height="50",
             style={'margin':'0 10px'}),
    dbc.Col([html.H5(children=[
        '''РЕСУРСНЫЙ ПЛАН ПРОИЗВОДСТВЕННЫХ ПОДРАЗДЕЛЕНИЙ ''',html.Br(),
        '''САРАТОВСКОГО ФИЛИАЛА (ПО БЮДЖЕТАМ ПРОЕКТОВ И РАЗБИВКАМ)'''],
        className='header_caption',
    )]),
    ], style={'display': 'flex'}),
    inform_row,
    html.Br(),
    dbc.Alert(children=err_body, color="danger",
            id='errors-alert',
            dismissable=True,
            is_open=err_is_open,
            # duration=4000,
    ),
    dbc.Row(id='indicators',children=[]),
    html.Br(),
    data_row,
    html.Br(),
    html.Div(id="output"),
],style={"padding": "10px"})

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Output('indicators',component_property='children'),
    Output('errors-alert',component_property='is_open'),
    Output('errors-alert',component_property='children'),
    [
        Input(component_id='department-dropdown', component_property='value'),
        Input('mode-department-dropdown',component_property='value'),
        Input('control-period-type',component_property='value'),
    ]
)
def update_graph(department_dropdown_value,multi_department,
                 period_type):
    global graph_data
    global red_line_lost
    errors=[]
    error,df=get_rest.get_LabourCost(department_dropdown_value,
                                        period_type)
    if error!=None: errors.append(error)

    graph_data=df
    error,red_line_lost=get_rest.get_ScheduledTime(department_dropdown_value)
    red_line_lost = 0 if red_line_lost==None else red_line_lost
    if error!=None: errors.append(error)

    layout = go.Layout(
        plot_bgcolor='#fff',
        legend=dict(
            x=.5, 
            y=1.2, 
            orientation='h',
            xanchor="center",
            yanchor="top",
            font=dict(
                size=12,),
        ),
    )

    fig = go.Figure(layout = layout)
    fig.add_trace(go.Bar(
            name="Трудозатраты, чел.дн",
            showlegend=True,
            x=graph_data['group_name'], y=graph_data['labor_costs'],
            marker_color='#88CBFF',
            # visible="legendonly"
        ),
    )
    fig.add_trace(go.Scatter(
            name="Трудозатраты, чел.дн",
            showlegend=True,
            x=graph_data['group_name'], y=graph_data['labor_costs'],
            # hoverinfo='x+y',
            mode='lines',
            # line=dict(width=0.5, color='rgb(131, 90, 241)'),
            stackgroup='one',
            marker_color='#6666FF',
        )
    )
    fig.add_hline(name="ФРВ",y=float(red_line_lost),
                  line_color='red',#line_dash="dot",
                  annotation_text=f"ФРВ {red_line_lost}",
                  annotation_position="top left",
                  showlegend=True,
    )

    if period_type==0: fig.update_xaxes(title_text='Неделя',gridcolor='#EFDECD')
    else: fig.update_xaxes(title_text="Месяц",tickangle=45,gridcolor='#EFDECD')
    
    fig.update_yaxes(title_text='Трудозатраты',gridcolor='#EFDECD')


    value_cookie_department=','.join(department_dropdown_value) \
        if multi_department.__contains__(1) else department_dropdown_value

    if value_cookie_department == '' or value_cookie_department == None:
        dash.callback_context.response.set_cookie(
            cookie_department,'', expires=0)
    else:
        dash.callback_context.response.set_cookie(
                cookie_department,value_cookie_department)
    
    dash.callback_context.response.set_cookie(
            cookie_period_type,str(period_type))
    
    err_is_show,err_text=update_text_error(errors)

    return fig,update_indicators(red_line_lost),err_is_show,err_text

@app.callback(
        [
            Output("department-dropdown", "value"),
            Output('mode-department-dropdown',component_property='value'),
            Output("department-dropdown", "multi"),
            Output("control-period-type", "value"),
        ],
        [Input("mode-department-dropdown", "value")])
def set_startup_value_or_mode_department_dropdown(multi_department_in):
    cookies=flask.request.cookies
    period_type=int(cookies[cookie_period_type]) \
        if cookie_period_type in cookies else 0
    if ctx.triggered_id == "mode-department-dropdown":
        if multi_department_in.__contains__(1):
            dash.callback_context.response.set_cookie(
                cookie_multi_department,'1')
            department_dropdown_value=departments
            department_dropdown_multi=True
        else:
            dash.callback_context.response.set_cookie(
                cookie_multi_department,'', expires=0)
            department_dropdown_value=''
            department_dropdown_multi=False
        return department_dropdown_value, \
            multi_department_in, department_dropdown_multi, period_type
    else:
        multi_department=[1]  if cookie_multi_department in cookies else []
        department_dropdown_multi= multi_department.__contains__(1)

        if cookie_department in cookies:        
            department_dropdown_value=cookies[cookie_department].split(',') if multi_department.__contains__(1)\
                else cookies[cookie_department]
        else:
            department_dropdown_value=departments if multi_department.__contains__(1)\
                else ''
        
        return department_dropdown_value, multi_department,\
            department_dropdown_multi, period_type


@app.callback(Output("output", "children"), [Input("department-dropdown", "value")])
def display_value(value):
    return f"Selected value: {','.join(value)if type(value)==list else value}"

def update_indicators(fwt):
    year=datetime.now().year
    pre_year=year-1
    worker_count='-' if fwt==None else str(int(int(fwt)/5))
    procent='-'
    pre_procent='-'
    diff_procent=0
    return [
        dbc.Col([Workload(pre_year,pre_procent,None),],width={"size": 2, "order": 1},),
        dbc.Col([Workload(year,procent,diff_procent),],width={"size": 2, "order": 2},),
        dbc.Col([WorkCount(worker_count)],width={"size": 2, "order": 3},),
    ]


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=False, host='0.0.0.0', port=8050)
