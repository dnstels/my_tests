import dash_bootstrap_components as dbc
from dash import html


class CardIndicator(dbc.Card):
    def __init__(self, header: str, top:int , body: str, diff_portent: float):
        empty='Empty'
        children=[
            dbc.CardHeader(header),
            dbc.CardBody(
                [
                html.P(empty,className='hidden')
                    if top==None
                    else html.P(top),
                html.H5(empty,className='hidden')
                    if body==None
                    else html.H5(body),
                html.P(empty,className='hidden')
                    if diff_portent==None
                    else self._set_footer(diff_portent),
                ]
            )
        ]
        super(CardIndicator, self).__init__(children=children,
                                        class_name=['indicator','w-75'])
    def _set_footer(self, diff_portent):
        if diff_portent<0:
            diff_color='procent_diff_down' 
            diff_sign='▼'
        else: 
            diff_color='procent_diff_up'
            diff_sign='▲'
        return html.P(f'{diff_portent}% {diff_sign}',className=diff_color)

class Workload(CardIndicator):
    def __init__(self, year, portent, diff_portent):
        header='Плановая загрузка'
        super(Workload, self).__init__(header, year, f'{portent}%',diff_portent)

class WorkCount(CardIndicator):
    def __init__(self, count):
        header='Общая численность'
        super(WorkCount,self).__init__(header, None, count, None)