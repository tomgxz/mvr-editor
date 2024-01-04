def getFixtureFromLayer(layer):

    fixture = {}

    match layer:

        case "Chauvet Ovation CYC 1 FC":
            fixture["Fixture"] = "Chauvet Ovation CYC 1 FC"
            fixture["DMX Mode"] = "HSV"
            fixture["DMX Channels"] = "3"

        case "Chauvet Ovation CYC 3 FC": # NOT IMPLEMENTED
            fixture["Fixture"] = "Chauvet Ovation CYC 3 FC"
            fixture["DMX Mode"] = "HSV"
            fixture["DMX Channels"] = "3"
            
        case "Clay Paky Sharpy X Frame":
            fixture["Fixture"] = "Clay Paky Sharpy X Frame"
            fixture["DMX Mode"] = "Default"
            fixture["DMX Channels"] = "43"
            
        case "Clay Paky Stormy CC": # NOT IMPLEMENTED
            fixture["Fixture"] = "Clay Paky Stormy CC"
            fixture["DMX Mode"] = "Independent"
            fixture["DMX Channels"] = "14"

        case "Generic 2-Cell Blinder":
            fixture["Fixture"] = "Generic 2-Cell Blinder"
            fixture["DMX Mode"] = "Control"
            fixture["DMX Channels"] = "1"

        case "Elation DTW Blinder 700 IP":
            fixture["Fixture"] = "Elation DTW Blinder 700 IP"
            fixture["DMX Mode"] = "01CH"
            fixture["DMX Channels"] = "1"

        case "ETC Source 4 LED":
            fixture["Fixture"] = "ETC Source Four LED Series 2 14 Lustr"
            fixture["DMX Mode"] = "RGB [Fan Mode=Auto]"
            fixture["DMX Channels"] = "4"

        case "Generic RGBAW LED Bulb":
            fixture["Fixture"] = "Generic RGBAW LED Bulb"
            fixture["DMX Mode"] = "Mode 1"
            fixture["DMX Channels"] = "6"

        case "GLP Impression FR10 Bar":
            fixture["Fixture"] = "GLP Impression FR10 Bar"
            fixture["DMX Mode"] = "SPIX"
            fixture["DMX Channels"] = "68"

        case "GLP Impression X4 Bar 10":
            fixture["Fixture"] = "GLP Impression X4 Bar 10"
            fixture["DMX Mode"] = "Compressed 1.1"
            fixture["DMX Channels"] = "20"

        case "GLP JDC1 Strobe":
            fixture["Fixture"] = "GLP JDC1 Strobe"
            fixture["DMX Mode"] = "SPIX"
            fixture["DMX Channels"] = "68"

        case "Martin MAC Aura PXL":
            fixture["Fixture"] = "Martin MAC Aura PXL"
            fixture["DMX Mode"] = "Ludicrous"
            fixture["DMX Channels"] = "512"

        case "Martin MAC Aura XB":
            fixture["Fixture"] = "Martin MAC Aura XB"
            fixture["DMX Mode"] = "Standard"
            fixture["DMX Channels"] = "14"

        case "Martin MAC Ultra Performance":
            fixture["Fixture"] = "Martin MAC Ultra Performance"
            fixture["DMX Mode"] = "Basic"
            fixture["DMX Channels"] = "48"

        case "Martin MAC Viper Performance":
            fixture["Fixture"] = "Martin MAC Viper Performance"
            fixture["DMX Mode"] = "Basic"
            fixture["DMX Channels"] = "32"

        case "Martin VDO Sceptron 10, 1000mm":
            fixture["Fixture"] = "Martin VDO Sceptron 10, 1000mm"
            fixture["DMX Mode"] = "DMX_Pixel"
            fixture["DMX Channels"] = "307"

        case "Mole-Richardson 24kW Molequartz Moleno Molepar": # NOT IMPLEMENTED
            fixture["Fixture"] = "Mole-Richardson 24kW Molequartz Moleno Molepar"
            fixture["DMX Mode"] = "Control"
            fixture["DMX Channels"] = "1"

            fixture["Fixture"] = "Elation DTW Blinder 700 IP"
            fixture["DMX Mode"] = "01CH"
            fixture["DMX Channels"] = "1"

        case "Portman P1 Evo":
            fixture["Fixture"] = "Portman P1 Evo"
            fixture["DMX Mode"] = "Pixel"
            fixture["DMX Channels"] = "42"

        case "Prolight StudioCob PlusFC":
            fixture["Fixture"] = "Prolight StudioCob PlusFC"
            fixture["DMX Mode"] = "6Ch"
            fixture["DMX Channels"] = "6"

        case "Robe HolyPATT": # NOT IMPLEMENTED
            fixture["Fixture"] = "Robe HolyPATT"
            fixture["DMX Mode"] = "Mode 1 - Standard 16 bit"
            fixture["DMX Channels"] = "33"
            
        case "Robe MolyPATT": # NOT IMPLEMENTED
            fixture["Fixture"] = "Robe MolyPATT"
            fixture["DMX Mode"] = "Mode 1 - Standard 16 bit"
            fixture["DMX Channels"] = "33"

        case "Robe Robin BMFL FollowSpot LT":
            fixture["Fixture"] = "Robe Robin BMFL FollowSpot LT"
            fixture["DMX Mode"] = "Mode 1 - Standard 16 bit"
            fixture["DMX Channels"] = "33"

        case "Robe Robin BMFL WashBeam":
            fixture["Fixture"] = "Robe Robin BMFL WashBeam"
            fixture["DMX Mode"] = "Mode 1 - Standard 16 bit"
            fixture["DMX Channels"] = "48"

        case "Robe Robin ColorStrobe":
            fixture["Fixture"] = "Robe Robin ColorStrobe"
            fixture["DMX Mode"] = "Mode 1 - RGBW No zones 8bit"
            fixture["DMX Channels"] = "9"

        case "Robe Robin Esprite":
            fixture["Fixture"] = "Robe Robin Esprite"
            fixture["DMX Mode"] = "Mode 1 - Standard 16 bit"
            fixture["DMX Channels"] = "49"

        case "Robe Robin Forte":
            fixture["Fixture"] = "Robe Robin Forte"
            fixture["DMX Mode"] = "Mode 1 - Standard 16 bit"
            fixture["DMX Channels"] = "54"

        case "Robe Robin LEDBeam 150":
            fixture["Fixture"] = "Robe Robin LEDBeam 150 FW RGBW"
            fixture["DMX Mode"] = "1 - Standard 16-Bit"
            fixture["DMX Channels"] = "22"

        case "Robe Robin LEDBeam 350":
            fixture["Fixture"] = "Robe Robin LEDBeam 350 FW"
            fixture["DMX Mode"] = "1 - Standard 16-Bit"
            fixture["DMX Channels"] = "22"

        case "Robe Robin MegaPointe":
            fixture["Fixture"] = "Robe Robin MegaPointe"
            fixture["DMX Mode"] = "Mode 1 - Standard 16-Bit"
            fixture["DMX Channels"] = "39"

        case "Robe Robin Painte":
            fixture["Fixture"] = "Robe Robin Painte"
            fixture["DMX Mode"] = "Mode 1 - Standard 16-Bit"
            fixture["DMX Channels"] = "44"
            
        case "Robe Robin Spiider":
            fixture["Fixture"] = "Robe Robin Spiider"
            fixture["DMX Mode"] = "Mode 7 - Pixel RGB"
            fixture["DMX Channels"] = "91"
            
        case "Robe Robin Tarrrantula":
            fixture["Fixture"] = "Robe Robin Tarrrantula"
            fixture["DMX Mode"] = "Mode 7 - Pixel RGB"
            fixture["DMX Channels"] = "91"

        case "Varilite VL2600 Profile":
            fixture["Fixture"] = "Varilite VL2600 Profile"
            fixture["DMX Mode"] = "16-Bit 1"
            fixture["DMX Channels"] = "42"

    if fixture == {}: return None
            
    return fixture


def getGDTFFromName(fname):

    path = None
        
    match fname:

        case "Generic RGBAW LED Bulb": path = "Generic@RGBAW_LED_BULB@version_1.3_Round" # NOT IMPLEMENTED

        case "Chauvet Ovation CYC 1 FC": path = "Chauvet_Professional@Ovation_CYC_1_FC@HSV_Mode" 
        case "Chauvet Ovation CYC 3 FC": path = "Chauvet_Professional@Ovation_CYC_1_FC@HSV_Mode" # NOT IMPLEMENTED
        
        case "Clay Paky Sharpy X Frame":  path = "Clay_Paky@Sharpy_X_Frame@1.00" 
        case "Clay Paky Stormy CC":  path = None

        case "Elation DTW Blinder 700 IP": path = "Elation@DTW_BLINDER_700_IP@2023-08-03_First_Release"

        case "ETC Source Four LED Series 2 14 Lustr": path = None

        case "Generic 2-Cell Blinder": path = "Generic@2-lite_Blinder@1.2.4"

        case "GLP Impression FR10 Bar": path = None
        case "GLP Impression X4 Bar 10": path = None
        case "GLP JDC1 Strobe": path = "GLP@JDC-1@FINISHED" # NOT IMPLEMENTED

        case "Martin MAC Aura PXL": path = "Martin_Professional@MAC_Aura_PXL@20230201" 
        case "Martin MAC Aura XB": path = None
        case "Martin MAC Ultra Performance": path = "Martin_Professional@MAC_Ultra_Performance@20230316" 
        case "Martin MAC Viper Performance": path = "Martin_Professional@MAC_Viper_Performance@20230516NoMeas" 
        case "Martin VDO Sceptron 10, 1000mm":  path = "Martin_Professional@VDO_Sceptron_10_1000mm@20201223" 
    
        case "Mole-Richardson 24kW Molequartz Moleno Molepar": path = "Generic@4-lite_Blinder@1.2.4" # NOT IMPLEMENTED

        case "Portman P1 Evo": path = "Portman_Lights@P1_EVO@0.92" 

        case "Prolight StudioCob PlusFC": path = "Prolights@StudioCobPlusFC2_18@Rev_0.3" 

        case "Robe HolyPATT": path = "Robe_Lighting@HolyPATT@2023-09-20__3D_models_update__Thumbnail_added"
        case "Robe MolyPATT": path = "Robe_Lighting@MolyPATT@2023-09-20__3D_models_update__Thumbnail_added"
        case "Robe Robin BMFL FollowSpot LT": path = "Robe_Lighting@Robin_BMFL_FollowSpot_LT@2023-06-21__3D_models_revision"
        case "Robe Robin BMFL WashBeam": path = "Robe_Lighting@Robin_BMFL_WashBeam@2023-06-21__3D_models_revision"
        case "Robe Robin ColorStrobe": path = "Robe_Lighting@Robin_ColorStrobe@2023-07-19__DMX_defaults_update__3D_models_and__Geometry_revision" # TODO: REMOVE
        case "Robe Robin Esprite": path = "Robe_Lighting@Robin_Esprite@2023-07-26__Wiring_object_revision__Animation_wheels_linked" 
        case "Robe Robin Forte": path = "Robe_Lighting@Robin_Forte@2023-06-13__Gobos_and_prism_channel_set_revision" 
        case "Robe Robin LEDBeam 150 FW RGBW": path = "Robe_Lighting@Robin_LEDBeam_150_FW_RGBA@2023-07-04__3D_models_revision" 
        case "Robe Robin LEDBeam 350 FW": path = "Robe_Lighting@Robin_LEDBeam_350_FW@2023-07-10__Wiring_object_revision__3D_objects_revision" 
        case "Robe Robin MegaPointe": path = "Robe_Lighting@Robin_MegaPointe@2023-06-14__3D_models_revision" 
        case "Robe Robin Painte": path = "Robe_Lighting@Robin_Painte@2023-07-18__Beam_output_revision" 
        case "Robe Robin Spiider":  path = "Robe_Lighting@Robin_Spiider@2023-07-21__Pattern_rotation_channel_set_fix" 
        case "Robe Robin Tarrantula": path = "Robe_Lighting@Robin_Tarrantula@2023-07-21__Pattern_rotation_channel_set_fix" 

        case "Varilite VL2600 Profile": path = None

    if path == None: return None
    return f"{path}.gdtf"