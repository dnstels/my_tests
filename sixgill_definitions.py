#Schlumberger Private
#Copyright (c) 2020 Schlumberger

from enum import Enum
"""The definitions sub-module maintains the enumerations and static classes
    that are available in the PIPESIM Python Toolkit.
"""

# The PIPESIM Python Toolkit version
PYTHON_TOOLKIT_VERSION = '2021.1'

# Globally available constants
NAN = float('NaN')
ALL = '___ALL___'
NONE = '___NONE___'
TEMPLATE = '___TEMPLATE___'
GLOBAL = 'Global'
DEFAULT = 'Default'
AT_TYPE = "@type"
AT_ID = "@id"


class Units:
    """ Available unit of measurement categories """
    METRIC = "PIPESIM_METRIC"
    SI = "PIPESIM_SI"
    FIELD = "PIPESIM_FIELD"


class Tasks:
    """ Available PIPESIM simulation tasks """
    NETWORKSIMULATION = "NetworkSim"
    NETWORKOPTIMIZERSIMULATION = "NetworkOptSim"
    PTPROFILESIMULATION = "PTProfileSim"
    NODALANALYSISOPERATION = "NodalAnalysisOp"
    WELLPERFORMANCECURVESOPERATION = "WellPerformanceCurvesSim"
    SYSTEMANALYSISOPERATION = "SystemAnalysisOp"
    GLDIAGNOSTICSOPERATION = "GLDiagnosticsOp"
    VFPTABLESSOPERATION = "VfpTablesOp"


class Connection:
    SOURCE = "Source"
    DESTINATION = "Destination"
    SOURCEPORT = "Source Port"

    class Separator:
        TOP = "Top Port"
        BOTTOM = "Bottom Port"
        BOOT = "Boot Port"


class SimulationState:
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

class SimulationOptions:
    PARALLELISM = "Parallelism"
    RESTART = "Restart"
    GENERATEOUTPUTFILE = "GenerateOutputFile"

class ModelComponents:
    """ Available model components """
    BLACKOILFLUID = "BlackOilFluid"
    BOUNDARY = "Boundary"
    CASING = "Casing"
    CHECKVALVE = "CheckValve"
    CHOKE = "Choke"
    COMPLETION = "Completion"
    COMPLETIONCONINGPOINT = "CompletionConingPoint"
    COMPLETIONMODEL = "CompletionModel"
    COMPOSITIONALFLUID = "CompositionalFluid"
    COMPRESSOR = "Compressor"
    ENGINEKEYWORDS = "EngineKeywords"
    ESP = "ESP"
    EXPANDER = "Expander"
    FILEBASEDFLUID = "FileBasedFluid"
    FLOWLINE = "Flowline"
    FLUIDCOMPONENT = "FluidComponent"
    GASLIFTINJECTION = "GasLiftInjection"
    GENERICEQUIPMENT = "GenericEquipment"
    PUMP = "Pump"
    GRAVELPACK = "GravelPack"
    HEATEXCHANGER = "HeatExchanger"
    INJECTOR = "Injector"
    IPRBACKPRESSURE = "IPRBackPressure"
    IPRDARCY = "IPRDarcy"
    IPRTRILINEAR = "IPRTriLinear"
    IPRFETKOVITCH = "IPRFetkovitch"
    IPRFORCHHEIMER = "IPRForchheimer"
    IPRHORIZONTALPI = "IPRHorizontalPI"
    IPRHYDRAULICFRACTURE = "IPRHydraulicFracture"
    IPRJONES = "IPRJones"
    IPRPIMODEL = "IPRPIModel"
    IPRPSSBABUODEH = "IPRPSSBabuOdeh"
    IPRSSJOSHI = "IPRSSJoshi"
    IPRVOGEL = "IPRVogel"
    JUNCTION = "Junction"
    LINER = "Liner"
    MEASUREMENTPOINT = "MeasurementPoint"
    MFLFLUID = "MFLFluid"
    MULTIPLIERADDER = "MultiplierAdder"
    MULTIPHASEBOOSTER = "MultiphaseBooster"
    GENERICBOOSTER = "GenericBooster"
    ONESUBSEABOOSTER = "OneSubseaBooster"
    WETGASCOMPRESSOR = "WetGasCompressor"
    OPEN_HOLE = "OpenHole"
    PACKER = "Packer"
    PCP = "PCP"
    PUMP = "Pump"
    PVTFLUID = "PVTFluid"
    RODPUMP = "RodPump"
    SINGLEPHASESEPARATOR = "SinglephaseSeparator"
    SINK = "Sink"
    SLIDINGSLEEVE = "SlidingSleeve"
    SOURCE = "Source"
    SPOTREPORT = "SpotReport"
    STUDY = "Study"
    SUBSURFACESAFETYVALVE = "SubsurfaceSafetyValve"
    THREEPHASESEPARATOR = "ThreePhaseSeparator"
    TUBING = "Tubing"
    TUBINGPLUG = "TubingPlug"
    TWOPHASESEPARATOR = "TwoPhaseSeparator"
    WATERTEMPVELOCITYSURVEY = "WaterTempVelocitySurvey"
    WELL = "Well"
    NETWORKSIMULATION = Tasks.NETWORKSIMULATION
    NETWORKOPTIMIZERSIMULATION = Tasks.NETWORKOPTIMIZERSIMULATION
    PTPROFILESIMULATION = Tasks.PTPROFILESIMULATION
    NODALANALYSISOPERATION = Tasks.NODALANALYSISOPERATION
    WELLPERFORMANCECURVESOPERATION = Tasks.WELLPERFORMANCECURVESOPERATION
    SYSTEMANALYSISOPERATION = Tasks.SYSTEMANALYSISOPERATION
    GLDIAGNOSTICSOPERATION = Tasks.GLDIAGNOSTICSOPERATION
    VFPTABLESOPERATION = Tasks.VFPTABLESSOPERATION
    GLOBALCATALOG = 'GlobalCatalog'
    RISKINDEXLIMITS = "RiskIndexLimits"
    FLOWCORRELATION = "FlowCorrelation"
    HEATTRANSFEROPTIONS = "HeatTransferOptions"


class Parameters:
    """ Available parameters by model component """

    # #############################################################################
    # Abstract parameters -- they will be mixed in with the concrete classes below
    # #############################################################################
    class Location:
        LATITUDE = "Latitude"
        LONGITUDE = "Longitude"
        NONCLUSTEREDLATITUDE = "SchematicLatitude"
        NONCLUSTEREDLONGITUDE = "SchematicLongitude"
        ELEVATION = "Elevation"

    class SchematicPosition:
        X_COORD = "X"
        Y_COORD = "Y"

    class DownholeLocation:
        TOPMEASUREDDEPTH = "TopMeasuredDepth"
        BOTTOMMEASUREDDEPTH = "BottomMeasuredDepth"

    class ModelComponent:
        NAME = "Name"
        ISACTIVE = "IsActive"

    class DownholeComponent(ModelComponent, DownholeLocation):
        pass

    class SurfaceComponent(ModelComponent, Location, SchematicPosition):
        pass

    class DownholeOrSurfaceComponent(ModelComponent, DownholeLocation, Location, SchematicPosition):
        pass

    class AbstractTubingSection(DownholeComponent):
        ISFLOWPRESENTINSIDE = "IsFlowPresentInside"
        TOPMEASUREDDEPTH = "TopMeasuredDepth"
        GRADE = "Grade"
        DENSITY = "Density"
        BOREHOLEDIAMETER = "BoreholeDiameter"
        CEMENTTOP = "CementTop"
        CEMENTDENSITY = "CementDensity"
        ANNULUSMATERIALTYPE = "AnnulusMaterialType"
        ANNULUSMATERIALDENSITY = "AnnulusMaterialDensity"
        INNERDIAMETER = "InnerDiameter"
        ROUGHNESS = "Roughness"
        WALLTHICKNESS = "WallThickness"
        LENGTH = "Length"
        THERMALCONDUCTIVITY = "ThermalConductivity"
        CEMENTTHERMALCONDUCTIVITY = "CementThermalConductivity"
        FLUIDTHERMALCONDUCTIVITY = "FluidThermalConductivity"

    class AssociatedToFluid:
        ASSOCIATEDBLACKOILFLUID = "AssociatedBlackOilFluid"
        ASSOCIATEDCOMPOSITIONALFLUID = "AssociatedCompositionalFluid"
        ASSOCIATEDMFLFLUID = "AssociatedMFLFluid"

    class CanBeTemplate:
        ISTEMPLATE = "IsTemplate"
        ISBUILTINTEMPLATE = "IsBuiltinTemplate"

    class SharedPumpParameters:
        EFFICIENCY = "Efficiency"
        POWER = "Power"
        PRESSURE = "Pressure"
        PRESSUREDIFFERENTIAL = "PressureDifferential"
        PRESSURERATIO = "PressureRatio"
        USECURVES = "UseCurves"

    class SharedPumpCatalogParameters:
        MANUFACTURER = "Manufacturer"
        MODEL = "Model"
        BASESPEED = "BaseSpeed"
        OPERATINGSPEED = "OperatingSpeed"
        SHOWPOWER = "ShowPower"

    class FluidLink:
        RESERVOIRPRESSURE = "ReservoirPressure"
        RESERVOIRTEMPERATURE = "ReservoirTemperature"
        COMPLETIONTESTTYPE= "CompletionTestType"
        USETESTDATA = "UseTestData"
        USECONINGDATA = "UseConingData"
        CONEDGASSG = "ConedGasSG"
        USEGASRATIO = "UseGasRatio"
        USEWATERRATIO = "UseWaterRatio"
        GOR = "GOR"
        OGR = "OGR"
        GLR = "GLR"
        LGR = "LGR"
        GWR = "GWR"
        WGR = "WGR"
        WATERCUT = "WaterCut"
        USEFLUIDOVERRIDES = "UseFluidOverrides"
        OVERRIDESINITIALIZED = "OverridesInitialized"

    class Fluid(CanBeTemplate, FluidLink):
        COMMENT = "Comment"
        HASOVERRIDE = "HasOverride"

    class FileBasedFluid(Fluid):
        FLUIDFILENAME = "FluidFileName"

    # #############################################################################
    # Concrete parameter classes
    # #############################################################################
    class About:
        TOOLKITVERSION = "ToolkitVersion"
        WEBAPIVERSION = "WebAPIVersion"
        MODELFILENAME = "ModelFilename"
        UNITSYSTEM = "UnitSystem"
        UIUNITSYSTEM = "UiUnitSystem"


    class SimulationSetting:
        AMBIENTTEMPERATURE = "AmbientTemperature"
        ATMOSPHERICPRESSURE = "AtmosphericPressure"
        WINDSPEED = "WindSpeed"
        SOILTYPE = "SoilType"
        SOILCONDUCTIVITY = "SoilConductivity"
        METOCEANDATALOCATION = "MetoceanDataLocation"
        EROSIONALVELOCITYCONSTANT = "ErosionalVelocityConstant"
        CORROSIONMODEL = "CorrosionModel"
        CORROSIONEFFICIENCY = "CorrosionEfficiency"
        PIPESEGMENTATIONMAXREPORTINGINTERVAL = "PipeSegmentationMaxReportingInterval"
        PIPESEGMENTATIONPRINTSEGMENTATIONRESULT = "PipeSegmentationPrintSegmentationResult"
        PIPESEGMENTATIONMAXSEGMENTLENGTH = "PipeSegmentationMaxSegmentLength"
        NETWORKSOLVERMETHOD = "NetworkSolver"
        NETWORKSOLVERTOLERANCE = "NetworkSolverTolerance"
        NETWORKSOLVERMAXITERATIONS = "NetworkSolverMaxIterations"
        SINGLEBRANCHKEYWORDS = "SingleBranchKeywords"
        NETWORKTOPKEYWORDS = "NetworkTopKeywords"
        NETWORKBOTTOMKEYWORDS = "NetworkBottomKeywords"
        GISELEVATIONINTERVAL = "GISElevationInterval"
        GISELEVATIONMAXPOINTS = "GISElevationMaxPoints"
        GISELEVATIONSOURCETYPE = "GISElevationSourceType"
        USEGLOBALFLOWCORRELATIONS = "UseGlobalFlowCorrelations"
        USEGLOBALHEATTRANSFER = "UseGlobalHeatTransfer"

    class FlowCorrelation:
        SWAPANGLE = "SwapAngle"
        OVERRIDEGLOBAL = "OverrideGlobal"
        class SinglePhase:
            CORRELATION = "SinglePhaseCorrelation"
            FACTOR = "SinglePhaseFactor"
        class Multiphase:
            class Vertical:
                SOURCE = "VerticalMultiphaseSource"
                CORRELATION = "VerticalMultiphaseCorrelation"
                HOLDUPFACTOR = "VerticalMultiphaseHoldupFactor"
                FRICTIONFACTOR = "VerticalMultiphaseFrictionFactor"
            class Horizontal:
                SOURCE = "HorizontalMultiphaseSource"
                CORRELATION = "HorizontalMultiphaseCorrelation"
                HOLDUPFACTOR = "HorizontalMultiphaseHoldupFactor"
                FRICTIONFACTOR = "HorizontalMultiphaseFrictionFactor"

    class HeatTransferOption:
        PIPEBURIALMETHOD = "PipeBurialMethod"
        INSIDEFILMCOEFFMETHOD = "InsideFilmCoeffMethod"
        UVALUEMULTIPLIER = "UValueMultiplier"
        ENABLEHYDRATESUBCOOLCALC = "EnableHydrateSubcoolCalc"
        OVERRIDEGLOBAL = "OverrideGlobal"

    class BlackOilFluid(Fluid):
        API = "API"
        FRACTIONCO2 = "CO2Fraction"
        FRACTIONCO = "COFraction"
        GASSPECIFICGRAVITY = "GasSpecificGravity"
        GLR = "GLR"
        GOR = "GOR"
        USEGASRATIO = "UseGasRatio"
        USEWATERRATIO = "UseWaterRatio"
        GWR = "GWR"
        FRACTIONH2 = "H2Fraction"
        FRACTIONH2S = "H2SFraction"
        FRACTIONN2 = "N2Fraction"
        WATERCUT = "WaterCut"
        WATERSPECIFICGRAVITY = "WaterSpecificGravity"
        DEADOILDENSITY = "DeadOilDensity"
        USEDEADOILDENSITY = "UseDeadOilDensity"
        DEADOILVISCOSITYCORR = "DeadOilViscosityCorr"
        DEADOILTEMPERATURE1 = "DeadOilTemperature1"
        DEADOILTEMPERATURE2 = "DeadOilTemperature2"
        DEADOILVISCOSITY1 = "DeadOilViscosity1"
        DEADOILVISCOSITY2 = "DeadOilViscosity2"
        LIVEOILVISCOSITYCORR = "LiveOilViscosityCorr"
        LIQUIDVISCOSITYCALC = "LiquidViscosityCalc"
        USEBRAUNERULLMANEQUATION = "UseBraunerUllmanEquation"
        USERWATERCUTCUTOFF = "UserWatercutCutOff"
        UNDERSATURATEDOILVISCOSITYPARA = "UndersaturatedOilViscosityParA"
        UNDERSATURATEDOILVISCOSITYPARB = "UndersaturatedOilViscosityParB"
        UNDERSATURATEDOILVISCOSITYCORR = "UndersaturatedOilViscosityCorr"
        VANDUSERK1 = "VandUserk1"
        VANDUSERK2 = "VandUserk2"
        RICHARDSONKOIW = "Richardsonkoiw"
        RICHARDSONKWIO = "Richardsonkwio"
        OGR = "OGR"
        LGR = "LGR"
        WGR = "WGR"
        ISTEMPLATE = "IsTemplate"
        ISBUILTINTEMPLATE = "IsBuiltinTemplate"
        class SinglePointCalibration:
            SOLUTIONGAS = "SolutionGas"
            OILFVFCORRELATION = "OilFVFCorrelation"
            LIVEOILVISCCORRELATION = "LiveOilViscCorrelation"
            GASCOMPRESSCORRELATION = "GasCompressCorrelation"
            GASVISCCORRELATION = "GasViscCorrelation"
            ABOVEBBPTYPE = "AboveBBPType"
            BELOWBBPTYPE = "BelowBBPType"
            BUBBLEPOINTSATGAS_VALUE = "BubblepointSatGas_Value"
            BUBBLEPOINTSATGAS_PRESSURE = "BubblepointSatGas_Pressure"
            BUBBLEPOINTSATGAS_TEMPERATURE = "BubblepointSatGas_Temperature"
            ABOVEBBPDENSITY_VALUE = "AboveBBPDensity_Value"
            ABOVEBBPDENSITY_PRESSURE = "AboveBBPDensity_Pressure"
            ABOVEBBPDENSITY_TEMPERATURE = "AboveBBPDensity_Temperature"
            ABOVEBBPOFVF_VALUE = "AboveBBPOFVF_Value"
            ABOVEBBPOFVF_PRESSURE = "AboveBBPOFVF_Pressure"
            ABOVEBBPOFVF_TEMPERATURE = "AboveBBPOFVF_Temperature"
            BELOWBBPDENSITY_VALUE = "BelowBBPDensity_Value"
            BELOWBBPDENSITY_PRESSURE = "BelowBBPDensity_Pressure"
            BELOWBBPDENSITY_TEMPERATURE = "BelowBBPDensity_Temperature"
            BELOWBBPOFVF_VALUE = "BelowBBPOFVF_Value"
            BELOWBBPOFVF_PRESSURE = "BelowBBPOFVF_Pressure"
            BELOWBBPOFVF_TEMPERATURE = "BelowBBPOFVF_Temperature"
            BELOWBBPLIVEOILVISCOSITY_VALUE = "BelowBBPLiveOilViscosity_Value"
            BELOWBBPLIVEOILVISCOSITY_PRESSURE = "BelowBBPLiveOilViscosity_Pressure"
            BELOWBBPLIVEOILVISCOSITY_TEMPERATURE = "BelowBBPLiveOilViscosity_Temperature"
            BELOWBBPGASVISCOSITY_VALUE = "BelowBBPGasViscosity_Value"
            BELOWBBPGASVISCOSITY_PRESSURE = "BelowBBPGasViscosity_Pressure"
            BELOWBBPGASVISCOSITY_TEMPERATURE = "BelowBBPGasViscosity_Temperature"
            BELOWBBPGASZ_VALUE = "BelowBBPGasZ_Value"
            BELOWBBPGASZ_PRESSURE = "BelowBBPGasZ_Pressure"
            BELOWBBPGASZ_TEMPERATURE = "BelowBBPGasZ_Temperature"
        class ThermalData:
            GASHEATCAPACITY="GasHeatCapacity"
            OILHEATCAPACITY="OilHeatCapacity"
            WATERHEATCAPACITY="WaterHeatCapacity"
            GASCONDUCTIVITY="GasConductivity"
            OILCONDUCTIVITY="OilConductivity"
            WATERCONDUCTIVITY="WaterConductivity"
            ENTHALPYCALCMETHOD="EnthalpyCalcMethod"
            LATENTHEATOFVAPORIZATION="LatentHeatOfVaporization"

    class Boundary:
        USEPQCURVE = "UsePQCurve"
        USEGASRATIO = "UseGasRatio"
        USEWATERRATIO = "UseWaterRatio"
        ISSURFACECONDITION = "IsSurfaceCondition"
        TEMPERATURE = "Temperature"
        PRESSURE = "Pressure"
        GASFLOWRATE = "GasFlowRate"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"
        GOR = "GOR"
        OGR = "OGR"
        GLR = "GLR"
        LGR = "LGR"
        WATERCUT = "WaterCut"
        GWR = "GWR"
        WGR = "WGR"
        FLOWRATETYPE = "FlowRateType"
        COMPLETIONNAME = "CompletionName"
        ISBOTTOMCOMPLETION = "IsBottomCompletion"
        
    class RateConstraint:
        OILFLOWRATE = "OilFlowRate"
        WATERFLOWRATE = "WaterFlowRate"
        GASFLOWRATE = "GasFlowRate"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"

    
    class LocalConstraint:
        WELLCONTRIBUTION = "IsControlledWell"
        ALHANATICHECK = "AlhanatiCheck"
        FORCESTABLEFLOW = "ForceStableFlow"
        WELLSTATUS = "WellMayShutIn"
        MINGASLIFTRATE = "MinGasliftRate"
        MAXGASLIFTRATE = "MaxGasliftRate"
        MAXCHPFORGASINJECTION = "MaxChpForGasInjection"
        MINLIQUIDRATE = "MinLiquidRate"
        MAXLIQUIDRATE = "MaxLiquidRate"
        MINTOTALGASRATE = "MinTotalGasRate"
        MAXTOTALGASRATE = "MaxTotalGasRate"
        MAXWATERRATE = "MaxWaterRate"
        MAXWELLHEADTEMPERATURE = "MaxWellheadTemperature"
        MAXDRAWDOWNPRESSURE = "MaxDrawdownPressure"
        MINBUBBLEPOINTPRESSURE = "MinBubblePointPressure"
        MAXEVR = "MaxEvr"
        MAXVELOCITY = "MaxVelocity"
        MINPOWER = "MinPower"
        MAXPOWER = "MaxPower"
        MINFREQUENCY = "MinFrequency"
        MAXFREQUENCY = "MaxFrequency"
        MINSPEED = "MinSpeed"
        MAXSPEED = "MaxSpeed"
        MINBEANSIZE = "MinBeanSize"
        MAXBEANSIZE = "MaxBeanSize"
        MAXPRODUCEDGASRATE = "MaxProducedGasRate"
        MAXINJECTIONGASRATE = "MaxInjectionGasRate"
        MAXGOR = "MaxGor"
        MAXCO2 = "MaxCo2"
        MAXH2S = "MaxH2s"
        MAXOILRATE = "MaxOilRate"

    class OptimizerInitialConditions:
        DUALSTRINGWELLID = "SiblingWellId"
        CONSTRAINTTYPE = "ConstraintType"
        INJECTIONGAS = "InjectionRate"
        ESPFREQUENCY = "ESPOperatingFrequency"
        PCPSPEED = "PCPOperatingSpeed"
        CHOKESIZE = "BeanSize"

    class Casing(AbstractTubingSection):
        pass

    class CheckValve(SurfaceComponent):
        CHECKVALVESETTING = "CheckValveSetting"

    class Choke(DownholeOrSurfaceComponent):
        ADJUSTSUBCRITICALCORRELATION = "AdjustSubcriticalCorrelation"
        BEANSIZE = "BeanSize"
        BOTHPHASESFLOWCOEFFICIENT = "BothPhasesFlowCoefficient"
        CALCULATECRITICALPRESSURERATIO = "CalculateCriticalPressureRatio"
        GASEXPANSIONFACTOR = "GasExpansionFactor"
        CRITICALCORRELATION = "CriticalCorrelation"
        CRITICALPRESSURERATIO = "CriticalPressureRatio"
        DISCHARGECOEFFICIENT = "DischargeCoefficient"
        GASPHASEFLOWCOEFFICIENT = "GasPhaseFlowCoefficient"
        HEATCAPACITYRATIO = "HeatCapacityRatio"
        USEFLOWRATEFORCRITICALFLOW = "UseFlowrateForCriticalFlow"
        USEPRESSURERATIOFORCRITICALFLOW = "UsePressureRatioForCriticalFlow"
        USESONICDOWNSTREAMVELOCITYFORCRITICALFLOW = "UseSonicDownstreamVelocityForCriticalFlow"
        USESONICUPSTREAMVELOCITYFORCRITICALFLOW = "UseSonicUpstreamVelocityForCriticalFlow"
        LIQUIDPHASEFLOWCOEFFICIENT = "LiquidPhaseFlowCoefficient"
        SUBCRITICALCORRELATION = "SubCriticalCorrelation"
        TOLERANCE = "Tolerance"
        UPSTREAMPIPEID = "UpstreamPipeID"
        PRINTDETAILEDCALCULATIONS = "PrintDetailedCalculations"
        GASFLOWRATELIMIT = "GasFlowRateLimit"
        LIQUIDFLOWRATELIMIT = "LiquidFlowRateLimit"
        MASSFLOWRATELIMIT = "MassFlowRateLimit"
        WATERFLOWRATELIMIT = "WaterFlowRateLimit"
        OILFLOWRATELIMIT = "OilFlowRateLimit"
        FLOWRATELIMITTYPE = "FlowRateLimitType"

    class Completion(DownholeComponent, AssociatedToFluid, FluidLink):
        DIAMETER = "Diameter"
        LENGTH = "Length"
        PHASEANGLE = "PhaseAngle"
        SHOTDENSITY = "ShotDensity"
        PENETRATIONDEPTH = "PenetrationDepth"
        FLUIDENTRYTYPE = "FluidEntryType"
        GEOMETRYPROFILETYPE = "GeometryProfileType"
        RESERVOIRPRESSURE = "ReservoirPressure"
        RESERVOIRTEMPERATURE = "ReservoirTemperature"
        TESTPOINTS = 'CompletionTestPoints'
        IPRMODEL = "IPRModel"

    class CompletionConingPoint:
        LIQUIDFLOWRATE = "LiquidFlowRate"
        GOR = "GOR"
        WATERCUT = "WaterCut"

    class CompositionalFluid(Fluid):
        COMPONENTFRACTIONTYPE = "ComponentFractionType"
        USETUNEDFRACTIONS = "UseTunedFractions"
        SHOWALLCOMPONENTS = "ShowAllComponents"
        LIQUIDVISCOSITYCALC = "LiquidViscosityCalc"
        USEBRAUNERULLMANEQUATION = "UseBraunerUllmanEquation"
        USERWATERCUTCUTOFF = "UserWatercutCutOff"
        VANDUSERK1 = "VandUserk1"
        VANDUSERK2 = "VandUserk2"
        RICHARDSONKOIW = "Richardsonkoiw"
        RICHARDSONKWIO = "Richardsonkwio"
        IONSODIUM = "SodiumIon"        # Ion suffixed so that users can find it easier (Feedback)
        IONCALCIUM = "CalciumIon"
        IONMAGNESIUM = "MagnesiumIon"
        IONPOTASSIUM = "PotassiumIon"
        IONSTRONTIUM = "StrontiumIon"
        IONBARIUM = "BariumIon"
        IONIRON = "IronIon"
        IONCHLORIDE = "ChlorideIon"
        IONSULPHATE = "SulphateIon"
        IONBICARBONATE = "BicarbonateIon"
        IONBROMIDE = "BromideIon"
        TOTALDISSOLVEDSOLIDS = "TotalDissolvedSolids"
        SALTWATERDENSITYTYPE = "SaltWaterDensityType"
        SALTWATERDENSITY = "SaltWaterDensity"
        SALTWATERSALINITY = "SaltWaterSalinity"
        SALTWATERTEMPERATURE = "SaltWaterTemperature"
        ISTEMPLATE = "IsTemplate"
        ISBUILTINTEMPLATE = "IsBuiltinTemplate"
        COMPOSITION = "Composition"

    class Compressor(SurfaceComponent, SharedPumpParameters, SharedPumpCatalogParameters):
        ROUTE = "Route"
        HONOURSTONEWALLLIMIT = "HonourStonewallLimit"
        ISRECIPROCATING = "IsReciprocating"
        HEADFACTOR = "HeadFactor"

    class IPRTriLinear:
        WELLRADIUS = "WellRadius"
        DISTANCETOBOUNDARY = "DistanceToBoundary"
        OUTERRESPERM = "OuterResPerm"
        INNERRESPERM = "InnerResPerm"
        OUTERRESPOROSITY = "OuterResPorosity"
        INNERRESPOROSITY = "InnerResPorosity"
        OUTERRESCOMPRESSIBILITY = "OuterResCompressibility"
        INNERRESCOMPRESSIBILITY = "InnerResCompressibility"
        NUMHYDRAULICFRAC = "NumHydraulicFrac"
        HYDRAULICFRACHALF = "HydraulicFracHalf"
        HYDRAULICFRACWIDTH = "HydraulicFracWidth"
        HYDRAULICFRACPERM = "HydraulicFracPerm"
        HYDRAULICFRACPOROSITY = "HydraulicFracPorosity"
        HYDRAULICFRACCOMPRESSIBILITY = "HydraulicFracCompressibility"
        CALCSKIN = "CalcSkin"
        TIME = "Time"
        RESERVOIRTHICKNESS = "ReservoirThickness"
        CALCULATIONTYPE = "CalculationType"

    class IPRDarcy:
        RATIOTYPE = "RatioType"
        DAMAGEDZONEPERMRATIO = "DamagedZonePermRatio"
        COMPACTEDZONEPERMRATIO = "CompactedZonePermRatio"
        COMPLETIONVERTICALPERMRATIO = "CompletionVerticalPermRatio"
        COMPLETIONINTERVALRATIO = "CompletionIntervalRatio"
        DAMAGEDZONESKIN = "DamagedZoneSkin"
        PERFORATIONSKIN = "PerforationSkin"
        COMPACTEDZONESKIN = "CompactedZoneSkin"
        PARTIALPENETRATIONSKIN = "PartialPenetrationSkin"
        DEVIATIONSKIN = "DeviationSkin"
        GRAVELPACKSKIN = "GravelPackSkin"
        FRACPACKSKIN = "FracPackSkin"
        CALCULATEMECHANICALSKIN = "CalculateMechanicalSkin"
        CALCULATERATEDEPENDENTSKIN = "CalculateRateDependentSkin"
        CHOKELENGTH = "ChokeLength"
        OBSOLETECOMPACTEDZONEDIAMETER = "ObsoleteCompactedZoneDiameter"
        COMPACTEDZONETHICKNESS = "CompactedZoneThickness"
        COMPACTEDZONEPERMEABILITY = "CompactedZonePermeability"
        COMPLETIONDEVIATION = "CompletionDeviation"
        COMPLETIONVERTICALPERMEABILITY = "CompletionVerticalPermeability"
        COMPLETIONINTERVAL = "CompletionInterval"
        DAMAGEDEPTH = "DamageDepth"
        OBSOLETEDAMAGEDZONEDIAMETER = "ObsoleteDamagedZoneDiameter"
        DAMAGEDZONETHICKNESS = "DamagedZoneThickness"
        DAMAGEDZONEPERMEABILITY = "DamagedZonePermeability"
        DRAINAGERADIUS = "DrainageRadius"
        FRACTURECHOKEPERMEABILITY = "FractureChokePermeability"
        FRACTUREFACEDAMAGEPERMEABILITY = "FractureFaceDamagePermeability"
        FRACTUREHALFLENGTH = "FractureHalfLength"
        FRACTUREPROPPANTPERMEABILITY = "FractureProppantPermeability"
        FRACTUREWIDTH = "FractureWidth"
        ISGASMODEL = "IsGasModel"
        MECHANICALSKIN = "MechanicalSkin"
        PERFSKINMETHOD = "PerfSkinMethod"
        RATEDEPENDENTGASSKIN = "RateDependentGasSkin"
        RATEDEPENDENTLIQUIDSKIN = "RateDependentLiquidSkin"
        RESERVOIRAREA = "ReservoirArea"
        RESERVOIRPERMEABILITY = "ReservoirPermeability"
        RESERVOIRTHICKNESS = "ReservoirThickness"
        SHAPEFACTOR = "ShapeFactor"
        USERELATIVEPERMEABILITY = "UseRelativePermeability"
        USECHOKEFRACTURESKIN = "UseChokeFractureSkin"
        USEDAMAGEDZONESKIN = "UseDamagedZoneSkin"
        USEDRAINAGERADIUS = "UseDrainageRadius"
        USEFRACTUREFACESKIN = "UseFractureFaceSkin"
        USEFRACTURESKIN = "UseFractureSkin"
        USEGRAVELPACKSKIN = "UseGravelPackSkin"
        USEPARTIALPENETRATIONDEVIATIONSKIN = "UsePartialPenetrationDeviationSkin"
        USEPERFORATIONSKIN = "UsePerforationSkin"
        USEPSEUDOPRESSUREMETHOD = "UsePseudoPressureMethod"
        USEVOGELBELOWBUBBLEPOINT = "UseVogelBelowBubblepoint"
        USEVOGELWATERCUTCORRECTION = "UseVogelWaterCutCorrection"
        WELLCOMPLETIONTYPE = "WellCompletionType"
        ISTRANSIENT = "IsTransient"
        COMPRESSIBILITY = "Compressibility"
        POROSITY = "Porosity"
        TIME = "Time"
        WATERSATURATION = "WaterSaturation"
        RELATIVEPERMEABILITYOIL = "RelativePermeabilityOil"
        RELATIVEPERMEABILITYWATER = "RelativePermeabilityWater"

    class DistributedCompletionModel:
        RATIOTYPE = "RatioType"
        DAMAGEDZONEPERMRATIO = "DamagedZonePermRatio"
        COMPACTEDZONEPERMRATIO = "CompactedZonePermRatio"
        COMPLETIONVERTICALPERMRATIO = "CompletionVerticalPermRatio"
        DAMAGEDZONESKIN = "DamagedZoneSkin"
        PERFORATIONSKIN = "PerforationSkin"
        COMPACTEDZONESKIN = "CompactedZoneSkin"
        PARTIALPENETRATIONSKIN = "PartialPenetrationSkin"
        DEVIATIONSKIN = "DeviationSkin"
        GRAVELPACKSKIN = "GravelPackSkin"
        FRACPACKSKIN = "FracPackSkin"
        CALCULATESKIN = "CalculateSkin"
        OBSOLETECOMPACTEDZONEDIAMETER = "ObsoleteCompactedZoneDiameter"
        COMPACTEDZONETHICKNESS = "CompactedZoneThickness"
        COMPACTEDZONEPERMEABILITY = "CompactedZonePermeability"
        COMPLETIONLENGTH = "CompletionLength"
        COMPLETIONMODELTYPE = "CompletionModelType"
        OBSOLETEDAMAGEDZONEDIAMETER = "ObsoleteDamagedZoneDiameter"
        DAMAGEDZONETHICKNESS = "DamagedZoneThickness"
        DAMAGEDZONEPERMEABILITY = "DamagedZonePermeability"
        FLUIDOFVF = "FluidOFVF"
        FLUIDVISCOSITY = "FluidViscosity"
        GASPI = "GasPI"
        GASZ = "GasZ"
        GRAVELPACKPERMEABILITY = "GravelPackPermeability"
        GRAVELPACKTUNNEL = "GravelPackTunnel"
        ISGASMODEL = "IsGasModel"
        LIQUIDPI = "LiquidPI"
        LOCATIONECCEN = "LocationEccen"
        LOCATIONXPOS = "LocationXPos"
        LOCATIONYPOS = "LocationYPos"
        LOCATIONZPOS = "LocationZPos"
        PERFORATIONDIAMETER = "PerforationDiameter"
        PERFORATIONLENGTH = "PerforationLength"
        PERFORATIONSHOTDENSITY = "PerforationShotDensity"
        PERMEABILITYX = "PermeabilityX"
        PERMEABILITYY = "PermeabilityY"
        PERMEABILITYZ = "PermeabilityZ"
        RESERVOIREXTENT = "ReservoirExtent"
        RESERVOIRTHICKNESS = "ReservoirThickness"
        RESERVOIRXDIM = "ReservoirXDim"
        RESERVOIRYDIM = "ReservoirYDim"
        SPECIFIEDSKIN = "SpecifiedSkin"
        USEDISTRIBUTEDPI = "UseDistributedPI"
        WELLLENGTH = "WellLength"
        WELLCOMPLETIONTYPE = "WellCompletionType"

    class IPRPSSBabuOdeh(DistributedCompletionModel):
        pass

    class IPRSSJoshi(DistributedCompletionModel):
        pass

    class IPRHorizontalPI(DistributedCompletionModel):
        pass

    class EngineKeywords(DownholeOrSurfaceComponent):
        KEYWORDS = "Keywords"

    class ESP(DownholeComponent):
        SERIES = "Series"
        USESTAGEBYSTAGECALC = "UseStageByStageCalc"
        BASEFREQUENCY = "BaseFrequency"
        CASINGID = "CasingID"
        OPERATINGPRODUCTIONRATE = "OperatingProductionRate"
        OPERATINGFREQUENCY = "OperatingFrequency"
        DIAMETER = "Diameter"
        GASSEPARATOREFFICIENCY = "GasSeparatorEfficiency"
        HASGASSEPARATOR = "HasGasSeparator"
        HEADFACTOR = "HeadFactor"
        MANUFACTURER = "Manufacturer"
        MAXFLOWRATE = "MaxFlowRate"
        MINFLOWRATE = "MinFlowRate"
        MODEL = "Model"
        NUMBERSTAGES = "NumberStages"
        USEVISCOSITYCORRECTION = "UseViscosityCorrection"
        POWER = "Power"
        USEPOWER = "UsePower"
        ESPSPEEDFACTOR = "ESPSpeedFactor"
        SLIPFACTOR = "SlipFactor"
        FLOWRATEFACTOR = "FlowrateFactor"
        POWERFACTOR = "PowerFactor"
        COEFFICIENTA = "CoefficientA"
        COEFFICIENTB = "CoefficientB"
        POWERCORRECTION = "PowerCorrection"
        ISPOWERCORRECTIONCALCULATED = "IsPowerCorrectionCalculated"
        CABLELENGTHBELOWPUMP = "CableLengthBelowPump"
        RECOMBINEGAS = "RecombineGas"
        class MotorCoefficients:
            AMPValues = "AMPValues"
            PFValues = "PFValues"
            AMPValues = "AMPValues"
            EFFValues = "EFFValues"
        class MotorCatalogData:
            MANUFACTURER = "MotorManufacturer"
            MOTORNAME = "MotorName"
            NPPOWER = "NPPower"
            NPVOLTAGE = "NPVoltage"
            NPAMPERAGE = "NPAmperage"
            FLOOREFFICIENCY = "FloorEfficiency"
            FLOORPOWERFACTOR = "FloorPowerFactor"
        class CableCatalogData:
            NAME = "CableName"
            VDROP = "VDrop"
            MAXAMPS = "MaxAmps"
    
    class ESPMotorCoefficient:
        AMPVALUE = "AMPValue"
        PFVALUE = "PFValue"
        EFFVALUE = "EFFValue"
        
        
    class Expander(SurfaceComponent, SharedPumpParameters):
        ROUTE = "Route"

    class FetkovitchEquationModel:
        ABSOLUTEOPENFLOWPOTENTIAL = "AbsoluteOpenFlowPotential"
        NEXPONENT = "NExponent"

    class Flowline(SurfaceComponent):
        SHOWASRISER = "ShowAsRiser"
        DETAILEDMODEL = "DetailedModel"
        USEGISDATA = "UseGISData"
        UNDULATIONRATE = "UndulationRate"
        ENTERSURVEYLENGTH = "EnterSurveyLength"
        MEASUREDDISTANCE = "MeasuredDistance"
        HORIZONTALDISTANCE = "HorizontalDistance"
        ELEVATIONDIFFERENCE = "ElevationDifference"
        SEABEDDEPTH = "SeabedDepth"
        PLATFORMHEIGHT = "PlatformHeight"
        AMBIENTTEMPERATURE = "AmbientTemperature"
        AMBIENTAIRTEMPERATURE = "AmbientAirTemperature"
        AMBIENTWATERTEMPERATURE = "AmbientWaterTemperature"
        AMBIENTTEMPERATUREOPTIONS = "AmbientTemperatureOptions"
        AMBIENTFLUIDTYPE = "AmbientFluidType"
        WATERINTERPOLATIONMETHOD = "WaterInterpolationMethod"
        DEVIATIONSURVEYCALC = "DeviationSurveyCalc"
        ISFLIPPED = "IsFlipped"
        GEOTHERMALSURVEYINDEX = "GeothermalSurveyIndex"
        USEGLOBALSETTINGS = "UseGlobalSettings"
        ISDOWNCOMER = "IsDowncomer"
        USEENVIRONMENTALDATA = "UseEnvironmentalData"
        SURFACETEMPERATURE = "SurfaceTemperature"
        DEPTHATSTART = "DepthAtStart"
        USEDEPTH = "UseDepth"
        ANNULUSFLOW = "AnnulusFlow"
        INNERDIAMETER = "InnerDiameter"
        LENGTH = "Length"
        ROUGHNESS = "Roughness"
        WALLTHICKNESS = "WallThickness"
        INNERPIPEOUTSIDEDIAMETER = "InnerPipeOutsideDiameter"
        OUTERPIPEINSIDEDIAMETER = "OuterPipeInsideDiameter"
        OUTERPIPEWALLTHICKNESS = "OuterPipeWallThickness"
        CATALOGNAME = "CatalogName"
        CATALOGLABEL = "CatalogLabel"
        ENTEROD = "EnterOD"
        GEOMETRYPROFILE = 'GeometryProfile'
        GEOTHERMALPROFILE = 'FlowlineGeothermalProfile'
        class HeatTransfer:
            GROUNDCONDUCTIVITY = "GroundConductivity"
            INCLUDEINSIDEFILMCOEFF = "IncludeInsideFilmCoeff"
            ISUCALCULATED = "IsUCalculated"
            PIPEBURIALDEPTH = "PipeBurialDepth"
            PIPECONDUCTIVITY = "PipeConductivity"
            SURROUNDINGFLUIDVELOCITY = "SurroundingFluidVelocity"
            USETHERMALSURVEY = "UseThermalSurvey"
            UCOEFFUSER = "UCoeffUser"
            UCOEFFUSERAIR = "UCoeffUserAir"
            UCOEFFUSERWATER = "UCoeffUserWater"
            UTYPE = "UType"
            UTYPEAIR = "UTypeAir"
            UTYPEWATER = "UTypeWater"

    class FluidComponent(ModelComponent):
        MOLECULARWEIGHT = "MolecularWeight"
        TCRIT = "Tcrit"
        TBOIL = "Tboil"
        TMELT = "Tmelt"
        PCRIT = "Pcrit"
        VCRIT = "Vcrit"
        ZCRIT = "Zcrit"
        VCRITVISCOSITY = "VcritViscosity"
        ACF = "Acf"
        PARACHOR = "Parachor"
        OMEGAA = "OmegaA"
        OMEGAB = "OmegaB"
        REFERENCEDENSITY = "ReferenceDensity"
        EOSVOLUMESHIFT = "EoSVolumeShift"
        SPECIFICGRAVITY = "SpecificGravity"
        WATSONKFACTOR = "WatsonKFactor"
        HEATVAPOURISATION = "HeatVapourisation"
        CALORIFICVALUE = "CalorificValue"
        THERMEXPCOEFF = "ThermExpCoeff"
        HYDROCARBONFORM = "HydrocarbonForm"
        ISUSERDEFINED = "IsUserDefined"
        THERMALCOEFFICIENT0 = "ThermalCoefficient0"
        THERMALCOEFFICIENT1 = "ThermalCoefficient1"
        THERMALCOEFFICIENT2 = "ThermalCoefficient2"
        THERMALCOEFFICIENT3 = "ThermalCoefficient3"
        THERMALCOEFFICIENT4 = "ThermalCoefficient4"
        THERMALCOEFFICIENT5 = "ThermalCoefficient5"
        THERMALCOEFFICIENT6 = "ThermalCoefficient6"

    class FluidComponentFraction:
        SPECIFIEDFRACTION = "SpecifiedFraction"
        TUNEDFRACTION = "TunedFraction"
        COMPONENT = "Component"

    class IPRForchheimer:
        COEFFICIENTA = "CoefficientA"
        COEFFICIENTF = "CoefficientF"

    class GasLiftInjection(DownholeComponent):
        GASLIFTTYPE = "GasLiftType"
        GASRATE = "GasRate"
        GLR = "GLR"
        GLRINCREASE = "GLRIncrease"
        VALVEDIAMETER = "ValveDiameter"
        MANUFACTURER = "Manufacturer"
        SERIES = "Series"
        VALVETYPE = "ValveType"
        VALVESIZE = "ValveSize"
        PORTSIZE = "PortSize"
        PORTAREA = "PortArea"
        BELLOWAREA = "BellowArea"
        DISCHARGECOEFFICIENT = "DischargeCoefficient"
        DISCHARGETOFULLYOPEN = "DischargeToFullyOpen"
        PTRO = "Ptro"
        VALVECHOKE = "ValveChoke"
        SPRINGPRESSURE = "SpringPressure"

    class GenericEquipment(SurfaceComponent):
        DISCHARGEPRESSURE = "DischargePressure"
        DISCHARGETEMPERATURE = "DischargeTemperature"
        DUTY = "Duty"
        PRESSUREDROP = "PressureDrop"
        PRESSURERATIO = "PressureRatio"
        PRESSURESPEC = "PressureSpec"
        ROUTE = "Route"
        TEMPERATUREDIFFERENTIAL = "TemperatureDifferential"
        TEMPERATURESPEC = "TemperatureSpec"

    class Pump(SurfaceComponent, SharedPumpParameters, SharedPumpCatalogParameters):
        ROUTE = "Route"
        DESIGNPRODUCTIONRATE = "DesignProductionRate"
        MAXFLOWRATE = "MaxFlowRate"
        MINFLOWRATE = "MinFlowRate"
        NUMBERSTAGES = "NumberStages"
        USEVISCOSITYCORRECTION = "UseViscosityCorrection"
        BASESTAGES = "BaseStages"
        HEADFACTOR = "HeadFactor"

    class GeographicSurvey:
        LATITUDE = "Latitude"
        LONGITUDE = "Longitude"
        ISVERTEX = "IsVertex"

    class GravelPack:
        GRAVELCASINGID = "GravelCasingId"
        GRAVELPERMEABILITY = "GravelPermeability"
        GRAVELSCREENSIZE = "GravelScreenSize"
        GRAVELTUNNELLENGTH = "GravelTunnelLength"

    class HeatExchanger:
        DISCHARGEPRESSURE = "DischargePressure"
        DISCHARGETEMPERATURE = "DischargeTemperature"
        DUTY = "Duty"
        PRESSUREDROP = "PressureDrop"
        PRESSURESPEC = "PressureSpec"
        TEMPERATUREDIFFERENTIAL = "TemperatureDifferential"
        TEMPERATURESPEC = "TemperatureSpec"

    class Injector(DownholeOrSurfaceComponent, AssociatedToFluid):
        GASFLOWRATE = "GasFlowRate"
        INJECTEDFLUID = "InjectedFluid"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"
        TEMPERATURE = "Temperature"
        FLOWRATETYPE = "FlowrateType"
        USEGASRATIO = "UseGasRatio"
        USEWATERRATIO = "UseWaterRatio"
        GOR = "GOR"
        OGR = "OGR"
        GLR = "GLR"
        LGR = "LGR"
        GWR = "GWR"
        WGR = "WGR"
        WATERCUT = "WaterCut"
        USEFLUIDOVERRIDES = "UseFluidOverrides"
        OVERRIDESINITIALIZED = "OverridesInitialized"

    class IPRBackPressure:
        CONSTANTC = "ConstantC"
        SLOPEN = "SlopeN"

    class IPRHydraulicFracture:
        FRACTUREHALFLENGTH = "FractureHalfLength"
        FRACTUREPERMEABILITY = "FracturePermeability"
        FRACTUREWIDTH = "FractureWidth"
        ISGASMODEL = "IsGasModel"
        POROSITY = "Porosity"
        RESERVOIRPERMEABILITY = "ReservoirPermeability"
        RESERVOIRRADIUS = "ReservoirRadius"
        RESERVOIRTHICKNESS = "ReservoirThickness"
        TIME = "Time"
        TOTALCOMPRESSIBILITY = "TotalCompressibility"
        USETRANSIENTMODEL = "UseTransientModel"
        USEVOGELBELOWBUBBLEPOINT = "UseVogelBelowBubblepoint"
        USEVOGELWATERCUTCORRECTION = "UseVogelWaterCutCorrection"

    class IPRPIModel:
        GASPI = "GasPI"
        ISGASMODEL = "IsGasModel"
        LIQUIDPI = "LiquidPI"
        USEVOGELBELOWBUBBLEPOINT = "UseVogelBelowBubblepoint"
        USEVOGELWATERCUTCORRECTION = "UseVogelWaterCutCorrection"

    class IPRJones:
        GASCOEFFICIENTA = "GasCoefficientA"
        GASCOEFFICIENTB = "GasCoefficientB"
        ISGASMODEL = "IsGasModel"
        LIQUIDCOEFFICIENTA = "LiquidCoefficientA"
        LIQUIDCOEFFICIENTB = "LiquidCoefficientB"

    class Source(SurfaceComponent, AssociatedToFluid):
        USEPQCURVE = "UsePQCurve"
        TEMPERATURE = "Temperature"
        SELECTEDRATETYPE = "SelectedRateType"
        GASFLOWRATE = "GasFlowRate"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"
        PRESSURE = "Pressure"
        USEGASRATIO = "UseGasRatio"
        USEWATERRATIO = "UseWaterRatio"
        GOR = "GOR"
        OGR = "OGR"
        GLR = "GLR"
        LGR = "LGR"
        GWR = "GWR"
        WGR = "WGR"
        WATERCUT = "WaterCut"
        USEFLUIDOVERRIDES = "UseFluidOverrides"
        OVERRIDESINITIALIZED = "OverridesInitialized"
        PQCURVE = 'PQCurve'

    class Junction(Source):
        TREATASSOURCE = "TreatAsSource"

    class Liner(AbstractTubingSection):
        pass

    class MeasurementPoint:
        CONNECTEDTOSTARTEQUIPMENT = "ConnectedToStartEquipment"

    class MFLFluid(FileBasedFluid):
        pass

    class MultiphaseBooster(SurfaceComponent):
        TOTALPOWER = "Power"
        DISCHARGEPRESSURE = "Pressure"
        PRESSUREDIFFERENTIAL = "PressureDifferential"
        PRESSURERATIO = "PressureRatio"
        TYPE = "BoosterType"

    class GenericMultiphaseBooster(MultiphaseBooster):
        PUMPEFFICIENCY = "Efficiency"
        COMPRESSOREFFICIENCY = "BoosterEfficiency"

    class SharedOneSubseaParameters(MultiphaseBooster):
        PUMPMODEL = "PumpModel"
        TUNINGFACTOR = "TuningFactor"
        NUMBEROFBOOSTERSINPARALLEL = "NumberOfBoostersInParallel"
        
    class OneSubseaMultiphaseBooster(SharedOneSubseaParameters):
        SPEEDLIMIT = "SpeedLimit"
        RECIRCULATIONFLOWRATE = "RecirculationFlowRate"

    class OneSubseaWetGasCompressor(SharedOneSubseaParameters):
        SPEEDSETPOINT = "SpeedSetPoint"
        UPSTREAMCOOLERMODEL = "UpstreamCoolerModel"
        UPSTREAMCOOLERDUTY = "UpstreamCoolerDuty"
        DOWNSTREAMCOOLERMODEL = "DownstreamCoolerModel"
        DOWNSTREAMCOOLERDUTY = "DownstreamCoolerDuty"
        RECIRCULATIONMASSRATE = "RecirculationRate"
        MAXTEMPERATURE = "MaxTemperature"

    class MultiplierAdder(SurfaceComponent):
        ADDER = "Adder"
        SCALER = "Scaler"
        USEASMULTIPLIER = "UseAsMultiplier"
        ADDERRATETYPE = "AdderRateType"
        ADDEDLIQUID = "AddedLiquid"
        ADDEDGAS = "AddedGas"
        ADDEDMASS = "AddedMass"

    class OpenHole(AbstractTubingSection):
        pass

    class Packer(DownholeComponent):
        pass

    class PCP(DownholeComponent):
        BASESPEED = "BaseSpeed"
        CASINGID = "CasingID"
        OPERATINGPRODUCTIONRATE = "OperatingProductionRate"
        OPERATINGSPEED = "OperatingSpeed"
        DIAMETER = "Diameter"
        GASSEPARATOREFFICIENCY = "GasSeparatorEfficiency"
        HASGASSEPARATOR = "HasGasSeparator"
        HEADFACTOR = "HeadFactor"
        MANUFACTURER = "Manufacturer"
        NOMINALFLOWRATE = "NominalFlowRate"
        MODEL = "Model"
        USEVISCOSITYCORRECTION = "UseViscosityCorrection"
        POWER = "Power"
        USEPOWER = "UsePower"
        SPEEDFACTOR = "SpeedFactor"
        SLIPFACTOR = "SlipFactor"
        FLOWRATEFACTOR = "FlowrateFactor"
        POWERFACTOR = "PowerFactor"
        ISTOPDRIVE = "IsTopDrive"
        RODDIAMETER = "RodDiameter"

    class PVTFluid(FileBasedFluid):
        pass

    class RodPump(DownholeComponent):
        GASSEPARATOREFFICIENCY = "GasSeparatorEfficiency"
        HASGASSEPARATOR = "HasGasSeparator"
        HASGASRECOMBINEDATWELLHEAD = "HasGasRecombinedAtWellHead"
        NOMINALFLOWRATE = "NominalFlowRate"
        USEVISCOSITYCORRECTION = "UseViscosityCorrection"
        MAXDP = "MaxDP"
        MAXPOWER = "MaxPower"
        RODDIAMETER = "RodDiameter"
        BASISTYPE = "BasisType"
        SLIPECOEFFICIENT = "SlipCoefficient"
        PUMPEFFICIENCY = "PumpEfficiency"
        STROKEPERMINUTE = "StrokesPerMinute"
        STROKELENGTH = "StrokeLength"
        PLUNGERDIAMTER = "PlungerDiameter"

    class SinglePhaseSeparator(DownholeComponent):
        EFFICIENCY = "Efficiency"
        SEPARATEDFLUID = "SeparatedFluid"

    class Sink(SurfaceComponent):
        GASFLOWRATE = "GasFlowRate"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"
        PRESSURE = "Pressure"
        FLOWRATETYPE = "FlowrateType"

    class SlidingSleeve(DownholeComponent):
        ISOPEN = "IsOpen"

    class SpotReport(DownholeOrSurfaceComponent):
        FLOWMAP = "FlowMap"
        PHASEENVELOPE = "PhaseEnvelope"
        COMPOSITIONDETAILS = "CompositionDetails"
        STOCKTANKFLUID = "StockTankFluid"
        FLOWINGFLUID = "FlowingFluid"
        CUMULATIVEVALUES = "CumulativeValues"
        MULTIPHASEFLOWVALUES = "MultiPhaseFlowValues"
        SLUGGINGVALUES  ="SluggingValues"
        PIGGINGVALUES = "PiggingValues"
        HEATTRANSFERVALUES = "HeatTransferValues"
        CUSTOM = "Custom"
        CUSTOMREPORTNAME = "CustomReportName"
        CUSTOMKEYWORDS = "CustomKeywords"

    class SubsurfaceSafetyValve(DownholeComponent):
        BEANID = "BeanID"

    class Study:
        NAME = "Name"
        DESCRIPTION = "Description"

    class AbstractTask:
        TASKNAME = "Name"
        DESCRIPTION = "Description"
        STUDY = "Study"
        USEPHASERATIO = "UsePhaseRatio"
        FLOWRATECONDITION = "FlowRateCondition"
        FLOWRATECONDITIONTEMPERATURE = "FlowRateConditionTemperature"
        FLOWRATECONDITIONPRESSURE = "FlowRateConditionPressure"

    class SingleBranchSimulation(AbstractTask):
        PRODUCER = "Producer"
        BRANCHTERMINATOR = "BranchTerminator"
        SENSITIVITYVARIABLES = "SensitivityVariables"
        SENSITIVITYVARIABLE = "SensitivityVariable"
        class SensitivityVariable:
            COMPONENT = "Component"
            VARIABLE = "Variable"
            VALUES = "Values"
            APPLYALL = "ApplyAll"
            TYPE = "Type"
            
    class VfpTablesSimulation(SingleBranchSimulation):
        ARTIFICIALLIFTSENSITIVITY = "ArtificialLiftSensitivity"
        LIQUIDRATESENSITIVITY = "LiquidRateSensitivity"
        GASRATESENSITIVITY = "GasRateSensitivity"
        GORSENSITIVITY = "GorSensitivity"
        GLRSENSITIVITY = "GlrSensitivity"
        OGRSENSITIVITY = "OgrSensitivity"
        LGRSENSITIVITY = "LgrSensitivity"
        WATERCUTSENSITIVITY = "WatercutSensitivity"
        WGRSENSITIVITY = "WgrSensitivity"
        GWRSENSITIVITY = "GwrSensitivity"
        OUTLETPRESSURESENSITIVITY = "OutletPressureSensitivity"
        
        RESERVOIRSIMULATOR = "TableType" #VFPTablesOperationTable
        TABLENUMBER = "TableNumber" #integer
        INCLUDETEMPERATURE = "IncludeTemperature"
        BOTTOMHOLEDATUMDEPTH = "WellHeadDepth" #float
        '''
        Note: VFPTABLETYPE is for source only(no need for well)
        '''
        VFPTABLETYPE = "GenerateInjectionTable"
        RATETYPE = "RateType" #[Parameter.VfpTablesSimulation.GASFLOWRATE,Parameter.VfpTablesSimulation.LIQUIDFLOWRATE]
        GLRATIOTYPE = "GLRatioType" #[Parameter.VfpTablesSimulation.GOR,Parameter.VfpTablesSimulation.GLR]
        GWRATIOTYPE = "GWRatioType" #[Parameter.VfpTablesSimulation.WATERCUT,Parameter.VfpTablesSimulation.WGR,Parameter.VfpTablesSimulation.GWR]
        GOR = "GOR"
        GLR = "GLR"
        GWR = "GWR"
        WGR = "WGR"
        WATERCUT = "WaterCut"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        GASFLOWRATE = "GasFlowRate"
        
        

    class NetworkSimulation(AbstractTask):
        USESURFACEBOUNDARYCONDITIONS = "UseSurfaceBoundaryConditions"

    class NetworkOptimizerSimulation(AbstractTask):

        class ObjectiveFunctionTypes:
            MAXOILRATE = "MaxOilRate"
            MAXLIQUIDRATE = "MaxLiquidRate"
            MAXPRODUCEDGASRATE = "MaxProducedGasRate"
            MAXTOTALGASRATE = "MaxTotalGasRate"
            MINOILRATE = "MinOilRate"
            MINLIQUIDRATE = "MinLiquidRate"
            MINPRODUCEDGASRATE = "MinProducedGasRate"
            MINTOTALGASRATE = "MinTotalGasRate"
            MINPOWER = "MinPower"

        class InjectionGasrateTypes:
            FIXEDINJECTIONGASRATE = "FixedInjectionGasrate"
            MAXIMUMINJECTIONGASRATE = "MaximumInjectionGasrate"

        class GenerateCurvesTypes:
            ALWAYS = "Always"
            SELECTEDWELLS = "SelectedWells"

        class PowerTypes:
            FIXEDPOWER = "FixedPower"
            MAXIMUMPOWER = "MaximumPower"

        class RateTypes:
            FIXEDLIQUIDRATE = "FixedLiquidrate"
            FIXEDGASRATE = "FixedGasrate"
            FIXEDOILRATE = "FixedOilrate"

        class ControlTypes:
            GASLIFT = "Gaslift"
            ESP = "Esp"
            PCP = "Pcp"
            CHOKE = "Choke"

        class Options:
            class WellCurveParameters:
                CONTROLVALUESPERCURVE = "ControlValuesPerCurve"
                PRESSUREVALUESPERWELL = "PressureValuesPerWell"
                MINIMUMCHOKEBEANSIZE = "MinBeanSizePerWell"
                MAXIMUMCHOKEBEANSIZE = "MaxBeanSizePerWell"
                MINIMUMESPFREQUENCY = "MinFrequencyPerWell"
                MAXIMUMESPFREQUENCY = "MaxFrequencyPerWell"
                MINIMUMPCPSPEED = "MinSpeedPerWell"
                MAXIMUMPCPSPEED = "MaxSpeedPerWell"
                MINIMUMGASLIFTPERWELL = "MinGasliftPerWell"
                MAXIMUMGASLIFTPERWELL = "MaxGasliftPerWell"
                REGENERATECURVES = "GenerateCurvesType"

            class NetworkSolver:
                LINKTOOPTIMIZERTOLERANCE = "LinkToTolerance"
                NATWORKFAILURETOLERANCE = "FailureTolerance"

            class Search:
                CONSTRAINTSCONVEGENCETOLERANCE = "SearchConverganceTolerance"
                MAXIMUMGASRATE = "SearchMinGasRate"
                GASRATEMARGINALGRADIENT = "SearchMarginGradient"
                MINIMUMPOWER = "SearchMinPower"
                POWERMARGINALGRADIENT = "SearchPowerMarginGradient"

            class Initialization:
                UseLastKnownWellheadPressure = "UseLastKnownWellheadPressures"
                InitialWellheadPressure = "InitialWellheadPressure"
                UseCurrentControlParameters = "UseCurrentControlParameters"

            class Optimization:
                CONSTRAINTSCONVERGENCETOLERANCE = "ToleranceConstraint"
                PRESSURECONVERGENCETOLERANCE = "TolerancePressure"
                CONSTRAINTSMAXITERATIONS = "MaxIterationsConstraint"
                PRESSUREMAXITERATIONS = "MaxIterationsPressure"
                DAMPINGTHRESHOLD = "DampingThreshold"
                DAMPINGFACTOR = "DampingFactor"
                STABLEFLOWMARGIN = "StableFlowMargin"
                ACCELERATEBRANCHCONSTRAINTS = "AccelerateBranchConstraints"
                MAXIMUMOPTIMIZERRESTARTS = "MaximumRestarts"
                VERBOSEMESSAGES = "VerboseMessages"

        class OptimizationControl:
            OBJECTIVEFUNCTION = "ObjectiveFunction"
            class ControlVariables:
                CHOKEBEANSIZE = "ChokeBeanSize"
                GASLIFTRATE = "GasliftRate"
                ESPFREQUENCY = "ESPFrequency"
                PCPSPEED = "PCPSpeed"

            class OptimizationTargets:
                INJECTIONTYPE = "InjectionType"
                INJECTIONRATE = "InjectionGasRate"
                POWERTYPE = "PowerType"
                POWER = "Power"
                LIQUIDRATETYPE = "RateType"
                LIQUIDRATE = "LiquidRate"

            class GlobalConstraints:
                MINIMUMTOTALGASRATE = "MinimumTotalGasRate"
                MAXIMUMTOTALGASRATE = "MaximumTotalGasRate"
                MAXIMUMPRODUCEDGASRATE = "MaximumProducedGasRate"
                MAXIMUMWATERRATE = "MaximumWaterRate"
                MAXIMUMLIQUIDRATE = "MaximumLiquidRate"
                MAXIMUMOILRATE = "MaximumOilRate"
                MAXIMUMTOTALGOR = "MaximumTotalGOR"
                MAXIMUMCO2 = "MaximumCO2"
                MAXIMUMH2S = "MaximumH2S"

            class Scope:
                IGNOREGLOBALCONSTRAINS = "IgnoreGlobalConstrains"
                IGNORELOCALCONSTRAINS = "IgnoreLocalConstrains"
        


    class GLDiagnosticsSimulation(SingleBranchSimulation):
        OUTLETPRESSURE = "OutletPressure" 
        DIAGNOSTICSTYPE = "DiagnosticsType" 
        THROTTLING = "ThrottlingOption" 
        INJECTIONGRADIENT = "PressureGradientType" 
        TARGETINJECTIONRATE = "TargetInjectionRate" 
        SURFACEINJECTIONTEMPERATURE = "SurfaceGasTemperature" 
        SURFACEINJECTIONPRESSURE = "SurfaceGasPressure" 


    class PTProfileSimulation(SingleBranchSimulation):
        CALCULATEDVARIABLE = "CalculationVariableType"
        CUSTOMVARIABLE = "CalculationVariable"
        FLOWRATETYPE = "FlowRateType"
        GASFLOWRATE = "GasFlowRate"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"
        INLETPRESSURE = "InletPressure"
        OUTLETPRESSURE = "OutletPressure"
        
        class CustomVariable:
            COMPONENT = "Component"
            VARIABLE = "Variable"
            MINVALUE = "MinValue"
            MAXVALUE = "MaxValue"
            ISDIRECTPROPORTIONALITY = "IsDirectProportionality"

    class SystemAnalysisSimulation(PTProfileSimulation):
        SENSITIVITYMETHOD = "SensitivityMethod"

    class WellPerformanceCurvesSimulation(SingleBranchSimulation):
        FLOWRATEPOINTS = "FlowratePoints"
        """
        Deprecated, please use SensitivityVariable instead
        """
        class SENSITIVITYVARIABLE:
            COMPONENT = "Component"
            VARIABLE = "Variable"
            VALUES = "Values"
            APPLYALL = "ApplyAll"
       
    class NodalAnalysisSimulation(SingleBranchSimulation):
        OUTLETPRESSURE = "OutletPressure"
        NODALMEASUREMENTPOINT = "NodalMeasurementPoint"
        MAXOUTFLOWPRESSURE = "MaxOutflowPressure"
        MAXFLOWRATETYPE = "MaxFlowRateType"
        MAXGASRATE = "MaxGasRate"
        MAXLIQUIDRATE = "MaxLiquidRate"
        MAXMASSRATE = "MaxMassRate"
        INFLOWPOINTS = "InflowPoints"
        OUTFLOWPOINTS = "OutflowPoints"
        LIMITINFLOW = "LimitInflow"
        LIMITOUTFLOW = "LimitOutflow"  

    class ThreePhaseSeparator(SurfaceComponent):
        GASOILEFFICIENCY = "GasOilEfficiency"
        WATEROILEFFICIENCY = "WaterOilEfficiency"
        PRESSURE = "Pressure"
        PRODUCTFLUID = "ProductFluid"

    class Tubing(AbstractTubingSection):
        pass

    class TwoPhaseSeparator(SurfaceComponent):
        EFFICIENCY = "Efficiency"
        PRESSURE = "Pressure"
        PRODUCTIONSTREAM = "ProductionStream"
        DISCARDEDSTREAM = "DiscardedStream"

    class IPRVogel:
        ABSOLUTEOPENFLOWPOTENTIAL = "AbsoluteOpenFlowPotential"
        VOGELCOEFFICIENT = "VogelCoefficient"

    class WaterTempVelocitySurvey:
        ISGLOBAL = "IsGlobal"
        
    class GasliftSensitivity:
        COMPONENTNAME = "Gas lift data"
        SURFACEGASTEMPERATURE = "SurfaceGasTemperature"
        SURFACEGASPRESSURE = "SurfaceGasPressure"
        TARGETINJECTIONRATE = "TargetInjectionRate"
        MINIMUMINJECTIONRATE = "MinimumInjectionRate"
        MAXIMUMINJECTIONRATE = "MaximumInjectionRate"
        MINVALVEINJECTIONDP = "MinValveInjectionDP"

    class Well(SurfaceComponent, AssociatedToFluid, CanBeTemplate):
        GASFLOWRATE = "GasFlowRate"
        LIQUIDFLOWRATE = "LiquidFlowRate"
        MASSFLOWRATE = "MassFlowRate"
        FLOWRATETYPE = "FlowRateType"
        ISINJECTION = "IsInjection"
        ISSIMPLE = "IsSimple"
        CHECKVALVESETTING = "CheckValveSetting"
        WELLHEADDEPTH = "WellheadDepth"
        AMBIENTTEMPERATURE = "AmbientTemperature"
        USEGASLIFTVALVE = "UseGasliftValve"
        ALHANATICHECK = "AlhanatiCheck"
        SURFACEGASTEMPERATURE = "SurfaceGasTemperature"
        SURFACEGASPRESSURE = "SurfaceGasPressure"
        TARGETINJECTIONRATE = "TargetInjectionRate"
        MINIMUMINJECTIONRATE = "MinimumInjectionRate"
        MAXIMUMINJECTIONRATE = "MaximumInjectionRate"
        MINVALVEINJECTIONDP = "MinValveInjectionDP"
        GASLIFTINPUTOPTION = "GasLiftInputOption"
        GASSPECIFICGRAVITY = "GasSpecificGravity"
        TUNINGFACTOR = "TuningFactor"
        TESTRACKTEMPERATURE = "TestRackTemperature"
        NITROGENCORRECTIONTYPE = "NitrogenCorrectionType"
        TRAJECTORY = 'Trajectory'
        GEOTHERMALPROFILE = 'BoreholeGeothermalProfile'
        COMMENTS = 'Comments'
        WELLOUTLETEQUIPMENT = "WellOutletEquipment"
        ISMULTIPOINTING = 'IsMultiPointing'
        DIAGNOSTICSTYPE = 'DiagnosticsType'
        THROTTLINGOPTION = 'ThrottlingOption'
        PRESSUREGRADIENTTYPE = 'PressureGradientType'
        class HeatTransfer:
            UVALUEINPUTOPTION = "HeatTransferMethod"
            UCOEFF = "UCoeff"
            USEWELLHEADAMBIENTTEMPERATURE = "UseWellHeadAmbientTemperature"
            PRODUCTIONINJECTIONTIME = 'ProductionInjectionTime'
            HEATTRANSFERCOEFFICIENTSTATUS = 'HeatTransferCoefficientStatus'
            ISGEOSURVEYDEPTHTVD = "IsGeoSurveyDepthTVD"
        class DeviationSurvey:
            SURVEYTYPE = "SurveyType"
            RELATIVEDEPTHOPTION = "DeviationRelativeDepth"
            DEPENDENTPARAMETER = "TrajectoryDependantParameter"
            CALCULATEUSINGTANGENTIALMETHOD = "CalculateUsingTangentialMethod"
        

    class NodalPoint:
        NODALTYPE = "NodalType"
        DEPTH = "Depth"
        WELLSTRINGTYPE = "WellStringType"
        EQUIPMENT = "Equipment"
        NAME = "Name"

    class NodalOperatingEnvelopePlot:
        GASFLOWRATE = 'GasFlowrate'
        GASFLOWRATEPRESSURE = 'GasFlowratePressure'
        MASSFLOWRATE = 'MassFlowrate'
        MASSFLOWRATEPRESSURE = 'MassFlowratePressure'
        LIQUIDFLOWRATE = 'LiquidFlowrate'
        LIQUIDFLOWRATEPRESSURE = 'LiquidFlowratePressure'

    class GlobalCatalog:
        NAME = 'Name'
        CATALOGTYPE = 'CatalogType'


    # #############################################################################
    # Concrete parameter classes for Tables
    # #############################################################################
    class FlowlineGeometry:
        MEASUREDDISTANCE = 'MeasuredDistance'
        HORIZONTALDISTANCE = 'HorizontalDistance'
        ELEVATION = 'Elevation'
        LATITUDE = 'Latitude'
        LONGITUDE = 'Longitude'
        ISVERTEX = 'IsVertex'

    class GeothermalSurvey:
        MEASUREDDISTANCE = 'MeasuredDistance'
        HORIZONTALDISTANCE = 'HorizontalDistance'
        TEMPERATURE = 'Temperature'
        CURRENTVELOCITY = 'CurrentVelocity'
        UCOEFF = 'UCoeff'
        THERMALCONDUCTIVITY = 'ThermalConductivity'
        DENSITY = 'Density'
        SPECIFICHEATCAPACITY = 'SpecificHeatCapacity'

    class WellTrajectory:
        MEASUREDDEPTH = 'MeasuredDepth'
        TRUEVERTICALDEPTH = 'TrueVerticalDepth'
        INCLINATION = 'Inclination'
        AZIMUTH = 'Azimuth'
        MAXDOGLEGSEVERITY = 'MaxDogLegSeverity'

    class CompletionTestPoint:
        LIQUIDFLOWRATE = 'LiquidFlowRate'
        GASFLOWRATE = "GasFlowRate"
        STATICRESERVOIRPRESSURE = 'StaticReservoirPressure'
        BOTTOMHOLEFLOWINGPRESSURE = 'BottomHoleFlowingPressure'

    class PQCurve:
        GASFLOWRATE = 'GasFlowRate'
        LIQUIDFLOWRATE = 'LiquidFlowRate'
        MASSFLOWRATE = 'MassFlowRate'
        PRESSURE = 'Pressure'
        
    class RiskIndexLimits:
        NEGLIGIBLE = 'Negligible'
        LOW = 'Low'
        MODERATE = 'Moderate'
        HIGH = 'High'
        
            
    class TpaCorrosionModel:
        OXYGENORBACTERIA = 'OxygenOrBacteria'
        PREEXISTINGDAMAGE = 'PreExistingDamage'
        POWDERORDEBRIS = 'PowderOrDebris'
        PIPEDEPLOYMENTYEAR = 'PipeDeploymentYear'
        CORROSIONASSESSMENTYEAR = 'CorrosionAssessmentYear'

    class DeWaardCorrosionModel:
        EFFICIENCY = 'Efficiency'
        CALCULATEPH = 'CalculatePH'
        PHVALUE = 'PHValue'

# #############################################################################
# Enumerated constants used by PIPESIM domain model
# #############################################################################
class Constants:
    ''' Enumerated constants used by PIPESIM domain model '''

    
    class ConstraintType:
        GASLIFT = "Gaslift"
        ESP = "Esp"
        PCP = "Pcp"
        CHOKE = "Choke"
        FLOWLINE = "Flowline"
        SINK = "Sink"
        NOCONTROL = "NoControl"

    class WellImportFluidConflict:
        CREATENEW = "CreateNew"
        USEEXISTING = "UseExisting"
        DONTIMPORT = "DontImport"

    class SoilType:
        PEATDRY = "PeatDry"
        PEATWET = "PeatWet"
        PEATICY = "PeatIcy"
        LOAM = "Loam"
        SANDYDRY = "SandyDry"
        SANDYMOIST = "SandyMoist"
        SANDYSOAKED = "SandySoaked"
        CLAYDRY = "ClayDry"
        CLAYMOIST = "ClayMoist"
        CLAYWET = "ClayWet"
        CLAYFROZEN = "ClayFrozen"
        GRAVEL = "Gravel"
        GRAVELSANDY = "GravelSandy"
        LIMESTONE = "Limestone"
        SANDSTONE = "Sandstone"
        ICE = "Ice"
        ICEN40C = "IceN40C"
        SNOWLOOSE = "SnowLoose"
        SNOWHARD = "SnowHard"
        USERDEFINED = "UserDefined"

    class MetoceanDataLocation:
        GULFOFMEXICO = "GOM"
        NORTHSEA = "NSea"
        WESTAFRICA = "WAfrica"
        WESTAUSTRALIA = "WAustralia"
        OFFSHOREBRAZIL = "OffshoreBrazil"
        USERDEFINED = "UserDefined"

    class NetworkSolverMethod:
        AUTOMATIC = "Automatic"
        STANDARD = "Standard"
        ADVANCED = "Advanced"

    class GisElevationDataSource:
        ASTER = "astergdem"
        ESRI = "Esri"
        SRTM = "srtm3"

    class OilFVFCorrelation:
        STANDING = "Standing"
        VASQUEZANDBEGGS = "VasquezAndBeggs"
        KARTOATMODJO = "Kartoatmodjo"
        KARTOATMODJO = "Kartoatmodjo"

    class LiveOilViscCorrelation:
        BEGGSANDROBINSON = "BeggsAndRobinson"
        CHEWANDCONNALY = "ChewandConnaly"
        KARTOATMODJO = "Kartoatmodjo"
        KHAN = "Khan"
        DEGHETTO = "DeGhetto"
        HOSSAIN = "Hossain"
        ELSHARKAWY = "Elsharkawy"
        PETROSKYFARSHAD = "PetroskyFarshad"

    class GasCompressCorrelation:
        STANDING = "Standing"
        HALLANDYARBOROUGH = "HallAndYarborough"
        ROBINSONETAL = "Robinsonetal"

    class GasViscCorrelation:
        LEEETAL = "Leeetal"


    class CharacterizationSystem:
        PVTI = "PVTi"
        DBR = "DBR"
        MULTIFLASH = "Multiflash"

    class BICsCorrelation:
        PVTI = "PVTi"
        OILANDGAS1 = "OilAndGas1"
        OILANDGAS2 = "OilAndGas2"
        OILANDGAS3 = "OilAndGas3"
        OILANDGAS4 = "OilAndGas4"

    class IPRModels:
        IPRBACKPRESSURE = "IPRBackPressure"
        IPRDARCY = "IPRDarcy"
        IPRTRILINEAR = "IPRTriLinear"
        IPRFETKOVITCH = "IPRFetkovitch"
        IPRFORCHHEIMER = "IPRForchheimer"
        IPRHORIZONTALPI = "IPRHorizontalPI"
        IPRHYDRAULICFRACTURE = "IPRHydraulicFracture"
        IPRJONES = "IPRJones"
        IPRPIMODEL = "IPRPIModel"
        IPRPSSBABUODEH = "IPRPSSBabuOdeh"
        IPRSSJOSHI = "IPRSSJoshi"
        IPRVOGEL = "IPRVogel"

    class ErosionModels:
        API14E = "API14e"

    class CorrosionModels:
        DEWAARD1995 = "deWaard1995"
        TPA = "Tpa"
        NONE = "None"

    class SalinityModel:
        NONE = "None"
        IONANALYSIS = "IonAnalysis"
        TDS = "TDS"

    class CompositionalFluidFlash:
        class PhysicalPropertiesMethod:
            INTERPOLATE = "Interpolate"
            HYBRID = "Hybrid"
            RIGOROUS = "Rigorous"
        class TemperatureEnthalpyMethod:
            INTERPOLATE = "Interpolate"
            HYBRID = "Hybrid"
            RIGOROUS = "Rigorous"
        class SingleComponentSystem:
            YES = "Yes"
            NO = "No"
            AUTOMATIC = "Automatic"

    class MultiphaseFlowCorrelationSource:
        BAKER_JARDINE = "BJA"
        TULSA = "Tulsa"
        OLGAS = "OLGAS"
        TUFFPUNIFIED = "TUFFP Unified"
        LEDAFLOWPM = "LedaFlow PM"
        NEOTEC = "Neotec"

    class MultiphaseFlowCorrelation:
        class BakerJardine:
            ANSARI = "Ansari"
            BEGGSBRILLORIGINAL = "Beggs & Brill Original"
            BEGGSBRILLTAITELDUKLERMAP = "Beggs & Brill Taitel Dukler map"
            BEGGSBRILLREVISED = "Beggs & Brill Revised"
            BEGGSBRILLREVISEDTAITELDUKLERMAP = "Beggs & Brill Revised Taitel Dukler map"
            BAKERJARDINEREVISED = "Baker Jardine Revised"
            DUKLERAGAFLANIGAN = "Dukler AGA & Flanigan"
            DUKLERAGAFLANIGAN_EATONHOLDUP = "Dukler AGA & Flanigan (Eaton Holdup)"
            MUKHERJEEBRILL = "Mukherjee & Brill"
            NOSLIPASSUMPTION = "No Slip Assumption"
            OLIEMANS = "Oliemans"
            XIAO = "Xiao"
            BEGGSBRILL = "Beggs & Brill"
            DUKLER = "Dukler"
            DUNSROS = "Duns & Ros"
            GOVIERAZIZFOGARASI = "Govier Aziz & Fogarasi"
            GRAY_MODIFIED = "Gray (modified)"
            GRAY_ORIGINAL = "Gray (original)"
            HAGEDORNBROWN = "Hagedorn & Brown"
            HAGEDORNBROWNDUNSROSMAP = "Hagedorn & Brown Duns & Ros map"
            ORKISZEWSKI = "Orkiszewski"
        class OLGAS:
            OLGASV731_3PHASE = "OLGAS v. 7.3.1 3-Phase"
            OLGASV731_2PHASE = "OLGAS v. 7.3.1 2-Phase"
            OLGASV72_3PHASE = "OLGAS v. 7.2 3-Phase"
            OLGASV72_2PHASE = "OLGAS v. 7.2 2-Phase"
            OLGASV627_3PHASE = "OLGAS v. 6.2.7 3-Phase"
            OLGASV627_2PHASE = "OLGAS v. 6.2.7 2-Phase"
            OLGAS20171_2PHASE = "OLGAS 2017.1 2-Phase"
            OLGAS20171_3PHASE = "OLGAS 2017.1 3-Phase"
            OLGAS20171_3PHASEHD = "OLGAS 2017.1 3-Phase HD"
        class TUFFPUnified:
            TUFFPV20111_3PHASE_DEFAULT = "TUFFP v. 2011.1 3-Phase (default)"
            TUFFPV20111_3PHASE_EMULSIONOVERRIDE = "TUFFP v. 2011.1 3-Phase (emulsion override)"
            TUFFPV20111_2PHASE = "TUFFP v. 2011.1 2-Phase"
        class LedaFlowPM:
            LEDAFLOWV14_3PHASE = "LedaFlow v. 1.4 3-Phase"
            LEDAFLOWV14_2PHASE = "LedaFlow v. 1.4 2-Phase"
            LEDAFLOWV22_3PHASE = "LedaFlow v. 2.2 3-Phase"
            LEDAFLOWV22_2PHASE = "LedaFlow v. 2.2 2-Phase"
        class Neotec:
            GREGORY = "Gregory"
            AZIZGOVIERFOGARASI = "Aziz Govier Fogarasi"
            EATONOLIEMANS = "Eaton Oliemans"
            HUGHMARKDUKLER = "Hughmark Dukler"
            XIAOMODFILM = "Xiao Mod. Film"
            GOMEZ = "Gomez"
            GOMEZENHANCED = "Gomez Enhanced"
        class TulsaLegacy:
            BEGGSBRILL = "Beggs & Brill"
            DUNSROS = "Duns & Ros"
            GOVIERAZIZ = "Govier Aziz"
            HAGEDORNBROWN_REVISED = "Hagedorn & Brown (Revised)"
            HAGEDORNBROWN_ORIGINAL = "Hagedorn & Brown (Original)"
            MUKHERJEEBRILL = "Mukherjee & Brill"
            ORKISZEWSKI = "Orkiszewski"
        

    class NodalAnalysisLimits:
        LIQUIDFLOWRATE = "LiquidFlowRate"
        GASFLOWRATE = "GasFlowRate"
        MASSFLOWRATE = "MassFlowRate"

    class FlowRateCondition:
        STOCKTANK = "StockTank"
        INSITU = "Flowing"

    class TubingPosition:
        POSITIONED = "Positioned"
        CENTRALIZED = "Centralized"
        FLUSHJOINT = "FlushJoint"
        NOTPOSITIONED = "NotPositioned"
        
    class HeatTransferCoefficient:
        CALCULATE = "Calculate"
        SPECIFY = "Specify"

    class PerforationPosition:
        POSITIONED = "Positioned"
        CENTERED = "Centered"
        ECCENTERED = "Eccentered"

    class PerforationGunPhaseAngle:
        ZERO = "zero"
        P45 = "p45"
        P60 = "p60"
        P72 = "p72"
        P90 = "p90"
        P99 = "p99"
        P120 = "p120"
        P120_P60 = "p120_p60"
        P135_P45 = "p135_p45"
        P140_P20 = "p140_p20"
        P180 = "p180"
        PM10 = "pm10"
        PM20 = "pm20"
        PM45 = "pm45"
        ZERO_PM45 = "zero_pm45"
        PM60 = "pm60"
        ZERO_PM60 = "zero_pm60"
        PM90 = "pm90"
        P45_PNDLM = "p45_pndlm"
        ZERO_PM35 = "zero_pm35"
        MOEB45 = "moeb45"
        P120_P40 = "p120_p40"

    class PerforationGunHardware:
        STANDARD = "Standard"
        OBSOLETE = "Obsolete"
        NONSTANDARD = "NonStandard"
        PURE = "PURE"
        STDPURE = "STDPURE"
        OBSPURE = "ObsPURE"
        NONSTANDARDPURE = "NonStandardPURE"
        MYSTERY = "Mystery"
        UNKNOWN = "Unknown"

    class PenetrationModelOptions:
        ROCKONLY = "RockOnly"
        CONCRETEONLY = "ConcreteOnly"
        ROCKORCONCRETE = "RockOrConcrete"

    class PenetrationModelType:
        ROCK = "Rock"
        CONCRETE = "Concrete"

    class NodalPointType:
        SURFACE = "Surface"
        DOWNHOLE = "Downhole"

    class PerforationGunAPITestEdition:
        ESTIMATED_API = "Estimated_API"
        UNOFFICIAL_API = "Unofficial_API"
        UNOFFICIAL_C_33M = "Unofficial_C_33M"
        UNOFFICIAL_19B_1ST_ED = "Unofficial_19B_1st_Ed"
        RP43_4THED = "RP43_4thEd"
        RP43_5THED = "RP43_5thEd"
        RP43_C_33M = "RP43_C_33M"
        A19B_1STED = "A19B_1stEd"
        CUSTOM_VALUES = "Custom_Values"
        BASED_CUSTOM_VALUES = "Based_Custom_Values"
        BASED_A19B_1STED = "Based_A19B_1stEd"
        BASED_RP43_C_33M = "Based_RP43_C_33M"
        BASED_RP43_5THED = "Based_RP43_5thEd"
        BASED_RP43_4THED = "Based_RP43_4thEd"
        BASED_UNOFFICIAL_19B_1ST_ED = "Based_Unofficial_19B_1st_Ed"
        BASED_UNOFFICIAL_C_33M = "Based_Unofficial_C_33M"
        BASED_UNOFFICIAL_API = "Based_Unofficial_API"

    class DeviationSurveyType:
        VERTICAL = "VerticalDeviation"
        TWODIMENSIONAL = "TwoDimensional"
        THREEDIMENSIONAL = "ThreeDimensional"

    class ReferenceDepthOption:
        OriginalRKB = "OriginalRKB"
        RKB = "RKB"
        GL = "GL"
        MSL = "MSL"
        THF = "THF"

    class TrajectoryDependentParameter:
        MD = "MD"
        TVD = "TVD"
        ANGLE = "Angle"

    class UValueInputOption:
        InputSingleUValue = "InputSingleUValue"
        InputMultipleUValues = "InputMultipleUValues"


    class PipeHeatTransfer:
        INSULATED = "Insulated"
        COATED = "Coated"
        BAREINAIR = "BareInAir"
        BAREINWATER = "BareInWater"
        USERSUPPLIED = "UserSupplied"

    class PipeBurialMethod:
        METHOD2009 = "Method2009"
        METHOD2000 = "Method2000"
        METHOD1983 = "Method1983"

    class InsideFilmCoeffMethod:
        KREITH = "Kreith"
        KAMINSKY = "Kaminsky"

        
    class TrilinearCalculationType:
        CONSTANTPRESSURE = "ConstantPressure"
        CONSTANTRATE = "ConstantRate"

    class FlowRateType:
        LIQUIDFLOWRATE = "LiquidFlowRate"
        GASFLOWRATE = "GasFlowRate"
        MASSFLOWRATE = "MassFlowRate"

    class RangeType:
        RANGEINCREMENT = "rangeIncrement"
        RANGEDECREMENT = "rangeDecrement"
        RANGESTEP = "rangeStep"
        RANGEMULTIPLY = "rangeMultiply"

    class SinglePhaseFlowCorrelation:
        MOODY = "Moody"
        AGA = "AGA"
        PANHANDLEA = "Panhandle 'A'"
        PANHANDLEB = "Panhandle 'B'"
        HAZEN_WILLIAMS = "Hazen - Williams"
        WEYMOUTH = "Weymouth"
        CULLENDER_SMITH = "Cullender - Smith"

    class SensitivityType:
        UNDEFINED = "Undefined"
        FLUID = "Fluid"
        SYSTEMDATA = "SystemData"
        GASLIFTDATA = "GasliftData"

    class SystemVarType:
        UNDEFINED = "varUndefined"
        INLETPRESSURE = "varInletPressure"
        OUTLETPRESSURE = "varOutletPressure"
        LIQFLOWRATE = "varLiqFlowrate"
        GASFLOWRATE = "varGasFlowrate"
        MASSFLOWRATE = "varMassFlowrate"
        CUSTOM = "varCustom"

    class DeviationRelativeDepth:
        ORIGINALRKB = "OriginalRKB"
        RKB = "RKB"
        GL = "GL"
        MSL = "MSL"
        THF = "THF"

    class TrajectoryDependentParameter:
        MD = "MD"
        TVD = "TVD"
        ANGLE = "Angle"

    class SurveyType:
        VERTICALDEVIATION = "VerticalDeviation"
        TWODIMENSIONAL = "TwoDimensional"
        THREEDIMENSIONAL = "ThreeDimensional"

    class ZoneMaterial:
        UNKNOWN = "unknown"
        SHALE = "shale"
        SAND = "sand"
        WATER = "water"

    class GISWMSLayerPropertyFormat:
        PNG = "PNG"
        JPEG = "JPEG"

    class ElevationSource:
        SRTM3 = "srtm3"
        ASTERGDEM = "astergdem"
        ESRI = "Esri"

    class GasRatioOption:
        GLR = "GLR"
        GOR = "GOR"
        LGR = "LGR"
        OGR = "OGR"

    class WaterRatioOption:
        WATERCUT = "WaterCut"
        GWR = "GWR"
        WGR = "WGR"

    class DeadOilViscosityCorrelation:
        BEGGSANDROBINSON = "BeggsAndRobinson"
        GLASO = "Glaso"
        KARTOATMODJO = "Kartoatmodjo"
        DEGHETTO = "DeGhetto"
        HOSSAIN = "Hossain"
        ELSHARKAWY = "Elsharkawy"
        PETROSKYFARSHAD = "PetroskyFarshad"
        USER2POINT = "User2Point"
        USERTABLE = "UserTable"


    class LiveOilViscosityCorrelation:
        BEGGSANDROBINSON = "BeggsAndRobinson"
        CHEWANDCONNALY = "ChewandConnaly"
        KARTOATMODJO = "Kartoatmodjo"
        KHAN = "Khan"
        DEGHETTO = "DeGhetto"
        HOSSAIN = "Hossain"
        ELSHARKAWY = "Elsharkawy"
        PETROSKYFARSHAD = "PetroskyFarshad"

    class LiquidViscosityCalculationMethod:
        CONTINUOUSPHASE = "ContinuousPhase"
        OILWATERVOLUMERATIO = "OilWaterVolumeRatio"
        ORIGINALWOELFLIN = "OriginalWoelflin"
        WOELFLINLOOSE = "WoelflinLoose"
        WOELFLINMEDIUM = "WoelflinMedium"
        WOELFLINTIGHT = "WoelflinTight"
        BRINKMAN = "Brinkman"
        VANDVAND = "VandVand"
        VANDBARNEAMIZRAHI = "VandBarneaMizrahi"
        VANDUSER = "VandUser"
        RICHARDSON = "Richardson"
        LEVITONLEIGHTON = "LevitonLeighton"
        USERTABLE = "UserTable"

    class EnthalpyCalcMethod:
        METHOD1983 = "Method1983"
        METHOD2009 = "Method2009"

    class UndersaturatedOilViscosityCorrelation:
        NONE = "None"
        VASQUEZANDBEGGS = "VasquezAndBeggs"
        KOUZEL = "Kouzel"
        KARTOATMODJO = "Kartoatmodjo"
        KHAN = "Khan"
        DEGHETTO = "DeGhetto"
        HOSSAIN = "Hossain"
        ELSHARKAWY = "Elsharkawy"
        BERGMANANDSUTTON = "BergmanAndSutton"
        PETROSKYFARSHAD = "PetroskyFarshad"

    class CriticalFlowCorrelation:
        MECHANISTIC = "Mechanistic"
        GILBERT = "Gilbert"
        ROS = "Ros"
        ACHONG = "Achong"
        BAXENDELL = "Baxendell"
        ASHFORD = "Ashford"
        POETBECK = "Poetbeck"
        OMANA = "Omana"
        PILEHVARI = "Pilehvari"

    class SubCriticalFlowCorrelation:
        MECHANISTIC = "Mechanistic"
        API14B = "API14b"
        ASHFORD = "Ashford"

    class ComponentFractionType:
        MOLE = "Mole"
        MASS = "Mass"

    class LiquidViscosityCalculationMethod:
        CONTINUOUSPHASE = "ContinuousPhase"
        OILWATERVOLUMERATIO = "OilWaterVolumeRatio"
        ORIGINALWOELFLIN = "OriginalWoelflin"
        WOELFLINLOOSE = "WoelflinLoose"
        WOELFLINMEDIUM = "WoelflinMedium"
        WOELFLINTIGHT = "WoelflinTight"
        BRINKMAN = "Brinkman"
        VANDVAND = "VandVand"
        VANDBARNEAMIZRAHI = "VandBarneaMizrahi"
        VANDUSER = "VandUser"
        RICHARDSON = "Richardson"
        LEVITONLEIGHTON = "LevitonLeighton"
        USERTABLE = "UserTable"

    class SaltWaterDensity:
        DEFAULTDENSITY = "DefaultDensity"
        DENSITY = "Density"
        SALINITY = "Salinity"

    class FluidFlashType:
        PRESSURETEMPERATURE = "PressureTemperature"
        PRESSUREENTHALPYMASS = "PressureEnthalpyMass"
        PRESSUREENTROPYMASS = "PressureEntropyMass"
        PRESSUREENTHALPYMOLAR = "PressureEnthalpyMolar"
        PRESSUREENTROPYMOLAR = "PressureEntropyMolar"

    class IPRDarcyRatioType:
        RATIO = "Ratio"
        ABSOLUTE = "Absolute"

    class PerforationSkinMethod:
        MCLEOD = "McLeod"
        KARAKASTARIQ = "KarakasTariq"

    class WellCompletionType:
        NONE = "None"
        OPENHOLE = "OpenHole"
        PERFORATED = "Perforated"
        GRAVELPACKEDANDPERFORATED = "GravelPackedAndPerforated"
        OPENHOLEGRAVELPACK = "OpenHoleGravelPack"
        FRACPACK = "FracPack"

    class ChokeValveEquation:
        MECHANISTIC = "Mechanistic"
        APIRP11V2 = "APIRP11V2"

    class AmbientTemperatureOption:
        INPUTSINGLEVALUE = "InputSingleValue"
        INPUTMULTIPLEVALUES = "InputMultipleValues"
        USEGLOBALVALUE = "UseGlobalValue"

    class AmbientFluid:
        AIR = "Air"
        WATER = "Water"

    class WaterInterpolationMethod:
        INTERPOLATE = "Interpolate"
        STEPFUNCTION = "StepFunction"

    class DeviationSurveyCalculationMethod:
        MEASUREDDISTANCE = "measuredDistance"
        HORIZONTALDISTANCE = "horizontalDistance"
        VERTICALDISTANCE = "verticalDistance"

    class CompletionTestType:
        MULTIPOINT = "Multipoint"
        ISOCHRONAL = "Isochronal"

    class GasLiftType:
        INJECTIONGASRATE = "InjectionGasRate"
        GLR = "GLR"
        GLRINCREASE = "GLRIncrease"

    class GaugeType:
        UNDEFINED = "gaugeUndefined"
        PRESSURE = "gaugePressure"
        FLOWRATE = "gaugeFlowRate"
        TEMPERATURE = "gaugeTemperature"

    class HeatExchangerPressureSpecification:
        DISCHARGEPRESSURE = "dischargePressure"
        PRESSUREDROP = "pressureDrop"

    class HeatExchangerTemperatureSpecification:
        DELTATEMPERATURE = "deltaTemperature"
        DISCHARGETEMPERATURE = "dischargeTemperature"
        DUTY = "duty"

    class OilCalibrationType:
        DENSITY = "Density"
        OFVF = "OFVF"

    class RodPumpBasisType:
        STROKELENGTHFREQUENCY = "StrokeLengthFrequency"
        NOMINALRATE = "NominalRate"

    class NetworkDiagramLayerProperty:
        DEFAULT = "Default"
        LINKLAYER = "LinkLayer"
        EQUIPMENT = "Equipment"
        JUNCTION = "Junction"
        SINKSOURCE = "SinkSource"
        FOLDERS = "Folders"
        GAUGES = "Gauges"
        PROPERTYPANELS = "PropertyPanels"
        CUSTOM = "Custom"

    class SensitivityVariableType:
        NONE = "varNone"
        INFLOW = "varInflow"
        OUTFLOW = "varOutflow"
        XAXIS = "varXAxis"
        SENSITIVITY = "varSensitivity"

    class CalculatedVariable:
        INLETPRESSURE = "calcInletPressure"
        OUTLETPRESSURE = "calcOutletPressure"
        FLOWRATE = "calcFlowrate"
        CUSTOM = "calcCustom"

    class Fluid:
        LIQUID = "liquid"
        GAS = "gas"
        WATER = "water"

    class FluidType:
        BLACKOIL = "fluidBlackOil"
        COMPOSITIONAL = "fluidCompositional"
        PVT = "fluidPVT"
        MFL = "fluidMFL"
        STEAM = "fluidSteam"

    class PVTPackage:
        E300 = "E300"
        GERG = "GERG"
        MULTIFLASH = "MULTIFLASH"

    class MultiphaseBoosterType:
        GENERIC = "GenericBooster"
        ONESUBSEA = "OneSubseaBooster"
        WETGASCOMPRESSOR = "WetGasCompressor"

    class OneSubseaBoosterModel:
        HX310_250_180 = "FRAMO Helico-Axial 310-250/180"
        HX310_400_180 = "FRAMO Helico-Axial 310-400/180"
        HX310_500_45 = "FRAMO Helico-Axial 310-500/45"
        HX310_500_180 = "FRAMO Helico-Axial 310-500/180"
        HX310_600_120 = "FRAMO Helico-Axial 310-600/120"
        HX310_700_45 = "FRAMO Helico-Axial 310-700/45"
        HX310_800_120 = "FRAMO Helico-Axial 310-800/120"
        HX310_900_45 = "FRAMO Helico-Axial 310-900/45"
        HX310_1100_45 = "FRAMO Helico-Axial 310-1100/45"
        HX310_1100_120 = "FRAMO Helico-Axial 310-1100/120"
        HX360_1200_38 = "FRAMO Helico-Axial 360-1200/38"
        HX360_1500_38 = "FRAMO Helico-Axial 360-1500/38"
        HX360_1800_38 = "FRAMO Helico-Axial 360-1800/38"

    class WetGasCompressorModel:
        CRC385_2400_51 = "OneSubsea-CRC385-2400-51"
        CRC385_3600_51 = "OneSubsea-CRC385-3600-51"
        CRC385_4800_51 = "OneSubsea-CRC385-4800-51"
        CRC385_5800_51 = "OneSubsea-CRC385-5800-51"
        CRC385_6900_51 = "OneSubsea-CRC385-6900-51"
        CRC385_8400_51 = "OneSubsea-CRC385-8400-51"

    class WetGasCompressorCoolerModel:
        NONE = "None"
        USERSPECIFIED = "User specified"
        COOLER6M8B = "Cooler-6m-8b"

    class SeparatorProductFluid:
        LIQUID = "liquid"
        GAS = "gas"
        WATER = "water"
        OIL = "oil"
        GASOIL = "gasOil"
        GASWATER = "gasWater"

    class TubingSectionType:
        CASING = "Casing"
        LINER = "Liner"
        OPENHOLE = "OpenHole"
        TUBING = "Tubing"

    class AnnulusMaterial:
        CEMENT = "Cement"
        MUD = "Mud"
        BRINE = "Brine"
        WATER = "Water"
        GAS = "Gas"
        OIL = "Oil"
        DIESEL = "Diesel"
        ACID = "Acid"

    class UserEquipmentType:
        SURFACE = "Surface"
        ARTIFICIALLIFT = "ArtificialLift"
        DOWNHOLE = "Downhole"

    class CheckValveSetting:
        NONE = "None"
        BLOCKFORWARD = "BlockForward"
        BLOCKREVERSE = "BlockReverse"
        BLOCKBOTH = "Off"

    class GasLiftInputOption:
        USEGASSPECIFICGRAVITY = "UseGasSpecificGravity"
        ASSOCIATEEXISTINGFLUID = "AssociateExistingFluid"

    class NitrogenCorrectionMethod:
        DAKSUTTON = "DakSutton"
        WRINKLEREADES1989 = "WrinklerEades1989"

    class GenericEquipmentPressureSpecification:
        DISCHARGEPRESSURE = "dischargePressure"
        DELTAPRESSURE = "deltaPressure"
        PRESSURERATIO = "pressureRatio"

    class GenericEquipmentThermodynamics:
        DEFAULT = "defaultRoute"
        ISENTHALPIC = "isenthalpicRoute"
        ISENTROPIC = "isentropicRoute"
        ISOTHERMAL = "isothermalRoute"

    class CompressorThermodynamics:
        ADIABATIC = "routeAdiabatic"
        POLYTROPIC = "routePolytropic"
        MOLLIER = "routeMollier"

    class ViscosityCorrection:
        NONE = "None"
        CENTRILIFT = "Centrilift"
        REDA = "Reda"
        TURZO = "Turzo"
        USER = "User"

    class ProfilePlotOption:
        DEFAULT = "Default"
        ELEVATIONVSPRESSURE = "ElevationVsPressure"
        ELEVATIONVSTEMPERATURE = "ElevationVsTemperature"
        PRESSUREVSTOTAL_DISTANCE = "PressureVsTotal_Distance"
        TEMPERATUREVSTOTAL_DISTANCE = "TemperatureVsTotal_Distance"

    class PumpThermodynamics:
        ADIABATIC = "Adiabatic"
        MOLLIER = "Mollier"
        ISOTHERMAL = "Isothermal"

    class CompletionFluidEntry:
        SINGLEPOINT = "SinglePoint"
        DISTRIBUTED = "Distributed"

    class Orientation:
        VERTICAL = "Vertical"
        HORIZONTAL = "Horizontal"

    class BoreholeFluid:
        MUD = "Mud"
        BRINE = "Brine"
        WATER = "Water"
        GAS = "Gas"
        OIL = "Oil"
        DIESEL = "Diesel"
        ACID = "Acid"

    class FormationFluid:
        OIL = "Oil"
        WATER = "Water"
        GAS = "Gas"

    class RockType:
        SANDSTONE = "Sandstone"
        LIMESTONE = "Limestone"
        DOLOMITE = "Dolomite"
        SHALE = "Shale"
        COAL = "Coal"

    class PerforationFlowRate:
        LIQUIDFLOWRATE = "LiquidFlowRate"
        GASFLOWRATE = "GasFlowRate"

    class SensitivityMethod:
        PERMUTED = "Permuted"
        STEPWITHVARIABLE1 = "StepWithVariable1"
        STEPWITHXAXIS = "StepWithXAxis"

    class VFPTablesOperationTable:
        ECLIPSE = "TableEclipse"
        PORES = "TablePores"
        VIP = "TableVIP"
        COMP4 = "TableComp4"
        MORES = "TableMoRes"
        
    class VfpTablesType:
        PRODUCTION = "Production"
        INJECTION = "Injection"

    class DiagnosticsType:
        FIXEDPRESSURE = "FixedPressure"
        FIXEDINJECTION = "FixedInjection"
        FIXEDBOTH = "FixedBoth"

    class ThrottlingType:
        ON = "On"
        OFF = "Off"

    class PressureGradientType:
        INCLUDEFRICTIONLOSSES = "FrictionElevation"
        STATIC = "Static"

    class GasLift:
        ''' Gas Lift Design constants '''

        class DiagnosticsOperationDiagnostics:
            FIXEDPRESSURE = "FixedPressure"
            FIXEDINJECTION = "FixedInjection"
            FIXEDBOTH = "FixedBoth"

        class DiagnosticsOperationThrottling:
            ON = "On"
            OFF = "Off"

        class PressureGradient:
            FRICTIONELEVATION = "FrictionElevation"
            STATIC = "Static"

        class SolutionPoint:
            LIQUIDPRODRATE = "LiquidProdRate"
            RESERVOIRPRESSURE = "ReservoirPressure"
            INJECTIONRATE = "InjectionRate"
            INJECTIONPRESSURE = "InjectionPressure"

        class DesignSpacing:
            NEWSPACING = "NewSpacing"
            CURRENTSPACING = "CurrentSpacing"
            OPTIMUMDEPTH = "OptimumDepth"
            VALVEPORTDEPTH = "ValvePortDepth"

        class ResponseSolution:
            LIQUIDPRODRATE = "LiquidProdRate"
            RESERVOIRPRESSURE = "ReservoirPressure"
            INJECTIONRATE = "InjectionRate"
            INJECTIONPRESSURE = "InjectionPressure"

        class TransferFactor:
            PINJPPROD = "PinjPprod"
            PPROD = "Pprod"

        class TransferGradient:
            SURFACEOFFSET = "SurfaceOffset"
            SURFACEOFFSETDP = "SurfaceOffsetDP"

        class DesignMethod:
            IPOSURFACECLOSE = "IpoSurfaceClose"
            IPOPTMINMAX = "IpoPtMinMax"
            PPODESIGN = "PpoDesign"

        class UnloadingTemperature:
            INJECTION = "Injection"
            PRODUCTION = "Production"
            AMBIENT = "Ambient"
            UNLOADING = "Unloading"

        class ProductionPressureCurve:
            MODEL = "Model"

        class DesignSolutionPoint:
            LIQUIDPRODRATE = "LiquidProdRate"
            RESERVOIRPRESSURE = "ReservoirPressure"
            INJECTIONRATE = "InjectionRate"
            INJECTIONPRESSURE = "InjectionPressure"


        class TopValveLocation:
            LIQUIDTOSURFACE = "LiquidToSurface"
            LIQUIDLEVEL = "LiquidLevel"
            CALCLIQUIDLEVEL = "CalcLiquidLevel"

        class OperatingValves:
            ORIFICE = "Orifice"
            IPO = "IPO"
            PPO = "PPO"

        class DesignTreatTransferGradient:
            OPENINGPRESSURE = "OpeningPressure"
            CLOSINGPRESSURE = "ClosingPressure"

        class DesignTransferGradientDP:
            INJECTIONPRESSURE = "InjectionPressure"
            PRODUCTIONPRESSURE = "ProductionPressure"

    class BlackOilCalibrationSolutionGas:
        LASATER = "Lasater"
        STANDING = "Standing"
        VASQUEZANDBEGGS = "VasquezAndBeggs"
        GLASO = "Glaso"
        KARTOATMODJO = "Kartoatmodjo"
        DEGHETTOETAL = "DeGhettoEtAl"
        PETROSKYFARSHAD = "PetroskyFarshad"

    class MultiflashComponent:
        ONE_2_DIETHYLBENZENE = '1,2-Diethylbenzene'
        TWO_2_DIMETHYLPROPANE = '2,2-Dimethylpropane'
        THREE_METHYL_HEXANE = '3-methyl hexane'
        AMMONIA = 'Ammonia'
        ARGON = 'Argon'
        BENZENE = 'Benzene'
        BUTANE = 'Butane'
        CARBON_DIOXIDE = 'Carbon Dioxide'
        CARBON_MONOXIDE = 'Carbon Monoxide'
        CUMENE = 'Cumene'
        CYCLOHEXANE = 'Cyclohexane'
        CYCLOPENTANE = 'Cyclopentane'
        DECANE = 'Decane'
        DIETHYLENE_GLYCOL = 'Diethylene Glycol'
        DOCOSANE = 'Docosane'
        DODECANE = 'Dodecane'
        DOTRIACONTANE = 'Dotriacontane'
        EICOSANE = 'Eicosane'
        ETHANE = 'Ethane'
        ETHANOL = 'Ethanol'
        ETHYLBENZENE = 'Ethylbenzene'
        ETHYLCYCLOHEXANE = 'Ethylcyclohexane'
        ETHYLENE = 'Ethylene'
        ETHYLENE_GLYCOL = 'Ethylene Glycol'
        HELIUM = 'Helium'
        HENEICOSANE = 'Heneicosane'
        HEPTACOSANE = 'Heptacosane'
        HEPTADECANE = 'Heptadecane'
        HEPTANE = 'Heptane'
        HEXACOSANE = 'Hexacosane'
        HEXADECANE = 'Hexadecane'
        HEXANE = 'Hexane'
        HEXATRIACONTANE = 'Hexatriacontane'
        HYDROGEN = 'Hydrogen'
        HYDROGEN_SULPHIDE = 'Hydrogen Sulphide'
        ISOBUTANE = 'Isobutane'
        ISOPENTANE = 'Isopentane'
        METHANE = 'Methane'
        METHANOL = 'Methanol'
        METHYLCYCLOHEXANE = 'Methylcyclohexane'
        METHYLCYCLOPENTANE = 'Methylcyclopentane'
        M_XYLENE = 'M-Xylene'
        NAPHTHALENE = 'Naphthalene'
        NITROGEN = 'Nitrogen'
        NONACOSANE = 'Nonacosane'
        NONADECANE = 'Nonadecane'
        NONANE = 'Nonane'
        OCTACOSANE = 'Octacosane'
        OCTADECANE = 'Octadecane'
        OCTANE = 'Octane'
        OXYGEN = 'Oxygen'
        O_XYLENE = 'O-Xylene'
        PENTACOSANE = 'Pentacosane'
        PENTADECANE = 'Pentadecane'
        PENTANE = 'Pentane'
        PROPANE = 'Propane'
        P_XYLENE = 'P-Xylene'
        SALT_COMPONENT = 'Salt Component'
        TETRACOSANE = 'Tetracosane'
        TETRADECANE = 'Tetradecane'
        TOLUENE = 'Toluene'
        TRIACONTANE = 'Triacontane'
        TRICOSANE = 'Tricosane'
        TRIDECANE = 'Tridecane'
        TRIETHYLENE_GLYCOL = 'Triethylene Glycol'
        UNDECANE = 'Undecane'
        WATER = 'Water'

    class E300Component:
        BEN = 'BEN'
        C1 = 'C1'
        C10 = 'C10'
        C11 = 'C11'
        C12 = 'C12'
        C13 = 'C13'
        C14 = 'C14'
        C15 = 'C15'
        C16 = 'C16'
        C17 = 'C17'
        C18 = 'C18'
        C19 = 'C19'
        C2 = 'C2'
        C20 = 'C20'
        C21 = 'C21'
        C22 = 'C22'
        C23 = 'C23'
        C24 = 'C24'
        C25 = 'C25'
        C26 = 'C26'
        C27 = 'C27'
        C28 = 'C28'
        C29 = 'C29'
        C3 = 'C3'
        C30 = 'C30'
        C31 = 'C31'
        C32 = 'C32'
        C33 = 'C33'
        C34 = 'C34'
        C35 = 'C35'
        C36 = 'C36'
        C37 = 'C37'
        C38 = 'C38'
        C39 = 'C39'
        C4 = 'C4'
        C40 = 'C40'
        C41 = 'C41'
        C42 = 'C42'
        C43 = 'C43'
        C44 = 'C44'
        C45 = 'C45'
        C5 = 'C5'
        C6 = 'C6'
        C7 = 'C7'
        C8 = 'C8'
        C9 = 'C9'
        CO = 'CO'
        CO2 = 'CO2'
        CYCLOC6 = 'CycloC6'
        ETHYLBENZENE = 'Ethylbenzene'
        H2 = 'H2'
        H2O = 'H2O'
        H2S = 'H2S'
        IC4 = 'IC4'
        IC5 = 'IC5'
        MCYCLOC5 = 'McycloC5'
        MCYCLOC6 = 'McycloC6'
        MPXYLENE = 'MPXylene'
        N2 = 'N2'
        NC4 = 'NC4'
        NC5 = 'NC5'
        OXYLENE = 'OXylene'
        TOL = 'TOL'

    class GERGComponent:
        ARGON = 'Argon'
        CARBON_DIOXIDE = 'Carbon dioxide'
        CARBON_MONOXIDE = 'Carbon monoxide'
        ETHANE = 'Ethane'
        HELIUM = 'Helium'
        HYDROGEN = 'Hydrogen'
        HYDROGEN_SULPHIDE = 'Hydrogen sulphide'
        ISOBUTANE = 'Isobutane'
        ISOPENTANE = 'Isopentane'
        METHANE = 'Methane'
        N_BUTANE = 'n-Butane'
        N_DECANE = 'n-Decane'
        N_HEPTANE = 'n-Heptane'
        N_HEXANE = 'n-Hexane'
        NITROGEN = 'Nitrogen'
        N_NONANE = 'n-Nonane'
        N_OCTANE = 'n-Octane'
        N_PENTANE = 'n-Pentane'
        OXYGEN = 'Oxygen'
        PROPANE = 'Propane'
        WATER = 'Water'

    class EmulsionViscosityMethod:
        """Set to viscosity of the continuous phase"""
        CONTINUOUSPHASE = "ContinuousPhase"
        OILWATERVOLUMERATIO = "OilWaterVolumeRatio"
        ORIGINALWOELFLIN = "OriginalWoelflin"
        WOELFLINLOOSE = "WoelflinLoose"
        WOELFLINMEDIUM = "WoelflinMedium"
        WOELFLINTIGHT = "WoelflinTight"
        BRINKMAN = "Brinkman"
        VANDVAND = "VandVand"
        VANDBARNEAMIZRAHI = "VandBarneaMizrahi"
        VANDUSER = "VandUser"
        RICHARDSON = "Richardson"
        LEVITONLEIGHTON = "LevitonLeighton"
        USERTABLE = "UserTable"

    class EquationOfState:
        class Multiflash:
            PENGROBINSON2PARAMETER = "PengRobinson2Parameter"
            PENGROBINSON3PARAMETER = "PengRobinson3Parameter"
            REDLICHKWONG = "RedlichKwong"
            SOAVEREDLICHKWONG2PARAMETER = "SoaveRedlichKwong2Parameter"
            SOAVEREDLICHKWONG3PARAMETER = "SoaveRedlichKwong3Parameter"
            SOAVEREDLICHKWONG3PARAMETERNRTLMIXINGRULE = "SoaveRedlichKwong3ParameterNRTLMixingRule"
            BENEDICTWEBBRUBINSTARLING = "BenedictWebbRubinStarling"
            CUBICPLUSASSOCIATION = "CubicPlusAssociation"
            CORRESPONDINGSTATES = "CorrespondingStates"
        class GERG:
            GERG_REFPROP = "GERG_REFPROP"
        class E300:
            PENGROBINSON3PARAMETERCORRECTED = "PengRobinson3ParameterCorrected"
            PENGROBINSON2PARAMETERCORRECTED = "PengRobinson2ParameterCorrected"
            SOAVEREDLICHKWONG3PARAMETER = "SoaveRedlichKwong3Parameter"
            SOAVEREDLICHKWONG2PARAMETER = "SoaveRedlichKwong2Parameter"

    class ViscosityCorrelationMethod:
        LOHRENZBRAYCLARK = "LohrenzBrayClark"
        PEDERSEN = "Pedersen"
        AASBERGPETERSEN = "AasbergPetersen"
        NIST = "NIST"
        PEDERSENTWU = "PedersenTwu"
        SUPERTRAPP = "SuperTRAPP"

    class VolumeShiftCorrelationMethod:
        SORIEDE = "Soriede"
        PENELOUXDBR = "PenelouxDBR"
        MULTIFLASH = "Multiflash"

    class CriticalPropertyCorrelationMethod:
        KESLERLEE = "KeslerLee"
        CAVETT = "Cavett"
        RIAZIDAUBERT = "RiaziDaubert"
        WINN = "Winn"
        PEDERSEN = "Pedersen"
        SINGLECARBONNUMBER = "SingleCarbonNumber"

    class ThermalCoefficientsCorrelationMethod:
        KESLERLEE = "KeslerLee"
        KESLERLEEMODIFIED = "KeslerLeeModified"
        MULTIFLASH = "Multiflash"

    class AcfCorrelationMethod:
        KESLERLEE = "KeslerLee"
        EDMISTER = "Edmister"
        THOMASSEN = "Thomassen"
        PEDERSEN = "Pedersen"
        SINGLECARBONNUMBER = "SingleCarbonNumber"

    class SalinityModel:
        NONE = "None"
        IONANALYSIS = "IonAnalysis"
        TDS = "TDS"

    class FluidComponentType:
        HYDROCARBON = "Hydrocarbon"
        NONHYDROCARBON = "NonHydrocarbon"

class OptimizerVariables:
    ''' The optimizer Results Variables '''
    GAS_LIFT_RATE =  "OptimizerGas_lift_rate"
    WELL_IS_SHUT_OFF =  "OptimizerWell_is_shut_off"
    TOTAL_ALLOCATED_POWER_USED =  "OptimizerTotal_allocated_power_used"
    TOTAL_ALLOCATED_GAS_INJECTED =  "OptimizerTotal_allocated_gas_injected"
    PERCENT_CHANGE_IN_WATER_RATE =  "OptimizerPercent_change_in_water_rate"
    PERCENT_CHANGE_IN_GAS_RATE =  "OptimizerPercent_change_in_gas_rate"
    PERCENT_CHANGE_IN_OIL_RATE =  "OptimizerPercent_change_in_oil_rate"
    TOTAL_WATER_RATE =  "OptimizerTotal_water_rate"
    TOTAL_OIL_RATE =  "OptimizerTotal_oil_rate"
    EFFICIENCY =  "OptimizerEfficiency"
    POWER =  "OptimizerPower"
    FREQUENCY =  "OptimizerFrequency"
    SPEED =  "OptimizerSpeed"
    MAXIMUM_GOR =  "OptimizerMaximum_GOR"
    MAXIMUM_CO2 =  "OptimizerMaximum_CO2"
    MAXIMUM_H2S =  "OptimizerMaximum_H2S"
    BUBBLE_POINT_MARGIN_ =  "OptimizerBubble_point_margin_"
    DRAWDOWN_PRESSURE_DROP =  "OptimizerDrawdown_pressure_drop"
    MAXIMUM_EROSIONAL_VELOCITY_RATIO =  "OptimizerMaximum_Erosional_velocity_ratio"
    CASING_HEAD_PRESSURE =  "OptimizerCasing_head_pressure"
    OUTLET_TEMPERATURE =  "OptimizerOutlet_temperature"
    OUTLET_PRESSURE =  "OptimizerOutlet_pressure"
    WATER_RATE =  "OptimizerWater_rate"
    LIQUID_RATE =  "OptimizerLiquid_rate"
    OIL_RATE =  "OptimizerOil_rate"
    BEAN_SIZE =  "OptimizerBean_size"
    TOTAL_GAS_RATE =  "OptimizerTotal_gas_rate"

class SystemVariables:
    ''' The System and Equipment Results Variables '''
    ALHANATI_CRITERION1="AlhanatiCriterion1"
    ALHANATI_CRITERION2="AlhanatiCriterion2"
    ARTIFICIAL_LIFT_QUANTITY="ArtificialLiftQuantity"
    BOTTOM_HOLE_PRESSURE="BottomHolePressure"
    CASE_NUMBER="CaseNumber"
    CASE_STATUS="CaseStatus"
    CASING_HEAD_PRESSURE="CasingHeadPressure"
    CONED_GOR="ConedGOR"
    ESP_DELTA_PRESSURE="ESPDeltaPressure"
    ESP_DELTA_TEMPERATURE="ESPDeltaTemperature"
    ESP_DISCHARGE_PRESSURE="ESPDischargePressure"
    ESP_EFFICIENCY="ESPEfficiency"
    ESP_EFFICIENCY_FACTOR="ESPEfficiencyFactor"
    ESP_FLOWRATE_FACTOR="ESPFlowrateFactor"
    ESP_FREQUENCY="ESPFrequency"
    ESP_HEAD="ESPHead"
    ESP_HEAD_FACTOR="ESPHeadFactor"
    ESP_INTAKE_GAS_VOLUME_FRACTION="ESPIntakeGasVolumeFraction"
    ESP_INTAKE_PRESSURE="ESPIntakePressure"
    ESP_INTAKE_TOTAL_VOLUMETRIC_FLOWRATE="ESPIntakeTotalVolumetricFlowrate"
    ESP_NUMBER_OF_STAGES="ESPNumberOfStages"
    ESP_POWER="ESPPower"
    ESP_POWER_FACTOR="ESPPowerFactor"
    ESP_SUCTION_GAS_VOLUME_FRACTION="ESPSuctionGasVolumeFraction"
    FRICTION_FACTOR_MEAN="FrictionFactorMean"
    GAS_INJECTION_DEPTH="GasInjectionDepth"
    GAS_INJECTION_GAS_TEMPERATURE_BEFORE_MIXING="GasInjectionGasTemperatureBeforeMixing"
    GAS_INJECTION_PRODUCTION_TEMPERATURE_DOWNSTREAM="GasInjectionProductionTemperatureDownstream"
    GAS_INJECTION_PRODUCTION_TEMPERATURE_UPSTREAM="GasInjectionProductionTemperatureUpstream"
    GAS_INJECTION_VALVE_DELTA_TEMPERATURE="GasInjectionValveDeltaTemperature"
    GAS_INJECTION_VALVE_DELTA_PRESSURE="GasInjectionValveDeltaPressure"
    GAS_LIFT_DIAGNOSTICS_PORT_DIAMETER = "GLDiagnosticsValvePortDiameter"
    GAS_LIFT_DIAGNOSTICS_POSITION_STATUS= "GLDiagnosticsValvePositionStatus"
    GAS_LIFT_DIAGNOSTICS_DOME_TEMPERATURE = "GLDiagnosticsValveDomeTemperature"
    GAS_LIFT_DIAGNOSTICS_GAS_RATE_NO_THROTTLING = "GLDiagnosticsValveGasRateNoThrottling"
    GAS_LIFT_DIAGNOSTICS_STATUS = "GLDiagnosticsValveStatus"
    GAS_LIFT_DIAGNOSTICS_CLOSING_PRESSURE = "GLDiagnosticsValveClosingPressure"
    GAS_LIFT_DIAGNOSTICS_OPENING_PRESSURE = "GLDiagnosticsValveOpeningPressure"
    GAS_LIFT_DIAGNOSTICS_DOME_PRESSURE = "GLDiagnosticsValveDomePressure"
    GAS_LIFT_DIAGNOSTICS_PTRO = "GLDiagnosticsValvePtro"
    GAS_LIFT_DIAGNOSTICS_DISCHARGE_COEFFICIENT = "GLDiagnosticsValveDischargeCoefficient"
    GAS_LIFT_DIAGNOSTICS_PORT_TO_BELLOW_AREA = "GLDiagnosticsValvePortToBellowArea"
    GAS_LIFT_DIAGNOSTICS_OPERATION_MODE = "GLDiagnosticsValveOperationMode"
    GAS_LIFT_DIAGNOSTICS_PORT_TYPE = "GLDiagnosticsValveType"

    GAS_LIFT_INJECTION_CASING_HEAD_TEMPERATURE="GasLiftInjectionCasingHeadTemperature"
    GAS_LIFT_INJECTION_PORT_DIAMETER="GasLiftInjectionPortDiameter"
    GAS_LIFT_INJECTION_CASING_PRESSURE="GasLiftInjectionCasingPressure"
    GAS_LIFT_INJECTION_PRESSURE="GasLiftInjectionPressure"
    GAS_LIFT_INJECTION_RATIO="GasLiftInjectionRatio"
    GAS_LIFT_INJECTION_SOURCE_PRESSURE="GasLiftInjectionSourcePressure"
    GAS_LIFT_INJECTION_CASING_TEMPERATURE="GasLiftInjectionCasingTemperature"
    GAS_LIFT_INJECTION_TEMPERATURE="GasLiftInjectionTemperature"
    HEAT_TRANSFER_COEFFICIENT="HeatTransferCoefficient"
    HEEL_GOR_STOCKTANK="HeelGORStockTank"
    HEEL_MASS_FLOWRATE_FLUID="HeelMassFlowrateFluid"
    HEEL_PRESSURE="HeelPressure"
    HEEL_RESERVOIR_DRAWDOWN="HeelReservoirDrawdown"
    HEEL_TEMPERATURE="HeelTemperature"
    HEEL_VELOCITY_FLUID="HeelVelocityFluid"
    HEEL_VOLUME_FLOWRATE_FLUID_INSITU="HeelVolumeFlowrateFluidInSitu"
    HEEL_VOLUME_FLOWRATE_FLUID_STOCKTANK="HeelVolumeFlowrateFluidStockTank"
    HEEL_VOLUME_FLOWRATE_GAS_STOCKTANK="HeelVolumeFlowrateGasStockTank"
    HEEL_VOLUME_FLOWRATE_GAS_STOCKTANK="HeelVolumeFlowrateGasStockTank"
    HEEL_VOLUME_FLOWRATE_LIQUID_INSITU="HeelVolumeFlowrateLiquidInSitu"
    HEEL_VOLUME_FLOWRATE_LIQUID_STOCKTANK="HeelVolumeFlowrateLiquidStockTank"
    HEEL_VOLUME_FLOWRATE_OIL_STOCKTANK="HeelVolumeFlowrateOilStockTank"
    HEEL_WATER_CUT_STOCKTANK="HeelWaterCutStockTank"
    INLET_EROSIONAL_VELOCITY_RATIO="InletErosionalVelocityRatio"
    INLET_GOR_STOCKTANK="InletGORStockTank"
    INLET_MASS_FLOWRATE_FLUID="InletMassFlowrateFluid"
    INLET_MASS_FRACTION_GAS="InletMassFractionGas"
    INLET_TEMPERATURE="InletTemperature"
    INLET_VELOCITY_FLUID="InletVelocityFluid"
    INLET_VELOCITY_GAS="InletVelocityGas"
    INLET_VELOCITY_LIQUID="InletVelocityLiquid"
    INLET_VOLUME_FLOWRATE_FLUID_INSITU="InletVolumeFlowrateFluidInSitu"
    INLET_VOLUME_FLOWRATE_FLUID_STOCKTANK="InletVolumeFlowrateFluidStockTank"
    INLET_VOLUME_FLOWRATE_GAS_INSITU="InletVolumeFlowrateGas"
    INLET_VOLUME_FLOWRATE_GAS_STOCKTANK="InletVolumeFlowrateGasStockTank"
    INLET_VOLUME_FLOWRATE_LIQUID_INSITU="InletVolumeFlowrateLiquid"
    INLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK="InletVolumeFlowrateLiquidStockTank"
    INLET_VOLUME_FLOWRATE_OIL_STOCKTANK="InletVolumeFlowrateOilStockTank"
    INLET_VOLUME_FRACTION_LIQUID="InletVolumeFractionLiquid"
    INLET_WATER_CUT_STOCKTANK="InletWaterCutStockTank"
    INPUT_FLOWRATE="InputFlowrate"
    INPUT_TUBING_HEAD_PRESSURE="InputTubingHeadPressure"
    INPUT_WATERCUT="InputWatercut"
    INPUT_WATER_RATIO="InputWaterRatio"
    MASS_FLOWRATE_AT_NODAL_ANALYSIS_POINT="MassFlowrateAtNodalAnalysisPoint"
    MAXIMUM_CORROSION_RATE="MaximumCorrosionRate"
    MAXIMUM_CORROSION_RISK="MaximumCorrosionRisk"
    MAXIMUM_EROSION_RISK="MaximumErosionRisk"
    MAXIMUM_EROSIONAL_VELOCITY_RATIO="MaximumErosionalVelocityRatio"
    MAXIMUM_EROSION_RATE="MaximumErosionRate"
    MAXIMUM_HEAT_TRANSFER_COEFFICIENT="MaximumHeatTransferCoefficient"
    MAXIMUM_HYDRATE_SUB_COOLING_TEMPERATURE_DIFFERENCE="MaximumHydrateSubCoolingTemperatureDifference"
    MAXIMUM_LIQUID_LOADING_GAS_RATE="MaximumLiquidLoadingGasRate"
    MAXIMUM_LIQUID_LOADING_VELOCITY_RATIO="MaximumLiquidLoadingVelocityRatio"
    MAXIMUM_VELOCITY_FLUID="MaximumVelocityFluid"
    MAXIMUM_VELOCITY_GAS="MaximumVelocityGas"
    MAXIMUM_VELOCITY_LIQUID="MaximumVelocityLiquid"
    MAXIMUM_WAX_SUB_COOLING_TEMPERATURE_DIFFERENCE="MaximumWaxSubCoolingTemperatureDifference"
    NODAL_POINT_BUBBLE_POINT_PRESSURE="NodalPointBubblePointPressure"
    NODAL_POINT_ENTHALPY_FLUID="NodalPointEnthalpyFluid"
    NODAL_POINT_FRACTION_LIQUID="NodalPointFractionLiquid"
    NODAL_POINT_GLR_STOCKTANK="NodalPointGLRStockTank"
    NODAL_POINT_LGR_STOCKTANK="NodalPointLGRStockTank"
    NODAL_POINT_MASS_FLOWRATE_FLUID="NodalPointMassFlowrateFluid"
    NODAL_POINT_PRESSURE="NodalPointPressure"
    NODAL_POINT_TEMPERATURE="NodalPointTemperature"
    NODAL_POINT_VELOCITY_FLUID="NodalPointVelocityFluid"
    NODAL_POINT_VOLUME_FLOWRATE_FLUID_INSITU="NodalPointVolumeFlowrateFluidInSitu"
    NODAL_POINT_VOLUME_FLOWRATE_FLUID_STOCKTANK="NodalPointVolumeFlowrateFluidStockTank"
    NODAL_POINT_VOLUME_FLOWRATE_GAS_INSITU="NodalPointVolumeFlowrateGasInSitu"
    NODAL_POINT_VOLUME_FLOWRATE_GAS_STOCKTANK="NodalPointVolumeFlowrateGasStockTank"
    NODAL_POINT_VOLUME_FLOWRATE_LIQUID_INSITU="NodalPointVolumeFlowrateLiquidInSitu"
    NODAL_POINT_VOLUME_FLOWRATE_LIQUID_STOCKTANK="NodalPointVolumeFlowrateLiquidStockTank"
    NODAL_POINT_VOLUME_FLOWRATE_OIL_STOCKTANK="NodalPointVolumeFlowrateOilStockTank"
    NODAL_POINT_WATER_CUT_INSITU="NodalPointWaterCutInSitu"
    NODAL_POINT_WATER_CUT_STOCKTANK="NodalPointWaterCutStockTank"
    OUTLET_EROSIONAL_VELOCITY="OutletErosionalVelocity"
    OUTLET_EROSIONAL_VELOCITY_RATIO="OutletErosionalVelocityRatio"
    OUTLET_FRACTION_CO="OutletFractionCO"
    OUTLET_FRACTION_CO2="OutletFractionCO2"
    OUTLET_FRACTION_H2S="OutletFractionH2S"
    OUTLET_FRACTION_H2S="OutletFractionH2S"
    OUTLET_FRACTION_N2="OutletFractionN2"
    OUTLET_GLR_STOCKTANK="OutletGLRStockTank"
    OUTLET_GOR_STOCKTANK="OutletGORStockTank"
    OUTLET_LGR_STOCKTANK="OutletLGRStockTank"
    OUTLET_MASS_FLOWRATE_FLUID="OutletMassFlowrateFluid"
    OUTLET_MASS_FLOWRATE_GAS_STOCKTANK="OutletMassFlowrateGasStockTank"
    OUTLET_MASS_FLOWRATE_OIL_STOCKTANK="OutletMassFlowrateOilStockTank"
    OUTLET_MASS_FLOWRATE_WATER_STOCKTANK="OutletMassFlowrateWaterStockTank"
    OUTLET_MASS_FRACTION_GAS="OutletMassFractionGas"
    OUTLET_SPECIFIC_GRAVITY_GAS="OutletSpecificGravityGas"
    OUTLET_VELOCITY_FLUID="OutletVelocityFluid"
    OUTLET_VELOCITY_GAS="OutletVelocityGas"
    OUTLET_VELOCITY_LIQUID="OutletVelocityLiquid"
    OUTLET_VOLUME_FLOWRATE_FLUID_INSITU="OutletVolumeFlowrateFluidInSitu"
    OUTLET_VOLUME_FLOWRATE_FLUID_STOCKTANK="OutletVolumeFlowrateFluidStockTank"
    OUTLET_VOLUME_FLOWRATE_GAS_INSITU="OutletVolumeFlowrateGas"
    OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK="OutletVolumeFlowrateGasStockTank"
    OUTLET_VOLUME_FLOWRATE_LIQUID_INSITU="OutletVolumeFlowrateLiquid"
    OUTLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK="OutletVolumeFlowrateLiquidStockTank"
    OUTLET_VOLUME_FLOWRATE_OIL_STOCKTANK="OutletVolumeFlowrateOilStockTank"
    OUTLET_VOLUME_FLOWRATE_WATER_STOCKTANK="OutletVolumeFlowrateWaterStockTank"
    OUTLET_VOLUME_FRACTION_LIQUID="OutletVolumeFractionLiquid"
    OUTLET_WATER_CUT_STOCKTANK="OutletWaterCutStockTank"
    PCP_DISCHARGE_PRESSURE="PCPDischargePressure"
    PCP_EFFICIENCY="PCPEfficiency"
    PCP_INTAKE_PRESSURE="PCPIntakePressure"
    PCP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID="PCPIntakeVolumetricFlowrateFluid"
    PCP_POWER="PCPPower"
    PCP_SPEED="PCPSpeed"
    PCP_TORQUE="PCPTorque"
    PIPE_OUTSIDE_DIAMETER="PipeOutsideDiameter"
    PRESSURE_AT_NODAL_ANALYSIS_POINT="PressureAtNodalAnalysisPoint"
    PRESSURE_DROP_TOTAL_ACCELERATION="PressureDropTotalAcceleration"
    PRESSURE_DROP_TOTAL_COMPLETION="PressureDropTotalCompletion"
    RECORD_COUNT="RecordCount"
    RESISTANCE_ELEVATIONAL="ResistanceElevational"
    RESISTANCE_FRICTIONAL="ResistanceFrictional"
    REYNOLDS_NUMBER_MEAN="ReynoldsNumberMean"
    ROD_PUMP_DELTA_PRESSURE="RodPumpDeltaPressure"
    ROD_PUMP_DISCHARGE_PRESSURE="RodPumpDischargePressure"
    ROD_PUMP_EFFICIENCY="RodPumpEfficiency"
    ROD_PUMP_INTAKE_VOLUME_FLOWRATE_FREE_GAS="RodPumpIntakeVolumeFlowrateFreeGas"
    ROD_PUMP_INTAKE_VOLUME_FRACTION_GAS="RodPumpIntakeVolumeFractionGas"
    ROD_PUMP_INTAKE_VOLUME_FLOWRATE_LIQUID="RodPumpIntakeVolumeFlowrateLiquid"
    ROD_PUMP_INTAKE_PRESSURE="RodPumpIntakePressure"
    ROD_PUMP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID="RodPumpIntakeVolumetricFlowrateFluid"
    ROD_PUMP_POWER="RodPumpPower"
    SEVERE_SLUGGING_INDICATOR="SevereSluggingIndicator"
    SLUG_FREQUENCY1IN1000="SlugFrequency1In1000"
    SLUG_FREQUENCY_MEAN="SlugFrequencyMean"
    SLUG_LENGTH1IN1000="SlugLength1In1000"
    SLUG_LENGTH_MEAN="SlugLengthMean"
    SLUG_VOLUME1IN1000="SlugVolume1In1000"
    SLUG_VOLUME_MEAN="SlugVolumeMean"
    SPECIFIC_GRAVITY_PRODUCED_GAS="SpecificGravityProducedGas"
    SPHERE_GENERATED_LIQUID_VOLUME="SphereGeneratedLiquidVolume"
    SPHERE_GENERATED_LIQUID_VOLUME_DUMPING_TIME="SphereGeneratedLiquidVolumeDumpingTime"
    SPHERE_TRANSIT_TIME="SphereTransitTime"
    STOCK_TANK_GAS_AT_NODAL_ANALYSIS_POINT="StockTankGasAtNodalAnalysisPoint"
    STOCK_TANK_LIQUID_AT_NODAL_ANALYSIS_POINT="StockTankLiquidAtNodalAnalysisPoint"
    SURFACE_INJECTION_CHOKE_DIAMETER="SurfaceInjectionChokeDiameter"
    SYSTEM_INLET_PRESSURE="SystemInletPressure"
    SYSTEM_OUTLET_PRESSURE="SystemOutletPressure"
    SYSTEM_OUTLET_TEMPERATURE="SystemOutletTemperature"
    SYSTEM_PRESSURE_LOSS="SystemPressureLoss"
    SYSTEM_TEMPERATURE_DIFFERENCE="SystemTemperatureDifference"
    TIME_HOURS="Time_Hours"
    TOE_PRESSURE="ToePressure"
    TOE_RESERVOIR_DRAWDOWN="ToeReservoirDrawdown"
    TOE_TEMPERATURE="ToeTemperature"
    TOE_VELOCITY_FLUID="ToeVelocityFluid"
    TOTAL_INJECTION_GAS="TotalInjectionGas"
    TOTAL_LIQUID_HOLDUP="TotalLiquidHoldup"
    TOTAL_OIL_HOLDUP="TotalOilHoldup"
    TOTAL_PRESSURE_DROP_ELEVATIONAL="TotalPressureDropElevational"
    TOTAL_PRESSURE_DROP_FRICTIONAL="TotalPressureDropFrictional"
    TOTAL_WATER_HOLDUP="TotalWaterHoldup"
    WELLHEAD_GOR_STOCKTANK="WellheadGORStockTank"
    WELLHEAD_MASS_FLOWRATE_FLUID="WellheadMassFlowrateFluid"
    WELLHEAD_PRESSURE="WellheadPressure"
    WELLHEAD_TEMPERATURE="WellheadTemperature"
    WELLHEAD_TRUE_VERTICAL_DEPTH="WellheadTrueVerticalDepth"
    WELLHEAD_VOLUME_FLOWRATE_FLUID_INSITU="WellheadVolumeFlowrateFluidInSitu"
    WELLHEAD_VOLUME_FLOWRATE_GAS_STOCKTANK="WellheadVolumeFlowrateGasStockTank"
    WELLHEAD_VOLUME_FLOWRATE_LIQUID_INSITU="WellheadVolumeFlowrateLiquidInSitu"
    WELLHEAD_VOLUME_FLOWRATE_LIQUID_STOCKTANK="WellheadVolumeFlowrateLiquidStockTank"
    WELLHEAD_VOLUME_FLOWRATE_OIL_STOCKTANK="WellheadVolumeFlowrateOilStockTank"
    WELLHEAD_VOLUME_FLOWRATE_FLUID_STOCKTANK="WellheadVolumeFlowrateFluidStockTank"
    WELLHEAD_WATER_CUT_STOCKTANK="WellheadWaterCutStockTank"
    ABSOLUTE_SPEED="AbsoluteSpeed"
    API_GRAVITY_OIL="ApiGravityOil"
    ARTIFICIAL_LIFT_FLOWRATE_CONVERSION_FACTOR="ArtificialLiftFlowrateConversionFactor"
    ARTIFICIAL_LIFT_FLOWRATE_TYPE="ArtificialLiftFlowrateType"
    BEAN_SIZE="BeanSize"
    BRANCH_DELTA_PRESSURE="BranchDeltaPressure"
    CHOKE_DELTA_PRESSURE="ChokeDeltaPressure"
    COILED_TUBING_INJECTION_PRESSURE="CoiledTubingInjectionPressure"
    COMPLETION_VOLUME_FLOWRATE_LIQUID_STOCKTANK="CompletionVolumeFlowrateLiquidStockTank"
    COMPRESSOR_EFFICIENCY="CompressorEfficiency"
    COMPRESSOR_POWER="CompressorPower"
    CONTAMINANTS_CO2="ContaminantsCO2"
    CONTAMINANTS_H2S="ContaminantsH2S"
    CONTAMINANTS_N2="ContaminantsN2"
    CRITICAL_PRESSURE_RATIO="CriticalPressureRatio"
    DELTA_ENTHALPY="DeltaEnthalpy"
    DELTA_ENTROPY="DeltaEntropy"
    DELTA_PRESSURE="DeltaPressure"
    DELTA_TEMPERATURE="DeltaTemperature"
    DENSITY_FLUID_MEAN="DensityFluidMean"
    DENSITY_GAS_STOCKTANK="DensityGasStockTank"
    DENSITY_OIL_STOCKTANK="DensityOilStockTank"
    DENSITY_WATER_STOCKTANK="DensityWaterStockTank"
    DIAMETER_RATIO="DiameterRatio"
    DISCHARGE_COEFFICIENT="DischargeCoefficient"
    DISCHARGE_PRESSURE="DischargePressure"
    DOWNSTREAM_COOLER_DUTY="DownstreamCoolerDuty"
    DOWNSTREAM_DENSITY="DownstreamDensity"
    DOWNSTREAM_HEAT_CAPACITY_RATIO="DownstreamHeatCapacityRatio"
    DOWNSTREAM_MACH_NUMBER="DownstreamMachNumber"
    DOWNSTREAM_PRESSURE="DownstreamPressure"
    DOWNSTREAM_SONIC_VELOCITY="DownstreamSonicVelocity"
    DOWNSTREAM_VELOCITY="DownstreamVelocity"
    DOWNSTREAM_VELOCITY_RATIO_CRITICAL="DownstreamVelocityRatioCritical"
    DUTY="Duty"
    EFFICIENCY="Efficiency"
    ELEVATION_DELTA_PRESSURE="ElevationDeltaPressure"
    ELEVATION_DIFFERENCE="ElevationDifference"
    ENTHALPY="Enthalpy"
    EQUIPMENT_TYPE="EquipmentType"
    EROSIONAL_VELOCITY="ErosionalVelocity"
    EROSIONAL_VELOCITY_MAXIMUM="ErosionalVelocityMaximum"
    EROSIONAL_VELOCITY_RATIO="ErosionalVelocityRatio"
    EROSIONAL_VELOCITY_RATIO_MAXIMUM="ErosionalVelocityRatioMaximum"
    EXPANSION_FACTOR_GAS="ExpansionFactorGas"
    EXPANSION_FACTOR_GAS_CRITICAL="ExpansionFactorGasCritical"
    FLOW_COEFFICIENT_FLUID="FlowCoefficientFluid"
    FLOW_COEFFICIENT_GAS="FlowCoefficientGas"
    FLOW_COEFFICIENT_LIQUID="FlowCoefficientLiquid"
    FLOW_FACTOR="FlowFactor"
    FLOWING_GAS_VOLUME_FLOWRATE="FlowingGasVolumeFlowrate"
    FLOWRATE="Flowrate"
    FLOWRATE_BEYOND_CURVE_MAX_RATE="FlowrateBeyondCurveMaxRate"
    FLOWRATE_DERIVATIVE_OF_OUTLET_PRESSURE="FlowrateDerivativeOfOutletPressure"
    FLOWRATE_RATIO_CRITICAL="FlowrateRatioCritical"
    FLOWRATE_TYPE="FlowrateType"
    FLUID_HANDLE_STRING="FluidHandleString"
    FRICTION_DELTA_PRESSURE="FrictionDeltaPressure"
    GENERIC_EQUIPMENT_DELTA_PRESSURE="GenericEquipmentPressureDrop"
    GLR_INSITU="GLRInSitu"
    GLR_STOCKTANK="GLRStockTank"
    LGR_STOCKTANK="LGRStockTank"
    GOR_STOCKTANK="GORStockTank"
    GWR_STOCKTANK="GWRStockTank"
    HEAD="Head"
    COMPRESSOR_HEAD="CompressorHead"
    HEAT_CAPACITY_RATIO_UPSTREAM="HeatCapacityRatioUpstream"
    HEEL_DRAWDOWN="HeelDrawdown"
    INJECTION_FLUID_ENTHALPY="InjectionFluidEnthalpy"
    INJECTION_FLUID_GAS_FLOWRATE_STOCKTANK="InjectionFluidGasFlowrateStockTank"
    INJECTION_FLUID_LIQUID_FLOWRATE_STOCKTANK="InjectionFluidLiquidFlowrateStockTank"
    INJECTION_FLUID_MASS_FLOWRATE_STOCKTANK="InjectionFluidMassFlowrateStockTank"
    INJECTION_FLUID_SPECIFIC_GRAVITY_GAS="InjectionFluidSpecificGravityGas"
    INJECTION_FLUID_TEMPERATURE="InjectionFluidTemperature"
    INJECTION_GAS_PRESSURE_AT_CASING_HEAD="InjectionGasPressureAtCasingHead"
    INJECTION_GAS_PRESSURE_AT_INJECTION_POINT="InjectionGasPressureAtInjectionPoint"
    INJECTION_GAS_TEMPERATURE_AT_CASING_HEAD="InjectionGasTemperatureAtCasingHead"
    INJECTION_GAS_TEMPERATURE_AT_INJECTION_POINT="InjectionGasTemperatureAtInjectionPoint"
    INJECTION_PORT_DELTA_PRESSURE="InjectionPortDeltaPressure"
    INJECTION_PORT_DELTA_TEMPERATURE="InjectionPortDeltaTemperature"
    INJECTION_PORT_DEPTH="InjectionPortDepth"
    INLET_PRESSURE="InletPressure"
    INLET_PRESSURE_DERIVATIVE_OF_FLOWRATE="InletPressureDerivativeOfFlowrate"
    INLET_PRESSURE_DERIVATIVE_OF_OUTLET_PRESSURE="InletPressureDerivativeOfOutletPressure"
    INLET_TEMPERATURE="InletTemperature"
    INPUT_FLOWRATE_GAS="InputFlowrateGas"
    INPUT_FLOWRATE_LIQUID="InputFlowrateLiquid"
    INPUT_FLOWRATE_OIL="InputFlowrateOil"
    INPUT_MASS_FLOWRATE_FLUID="InputMassFlowrateFluid"
    INPUT_TEMPERATURE="InputTemperature"
    IS_CRITICAL_FLOW="IsCriticalFlow"
    IS_INJECTING_INTO_COMPLETION="IsInjectingIntoCompletion"
    IS_SUPER_CRITICAL="IsSuperCritical"
    LIMITED_BY="LimitedBy"
    LIMIT_RATIO="LimitRatio"
    LIQUID_FLOWRATE_CRITICAL="LiquidFlowrateCritical"
    LIQUID_RATE="LiquidRate"
    MASS_FLOWRATE_CRITICAL="MassFlowrateCritical"
    MASS_FLOWRATE_FLUID="MassFlowrateFluid"
    MASS_FLOWRATE_GAS_STOCKTANK="MassFlowrateGasStockTank"
    MASS_FLOWRATE_O_IL_STOCKTANK="MassFlowrateOIlStockTank"
    MASS_FLOWRATE_STOCKTANK="MassFlowrateStockTank"
    MASS_FLOWRATE_WATER_STOCKTANK="MassFlowrateWaterStockTank"
    MASS_RATE="MassRate"
    MASS_RATE_REMOVED="MassRateRemoved"
    MAX_RATIO_CRITICAL="MaxRatioCritical"
    OGR_STOCKTANK="OGRStockTank"
    OUTLET_PRESSURE_DERIVATIVE_OF_FLOWRATE="OutletPressureDerivativeOfFlowrate"
    OUTLET_PRESSURE="OutputPressure"
    OUTPUT_FLOWRATE_GAS="OutputFlowrateGas"
    OUTPUT_FLOWRATE_LIQUID="OutputFlowrateLiquid"
    OUTPUT_FLOWRATE_OIL="OutputFlowrateOil"
    INPUT_FLOWRATE_WATER="InputFlowrateWater"
    OUTPUT_FLOWRATE_WATER="OutputFlowrateWater"
    OUTPUT_MASS_FLOWRATE_FLUID="OutputMassFlowrateFluid"
    PCP_TORQUE="PcpTorque"
    POWER="Power"
    SURFACEPOWER="SurfacePower"
    PRESSURE="Pressure"
    PRESSURE_DIFFERENCE="PressureDifference"
    PRESSURE_DIFFERENCE_CRITICAL="PressureDifferenceCritical"
    PRESSURE_MAXIMUM="PressureMaximum"
    PRESSURE_RATIO="PressureRatio"
    PRESSURE_RATIO_CRITICAL="PressureRatioCritical"
    PRESSURE_REDUCTION_PER_STAGE="PressureReductionPerStage"
    PUMP_EFFICIENCY="PumpEfficiency"
    PUMP_POWER="PumpPower"
    RESERVOIR_TEMPERATURE_AVERAGE="ReservoirTemperatureAverage"
    ROUTE="Route"
    SPECIFIC_GRAVITY_GAS_STOCKTANK="SpecificGravityGasStockTank"
    SPECIFIC_GRAVITY_OIL_INSITU="SpecificGravityOilInSitu"
    SPECIFIC_GRAVITY_WATER_INSITU="SpecificGravityWaterInSitu"
    SPEED="Speed"
    SPEED_FRACTION = "SpeedFraction"
    STAGES="Stages"
    STATIC_DELTA_PRESSURE="StaticDeltaPressure"
    STATIC_RESERVOIR_PRESSURE="StaticReservoirPressure"
    STONEWALL_LIMIT_EXCEEDED="StonewallLimitExceeded"
    SUCTION_INLET_GAS_VOLUME_PERCENT="SuctionInletGasVolumePercent"
    SUCTION_PRESSURE="SuctionPressure"
    SUCTION_PRESSURE_DOWNSTREAM_OF_INLET_CHOKE="SuctionPressureDownstreamOfInletChoke"
    SURFACE_CHOKE_DIAMETER="SurfaceChokeDiameter"
    SURFACE_INJECTION_PRESSURE="SurfaceInjectionPressure"
    TEMPERATURE="Temperature"
    TEMPERATURE_FLOWING="TemperatureFlowing"
    TEMPERATURE_MIXED_FLUID="TemperatureMixedFluid"
    TEMPERATURE_PRODUCTION_FLUID="TemperatureProductionFluid"
    TOE_DRAWDOWN="ToeDrawdown"
    TOTAL_VOLUME_RATE_BOOSTER="TotalVolumeRateBooster"
    TOTAL_VOLUME_RATE_OOS_BOOSTER="TotalVolumeRateOOSBooster"
    TUBING_PRESSURE="TubingPressure"
    TYPE="Type"
    UPSTREAM_COOLER_DUTY="UpstreamCoolerDuty"
    UPSTREAM_DENSITY="UpstreamDensity"
    UPSTREAM_MACH_NUMBER="UpstreamMachNumber"
    UPSTREAM_PIPE_ID="UpstreamPipeID"
    UPSTREAM_PRESSURE="UpstreamPressure"
    UPSTREAM_SONIC_VELOCITY="UpstreamSonicVelocity"
    UPSTREAM_VELOCITY="UpstreamVelocity"
    UPSTREAM_VELOCITY_RATIO_CRITICAL="UpstreamVelocityRatioCritical"
    VELOCITY_GAS="VelocityGas"
    VELOCITY_GAS_MAXIMUM="VelocityGasMaximum"
    VELOCITY_LIQUID="VelocityLiquid"
    VELOCITY_LIQUID_MAXIMUM="VelocityLiquidMaximum"
    VELOCITY_MEAN="VelocityMean"
    VELOCITY_MEAN_MAXIMUM="VelocityMeanMaximum"
    VISCOSITY_CORRELATION_FACTOR_FOR_EFFICIENCY="ViscosityCorrelationFactorForEfficiency"
    VISCOSITY_CORRELATION_FACTOR_FOR_FLOWRATE="ViscosityCorrelationFactorForFlowrate"
    VISCOSITY_CORRELATION_FACTOR_FOR_HEAD="ViscosityCorrelationFactorForHead"
    VISCOSITY_CORRELATION_FACTOR_FOR_POWER="ViscosityCorrelationFactorForPower"
    VOLUME_FLOWRATE_FLUID="VolumeFlowrateFluid"
    VOLUME_FLOWRATE_GAS_INSITU="VolumeFlowrateGasInSitu"
    VOLUME_FLOWRATE_GAS_STOCKTANK="VolumeFlowrateGasStockTank"
    VOLUME_FLOWRATE_GAS_STANDARD="VolumeFlowrateGasStandard"
    VOLUME_FLOWRATE_LIQUID_INSITU="VolumeFlowrateLiquidInSitu"
    VOLUME_FLOWRATE_LIQUID_STOCKTANK="VolumeFlowrateLiquidStockTank"
    VOLUME_FLOWRATE_OIL_INSITU="VolumeFlowrateOilInSitu"
    VOLUME_FLOWRATE_OIL_STOCKTANK="VolumeFlowrateOilStockTank"
    VOLUME_FLOWRATE_WATER_INSITU="VolumeFlowrateWaterInSitu"
    VOLUME_FLOWRATE_WATER_STOCKTANK="VolumeFlowrateWaterStockTank"
    VOLUME_FRACTION_GAS="VolumeFractionGas"
    WATER_CUT_INSITU="WaterCutInSitu"
    WATER_CUT_STOCKTANK="WaterCutStockTank"
    WATER_OIL_RATIO="WaterOilRatio"
    WGR_STOCKTANK="WGRStockTank"
    WORKING_SPEED="WorkingSpeed"
    WELL_CURVE_PERFORMANCE_PWI="WellCurvePerformancePwiId"
    VFP_TABLES="VFP_TABLES"
    VFP_TABLES_WITH_TEMPERATURE="VFP_TABLES_WITH_TEMPERATURE"


class ProfileVariables:
    """ Available Results Profile Variables """
    AMBIENT_FLUID_COEFFICIENT_OF_EXPANSION="AmbientFluidCoefficientOfExpansion"
    AMBIENT_FLUID_CONDUCTIVITY="AmbientFluidConductivity"
    AMBIENT_FLUID_DENSITY="AmbientFluidDensity"
    AMBIENT_FLUID_HEAT_CAPACITY="AmbientFluidHeatCapacity"
    AMBIENT_FLUID_VELOCITY="AmbientFluidVelocity"
    AMBIENT_FLUID_VISCOSITY="AmbientFluidViscosity"
    AMBIENT_TEMPERATURE_AT_NODE="AmbientTemperatureAtNode"
    ANNULUS_INSIDE_DIAMETER="AnnulusInsideDiameter"
    ANNULUS_OUTSIDE_DIAMETER="AnnulusOutsideDiameter"
    ASPHALTENE_FORMATION_TEMPERATURE="AsphalteneFormationTemperature"
    BP_BUBBLE_LENGTH1IN1000="BPBubbleLength1In1000"
    BP_BUBBLE_LENGTH_MEAN="BPBubbleLengthMean"
    BP_SLUG_FREQUENCY="BPSlugFrequency"
    BP_SLUG_FREQUENCY1IN1000="BPSlugFrequency1In1000"
    BP_SLUG_LENGTH1IN1000="BPSlugLength1In1000"
    BP_SLUG_LENGTH_MEAN="BPSlugLengthMean"
    BP_SLUG_LIQUID_HOLDUP="BPSlugLiquidHoldup"
    BUBBLE_POINT_PRESSURE_INSITU="BubblePointPressureInSitu"
    BURIAL_DEPTH_CIRCUMFERENCE="BurialDepthCircumference"
    BURIAL_DEPTH_FACTOR_EXTRA="BurialDepthFactorExtra"
    BURIAL_DEPTH_OF_PIPE_CENTERLINE="BurialDepthOfPipeCenterline"
    BURIAL_DEPTH_OF_PIPE_TOPMOST_COAT="BurialDepthOfPipeTopmostCoat"
    CASING_GAS_PRESSURE="CasingGasPressure"
    CASING_GAS_TEMPERATURE="CasingGasTemperature"
    COEF_OF_EXPANSION_GAS="CoefOfExpansionGas"
    COEF_OF_EXPANSION_LIQUID="CoefOfExpansionLiquid"
    COMPRESSIBILITY_OIL_INSITU="CompressibilityOilInSitu"
    CONDUCTIVITY_FLUID_INSITU="ConductivityFluidInSitu"
    CONDUCTIVITY_GAS_INSITU="ConductivityGasInSitu"
    CONDUCTIVITY_LIQUID_INSITU="ConductivityLiquidInSitu"
    CONDUCTIVITY_OIL_INSITU="ConductivityOilInSitu"
    CONDUCTIVITY_WATER_INSITU="ConductivityWaterInSitu"
    CORROSION_RATE="CorrosionRate"
    CORROSION_PIT_RATE="CorrosionPitRate"
    CORROSION_CUMULATIVE_LOSS="CorrosionCumulativeLoss"
    CORROSION_RISK='CorrosionRisk'
    CROSS_SECTIONAL_AREA_FOR_FLOW="CrossSectionalAreaForFlow"
    CUMULATIVE_ACCELERATION_PRESSURE_DIFFERENCE="CumulativeAccelerationPressureDifference"
    CUMULATIVE_ELEVATION_PRESSURE_DIFFERENCE="CumulativeElevationPressureDifference"
    CUMULATIVE_FRICTION_PRESSURE_DIFFERENCE="CumulativeFrictionPressureDifference"
    CUMULATIVE_GAS_HOLDUP="CumulativeGasHoldup"
    CUMULATIVE_LIQUID_HOLDUP="CumulativeLiquidHoldup"
    CUMULATIVE_OIL_HOLDUP="CumulativeOilHoldup"
    CUMULATIVE_PIPELINE_VOLUME="CumulativePipelineVolume"
    CUMULATIVE_WATER_HOLDUP="CumulativeWaterHoldup"
    DENSITY_FLUID_INSITU="DensityFluidInSitu"
    DENSITY_FLUID_NO_SLIP_INSITU="DensityFluidNoSlipInSitu"
    DENSITY_GAS_INSITU="DensityGasInSitu"
    DENSITY_GAS_STOCKTANK="DensityGasStockTank"
    DENSITY_LIQUID_INSITU="DensityLiquidInSitu"
    DENSITY_LIQUID_STOCKTANK="DensityLiquidStockTank"
    DENSITY_OIL_INSITU="DensityOilInSitu"
    DENSITY_OIL_STOCKTANK="DensityOilStockTank"
    DENSITY_WATER_INSITU="DensityWaterInSitu"
    DENSITY_WATER_STOCKTANK="DensityWaterStockTank"
    DISTRIBUTED_PI_GAS_INSITU="DistributedPIGasInSitu"
    DISTRIBUTED_PI_LIQUID_INSITU="DistributedPILiquidInSitu"
    EFFECTIVE_PERMEABILITY="EffectivePermeability"
    ELEVATION="Elevation"
    ENTHALPY_FLUID="EnthalpyFluid"
    ENTROPY_FLUID_INSITU="EntropyFluidInSitu"
    EQUIVALENT_HYDRAULIC_DIAMETER="EquivalentHydraulicDiameter"
    EROSION_RISK='ErosionRisk'
    EROSIONAL_VELOCITY="ErosionalVelocity"
    EROSIONAL_VELOCITY_RATIO="ErosionalVelocityRatio"
    EROSION_RATE="ErosionRate"
    FLOW_PATTERN_GAS_LIQUID="FlowPatternGasLiquid"
    FLOW_PATTERN_OIL_WATER="FlowPatternOilWater"
    FLOWRATE_GAS_INSITU="FlowrateGasInSitu"
    FLOWRATE_LIQUID_INSITU="FlowrateLiquidInsitu"
    FORMATION_VOLUME_FACTOR_OIL_INSITU="FormationVolumeFactorOilInSitu"
    FRICTION_FACTOR_RATIO_TWO_PHASE="FrictionFactorRatioTwoPhase"
    FRICTION_FACTOR_SINGLE_PHASE="FrictionFactorSinglePhase"
    FROUDE_NUMBER_GAS="FroudeNumberGas"
    FROUDE_NUMBER_LIQUID="FroudeNumberLiquid"
    GLR_STOCKTANK="GLRStockTank"
    GOR_STOCKTANK="GORStockTank"
    GROUND_CONDUCTIVITY="GroundConductivity"
    GROUND_HEAT_TRANSFER_COEFFICIENT="GroundHeatTransferCoefficient"
    GROUND_HEAT_TRANSFER_COEFFICIENT_NO_ADJUSTMENT_BY_AREA_RATIO="GroundHeatTransferCoefficientNoAdjustmentByAreaRatio"
    GWR_STOCKTANK="GWRStockTank"
    HEAT_CAPACITY_FLUID_INSITU="HeatCapacityFluidInSitu"
    HEAT_CAPACITY_GAS_INSITU="HeatCapacityGasInSitu"
    HEAT_CAPACITY_LIQUID_INSITU="HeatCapacityLiquidInSitu"
    HEAT_CAPACITY_OIL_INSITU="HeatCapacityOilInSitu"
    HEAT_CAPACITY_WATER_INSITU="HeatCapacityWaterInSitu"
    HOLDUP_FRACTION_LIQUID="HoldupFractionLiquid"
    HOLDUP_LIQUID_WATER="HoldupLiquidWater"
    HORIZONTAL_DISTANCE="HorizontalDistance"
    HORIZONTAL_POSITION="HorizontalPosition"
    HYDRATE_FORMATION_TEMPERATURE="HydrateFormationTemperature"
    HYDRATE_SUB_COOLING_DELTA_TEMPERATURE="HydrateSubCoolingDeltaTemperature"
    HYDROSTATIC_HEAD="HydrostaticHead"
    INLINE_HEATER_MINIMUM_TEMPERATURE="InlineHeaterMinimumTemperature"
    INLINE_HEATER_POWER_AVAILABLE="InlineHeaterPowerAvailable"
    INLINE_HEATER_POWER_USED="InlineHeaterPowerUsed"
    INPUT_HEAT_TRANSFER_COEFFICIENT="InputHeatTransferCoefficient"
    INSIDE_FILM_FORCED_CONV_NUSSELT_NUMBER="InsideFilmForcedConvNusseltNumber"
    INSIDE_FILM_GAS_GRASHOF_NUMBER="InsideFilmGasGrashofNumber"
    INSIDE_FILM_GAS_HEAT_TRANSFER_COEFFICIENT="InsideFilmGasHeatTransferCoefficient"
    INSIDE_FILM_GAS_NUSSELT_NUMBER="InsideFilmGasNusseltNumber"
    INSIDE_FILM_GAS_PRANDTL_NUMBER="InsideFilmGasPrandtlNumber"
    INSIDE_FILM_GAS_REYNOLDS_NUMBER="InsideFilmGasReynoldsNumber"
    INSIDE_FILM_GRASHOF_NUMBER="InsideFilmGrashofNumber"
    INSIDE_FILM_GRASHOF_NUMBER_LIQUID="InsideFilmGrashofNumberLiquid"
    INSIDE_FILM_LIQUID_HEAT_TRANSFER_COEFFICIENT="InsideFilmLiquidHeatTransferCoefficient"
    INSIDE_FILM_LIQUID_NUSSELT_NUMBER="InsideFilmLiquidNusseltNumber"
    INSIDE_FILM_LIQUID_PRANDTL_NUMBER="InsideFilmLiquidPrandtlNumber"
    INSIDE_FILM_LIQUID_REYNOLDS_NUMBER="InsideFilmLiquidReynoldsNumber"
    INSIDE_FILM_MEAN_HEAT_TRANSFER_COEFFICIENT="InsideFilmMeanHeatTransferCoefficient"
    INSIDE_FILM_NATURAL_CONV_NUSSELT_NUMBER="InsideFilmNaturalConvNusseltNumber"
    INSIDE_FILM_NUSSELT_NUMBER="InsideFilmNusseltNumber"
    INSIDE_FILM_PRANDTL_NUMBER="InsideFilmPrandtlNumber"
    INSIDE_FILM_REYNOLDS_NUMBER="InsideFilmReynoldsNumber"
    INSIDE_FLUID_FILM_HEAT_TRANSFER_COEFFICIENT="InsideFluidFilmHeatTransferCoefficient"
    JOULE_THOMPSON_COEFFICIENT_INSITU="JouleThompsonCoefficientInSitu"
    LAYER_STATIC_PRESSURE="LayerStaticPressure"
    LGR_STOCKTANK="LGRStockTank"
    LIQUID_LOADING_GAS_RATE="LiquidLoadingGasRate"
    LIQUID_LOADING_VELOCITY="LiquidLoadingVelocity"
    LIQUID_LOADING_VELOCITY_RATIO="LiquidLoadingVelocityRatio"
    LIVE_OIL_SATURATED_VISCOSITY_INSITU="LiveOilSaturatedViscosityInSitu"
    MACH_NUMBER_IN_FLUID="MachNumberInFluid"
    MASS_FLOWRATE="MassFlowrate"
    MASS_FLOWRATE_GAS_INSITU="MassFlowrateGasInSitu"
    MASS_FLOWRATE_GAS_STOCKTANK="MassFlowrateGasStockTank"
    MASS_FLOWRATE_LIQUID_INSITU="MassFlowrateLiquidInSitu"
    MASS_FLOWRATE_LIQUID_STOCKTANK="MassFlowrateLiquidStockTank"
    MASS_FLOWRATE_OIL_INSITU="MassFlowrateOilInSitu"
    MASS_FLOWRATE_OIL_STOCKTANK="MassFlowrateOilStockTank"
    MASS_FLOWRATE_WATER_INSITU="MassFlowrateWaterInSitu"
    MASS_FLOWRATE_WATER_STOCKTANK="MassFlowrateWaterStockTank"
    MASS_FRACTION_GAS_INSITU="MassFractionGasInSitu"
    MASS_FRACTION_LIQUID_INSITU="MassFractionLiquidInSitu"
    MEAN_COEF_OF_EXPANSION_FLUID="MeanCoefOfExpansionFluid"
    MEAN_VELOCITY_FLUID="MeanVelocityFluid"
    MEASURED_DEPTH="MeasuredDepth"
    MOLAR_DENSITY_STOCKTANK="MolarDensityStockTank"
    MOLAR_VOLUME_STOCKTANK="MolarVolumeStockTank"
    MOLECULAR_WEIGHT_FLUID="MolecularWeightFluid"
    MOLE_FRACTION_CO="MoleFractionCO"
    MOLE_FRACTION_CO2="MoleFractionCO2"
    MOLE_FRACTION_H2="MoleFractionH2"
    MOLE_FRACTION_H2S="MoleFractionH2S"
    MOLE_FRACTION_N2="MoleFractionN2"
    MUDLINE_TEMPERATURE="MudlineTemperature"
    NODE_NUMBER="NodeNumber"
    OGR_STOCKTANK="OGRStockTank"
    OIL_FORMATION_VOLUME_FACTOR="OilFormationVolumeFactor"
    OUTSIDE_FILM_FORCED_CONVECTION_HEAT_TRANSFER_COEFFICIENT="OutsideFilmForcedConvectionHeatTransferCoefficient"
    OUTSIDE_FILM_FORCED_CONVECTION_NUSSELT_NUMBER="OutsideFilmForcedConvectionNusseltNumber"
    OUTSIDE_FILM_FREE_CONVECTION_HEAT_TRANSFER_COEFFICIENT="OutsideFilmFreeConvectionHeatTransferCoefficient"
    OUTSIDE_FILM_FREE_CONVECTION_NUSSELT_NUMBER="OutsideFilmFreeConvectionNusseltNumber"
    OUTSIDE_FILM_GRASHOF_NUMBER="OutsideFilmGrashofNumber"
    OUTSIDE_FILM_HEAT_TRANSFER_COEFFICIENT_FOR_BURIED_PORTION="OutsideFilmHeatTransferCoefficientForBuriedPortion"
    OUTSIDE_FILM_HEAT_TRANSFER_COEFFICIENT_FOR_EXPOSED_PORTION="OutsideFilmHeatTransferCoefficientForExposedPortion"
    OUTSIDE_FILM_PRANDTL_NUMBER="OutsideFilmPrandtlNumber"
    OUTSIDE_FILM_RALEIGH_NUMBER="OutsideFilmRaleighNumber"
    OUTSIDE_FILM_REYNOLDS_NUMBER="OutsideFilmReynoldsNumber"
    OUTSIDE_FLUID_FILM_HEAT_TRANSFER_COEFFICIENT="OutsideFluidFilmHeatTransferCoefficient"
    OVERALL_AMBIENT_HEAT_TRANSFER_COEFFICIENT="OverallAmbientHeatTransferCoefficient"
    OVERALL_HEAT_TRANSFER_COEFFICIENT="OverallHeatTransferCoefficient"
    OVERALL_HEAT_TRANSFER_COEFFICIENT_OF_BURIED_PORTION="OverallHeatTransferCoefficientOfBuriedPortion"
    OVERALL_HEAT_TRANSFER_COEFFICIENT_OF_EXPOSED_PORTION="OverallHeatTransferCoefficientOfExposedPortion"
    PHASE_INVERSION_WATERCUT_LIQUID_INSITU="PhaseInversionWatercutLiquidInsitu"
    PIPE_ANGLE_TO_HORIZONTAL="PipeAngleToHorizontal"
    PIPE_COATINGS_THICKNESS="PipeCoatingsThickness"
    PIPE_INSIDE_DIAMETER="PipeInsideDiameter"
    PIPE_INSIDE_TEMPERATURE="PipeInsideTemperature"
    PIPE_INSIDE_TEMPERATURE_BURIED_PART="PipeInsideTemperatureBuriedPart"
    PIPE_INSIDE_TEMPERATURE_EXPOSED_PART="PipeInsideTemperatureExposedPart"
    PIPE_OUTSIDE_DIAMETER="PipeOutsideDiameter"
    PIPE_OUTSIDE_DIAMETER_WITH_COATINGS="PipeOutsideDiameterWithCoatings"
    PIPE_OUTSIDE_TEMPERATURE="PipeOutsideTemperature"
    PIPE_OUTSIDE_TEMPERATURE_BURIED_PART="PipeOutsideTemperatureBuriedPart"
    PIPE_OUTSIDE_TEMPERATURE_EXPOSED_PART="PipeOutsideTemperatureExposedPart"
    PIPE_WALL_CONDUCTIVITY="PipeWallConductivity"
    PIPE_WALL_HEAT_TRANSFER_COEFFICIENT="PipeWallHeatTransferCoefficient"
    PIPE_WALL_ROUGHNESS="PipeWallRoughness"
    PIPE_WALL_THICKNESS="PipeWallThickness"
    PRESSURE="Pressure"
    PRESSURE_DROP_RATIO_ELEVATION="PressureDropRatioElevation"
    PRESSURE_DROP_RATIO_FRICTION="PressureDropRatioFriction"
    PRESSURE_DROP_RATIO_TOTAL="PressureDropRatioTotal"
    PRESSURE_GRADIENT_ACCELERATION="PressureGradientAcceleration"
    PRESSURE_GRADIENT_ELEVATION="PressureGradientElevation"
    PRESSURE_GRADIENT_FRICTION="PressureGradientFriction"
    PRESSURE_GRADIENT_TOTAL="PressureGradientTotal"
    RELATIVE_PERMEABILITY_OIL="RelativePermeabilityOil"
    RELATIVE_PERMEABILITY_WATER="RelativePermeabilityWater"
    RESERVOIR_DRAWDOWN="ReservoirDrawdown"
    RESERVOIR_PRESSURE="ReservoirPressure"
    RESERVOIR_SATURATION="ReservoirSaturation"
    RESERVOIR_SPECIFIC_GAS_INFLOW="ReservoirSpecificGasInflow"
    RESERVOIR_SPECIFIC_MASS_INFLOW="ReservoirSpecificMassInflow"
    RESERVOIR_TEMPERATURE="ReservoirTemperature"
    RESISTANCE_OF_BURIED_PORTION_OVERALL="ResistanceOfBuriedPortionOverall"
    RESISTANCE_OF_EXPOSED_PORTION_OVERALL="ResistanceOfExposedPortionOverall"
    RESISTANCE_OF_OUTSIDE_FILM_ON_EXPOSED_PORTION="ResistanceOfOutsideFilmOnExposedPortion"
    REYNOLDS_NUMBER="ReynoldsNumber"
    SAND_PRODUCTION_RATE="SandProductionRate"
    SEGMENT_ENTHALPY_GRADIENT="SegmentEnthalpyGradient"
    SEGMENT_INFLOW_RATE_GRADIENT="SegmentInflowRateGradient"
    SEGMENT_LENGTH="SegmentLength"
    SEGMENT_PRESSURE_GRADIENT="SegmentPressureGradient"
    SEGMENT_TEMPERATURE_GRADIENT="SegmentTemperatureGradient"
    SINGLE_PHASE_ELEVATION_PRESSURE_GRADIENT="SinglePhaseElevationPressureGradient"
    SINGLE_PHASE_FRICTIONAL_PRESSURE_GRADIENT="SinglePhaseFrictionalPressureGradient"
    SINGLE_PHASE_TOTAL_PRESSURE_GRADIENT="SinglePhaseTotalPressureGradient"
    SKIN_DUE_TO_COMPACTED_ZONE="SkinDueToCompactedZone"
    SKIN_DUE_TO_DAMAGED_WELLBORE="SkinDueToDamagedWellbore"
    SKIN_DUE_TO_GRAVEL_PACK="SkinDueToGravelPack"
    SKIN_DUE_TO_PERFORATION_GEOMETRY="SkinDueToPerforationGeometry"
    SKIN_FACTOR_OVERALL="SkinFactorOverall"
    SKIN_FACTOR_RATE_DEPENDENT="SkinFactorRateDependent"
    SKIN_TURBULENT_DUE_TO_DAMAGED_WELLBORE="SkinTurbulentDueToDamagedWellbore"
    SKIN_TURBULENT_DUE_TO_GRAVEL_PACKING="SkinTurbulentDueToGravelPacking"
    SKIN_TURBULENT_DUE_TO_PERFORATIONS="SkinTurbulentDueToPerforations"
    SLIP_RATIO_GAS_LIQUID="SlipRatioGasLiquid"
    SLIP_RATIO_OIL_WATER="SlipRatioOilWater"
    SLUG_FREQUENCY1IN10="SlugFrequency1In10"
    SLUG_FREQUENCY1IN100="SlugFrequency1In100"
    SLUG_FREQUENCY1IN1000="SlugFrequency1In1000"
    SLUG_FREQUENCY_MEAN="SlugFrequencyMean"
    SLUG_LENGTH1IN10="SlugLength1In10"
    SLUG_LENGTH1IN100="SlugLength1In100"
    SLUG_LENGTH1IN1000="SlugLength1In1000"
    SLUG_LENGTH_MEAN="SlugLengthMean"
    SLUG_VOLUME1IN10="SlugVolume1In10"
    SLUG_VOLUME1IN100="SlugVolume1In100"
    SLUG_VOLUME1IN1000="SlugVolume1In1000"
    SLUG_VOLUME_MEAN="SlugVolumeMean"
    SOLUTION_GAS_IN_OIL_INSITU="SolutionGasInOilInSitu"
    SOLUTION_GAS_IN_WATER_INSITU="SolutionGasInWaterInSitu"
    SOLUTION_GAS_POTENTIAL_IN_LIQUID_INSITU="SolutionGasPotentialInLiquidInSitu"
    SOLUTION_GAS_POTENTIAL_IN_OIL_INSITU="SolutionGasPotentialInOilInSitu"
    SOLUTION_GAS_POTENTIAL_IN_WATER_INSITU="SolutionGasPotentialInWaterInSitu"
    SOLUTION_GAS_VOLUME_FLOWRATE_INSITU="SolutionGasVolumeFlowrateInSitu"
    SONIC_VELOCITY_IN_FLUID="SonicVelocityInFluid"
    SPECIFIC_GRAVITY_GAS_INSITU="SpecificGravityGasInSitu"
    SPECIFIC_GRAVITY_GAS_STOCKTANK="SpecificGravityGasStockTank"
    SPECIFIC_GRAVITY_LIQUID_STOCKTANK="SpecificGravityLiquidStockTank"
    SPECIFIC_GRAVITY_OIL_STOCKTANK="SpecificGravityOilStockTank"
    SPECIFIC_GRAVITY_WATER_STOCKTANK="SpecificGravityWaterStockTank"
    SPECIFIC_HEAT_CAPACITY_RATIO_GAS_INSITU="SpecificHeatCapacityRatioGasInSitu"
    SPHERE_GENERATED_LIQUID_VOLUME_DUMPING_TIME_TOTAL="SphereGeneratedLiquidVolumeDumpingTimeTotal"
    SPHERE_GENERATED_LIQUID_VOLUME_FROM_SECTION="SphereGeneratedLiquidVolumeFromSection"
    SPHERE_GENERATED_LIQUID_VOLUME_SO_FAR="SphereGeneratedLiquidVolumeSoFar"
    SPHERE_TRANSIT_TIME_FROM_SECTION="SphereTransitTimeFromSection"
    SUPERFICIAL_VELOCITY_GAS="SuperficialVelocityGas"
    SUPERFICIAL_VELOCITY_LIQUID="SuperficialVelocityLiquid"
    SUPERFICIAL_VELOCITY_OIL="SuperficialVelocityOil"
    SUPERFICIAL_VELOCITY_WATER="SuperficialVelocityWater"
    SURFACE_TENSION_LIQUID_INSITU="SurfaceTensionLiquidInSitu"
    SURFACE_TENSION_OIL_GAS_INSITU="SurfaceTensionOilGasInSitu"
    SURFACE_TENSION_OIL_WATER_INSITU="SurfaceTensionOilWaterInSitu"
    SURFACE_TENSION_WATER_GAS_INSITU="SurfaceTensionWaterGasInSitu"
    TEMPERATURE="Temperature"
    TEMPERATURE_FLUID="TemperatureFluid"
    TEMPERATURE_GRADIENT_ELEVATION="TemperatureGradientElevation"
    TEMPERATURE_GRADIENT_GROUND_AND_AMBIENT="TemperatureGradientGroundAndAmbient"
    TEMPERATURE_GRADIENT_HEAT_TRANSFER="TemperatureGradientHeatTransfer"
    TEMPERATURE_GRADIENT_INSIDE_FILM="TemperatureGradientInsideFilm"
    TEMPERATURE_GRADIENT_JOULE_THOMSON="TemperatureGradientJouleThomson"
    TEMPERATURE_GRADIENT_OVERALL="TemperatureGradientOverall"
    TEMPERATURE_GRADIENT_PIPE_AND_COATINGS="TemperatureGradientPipeAndCoatings"
    TOTAL_DISTANCE="TotalDistance"
    TOTAL_SPHERE_TRANSIT_TIME_SO_FAR="TotalSphereTransitTimeSoFar"
    TRUE_VERTICAL_DEPTH="TrueVerticalDepth"
    VELOCITY_GAS="VelocityGas"
    VELOCITY_LIQUID="VelocityLiquid"
    VELOCITY_OIL="VelocityOil"
    VELOCITY_WATER="VelocityWater"
    VISCOSITY_DEAD_OIL_STOCKTANK="ViscosityDeadOilStockTank"
    VISCOSITY_FLUID_NO_SLIP_INSITU="ViscosityFluidNoSlipInSitu"
    VISCOSITY_FLUID_SLIP_INSITU="ViscosityFluidSlipInSitu"
    VISCOSITY_GAS_INSITU="ViscosityGasInSitu"
    VISCOSITY_LIQUID_INSITU="ViscosityLiquidInSitu"
    VISCOSITY_OIL_INSITU="ViscosityOilInSitu"
    VISCOSITY_WATER_INSITU="ViscosityWaterInSitu"
    VOLUME_FLOWRATE_FLUID_INSITU="VolumeFlowrateFluidInSitu"
    VOLUME_FLOWRATE_GAS_INSITU="VolumeFlowrateGasInSitu"
    VOLUME_FLOWRATE_GAS_INSITU_IDEAL="VolumeFlowrateGasInsituIdeal"
    VOLUME_FLOWRATE_GAS_STOCKTANK="VolumeFlowrateGasStockTank"
    VOLUME_FLOWRATE_LIQUID_INSITU="VolumeFlowrateLiquidInSitu"
    VOLUME_FLOWRATE_LIQUID_STOCKTANK="VolumeFlowrateLiquidStockTank"
    VOLUME_FLOWRATE_OIL_INSITU="VolumeFlowrateOilInSitu"
    VOLUME_FLOWRATE_OIL_STOCKTANK="VolumeFlowrateOilStockTank"
    VOLUME_FLOWRATE_WATER_INSITU="VolumeFlowrateWaterInSitu"
    VOLUME_FLOWRATE_WATER_STOCKTANK="VolumeFlowrateWaterStockTank"
    VOLUME_FRACTION_GAS_INSITU="VolumeFractionGasInSitu"
    VOLUME_FRACTION_LIQUID="VolumeFractionLiquid"
    VOLUME_FRACTION_LIQUID_STOCKTANK="VolumeFractionLiquidStockTank"
    WATERCUT="Watercut"
    WATER_CUT_STOCKTANK="WaterCutStockTank"
    WAX_FORMATION_TEMPERATURE="WaxFormationTemperature"
    WAX_SUB_COOLING_DELTA_TEMPERATURE="WaxSubCoolingDeltaTemperature"
    WGR_STOCKTANK="WGRStockTank"
    Z_FACTOR_GAS_INSITU="ZFactorGasInSitu"
   


class OutputVariables:
    class System:
        GAS_FIELD = [
            SystemVariables.PIPE_OUTSIDE_DIAMETER,
            SystemVariables.SYSTEM_PRESSURE_LOSS,
            SystemVariables.SYSTEM_INLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_TEMPERATURE,
            SystemVariables.TOTAL_LIQUID_HOLDUP,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.INLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.OUTLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.OUTLET_GLR_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_FLUID,
            SystemVariables.CASE_NUMBER,
            SystemVariables.INLET_WATER_CUT_STOCKTANK,
            SystemVariables.INPUT_TUBING_HEAD_PRESSURE,
            SystemVariables.INPUT_FLOWRATE,
            SystemVariables.TOTAL_INJECTION_GAS,
            SystemVariables.GAS_LIFT_INJECTION_RATIO,
            SystemVariables.GAS_LIFT_INJECTION_CASING_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_TEMPERATURE,
            SystemVariables.GAS_LIFT_INJECTION_PORT_DIAMETER,
            SystemVariables.GAS_LIFT_INJECTION_SOURCE_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_HEAD_TEMPERATURE,
            SystemVariables.PCP_INTAKE_PRESSURE,
            SystemVariables.PCP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.PCP_EFFICIENCY,
            SystemVariables.PCP_POWER,
            SystemVariables.PCP_TORQUE,
            SystemVariables.PCP_SPEED,
            SystemVariables.PCP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FRACTION_GAS,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_LIQUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_FREE_GAS,
            SystemVariables.ROD_PUMP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_POWER,
            SystemVariables.ROD_PUMP_DELTA_PRESSURE,
            SystemVariables.ROD_PUMP_EFFICIENCY,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_INTAKE_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_INTAKE_PRESSURE,
            SystemVariables.ESP_INTAKE_TOTAL_VOLUMETRIC_FLOWRATE,
            SystemVariables.ESP_SUCTION_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_DISCHARGE_PRESSURE,
            SystemVariables.ESP_DELTA_PRESSURE,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_DELTA_TEMPERATURE,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_EFFICIENCY_FACTOR,
            SystemVariables.ESP_FLOWRATE_FACTOR,
            SystemVariables.ESP_HEAD_FACTOR,
            SystemVariables.ESP_POWER_FACTOR,
            SystemVariables.BOTTOM_HOLE_PRESSURE,
            SystemVariables.INPUT_WATERCUT,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.INLET_MASS_FLOWRATE_FLUID,
            SystemVariables.WELLHEAD_PRESSURE,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.WELLHEAD_MASS_FLOWRATE_FLUID,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.NODAL_POINT_PRESSURE,
            SystemVariables.NODAL_POINT_MASS_FLOWRATE_FLUID,
            SystemVariables.TOTAL_PRESSURE_DROP_ELEVATIONAL,
            SystemVariables.TOTAL_PRESSURE_DROP_FRICTIONAL,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.SEVERE_SLUGGING_INDICATOR,
            SystemVariables.SLUG_VOLUME_MEAN,
            SystemVariables.SLUG_LENGTH_MEAN,
            SystemVariables.SLUG_FREQUENCY_MEAN,
            SystemVariables.EROSIONAL_VELOCITY_MAXIMUM,
            SystemVariables.MAXIMUM_EROSIONAL_VELOCITY_RATIO,
            SystemVariables.ESP_FREQUENCY,
            SystemVariables.SPHERE_GENERATED_LIQUID_VOLUME,
            SystemVariables.INLET_MASS_FRACTION_GAS,
            SystemVariables.TOTAL_OIL_HOLDUP,
            SystemVariables.TOTAL_WATER_HOLDUP,
            SystemVariables.SYSTEM_TEMPERATURE_DIFFERENCE,
            SystemVariables.OUTLET_WATER_CUT_STOCKTANK,
            SystemVariables.OUTLET_GOR_STOCKTANK,
            SystemVariables.OUTLET_FRACTION_CO2,
            SystemVariables.OUTLET_FRACTION_H2S,
            SystemVariables.OUTLET_FRACTION_N2,
            SystemVariables.OUTLET_FRACTION_H2S,
            SystemVariables.OUTLET_FRACTION_CO,
            SystemVariables.CASE_STATUS,
            SystemVariables.MAXIMUM_VELOCITY_GAS,
            SystemVariables.INLET_EROSIONAL_VELOCITY_RATIO,
            SystemVariables.OUTLET_EROSIONAL_VELOCITY_RATIO,
            SystemVariables.MAXIMUM_HYDRATE_SUB_COOLING_TEMPERATURE_DIFFERENCE,
            SystemVariables.MAXIMUM_EROSION_RATE,
            SystemVariables.MAXIMUM_CORROSION_RATE,
            SystemVariables.MAXIMUM_EROSION_RISK,
            SystemVariables.MAXIMUM_CORROSION_RISK,
            SystemVariables.MAXIMUM_LIQUID_LOADING_VELOCITY_RATIO,
            SystemVariables.MAXIMUM_LIQUID_LOADING_GAS_RATE,
            SystemVariables.NODAL_POINT_BUBBLE_POINT_PRESSURE
            ]
        WELL_PERFORMANCE = [
            SystemVariables.PIPE_OUTSIDE_DIAMETER,
            SystemVariables.SYSTEM_PRESSURE_LOSS,
            SystemVariables.SYSTEM_INLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_TEMPERATURE,
            SystemVariables.TOTAL_LIQUID_HOLDUP,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.INLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.OUTLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.OUTLET_GLR_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_FLUID,
            SystemVariables.CASE_NUMBER,
            SystemVariables.INLET_WATER_CUT_STOCKTANK,
            SystemVariables.INPUT_TUBING_HEAD_PRESSURE,
            SystemVariables.INPUT_FLOWRATE,
            SystemVariables.TOTAL_INJECTION_GAS,
            SystemVariables.GAS_LIFT_INJECTION_RATIO,
            SystemVariables.GAS_LIFT_INJECTION_CASING_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_TEMPERATURE,
            SystemVariables.GAS_LIFT_INJECTION_PORT_DIAMETER,
            SystemVariables.GAS_LIFT_INJECTION_SOURCE_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_HEAD_TEMPERATURE,
            SystemVariables.PCP_INTAKE_PRESSURE,
            SystemVariables.PCP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.PCP_EFFICIENCY,
            SystemVariables.PCP_POWER,
            SystemVariables.PCP_TORQUE,
            SystemVariables.PCP_SPEED,
            SystemVariables.PCP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FRACTION_GAS,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_LIQUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_FREE_GAS,
            SystemVariables.ROD_PUMP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_POWER,
            SystemVariables.ROD_PUMP_DELTA_PRESSURE,
            SystemVariables.ROD_PUMP_EFFICIENCY,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_INTAKE_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_INTAKE_PRESSURE,
            SystemVariables.ESP_INTAKE_TOTAL_VOLUMETRIC_FLOWRATE,
            SystemVariables.ESP_SUCTION_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_DISCHARGE_PRESSURE,
            SystemVariables.ESP_DELTA_PRESSURE,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_DELTA_TEMPERATURE,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_EFFICIENCY_FACTOR,
            SystemVariables.ESP_FLOWRATE_FACTOR,
            SystemVariables.ESP_HEAD_FACTOR,
            SystemVariables.ESP_POWER_FACTOR,
            SystemVariables.BOTTOM_HOLE_PRESSURE,
            SystemVariables.INPUT_WATERCUT,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.INLET_MASS_FLOWRATE_FLUID,
            SystemVariables.WELLHEAD_PRESSURE,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.WELLHEAD_MASS_FLOWRATE_FLUID,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.NODAL_POINT_PRESSURE,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.NODAL_POINT_MASS_FLOWRATE_FLUID,
            SystemVariables.HEEL_RESERVOIR_DRAWDOWN,
            SystemVariables.TOTAL_PRESSURE_DROP_ELEVATIONAL,
            SystemVariables.TOTAL_PRESSURE_DROP_FRICTIONAL,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.SEVERE_SLUGGING_INDICATOR,
            SystemVariables.SLUG_VOLUME_MEAN,
            SystemVariables.SLUG_LENGTH_MEAN,
            SystemVariables.SLUG_FREQUENCY_MEAN,
            SystemVariables.EROSIONAL_VELOCITY_MAXIMUM,
            SystemVariables.MAXIMUM_EROSIONAL_VELOCITY_RATIO,
            SystemVariables.ESP_FREQUENCY,
            SystemVariables.SPHERE_GENERATED_LIQUID_VOLUME,
            SystemVariables.WELLHEAD_TEMPERATURE,
            SystemVariables.PRESSURE_DROP_TOTAL_COMPLETION,
            SystemVariables.INLET_MASS_FRACTION_GAS,
            SystemVariables.SYSTEM_TEMPERATURE_DIFFERENCE,
            SystemVariables.OUTLET_WATER_CUT_STOCKTANK,
            SystemVariables.OUTLET_GOR_STOCKTANK,
            SystemVariables.CASE_STATUS,
            SystemVariables.MAXIMUM_EROSION_RATE,
            SystemVariables.MAXIMUM_CORROSION_RATE,
            SystemVariables.MAXIMUM_EROSION_RISK,
            SystemVariables.MAXIMUM_CORROSION_RISK,
            SystemVariables.MAXIMUM_LIQUID_LOADING_VELOCITY_RATIO,
            SystemVariables.MAXIMUM_LIQUID_LOADING_GAS_RATE,
            SystemVariables.NODAL_POINT_BUBBLE_POINT_PRESSURE
            ]
        FLOW_ASSURANCE = [
            SystemVariables.PIPE_OUTSIDE_DIAMETER,
            SystemVariables.SYSTEM_PRESSURE_LOSS,
            SystemVariables.SYSTEM_INLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_TEMPERATURE,
            SystemVariables.TOTAL_LIQUID_HOLDUP,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.INLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.OUTLET_VELOCITY_FLUID,
            SystemVariables.HEAT_TRANSFER_COEFFICIENT,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.OUTLET_GLR_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_FLUID,
            SystemVariables.CASE_NUMBER,
            SystemVariables.INLET_WATER_CUT_STOCKTANK,
            SystemVariables.INPUT_TUBING_HEAD_PRESSURE,
            SystemVariables.INPUT_FLOWRATE,
            SystemVariables.TOTAL_INJECTION_GAS,
            SystemVariables.GAS_LIFT_INJECTION_RATIO,
            SystemVariables.GAS_LIFT_INJECTION_CASING_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_TEMPERATURE,
            SystemVariables.GAS_LIFT_INJECTION_PORT_DIAMETER,
            SystemVariables.GAS_LIFT_INJECTION_SOURCE_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_HEAD_TEMPERATURE,
            SystemVariables.PCP_INTAKE_PRESSURE,
            SystemVariables.PCP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.PCP_EFFICIENCY,
            SystemVariables.PCP_POWER,
            SystemVariables.PCP_TORQUE,
            SystemVariables.PCP_SPEED,
            SystemVariables.PCP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FRACTION_GAS,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_LIQUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_FREE_GAS,
            SystemVariables.ROD_PUMP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_POWER,
            SystemVariables.ROD_PUMP_DELTA_PRESSURE,
            SystemVariables.ROD_PUMP_EFFICIENCY,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_INTAKE_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_INTAKE_PRESSURE,
            SystemVariables.ESP_INTAKE_TOTAL_VOLUMETRIC_FLOWRATE,
            SystemVariables.ESP_SUCTION_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_DISCHARGE_PRESSURE,
            SystemVariables.ESP_DELTA_PRESSURE,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_DELTA_TEMPERATURE,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_EFFICIENCY_FACTOR,
            SystemVariables.ESP_FLOWRATE_FACTOR,
            SystemVariables.ESP_HEAD_FACTOR,
            SystemVariables.ESP_POWER_FACTOR,
            SystemVariables.BOTTOM_HOLE_PRESSURE,
            SystemVariables.INPUT_WATERCUT,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.INLET_MASS_FLOWRATE_FLUID,
            SystemVariables.WELLHEAD_PRESSURE,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.WELLHEAD_MASS_FLOWRATE_FLUID,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.NODAL_POINT_PRESSURE,
            SystemVariables.NODAL_POINT_MASS_FLOWRATE_FLUID,
            SystemVariables.TOTAL_PRESSURE_DROP_ELEVATIONAL,
            SystemVariables.TOTAL_PRESSURE_DROP_FRICTIONAL,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.SEVERE_SLUGGING_INDICATOR,
            SystemVariables.SLUG_VOLUME_MEAN,
            SystemVariables.SLUG_LENGTH_MEAN,
            SystemVariables.SLUG_FREQUENCY_MEAN,
            SystemVariables.SLUG_VOLUME1IN1000,
            SystemVariables.SLUG_LENGTH1IN1000,
            SystemVariables.SLUG_FREQUENCY1IN1000,
            SystemVariables.EROSIONAL_VELOCITY_MAXIMUM,
            SystemVariables.MAXIMUM_EROSIONAL_VELOCITY_RATIO,
            SystemVariables.ESP_FREQUENCY,
            SystemVariables.SPHERE_GENERATED_LIQUID_VOLUME,
            SystemVariables.PRESSURE_DROP_TOTAL_ACCELERATION,
            SystemVariables.INLET_MASS_FRACTION_GAS,
            SystemVariables.TOTAL_OIL_HOLDUP,
            SystemVariables.TOTAL_WATER_HOLDUP,
            SystemVariables.SYSTEM_TEMPERATURE_DIFFERENCE,
            SystemVariables.MAXIMUM_HEAT_TRANSFER_COEFFICIENT,
            SystemVariables.OUTLET_WATER_CUT_STOCKTANK,
            SystemVariables.OUTLET_GOR_STOCKTANK,
            SystemVariables.CASE_STATUS,
            SystemVariables.MAXIMUM_VELOCITY_FLUID,
            SystemVariables.MAXIMUM_VELOCITY_LIQUID,
            SystemVariables.MAXIMUM_VELOCITY_GAS,
            SystemVariables.MAXIMUM_HYDRATE_SUB_COOLING_TEMPERATURE_DIFFERENCE,
            SystemVariables.MAXIMUM_WAX_SUB_COOLING_TEMPERATURE_DIFFERENCE,
            SystemVariables.MAXIMUM_EROSION_RATE,
            SystemVariables.MAXIMUM_CORROSION_RATE,
            SystemVariables.MAXIMUM_EROSION_RISK,
            SystemVariables.MAXIMUM_CORROSION_RISK,
            SystemVariables.MAXIMUM_LIQUID_LOADING_VELOCITY_RATIO,
            SystemVariables.MAXIMUM_LIQUID_LOADING_GAS_RATE,
            SystemVariables.NODAL_POINT_BUBBLE_POINT_PRESSURE
            ]
        LARGE_NETWORK = [
            SystemVariables.PIPE_OUTSIDE_DIAMETER,
            SystemVariables.SYSTEM_PRESSURE_LOSS,
            SystemVariables.SYSTEM_INLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_PRESSURE,
            SystemVariables.SYSTEM_OUTLET_TEMPERATURE,
            SystemVariables.TOTAL_LIQUID_HOLDUP,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.INLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_INSITU,
            SystemVariables.OUTLET_VELOCITY_FLUID,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.OUTLET_GLR_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_FLUID,
            SystemVariables.TOTAL_INJECTION_GAS,
            SystemVariables.GAS_LIFT_INJECTION_RATIO,
            SystemVariables.GAS_LIFT_INJECTION_CASING_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_TEMPERATURE,
            SystemVariables.GAS_LIFT_INJECTION_PORT_DIAMETER,
            SystemVariables.GAS_LIFT_INJECTION_SOURCE_PRESSURE,
            SystemVariables.GAS_LIFT_INJECTION_CASING_HEAD_TEMPERATURE,
            SystemVariables.PCP_INTAKE_PRESSURE,
            SystemVariables.PCP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.PCP_EFFICIENCY,
            SystemVariables.PCP_POWER,
            SystemVariables.PCP_TORQUE,
            SystemVariables.PCP_SPEED,
            SystemVariables.PCP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_PRESSURE,
            SystemVariables.ROD_PUMP_INTAKE_VOLUMETRIC_FLOWRATE_FLUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FRACTION_GAS,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_LIQUID,
            SystemVariables.ROD_PUMP_INTAKE_VOLUME_FLOWRATE_FREE_GAS,
            SystemVariables.ROD_PUMP_DISCHARGE_PRESSURE,
            SystemVariables.ROD_PUMP_POWER,
            SystemVariables.ROD_PUMP_DELTA_PRESSURE,
            SystemVariables.ROD_PUMP_EFFICIENCY,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_INTAKE_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_INTAKE_PRESSURE,
            SystemVariables.ESP_INTAKE_TOTAL_VOLUMETRIC_FLOWRATE,
            SystemVariables.ESP_SUCTION_GAS_VOLUME_FRACTION,
            SystemVariables.ESP_DISCHARGE_PRESSURE,
            SystemVariables.ESP_DELTA_PRESSURE,
            SystemVariables.ESP_POWER,
            SystemVariables.ESP_NUMBER_OF_STAGES,
            SystemVariables.ESP_HEAD,
            SystemVariables.ESP_DELTA_TEMPERATURE,
            SystemVariables.ESP_EFFICIENCY,
            SystemVariables.ESP_EFFICIENCY_FACTOR,
            SystemVariables.ESP_FLOWRATE_FACTOR,
            SystemVariables.ESP_HEAD_FACTOR,
            SystemVariables.ESP_POWER_FACTOR,
            SystemVariables.BOTTOM_HOLE_PRESSURE,
            SystemVariables.INLET_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.INLET_MASS_FLOWRATE_FLUID,
            SystemVariables.WELLHEAD_PRESSURE,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_LIQUID_INSITU,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            SystemVariables.NODAL_POINT_PRESSURE,
            SystemVariables.NODAL_POINT_MASS_FLOWRATE_FLUID,
            SystemVariables.TOTAL_PRESSURE_DROP_ELEVATIONAL,
            SystemVariables.TOTAL_PRESSURE_DROP_FRICTIONAL,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_WATER_STOCKTANK,
            SystemVariables.OUTLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.OUTLET_MASS_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.WELLHEAD_VOLUME_FLOWRATE_OIL_STOCKTANK,
            SystemVariables.NODAL_POINT_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.INLET_VOLUME_FLOWRATE_GAS_STOCKTANK,
            SystemVariables.SEVERE_SLUGGING_INDICATOR,
            SystemVariables.SLUG_VOLUME_MEAN,
            SystemVariables.SLUG_LENGTH_MEAN,
            SystemVariables.SLUG_FREQUENCY_MEAN,
            SystemVariables.EROSIONAL_VELOCITY_MAXIMUM,
            SystemVariables.MAXIMUM_EROSIONAL_VELOCITY_RATIO,
            SystemVariables.ESP_FREQUENCY,
            SystemVariables.SPHERE_GENERATED_LIQUID_VOLUME,
            SystemVariables.INLET_MASS_FRACTION_GAS,
            SystemVariables.SYSTEM_TEMPERATURE_DIFFERENCE,
            SystemVariables.OUTLET_WATER_CUT_STOCKTANK,
            SystemVariables.OUTLET_GOR_STOCKTANK,
            SystemVariables.MAXIMUM_EROSION_RATE,
            SystemVariables.MAXIMUM_CORROSION_RATE,
            SystemVariables.MAXIMUM_EROSION_RISK,
            SystemVariables.MAXIMUM_CORROSION_RISK,
            SystemVariables.MAXIMUM_LIQUID_LOADING_VELOCITY_RATIO,
            SystemVariables.MAXIMUM_LIQUID_LOADING_GAS_RATE,
            SystemVariables.NODAL_POINT_BUBBLE_POINT_PRESSURE
            ]
    class Profile:
        GAS_FIELD = [
            ProfileVariables.HORIZONTAL_DISTANCE,
            ProfileVariables.TOTAL_DISTANCE,
            ProfileVariables.ELEVATION,
            ProfileVariables.PRESSURE,
            ProfileVariables.TEMPERATURE,
            ProfileVariables.HOLDUP_FRACTION_LIQUID,
            ProfileVariables.VELOCITY_LIQUID,
            ProfileVariables.VELOCITY_GAS,
            ProfileVariables.MEAN_VELOCITY_FLUID,
            ProfileVariables.NODE_NUMBER,
            ProfileVariables.HYDROSTATIC_HEAD,
            ProfileVariables.PIPE_INSIDE_DIAMETER,
            ProfileVariables.ENTHALPY_FLUID,
            ProfileVariables.WATERCUT,
            ProfileVariables.VOLUME_FRACTION_LIQUID,
            ProfileVariables.TRUE_VERTICAL_DEPTH,
            ProfileVariables.MEASURED_DEPTH,
            ProfileVariables.FLOWRATE_LIQUID_INSITU,
            ProfileVariables.FLOWRATE_GAS_INSITU,
            ProfileVariables.PRESSURE_GRADIENT_TOTAL,
            ProfileVariables.AMBIENT_TEMPERATURE_AT_NODE,
            ProfileVariables.PRESSURE_GRADIENT_FRICTION,
            ProfileVariables.PRESSURE_GRADIENT_ELEVATION,
            ProfileVariables.PRESSURE_GRADIENT_ACCELERATION,
            ProfileVariables.VOLUME_FLOWRATE_GAS_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_OIL_STOCKTANK,
            ProfileVariables.GLR_STOCKTANK,
            ProfileVariables.LGR_STOCKTANK,
            ProfileVariables.MASS_FLOWRATE,
            ProfileVariables.VOLUME_FLOWRATE_GAS_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_OIL_INSITU,
            ProfileVariables.VOLUME_FRACTION_GAS_INSITU,
            ProfileVariables.SPECIFIC_GRAVITY_GAS_INSITU,
            ProfileVariables.DENSITY_GAS_INSITU,
            ProfileVariables.VISCOSITY_GAS_INSITU,
            ProfileVariables.VISCOSITY_LIQUID_INSITU,
            ProfileVariables.ENTROPY_FLUID_INSITU,
            ProfileVariables.Z_FACTOR_GAS_INSITU,
            ProfileVariables.SLUG_VOLUME_MEAN,
            ProfileVariables.SLUG_LENGTH_MEAN,
            ProfileVariables.SLUG_FREQUENCY_MEAN,
            ProfileVariables.EROSIONAL_VELOCITY,
            ProfileVariables.EROSIONAL_VELOCITY_RATIO,
            ProfileVariables.FLOW_PATTERN_GAS_LIQUID,
            ProfileVariables.FLOW_PATTERN_OIL_WATER,
            ProfileVariables.SUPERFICIAL_VELOCITY_LIQUID,
            ProfileVariables.SUPERFICIAL_VELOCITY_GAS,
            ProfileVariables.HORIZONTAL_POSITION,
            ProfileVariables.EROSION_RATE,
            ProfileVariables.CORROSION_RATE,
            ProfileVariables.CORROSION_PIT_RATE,
            ProfileVariables.CORROSION_CUMULATIVE_LOSS,
            ProfileVariables.EROSION_RISK,
            ProfileVariables.CORROSION_RISK,
            ProfileVariables.HYDRATE_FORMATION_TEMPERATURE,
            ProfileVariables.HYDRATE_SUB_COOLING_DELTA_TEMPERATURE,
            ProfileVariables.LIQUID_LOADING_VELOCITY,
            ProfileVariables.LIQUID_LOADING_VELOCITY_RATIO,
            ProfileVariables.LIQUID_LOADING_GAS_RATE
            ]
        WELL_PERFORMANCE = [
            ProfileVariables.HORIZONTAL_DISTANCE,
            ProfileVariables.TOTAL_DISTANCE,
            ProfileVariables.ELEVATION,
            ProfileVariables.PRESSURE,
            ProfileVariables.TEMPERATURE,
            ProfileVariables.HOLDUP_FRACTION_LIQUID,
            ProfileVariables.VELOCITY_LIQUID,
            ProfileVariables.VELOCITY_GAS,
            ProfileVariables.MEAN_VELOCITY_FLUID,
            ProfileVariables.NODE_NUMBER,
            ProfileVariables.HYDROSTATIC_HEAD,
            ProfileVariables.PIPE_INSIDE_DIAMETER,
            ProfileVariables.WATERCUT,
            ProfileVariables.VOLUME_FRACTION_LIQUID,
            ProfileVariables.TRUE_VERTICAL_DEPTH,
            ProfileVariables.MEASURED_DEPTH,
            ProfileVariables.FLOWRATE_LIQUID_INSITU,
            ProfileVariables.FLOWRATE_GAS_INSITU,
            ProfileVariables.RESERVOIR_DRAWDOWN,
            ProfileVariables.PRESSURE_GRADIENT_TOTAL,
            ProfileVariables.LAYER_STATIC_PRESSURE,
            ProfileVariables.OIL_FORMATION_VOLUME_FACTOR,
            ProfileVariables.AMBIENT_TEMPERATURE_AT_NODE,
            ProfileVariables.SKIN_TURBULENT_DUE_TO_DAMAGED_WELLBORE,
            ProfileVariables.SKIN_FACTOR_OVERALL,
            ProfileVariables.SKIN_FACTOR_RATE_DEPENDENT,
            ProfileVariables.SKIN_DUE_TO_DAMAGED_WELLBORE,
            ProfileVariables.SKIN_DUE_TO_PERFORATION_GEOMETRY,
            ProfileVariables.SKIN_DUE_TO_COMPACTED_ZONE,
            ProfileVariables.SKIN_DUE_TO_GRAVEL_PACK,
            ProfileVariables.SKIN_TURBULENT_DUE_TO_PERFORATIONS,
            ProfileVariables.SKIN_TURBULENT_DUE_TO_GRAVEL_PACKING,
            ProfileVariables.EFFECTIVE_PERMEABILITY,
            ProfileVariables.PRESSURE_GRADIENT_FRICTION,
            ProfileVariables.PRESSURE_GRADIENT_ELEVATION,
            ProfileVariables.PRESSURE_GRADIENT_ACCELERATION,
            ProfileVariables.VOLUME_FLOWRATE_GAS_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_OIL_STOCKTANK,
            ProfileVariables.GLR_STOCKTANK,
            ProfileVariables.LGR_STOCKTANK,
            ProfileVariables.MASS_FLOWRATE,
            ProfileVariables.VOLUME_FLOWRATE_GAS_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_OIL_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_WATER_INSITU,
            ProfileVariables.VOLUME_FRACTION_GAS_INSITU,
            ProfileVariables.BUBBLE_POINT_PRESSURE_INSITU,
            ProfileVariables.DENSITY_LIQUID_INSITU,
            ProfileVariables.DENSITY_OIL_INSITU,
            ProfileVariables.DENSITY_WATER_INSITU,
            ProfileVariables.VISCOSITY_GAS_INSITU,
            ProfileVariables.VISCOSITY_LIQUID_INSITU,
            ProfileVariables.EROSIONAL_VELOCITY,
            ProfileVariables.EROSIONAL_VELOCITY_RATIO,
            ProfileVariables.HEAT_CAPACITY_GAS_INSITU,
            ProfileVariables.HEAT_CAPACITY_LIQUID_INSITU,
            ProfileVariables.FLOW_PATTERN_GAS_LIQUID,
            ProfileVariables.FLOW_PATTERN_OIL_WATER,
            ProfileVariables.SUPERFICIAL_VELOCITY_LIQUID,
            ProfileVariables.SUPERFICIAL_VELOCITY_GAS,
            ProfileVariables.HORIZONTAL_POSITION,
            ProfileVariables.EROSION_RATE,
            ProfileVariables.CORROSION_RATE,
            ProfileVariables.CORROSION_PIT_RATE,
            ProfileVariables.CORROSION_CUMULATIVE_LOSS,
            ProfileVariables.EROSION_RISK,
            ProfileVariables.CORROSION_RISK,
            ProfileVariables.LIQUID_LOADING_VELOCITY,
            ProfileVariables.LIQUID_LOADING_VELOCITY_RATIO,
            ProfileVariables.LIQUID_LOADING_GAS_RATE,
            ProfileVariables.SPECIFIC_HEAT_CAPACITY_RATIO_GAS_INSITU
            ]
        FLOW_ASSURANCE = [
            ProfileVariables.HORIZONTAL_DISTANCE,
            ProfileVariables.TOTAL_DISTANCE,
            ProfileVariables.ELEVATION,
            ProfileVariables.PRESSURE,
            ProfileVariables.TEMPERATURE,
            ProfileVariables.HOLDUP_FRACTION_LIQUID,
            ProfileVariables.VELOCITY_LIQUID,
            ProfileVariables.VELOCITY_GAS,
            ProfileVariables.MEAN_VELOCITY_FLUID,
            ProfileVariables.NODE_NUMBER,
            ProfileVariables.HYDROSTATIC_HEAD,
            ProfileVariables.PIPE_INSIDE_DIAMETER,
            ProfileVariables.ENTHALPY_FLUID,
            ProfileVariables.WATERCUT,
            ProfileVariables.VOLUME_FRACTION_LIQUID,
            ProfileVariables.TRUE_VERTICAL_DEPTH,
            ProfileVariables.MEASURED_DEPTH,
            ProfileVariables.FLOWRATE_LIQUID_INSITU,
            ProfileVariables.FLOWRATE_GAS_INSITU,
            ProfileVariables.PRESSURE_GRADIENT_TOTAL,
            ProfileVariables.AMBIENT_TEMPERATURE_AT_NODE,
            ProfileVariables.PRESSURE_GRADIENT_FRICTION,
            ProfileVariables.PRESSURE_GRADIENT_ELEVATION,
            ProfileVariables.PRESSURE_GRADIENT_ACCELERATION,
            ProfileVariables.REYNOLDS_NUMBER,
            ProfileVariables.VOLUME_FLOWRATE_GAS_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_OIL_STOCKTANK,
            ProfileVariables.GLR_STOCKTANK,
            ProfileVariables.LGR_STOCKTANK,
            ProfileVariables.MASS_FLOWRATE,
            ProfileVariables.VOLUME_FLOWRATE_GAS_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_OIL_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_WATER_INSITU,
            ProfileVariables.VOLUME_FRACTION_GAS_INSITU,
            ProfileVariables.BUBBLE_POINT_PRESSURE_INSITU,
            ProfileVariables.DENSITY_GAS_INSITU,
            ProfileVariables.DENSITY_LIQUID_INSITU,
            ProfileVariables.DENSITY_OIL_INSITU,
            ProfileVariables.DENSITY_WATER_INSITU,
            ProfileVariables.DENSITY_FLUID_NO_SLIP_INSITU,
            ProfileVariables.DENSITY_FLUID_INSITU,
            ProfileVariables.VISCOSITY_GAS_INSITU,
            ProfileVariables.VISCOSITY_LIQUID_INSITU,
            ProfileVariables.ENTROPY_FLUID_INSITU,
            ProfileVariables.SLUG_VOLUME_MEAN,
            ProfileVariables.SLUG_LENGTH_MEAN,
            ProfileVariables.SLUG_FREQUENCY_MEAN,
            ProfileVariables.SLUG_VOLUME1IN1000,
            ProfileVariables.SLUG_LENGTH1IN1000,
            ProfileVariables.SLUG_FREQUENCY1IN1000,
            ProfileVariables.EROSIONAL_VELOCITY,
            ProfileVariables.EROSIONAL_VELOCITY_RATIO,
            ProfileVariables.OVERALL_HEAT_TRANSFER_COEFFICIENT,
            ProfileVariables.INSIDE_FLUID_FILM_HEAT_TRANSFER_COEFFICIENT,
            ProfileVariables.HEAT_CAPACITY_GAS_INSITU,
            ProfileVariables.HEAT_CAPACITY_LIQUID_INSITU,
            ProfileVariables.FLOW_PATTERN_GAS_LIQUID,
            ProfileVariables.FLOW_PATTERN_OIL_WATER,
            ProfileVariables.SUPERFICIAL_VELOCITY_LIQUID,
            ProfileVariables.SUPERFICIAL_VELOCITY_GAS,
            ProfileVariables.HORIZONTAL_POSITION,
            ProfileVariables.EROSION_RATE,
            ProfileVariables.CORROSION_RATE,
            ProfileVariables.CORROSION_PIT_RATE,
            ProfileVariables.CORROSION_CUMULATIVE_LOSS,
            ProfileVariables.EROSION_RISK,
            ProfileVariables.CORROSION_RISK,
            ProfileVariables.HYDRATE_FORMATION_TEMPERATURE,
            ProfileVariables.HYDRATE_SUB_COOLING_DELTA_TEMPERATURE,
            ProfileVariables.WAX_FORMATION_TEMPERATURE,
            ProfileVariables.WAX_SUB_COOLING_DELTA_TEMPERATURE,
            ProfileVariables.ASPHALTENE_FORMATION_TEMPERATURE,
            ProfileVariables.LIQUID_LOADING_VELOCITY,
            ProfileVariables.LIQUID_LOADING_VELOCITY_RATIO,
            ProfileVariables.LIQUID_LOADING_GAS_RATE,
            ProfileVariables.TEMPERATURE_GRADIENT_ELEVATION,
            ProfileVariables.TEMPERATURE_GRADIENT_JOULE_THOMSON,
            ProfileVariables.TEMPERATURE_GRADIENT_HEAT_TRANSFER,
            ProfileVariables.TEMPERATURE_GRADIENT_OVERALL,
            ProfileVariables.TEMPERATURE_GRADIENT_INSIDE_FILM,
            ProfileVariables.TEMPERATURE_GRADIENT_PIPE_AND_COATINGS,
            ProfileVariables.TEMPERATURE_GRADIENT_GROUND_AND_AMBIENT,
            ProfileVariables.SPECIFIC_HEAT_CAPACITY_RATIO_GAS_INSITU
            ]
        LARGE_NETWORK = [
            ProfileVariables.HORIZONTAL_DISTANCE,
            ProfileVariables.TOTAL_DISTANCE,
            ProfileVariables.ELEVATION,
            ProfileVariables.PRESSURE,
            ProfileVariables.TEMPERATURE,
            ProfileVariables.HOLDUP_FRACTION_LIQUID,
            ProfileVariables.VELOCITY_LIQUID,
            ProfileVariables.VELOCITY_GAS,
            ProfileVariables.MEAN_VELOCITY_FLUID,
            ProfileVariables.HYDROSTATIC_HEAD,
            ProfileVariables.PIPE_INSIDE_DIAMETER,
            ProfileVariables.WATERCUT,
            ProfileVariables.VOLUME_FRACTION_LIQUID,
            ProfileVariables.FLOWRATE_LIQUID_INSITU,
            ProfileVariables.FLOWRATE_GAS_INSITU,
            ProfileVariables.PRESSURE_GRADIENT_TOTAL,
            ProfileVariables.AMBIENT_TEMPERATURE_AT_NODE,
            ProfileVariables.PRESSURE_GRADIENT_FRICTION,
            ProfileVariables.PRESSURE_GRADIENT_ELEVATION,
            ProfileVariables.PRESSURE_GRADIENT_ACCELERATION,
            ProfileVariables.VOLUME_FLOWRATE_GAS_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_STOCKTANK,
            ProfileVariables.VOLUME_FLOWRATE_OIL_STOCKTANK,
            ProfileVariables.GLR_STOCKTANK,
            ProfileVariables.LGR_STOCKTANK,
            ProfileVariables.MASS_FLOWRATE,
            ProfileVariables.VOLUME_FLOWRATE_GAS_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_LIQUID_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_OIL_INSITU,
            ProfileVariables.VOLUME_FLOWRATE_WATER_INSITU,
            ProfileVariables.VOLUME_FRACTION_GAS_INSITU,
            ProfileVariables.DENSITY_LIQUID_INSITU,
            ProfileVariables.DENSITY_OIL_INSITU,
            ProfileVariables.DENSITY_WATER_INSITU,
            ProfileVariables.VISCOSITY_GAS_INSITU,
            ProfileVariables.VISCOSITY_LIQUID_INSITU,
            ProfileVariables.SLUG_VOLUME_MEAN,
            ProfileVariables.SLUG_LENGTH_MEAN,
            ProfileVariables.SLUG_FREQUENCY_MEAN,
            ProfileVariables.EROSIONAL_VELOCITY,
            ProfileVariables.EROSIONAL_VELOCITY_RATIO,
            ProfileVariables.HEAT_CAPACITY_GAS_INSITU,
            ProfileVariables.HEAT_CAPACITY_LIQUID_INSITU,
            ProfileVariables.FLOW_PATTERN_GAS_LIQUID,
            ProfileVariables.FLOW_PATTERN_OIL_WATER,
            ProfileVariables.HORIZONTAL_POSITION,
            ProfileVariables.EROSION_RATE,
            ProfileVariables.CORROSION_RATE,
            ProfileVariables.CORROSION_PIT_RATE,
            ProfileVariables.CORROSION_CUMULATIVE_LOSS,
            ProfileVariables.EROSION_RISK,
            ProfileVariables.CORROSION_RISK,
            ProfileVariables.LIQUID_LOADING_VELOCITY,
            ProfileVariables.LIQUID_LOADING_VELOCITY_RATIO,
            ProfileVariables.LIQUID_LOADING_GAS_RATE,
            ProfileVariables.SPECIFIC_HEAT_CAPACITY_RATIO_GAS_INSITU
            ]

class EspCurvesVariables:
    """ Available Results Profile Variables """
    VARIABLESPEEDCURVE='Speed',
    VARIABLEPERFORMANCECURVE="Performance"
    VALUES="Values",
    VALUE="Value",
    UNIT="Unit",
    FREQUENCIES="Frequencies",
    OPERATINGENVELOPE="OperatingEnvelope",
    FLOWRATE="Flowrate",
    MODEL="Model",
    MANUFACTURER="Manufacturer",
    MAXFLOWRATE="MaxFlowrate",
    MINFLOWRATE="MinFlowrate",
    STAGES="BaseStages",
    FREQUENCY="Frequency",
    SPEED="Speed",
    POWER="Power",
    HEAD="Head",
    EFFICIENCY="Efficiency",
    INPUTS="Inputs",
    OPERATINGPOINT="OperatingPoint",
    MINCURVE="MinCurve",
    BEPCURVE="BepCurve",
    MAXCURVE="MaxCurve",

EspCurveVariablesOeratingEnvelopeMap = {
    "SpeedCurveFlowrateMinEfficiency":EspCurvesVariables.MINCURVE,
    "SpeedCurveFlowrateMidEfficiency":EspCurvesVariables.BEPCURVE,
    "SpeedCurveFlowrateMaxEfficiency":EspCurvesVariables.MAXCURVE,
    "SpeedCurveHeadMinEfficiency":EspCurvesVariables.MINCURVE,
    "SpeedCurveHeadMidEfficiency":EspCurvesVariables.BEPCURVE,
    "SpeedCurveHeadMaxEfficiency":EspCurvesVariables.MAXCURVE,
}

EspCurveVariablesMap = {
    "SpeedCurveFlowrate":EspCurvesVariables.FLOWRATE,
    "SpeedCurveHead":EspCurvesVariables.HEAD,
    "SpeedCurveFlowrateMinEfficiency":EspCurvesVariables.FLOWRATE,
    "SpeedCurveFlowrateMidEfficiency":EspCurvesVariables.FLOWRATE,
    "SpeedCurveFlowrateMaxEfficiency":EspCurvesVariables.FLOWRATE,
    "SpeedCurveHeadMinEfficiency":EspCurvesVariables.HEAD,
    "SpeedCurveHeadMidEfficiency":EspCurvesVariables.HEAD,
    "SpeedCurveHeadMaxEfficiency":EspCurvesVariables.HEAD,
    "PerformanceCurveFlowrate":EspCurvesVariables.FLOWRATE,
    "PerformanceCurveHead":EspCurvesVariables.HEAD,
    "PerformanceCurveEfficiency":EspCurvesVariables.EFFICIENCY,
    "PerformanceCurvePower":EspCurvesVariables.POWER,
    "EspFrequency":EspCurvesVariables.FREQUENCY,
    "EspHead":EspCurvesVariables.HEAD,
    "EspSpeed":EspCurvesVariables.SPEED,
    "FlowingLiquidVolumeFlowRate":EspCurvesVariables.FLOWRATE,
    "EspMinFlowrate":EspCurvesVariables.MINFLOWRATE,
    "EspMaxFlowrate":EspCurvesVariables.MAXFLOWRATE,
    "EspManufacturer":EspCurvesVariables.MANUFACTURER,
    "EspModel":EspCurvesVariables.MODEL,
    "EspBaseStages":EspCurvesVariables.STAGES,

}


class RequestMessageType(str, Enum):
    """ Available options for optimizer request message """
    NONE = "None",
    DATA_ONLY = "DataOnly",
    DATA_AND_MODELTEXT = "DataAndModelText",
    DATA_AND_MODELFILENAME = "DataAndModelFileName",

