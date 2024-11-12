from Constants import Constants as cs
import Wing as wi
import math as ma

Cd0 = cs.Cd0
Span = wi.WingSpan / 0.3048 #ft
SurfaceArea = wi.S / (0.3048**2) #ft2
OGFuelMassFraction = 0.2065
NewFuelMassFraction = 0.1398
FuelMassFraction = NewFuelMassFraction
QuarterSweep = ma.radians(cs.QuarterChordSweep) #rad
AspectRatio = cs.AspectRatio
DynamicLoad = (0.5 * cs.DensityAtCruise * cs.CruiseSpeed**2) * 0.02089 #lb / ft2
TaperRatio = cs.TaperRatio
RootChord = wi.RootChord / 0.3048
ThicknessToChord = 0.11
TailShape = 0
TailLength = 7.84 / 0.3048 #ft 

UltimateLoad = 3.75
UltimateLandingLoad = 2.5 * 1.5 
LandingMassRatio = cs.MassRatioLanding

PressureDifference = 8 #psi
EngineWeight = 1679 * 9.81 * 0.2248 #lbf
FuelDensity = 6.68 #lb / gallon
TankVolume = 8.62 * 264.172 #gallon
NumberOfPeople = 85
PayloadWeight = 9302 * 2.205 # pounds

MainLandingGearLength = 4.77 / 0.3048 #CHANGE
NoseLandingGearLength = 4.77 / 0.3048 #CHANGE

TailSurfaceHorizontal = 23 / (0.3048**2) #ft
TailTaperRatioHorizontal = 0.35 
TailAspectRatioHorizontal = 5 
TailSweepHorizontalLE = ma.radians(30) #rad
TailSpanHorizontal = 10.7 / (0.3048) #ft
TailRootChordHorizontal = 3.18 / 0.3048 #ft
TailSweepHorizontal = ma.atan((ma.tan(TailSweepHorizontalLE)*0.5*TailSpanHorizontal - 0.25*TailRootChordHorizontal + 0.25*TailRootChordHorizontal*TailTaperRatioHorizontal)/0.5 * TailSpanHorizontal) #RADIANS 42

TailSurfaceVertical = 16.2 / (0.3048**2) #ft2
TailTaperRatioVertical = 0.7
TailAspectRatioVertical = 1.2
TailSweepVerticalLE = ma.radians(42) #rad
TailSpanVertical = 4.41 / (0.3048) #ft
TailRootChordVertical = 4.33 / (0.3048) #ft
TailSweepVertical = ma.atan((ma.tan(TailSweepVerticalLE)*0.5*TailSpanVertical - 0.25*TailRootChordVertical + 0.25*TailRootChordVertical*TailTaperRatioVertical)/0.5 * TailSpanVertical) #RADIANS 42

FuselageDepth = 2.801 / (0.3048) # ft 
FuselageWettedArea = 270 / (0.3048**2) 
FuselageStrucLength = 16.08 / (0.3048) #ft (Without Tailcone/Radome)
FuselageVolume = (FuselageDepth/2)**2 * ma.pi * FuselageStrucLength

def EstWingWeight(EstimatedMTOWinPounds):
    WingWeight = 0.036 * SurfaceArea**0.758 * (FuelMassFraction * EstimatedMTOWinPounds)**0.0035 * (AspectRatio / (ma.cos(QuarterSweep))**2)**0.6 * DynamicLoad**0.006 * TaperRatio**0.04 * (100 * ThicknessToChord/(ma.cos(QuarterSweep)))**(-1*0.3) * (UltimateLoad*EstimatedMTOWinPounds)**0.49
    return(WingWeight)

def EstHorTailWeight(EstimatedMTOWinPounds):
    HorTailWeight = 0.016 * (UltimateLoad * EstimatedMTOWinPounds)**0.414 * DynamicLoad**0.168 * TailSurfaceHorizontal**0.896 * (100*ThicknessToChord/(ma.cos(QuarterSweep)))**(-1*0.12) * (TailAspectRatioHorizontal / (ma.cos(TailSweepHorizontal))**2)**0.043 * TailTaperRatioHorizontal**(-1*0.02)
    return(HorTailWeight)

def EstVertTailWeight(EstimatedMTOWinPounds):
    VertTailWeight = 0.073 * (1 + 0.2*TailShape) * (UltimateLoad*EstimatedMTOWinPounds)**0.376 * DynamicLoad**0.122 * TailSurfaceVertical**0.873 * (100 * ThicknessToChord / ma.cos(TailSweepVertical))**(-0.49) * (TailAspectRatioVertical / (ma.cos(TailSweepVertical))**2)**0.357 * TailTaperRatioVertical**0.039
    return(VertTailWeight)

def EstFuselageWeight(EstimatedMTOWinPounds):
    FuselageWeight = 0.052 * FuselageWettedArea**1.086 * (UltimateLoad*EstimatedMTOWinPounds)**0.177 * TailLength**(-0.051) * (FuselageStrucLength / FuselageDepth)**(-0.072) * DynamicLoad**0.241 + (11.9 + (FuselageVolume*PressureDifference)**0.271)
    return(FuselageWeight)

def EstMainLandingWeight(EstimatedMTOWinPounds):
    MainLandingWeight = 0.095 * (UltimateLandingLoad * (EstimatedMTOWinPounds * LandingMassRatio))**0.768 * (MainLandingGearLength / 12)**0.409
    return(MainLandingWeight)

def EstNoseLandingWeight(EstimatedMTOWinPounds):
    NoseLandingWeight = 0.125 * (UltimateLandingLoad * (EstimatedMTOWinPounds * LandingMassRatio))**0.566 * (NoseLandingGearLength/12)**0.845
    return(NoseLandingWeight)

def EstEngineWeight(EstimatedMTOWinPounds):
    EnginelWeight = 2.575 * EngineWeight**0.922 * 2
    return(EnginelWeight)

def EstFuelSysWeight(EstimatedMTOWinPounds):
    FuelSysWeight = 2.49 * (FuelMassFraction * EstimatedMTOWinPounds / FuelDensity)**0.726 * (1/(1 + TankVolume/(FuelMassFraction * EstimatedMTOWinPounds / FuelDensity)))**0.363 * 2**0.242 * 2**0.157
    return(FuelSysWeight)

def EstFlightControlWeight(EstimatedMTOWinPounds):
    FlightControlWeight = 0.053 * FuselageStrucLength**1.536 * Span**0.371 * (UltimateLoad*EstimatedMTOWinPounds*0.0001)**0.8
    return(FlightControlWeight)

def EstHydraulicsWeight(EstimatedMTOWinPounds):
    HydraulicsWeight = 0.001 * EstimatedMTOWinPounds
    return(HydraulicsWeight)

def EstAvionicsWeight(EstimatedMTOWinPounds):
    AvionicsWeight = 2.117 * 1000**0.933
    return(AvionicsWeight)

def EstElectricalWeight(EstimatedMTOWinPounds):
    ElectricalWeight = 12.57 * (EstFuelSysWeight(EstimatedMTOWinPounds) + EstAvionicsWeight(EstimatedMTOWinPounds))**0.51
    return(ElectricalWeight)

def EstAircoWeight(EstimatedMTOWinPounds):
    AircoWeight = 0.265 * EstimatedMTOWinPounds**0.52 * NumberOfPeople**0.68 * EstAvionicsWeight(EstimatedMTOWinPounds)**0.17 * 0.77**0.08
    return(AircoWeight)

def EstFurnishingsWeight(EstimatedMTOWinPounds):
    FurnishingsWeight = 0.0582 * EstimatedMTOWinPounds - 65
    return(FurnishingsWeight)



def ClassIIEstimation(WeightEstimate):
    Different = True
    while Different:

        FuelWeight = WeightEstimate * FuelMassFraction

        WingWeight = EstWingWeight(WeightEstimate)
        HorTailWeight = EstHorTailWeight(WeightEstimate)
        VertTailWeight = EstVertTailWeight(WeightEstimate)
        FuselageWeight = EstFuselageWeight(WeightEstimate)
        MainLandingWeight = EstMainLandingWeight(WeightEstimate)
        NoseLandingWeight = EstNoseLandingWeight(WeightEstimate)
        EngineSystemWeight = EstEngineWeight(WeightEstimate)
        FuelSystemWeight = EstFuelSysWeight(WeightEstimate)
        FlightControlWeight = EstFlightControlWeight(WeightEstimate)
        HydraulicsWeight = EstHydraulicsWeight(WeightEstimate)
        ElectricalWeight = EstElectricalWeight(WeightEstimate)
        AvionicsWeight = EstAvionicsWeight(WeightEstimate)
        AircoWeight = EstAircoWeight(WeightEstimate)
        FurnishingsWeight = EstFurnishingsWeight(WeightEstimate)

        OEW = FurnishingsWeight + AircoWeight + AvionicsWeight + ElectricalWeight + HydraulicsWeight + FlightControlWeight + FuelSystemWeight + EngineSystemWeight + NoseLandingWeight + MainLandingWeight + FuselageWeight + HorTailWeight + VertTailWeight + WingWeight

        NewWeight = OEW + FuelWeight + PayloadWeight

        Difference = abs(NewWeight - WeightEstimate) / WeightEstimate
        #print("The Weight estimate is " + str(WeightEstimate) + " pounds, and the calculated weight is then " + str(NewWeight) + " pounds.")
        #print("The OEW is " + str(OEW) + " pounds")
        #print(FurnishingsWeight , AircoWeight , AvionicsWeight , ElectricalWeight , HydraulicsWeight , FlightControlWeight , FuelSystemWeight , EngineSystemWeight , NoseLandingWeight , MainLandingWeight , FuselageWeight , HorTailWeight , VertTailWeight , WingWeight)

        #Different = False
        #DefiniteWeight = NewWeight

        #print("The Difference is " + str(Difference) + ".")

        if Difference < 0.01:
            Different = False
            DefiniteWeight = NewWeight
        else:
            WeightEstimate = NewWeight

        #ytab.append(NewWeight)
    return(DefiniteWeight)


Different = 1
OriginalWeight = 41253 / 0.4536 #(IN POUNDS)
CalculatedWeight = ClassIIEstimation(OriginalWeight)
CalculatedKilos = CalculatedWeight * 0.45359237 

print("The total estimated weight is " + str(CalculatedKilos) + " kilograms.")
print(CalculatedKilos*9.80665)
print(wi.S)

