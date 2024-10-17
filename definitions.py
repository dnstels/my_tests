from sixgill.definitions import Connection,Parameters,ModelComponents

class Orientation():
    SOURCE: Connection.SOURCE
    DESTINATION: Connection.DESTINATION

ORIENTATION_MAP_RU={
    Orientation.SOURCE: "Начало",
    Orientation.DESTINATION: "Конец",
}
class Properties():
    class Flowline():
        HORIZONTALDISTANCE: Parameters.Flowline.HORIZONTALDISTANCE
        ELEVATIONDIFFERENCE: Parameters.Flowline.ELEVATIONDIFFERENCE
        INNERDIAMETER: Parameters.Flowline.INNERDIAMETER
        WALLTHICKNESS: Parameters.Flowline.WALLTHICKNESS
        ROUGHNESS: Parameters.Flowline.ROUGHNESS
        AMBIENTAIRTEMPERATURE: Parameters.Flowline.AMBIENTAIRTEMPERATURE # Temperature
        UCOEFFUSERAIR: Parameters.Flowline.HeatTransfer.UCOEFFUSERAIR
        UCOEFFUSER: Parameters.Flowline.HeatTransfer.UCOEFFUSER
    class Source(): 
        pass
    class Sink():
        pass



class Components():
    FLOWLINE: ModelComponents.FLOWLINE
    SOURCE: ModelComponents.SOURCE
    SINK: ModelComponents.SINK
    JUNCTION: ModelComponents.JUNCTION
    CHOKE: ModelComponents.CHOKE
    
COMPONENTS_MAP_RU={
    Components.FLOWLINE: 'Трубопровод',
    Components.SOURCE: 'Источник',
    Components.SINK: 'Сток',
    Components.JUNCTION: 'Узел',
    Components.CHOKE: 'Штуцер',
}
MAP_RU={
    NETWORK: 'Сеть'
}
