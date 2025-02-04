import dash_bootstrap_components as dbc
from dash import Dash, Output, Input, State, html, dcc, callback, MATCH
import uuid


class CardFilter(dbc.Card):
    
    class ids:
        dropdown = lambda aio_id: {
            'component': 'CardFilter',
            'subcomponent': 'dropdown',
            'aio_id': aio_id
        }
        dropdown_check_mode = lambda aio_id: {
            'component': 'CardFilter',
            'subcomponent': 'dropdown_check_mode',
            'aio_id': aio_id
        }

    __dropdown_props=[]
    __dropdown_props_options=[]
    __dropdown_props_values=[]
    
    def __init__(
            self,
            description=None,
            # dropdown_props=None,
            dropdown_props_options=None,
            dropdown_props_values=None,
            dropdown_mode=None,
            aio_id=None
            ):
        empty='Empty'
        if aio_id is None: aio_id = str(uuid.uuid4())
        # dropdown_props = dropdown_props.copy() if dropdown_props else {}
        dropdown_props = {}
        # dropdown_props['options'] = dropdown_props_options \
        #     if dropdown_props_options else []
        # dropdown_props['value'] = dropdown_props_values \
        #     if dropdown_props_values else None

        CardFilter.__dropdown_props=dropdown_props
        CardFilter.__dropdown_props_options=dropdown_props_options
        CardFilter.__dropdown_props_values=dropdown_props_values
        
        children=[
            dbc.CardHeader(html.Div([
                f"{description}:" if description else '',
                dbc.Checklist(id=self.ids.dropdown_check_mode(aio_id),
                    options=[
                        {"label": "Несколько", "value": 1},
                    ],style={"display": "inline-block", "margin": "0px 5px"},
                value=[dropdown_mode] if dropdown_mode else []),
            ])),
            dbc.CardBody([dcc.Dropdown(
                options=dropdown_props_options,
                value=dropdown_props_values,
                id=self.ids.dropdown(aio_id),
                placeholder="Выбрать ...",
                multi=True,),
                      ],
            ),
        ]
        super(CardFilter, self).__init__(children=children)

    @callback(
        Output(ids.dropdown(MATCH), 'multi'),
        Output(ids.dropdown(MATCH), 'value'),
        Input(ids.dropdown_check_mode(MATCH), 'value'),
    )
    def update_dropdown_mode(check_mode):
        _dropdown_props=CardFilter.__dropdown_props_options
        multi_mode=check_mode.__contains__(1)
        dropdown_value=[
            _dropdown_props[i]['value'] \
                for i in range(len(_dropdown_props))
        ] if multi_mode and _dropdown_props else None
        return multi_mode,dropdown_value



if __name__ == '__main__':
    from dash import Dash
    app = Dash()
    dropdown_props={}
    dropdown_props_options = [
                {'label': f'Option {i}', 'value': f'Option {i}'} \
                    for i in range(1,11)
            ]
    
    app.layout = html.Div( [
        CardFilter(aio_id='filter-picker',
            description="Подразделение",
            # dropdown_mode=1,
            dropdown_props_options=dropdown_props_options,
            # dropdown_props_options=[],
        ),
        html.Div(id='test-result-output')
    ] )

    @callback(
        Output('test-result-output', 'children'),
        Input(CardFilter.ids.dropdown('filter-picker'), 'value'),
        Input(CardFilter.ids.dropdown_check_mode('filter-picker'), 'value'),
        State('test-result-output', 'children'),
    )
    def display_filter(value,mode,state):
        
        return f'You have selected {mode} => {value} => {state}'

    app.run(debug=True)
