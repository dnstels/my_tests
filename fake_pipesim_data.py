
import sys
from typing import OrderedDict

from numpy import nan
sys.path.append('.')

class Model():pass

def get_names(model:Model):
    return {
        'Flowline': ['kg202-205.Flowline_1', 'kg202.Flowline_1', 'kg205.Flowline_1'], 
        'Source': ['KG_205', 'KG_202'], 
        'Sink': ['u2-202-205'], 
        'Junction': ['t-u2-202-205'], 
        'Choke': ['Ck', 'Ckc']
    }

def get_data_flowlines(model:Model):
    return ( { 'kg202-205.Flowline_1': {
            'GeometryProfile': '<sixgill.core.flowline_profile.FlowlineGeometryProfile object at 0x0000020588321F40>', 
            'HorizontalDistance': 8197.999999999998, 
            'ElevationDifference': 80.0000000000004, 
            'InnerDiameter': 360.0, 
            'WallThickness': 32.99999999999999, 
            'Roughness': 0.09999999999999999, 
            'AmbientAirTemperature': 13.100000000000023, 
            'UCoeffUserAir': 3.302207673790568, 
            'UCoeffUser': 3.302207673790568
        }, 'kg202.Flowline_1': {
            'GeometryProfile': '<sixgill.core.flowline_profile.FlowlineGeometryProfile object at 0x0000020588321EB0>', 
            'HorizontalDistance': 1160.9999999999998, 
            'ElevationDifference': -96.00000000000036, 
            'InnerDiameter': 273.0, 
            'WallThickness': 26.0, 
            'Roughness': 0.09999999999999999, 
            'AmbientAirTemperature': 13.100000000000023, 
            'UCoeffUserAir': 4.272856596086583, 
            'UCoeffUser': 4.272856596086583
            }, 'kg205.Flowline_1': {
                'GeometryProfile': '<sixgill.core.flowline_profile.FlowlineGeometryProfile object at 0x000002058835D7F0>', 
                'HorizontalDistance': 11086.0, 
                'ElevationDifference': 89.99999999999979, 
                'InnerDiameter': 273.0, 
                'WallThickness': 26.0, 
                'Roughness': 0.09999999999999999, 
                'AmbientAirTemperature': 13.100000000000023, 
                'UCoeffUserAir': 4.272856596086583, 
                'UCoeffUser': 4.272856596086583
            }
        },{
            'kg202-205.Flowline_1': [
                {'MeasuredDistance': 0.0, 'HorizontalDistance': 0.0, 'Elevation': 1019.9999999999997}, 
                {'MeasuredDistance': 839.0, 'HorizontalDistance': 839.0, 'Elevation': 1019.9999999999997}, 
                {'MeasuredDistance': 1257.9140723346495, 'HorizontalDistance': 1256.0, 'Elevation': 1059.9999999999993}, 
                {'MeasuredDistance': 3028.9140723346495, 'HorizontalDistance': 3026.9999999999977, 'Elevation': 1059.9999999999993}, 
                {'MeasuredDistance': 3711.087803872298, 'HorizontalDistance': 3707.999999999998, 'Elevation': 1100.0}, 
                {'MeasuredDistance': 4171.827426652888, 'HorizontalDistance': 4166.999999999999, 'Elevation': 1139.9999999999998}, 
                {'MeasuredDistance': 4420.632571294232, 'HorizontalDistance': 4414.999999999998, 'Elevation': 1159.9999999999986}, 
                {'MeasuredDistance': 4834.632571294232, 'HorizontalDistance': 4828.999999999997, 'Elevation': 1159.9999999999986}, 
                {'MeasuredDistance': 5568.0908182313015, 'HorizontalDistance': 5560.000000000001, 'Elevation': 1100.0}, 
                {'MeasuredDistance': 6071.488275515305, 'HorizontalDistance': 6062.999999999998, 'Elevation': 1079.9999999999995}, 
                {'MeasuredDistance': 6870.488275515305, 'HorizontalDistance': 6861.999999999999, 'Elevation': 1079.9999999999995}, 
                {'MeasuredDistance': 8206.63796772797, 'HorizontalDistance': 8197.999999999998, 'Elevation': 1100.0}], 
            'kg202.Flowline_1': [
                {'MeasuredDistance': 0.0, 'HorizontalDistance': 0.0, 'Elevation': 1116.0}, 
                {'MeasuredDistance': 358.35736353534026, 'HorizontalDistance': 357.9999999999999, 'Elevation': 1100.0}, 
                {'MeasuredDistance': 1165.3325800073208, 'HorizontalDistance': 1160.9999999999998, 'Elevation': 1019.9999999999997}], 
            'kg205.Flowline_1': [
                {'MeasuredDistance': 0.0, 'HorizontalDistance': 0.0, 'Elevation': 929.9999999999999}, 
                {'MeasuredDistance': 386.12951195162486, 'HorizontalDistance': 385.99999999999994, 'Elevation': 940.0000000000001}, 
                {'MeasuredDistance': 1008.1496080900052, 'HorizontalDistance': 1007.9999999999994, 'Elevation': 944.9999999999991}, 
                {'MeasuredDistance': 1880.1639428345666, 'HorizontalDistance': 1880.0000000000002, 'Elevation': 940.0000000000001}, 
                {'MeasuredDistance': 2701.4075120635744, 'HorizontalDistance': 2700.999999999998, 'Elevation': 959.9999999999994}, 
                {'MeasuredDistance': 3619.6253511409905, 'HorizontalDistance': 3618.999999999997, 'Elevation': 979.9999999999999}, 
                {'MeasuredDistance': 3880.3934473490963, 'HorizontalDistance': 3878.999999999998, 'Elevation': 999.9999999999992}, 
                {'MeasuredDistance': 4191.037938689277, 'HorizontalDistance': 4189.0, 'Elevation': 1019.9999999999997}, 
                {'MeasuredDistance': 4518.648988563972, 'HorizontalDistance': 4515.999999999999, 'Elevation': 1039.9999999999998}, 
                {'MeasuredDistance': 5161.959955359969, 'HorizontalDistance': 5159.0, 'Elevation': 1059.9999999999993}, 
                {'MeasuredDistance': 5647.3721513336595, 'HorizontalDistance': 5643.999999999998, 'Elevation': 1079.9999999999995}, 
                {'MeasuredDistance': 6760.551831349424, 'HorizontalDistance': 6757.0, 'Elevation': 1059.9999999999993}, 
                {'MeasuredDistance': 8821.64886933672, 'HorizontalDistance': 8817.999999999996, 'Elevation': 1079.9999999999995}, 
                {'MeasuredDistance': 9147.64886933672, 'HorizontalDistance': 9143.999999999995, 'Elevation': 1079.9999999999995}, 
                {'MeasuredDistance': 10174.64886933672, 'HorizontalDistance': 10170.999999999995, 'Elevation': 1079.9999999999995}, 
                {'MeasuredDistance': 11091.613972271394, 'HorizontalDistance': 11086.0, 'Elevation': 1019.9999999999997}
            ]})
        

def get_network(model:Model):
    return [
        {'Source': 'kg202-205.Flowline_1', 'Source Port': '', 'Destination': 'u2-202-205'}, 
        {'Source': 't-u2-202-205', 'Source Port': '', 'Destination': 'kg202-205.Flowline_1'}, 
        {'Source': 'Ck', 'Source Port': '', 'Destination': 'kg202.Flowline_1'}, 
        {'Source': 'kg205.Flowline_1', 'Source Port': '', 'Destination': 't-u2-202-205'}, 
        {'Source': 'Ck', 'Source Port': '', 'Destination': 'KG_202'}, 
        {'Source': 'KG_205', 'Source Port': '', 'Destination': 'Ckc'}, 
        {'Source': 'Ckc', 'Source Port': '', 'Destination': 'kg205.Flowline_1'}, 
        {'Source': 'kg202.Flowline_1', 'Source Port': '', 'Destination': 't-u2-202-205'}
        ]

def get_indata(model:Model):
    return {
        'KG_205': {'Pressure': 169.1429, 'Temperature': 18.58113437096472, 'GasFlowRate': nan}, 
        'KG_202': {'Pressure': 159.4642, 'Temperature': 22.833473878316795, 'GasFlowRate': nan}, 
        'u2-202-205': {'Pressure': nan, 'GasFlowRate': 7.000000000002465}
    }

def get_simulation_(model:Model):
    # pd.DataFrame.from_dict(simulation.system, orient="index").to_dict()
    return {'Unit': {'SystemOutletPressure': 'bara', 
                                  'SystemOutletTemperature': 'degC', 
                                  'OutletVolumeFlowrateGasStockTank': 'mmsm3/d', 
                                  'SystemInletPressure': 'bara', 
                                  'MaximumVelocityGas': 'm/s', 
                                  'SystemTemperatureDifference': 'degC', 
                                  'OutletMassFlowrateFluid': 'kg/s'}, 
                         'u2-202-205': {'SystemOutletPressure': 148.4502232017729, 
                                        'SystemOutletTemperature': 13.320182012157034, 
                                        'OutletVolumeFlowrateGasStockTank': 0.6999924477544864, 
                                        'SystemInletPressure': 151.61798436814473, 
                                        'MaximumVelocityGas': 0.5259175107027361, 
                                        'SystemTemperatureDifference': 2.5634229813988725, 
                                        'OutletMassFlowrateFluid': 6.455140336557102}, 
                        'KG_202': {'SystemOutletPressure': 151.60039914333154, 
                                   'SystemOutletTemperature': 19.229520343329, 
                                   'OutletVolumeFlowrateGasStockTank': 0.2999924477547715, 
                                   'SystemInletPressure': 150.0023396701707, 
                                   'MaximumVelocityGas': 0.3364579881446892, 
                                   'SystemTemperatureDifference': 3.6038129900044, 
                                   'OutletMassFlowrateFluid': 2.76644891866537}, 
                        'KG_205': {'SystemOutletPressure': 151.61797432694075, 
                                   'SystemOutletTemperature': 13.374231654160042, 
                                   'OutletVolumeFlowrateGasStockTank': 0.4000000000001426, 
                                   'SystemInletPressure': 169.99713582035892, 
                                   'MaximumVelocityGas': 0.4849806385787681, 
                                   'SystemTemperatureDifference': 5.2068794569511, 
                                   'OutletMassFlowrateFluid': 3.6886914178956753}
    }

def get_conditions(model:Model):
    return {
        'KG_205': {'Temperature': 18.58113437096472, 'Pressure': 170.0, 'FlowRateType': 'GasFlowRate', 'GasFlowRate': nan}, 
        'u2-202-205': {'Temperature': nan, 'Pressure': nan, 'FlowRateType': 'GasFlowRate', 'GasFlowRate': 0.7000000000002481}, 
        'KG_202': {'Temperature': 22.833473878316795, 'Pressure': 150.0, 'FlowRateType': 'GasFlowRate', 'GasFlowRate': nan}
        }

def get_constraints(model:Model):
    return {'KG_202': {'GasFlowRate': 0.3000000000001063}, 'KG_205': {'GasFlowRate': 0.40000000000014174}}

def get_simulation(model:Model):
    return {
        'OutletVolumeFlowrateGasStockTank': OrderedDict([('Unit', 'mmsm3/d'), ('KG_202', 0.2999924477547715), ('KG_205', 0.4000000000001426), ('u2-202-205', 0.6999924477544864)]), 
        'OutletMassFlowrateFluid': OrderedDict([('Unit', 'kg/s'), ('KG_205', 3.6886914178956753), ('KG_202', 2.76644891866537), ('u2-202-205', 6.455140336557102)]), 
        'SystemOutletTemperature': OrderedDict([('Unit', 'degC'), ('u2-202-205', 13.320182012157034), ('KG_205', 13.374231654160042), ('KG_202', 19.229520343329)]), 
        'MaximumVelocityGas': OrderedDict([('Unit', 'm/s'), ('u2-202-205', 0.5259175107027361), ('KG_202', 0.3364579881446892), ('KG_205', 0.4849806385787681)]), 
        'SystemInletPressure': OrderedDict([('Unit', 'bara'), ('KG_202', 150.0023396701707), ('KG_205',169.99713582035892), ('u2-202-205', 151.61798436814473)]), 
        'SystemTemperatureDifference': OrderedDict([('Unit', 'degC'), ('u2-202-205', 2.5634229813988725), ('KG_205', 5.2068794569511), ('KG_202', 3.6038129900044)]), 
        'SystemOutletPressure': OrderedDict([('Unit', 'bara'), ('KG_202', 151.60039914333154), ('u2-202-205', 148.4502232017729), ('KG_205', 151.61797432694075)])
        }
