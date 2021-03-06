from devicefuncs import *
from airsenseurfuncs import *

# All sensor definitions, both base sensors (AirSensEUR) and derived (virtual) sensors
# Carbon_monoxide = c("co_a4","CO-B4", "CO_MF_200", "CO_MF_20", "COMF200", "CO3E300","co_mf_200"),
# Nitric_oxide = c("no_b4","NOB4_P1_op1","NOB4_P1", "NO_C_25", "NO/C-25","NO3E100"))
# Nitrogen_dioxide = c("no2_b43f","NO2-B43F", "NO2_C_20", "NO2/C-20", "NO23E50"),
# Ozone = c("o3_a431","O3_M-5","O3_M5", "O3-B4", "O33EF1","o3_m_5"),

# Names
# Geonovum1 ASE
# 'COMF200', 'NOB4_P1', 'NO2-B43F' 'O3_M5'
# JustObjects1 ASE
# 'COMF200', 'NOB4_P1', 'NO2-B43F' 'O3_M5'

# ASENL Deploy - 2018
# 'COA4', 'NOB4', 'NO2B43F' 'OX_A341'

# References:
# [1] "Evaluation of low-cost sensors for air pollution monitoring"
# by Spinelle, L., Gerboles, M., Kotsev, A. and Signorini, M. (2017)
# Technical report by the Joint Research Centre (JRC), the European
# Commission's science and knowledge service.
# JRC106095 EUR 28601 EN
#
# [2] https://www.samenmetenaanluchtkwaliteit.nl/sites/default/files/2017-12/Jan%20Vonk_AirSensEUR.pptx.pdf
# Jan Vonk - RIVM

# For now only support for AlphaSense (NO, NO2) and Membrapor (CO, O3) sensors.
SENSOR_DEFS = {
    # 'CO3E300':
    #     {
    #         'label': 'CORaw',
    #         'vendor': 'CityTech',
    #         'meta': 'https://www.thebigredguide.com/docs/fullspec/co3e300.pdf',
    #         'unit': 'unknown',
    #         'meta_id': 'CO3E300',
    #         'converter': convert_none,
    #         'type': int,
    #         'min': 10,
    #         'max': 150000
    #     },
    'COMF200':
        {
            'label': 'CORaw',
            'vendor': 'Membrapor',
            'meta': 'http://www.membrapor.ch/sheet/CO-MF-200.pdf',
            'unit': 'unknown',
            'meta_id': 'COMF200',
            'params': {
                'v_ref': 2,
                'v_ref_ad': 1
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },
    'COA4':
        {
            'label': 'CORaw',
            'vendor': 'AlphaSense',
            'meta': 'http://www.alphasense.com/WEB1213/wp-content/uploads/2017/01/COA4.pdf',
            'unit': 'unknown',
            'meta_id': 'COA4',
            'params': {
                'v_ref': 2,
                'v_ref_ad': 1
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },
    # 'NO3E100':
    #     {
    #         'label': 'NORaw',
    #         'vendor': 'CityTech',
    #         'meta': 'http://www.gassensor.ru/data/files/nitric_oxide/no3e100.pdf',
    #         'unit': 'unknown',
    #         'meta_id': 'NO3E100',
    #         'converter': convert_none,
    #         'type': int,
    #         'min': 10,
    #         'max': 150000
    #     },
    'NOB4_P1':
        {
            'label': 'NORaw',
            'vendor': 'AlphaSense',
            'meta': 'http://www.alphasense.com/WEB1213/wp-content/uploads/2015/03/NOB4_P1.pdf',
            'unit': 'unknown',
            'meta_id': 'NOB4_P1',
            'params': {
                'v_ref': 1.7,
                'v_ref_ad': 1
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },
    'NOB4':
        {
            'label': 'NORaw',
            'vendor': 'AlphaSense',
            'meta': 'http://www.alphasense.com/WEB1213/wp-content/uploads/2015/03/NO-B4.pdf',
            'unit': 'unknown',
            'meta_id': 'NOB4',
            'params': {
                'v_ref': 1.7,
                'v_ref_ad': 1
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },
    # 'NO23E50':
    #     {
    #         'label': 'NO2Raw',
    #         'vendor': 'CityTech',
    #         'meta': 'http://www.gassensor.ru',
    #         'unit': 'unknown',
    #         'meta_id': 'NO23E50',
    #         'converter': convert_none,
    #         'type': int,
    #         'min': 10,
    #         'max': 150000
    #     },
    'NO2B43F':
        {
            'label': 'NO2Raw',
            'vendor': 'AlphaSense',
            'meta': 'http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO2B43F.pdf',
            'unit': 'unknown',
            'meta_id': 'NO2B43F',
            'params': {
                'v_ref': 1.7,
                'v_ref_ad': 0.5
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },
    # 'O33EF1':
    #     {
    #         'label': 'O3Raw',
    #         'vendor': 'CityTech',
    #         'meta': 'http://www.yousensing.com/UploadFiles/20081213232449907.pdf',
    #         'desc': 'must be O3 3E1F',
    #         'unit': 'unknown',
    #         'meta_id': 'O33EF1',
    #         'converter': convert_none,
    #         'type': int,
    #         'min': 10,
    #         'max': 150000
    #     },
    'O3_M5':
        {
            'label': 'O3Raw',
            'vendor': 'Membrapor',
            'meta': 'http://www.diltronic.com/wordpress/wp-content/uploads/O3-M-5.pdf',
            'unit': 'unknown',
            'meta_id': 'O3_M5',
            'params': {
                'v_ref': 1.7,
                'v_ref_ad': 0.5
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },
    'OX_A431':
        {
            'label': 'OX_A431',
            'vendor': 'AlphaSense',
            'meta': 'http://www.alphasense.com/WEB1213/wp-content/uploads/2017/03/OX-A431.pdf',
            'unit': 'unknown',
            'meta_id': 'OX_A431',
            'params': {
                'v_ref': 1.7,
                'v_ref_ad': 0.5
            },
            'converter': convert_none,
            'type': int,
            'min': 0,
            'max': 65535
        },


        'Tempe':
        {
            'label': 'Temperatuur',
            'unit': 'Celsius',
            'min': -25,
            'max': 60
        },
    'Press':
        {
            'label': 'Luchtdruk',
            'unit': 'HectoPascal',
            'min': 200,
            'max': 1100

        },
    'Humid':
        {
            'label': 'Relative Humidity',
            'unit': '%RH',
            'min': 20,
            'max': 100
        },
    'temperature':
        {
            'label': 'Temperatuur',
            'unit': 'Celsius',
            'input': 'Tempe',
            'meta_id': 'ase-Tempe',
            # Is already in Celsius
            'converter': convert_none,
            'type': int,
            'min': -25,
            'max': 70
        },
    'pressure':
        {
            'label': 'Luchtdruk',
            'unit': 'HectoPascal',
            'input': 'Press',
            'meta_id': 'ase-Press',
            # Is already in HectoPascal
            'converter': convert_none,
            'type': int,
            'min': 200,
            'max': 1100
        },
    'humidity':
        {
            'label': 'Luchtvochtigheid',
            'unit': 'Procent',
            'input': 'Humid',
            'meta_id': 'ase-Humid',
            # Is already in percent
            'converter': convert_none,
            'type': int,
            'min': 20,
            'max': 100
        },
    'coraw':
        {
            'label': 'CORaw',
            'unit': 'Millivolt',
            # 'input': ['CO3E300', 'COMF200'],
            'input': ['COA4'],
            'min': 0,
            'max': 5000,
            'converter': bits2millivolt,
        },
    'noraw':
        {
            'label': 'NORaw',
            'unit': 'Millivolt',
            # 'input': ['NO3E100', 'NOB4_P1'],
            'input': ['NOB4'],
            'min': 0,
            'max': 5000,
            'converter': bits2millivolt,
        },
    'no2raw':
        {
            'label': 'NO2Raw',
            'unit': 'Millivolt',
            # 'input': ['NO23E50', 'NO2-B43F'],
            'input': ['NO2B43F'],
            'min': 0,
            'max': 5000,
            'converter': bits2millivolt,
        },
    'o3raw':
        {
            'label': 'O3Raw',
            'unit': 'Millivolt',
            # 'input': ['O33EF1', 'O3_M5'],
            'input': ['OX_A431'],
            'min': 0,
            'max': 5000,
            'converter': bits2millivolt,
        }
}
