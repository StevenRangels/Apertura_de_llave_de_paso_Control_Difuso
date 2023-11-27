import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variables de entrada.
humedad_suelo = ctrl.Antecedent(np.arange(0, 101, 1), 'Humedad del Suelo')
temperatura_ambiente = ctrl.Antecedent(np.arange(0, 31, 1), 'Temperatura del Ambiente')

# Variable de salida.
apertura_llave_paso = ctrl.Consequent(np.arange(0, 101, 1), 'Apertura de la Llave de Paso')

# Funciones de membresía para la humedad del suelo
humedad_suelo['muy_seco'] = fuzz.trimf(humedad_suelo.universe, [0, 0, 30])
humedad_suelo['seco'] = fuzz.trimf(humedad_suelo.universe, [20, 30, 40])
humedad_suelo['optimo'] = fuzz.trimf(humedad_suelo.universe, [30, 50, 70])
humedad_suelo['humedo'] = fuzz.trimf(humedad_suelo.universe, [60, 70, 80])
humedad_suelo['muy_humedo'] = fuzz.trimf(humedad_suelo.universe, [ 70, 100, 100])

# Funciones de membresía para la temperatura del ambiente.
temperatura_ambiente['muy_frio'] = fuzz.trimf(temperatura_ambiente.universe, [0, 0, 7])
temperatura_ambiente['frio'] = fuzz.trimf(temperatura_ambiente.universe, [5, 8, 12])
temperatura_ambiente['templado'] = fuzz.trimf(temperatura_ambiente.universe, [10, 15, 20])
temperatura_ambiente['calido'] = fuzz.trimf(temperatura_ambiente.universe, [18, 23, 28]) 
temperatura_ambiente['muy_calido'] = fuzz.trimf(temperatura_ambiente.universe, [26, 30, 30])

# Funciones de membresía para la apertura de la llave de paso.
apertura_llave_paso['cerrada'] = fuzz.trimf(apertura_llave_paso.universe, [0, 0, 14])
apertura_llave_paso['parcialmente_abierta'] = fuzz.trimf(apertura_llave_paso.universe, [10, 25, 40])
apertura_llave_paso['abierta'] = fuzz.trimf(apertura_llave_paso.universe, [35, 50, 65])
apertura_llave_paso['muy_abierta'] = fuzz.trimf(apertura_llave_paso.universe, [60, 75, 90])
apertura_llave_paso['totalmente_abierta'] = fuzz.trimf(apertura_llave_paso.universe, [80, 100, 100])

# Reglas difusas.
regla1 = ctrl.Rule(humedad_suelo['muy_seco'] & temperatura_ambiente['muy_frio'],apertura_llave_paso['parcialmente_abierta'])
regla2 = ctrl.Rule(humedad_suelo['muy_seco'] & temperatura_ambiente['frio'],apertura_llave_paso['parcialmente_abierta'])
regla3 = ctrl.Rule(humedad_suelo['muy_seco'] & temperatura_ambiente['templado'],apertura_llave_paso['abierta'])
regla4 = ctrl.Rule(humedad_suelo['muy_seco'] & temperatura_ambiente['calido'],apertura_llave_paso['muy_abierta'])
regla5 = ctrl.Rule(humedad_suelo['muy_seco'] & temperatura_ambiente['muy_calido'],apertura_llave_paso['totalmente_abierta'])

regla6 = ctrl.Rule(humedad_suelo['seco'] & temperatura_ambiente['muy_frio'],apertura_llave_paso['parcialmente_abierta'])
regla7 = ctrl.Rule(humedad_suelo['seco'] & temperatura_ambiente['frio'],apertura_llave_paso['parcialmente_abierta'])
regla8 = ctrl.Rule(humedad_suelo['seco'] & temperatura_ambiente['templado'],apertura_llave_paso['abierta'])
regla9 = ctrl.Rule(humedad_suelo['seco'] & temperatura_ambiente['calido'],apertura_llave_paso['abierta'])
regla10 = ctrl.Rule(humedad_suelo['seco'] & temperatura_ambiente['muy_calido'],apertura_llave_paso['abierta'])

regla11 = ctrl.Rule(humedad_suelo['optimo'] & temperatura_ambiente['muy_frio'],apertura_llave_paso['cerrada'])
regla12 = ctrl.Rule(humedad_suelo['optimo'] & temperatura_ambiente['frio'],apertura_llave_paso['cerrada'])
regla13 = ctrl.Rule(humedad_suelo['optimo'] & temperatura_ambiente['templado'],apertura_llave_paso['cerrada'])
regla14 = ctrl.Rule(humedad_suelo['optimo'] & temperatura_ambiente['calido'],apertura_llave_paso['cerrada'])
regla15 = ctrl.Rule(humedad_suelo['optimo'] & temperatura_ambiente['muy_calido'],apertura_llave_paso['cerrada'])

regla16 = ctrl.Rule(humedad_suelo['humedo'] & temperatura_ambiente['muy_frio'],apertura_llave_paso['cerrada'])
regla17 = ctrl.Rule(humedad_suelo['humedo'] & temperatura_ambiente['frio'],apertura_llave_paso['cerrada'])
regla18 = ctrl.Rule(humedad_suelo['humedo'] & temperatura_ambiente['templado'],apertura_llave_paso['cerrada'])
regla19 = ctrl.Rule(humedad_suelo['humedo'] & temperatura_ambiente['calido'],apertura_llave_paso['cerrada'])
regla20 = ctrl.Rule(humedad_suelo['humedo'] & temperatura_ambiente['muy_calido'],apertura_llave_paso['cerrada'])

regla21 = ctrl.Rule(humedad_suelo['muy_humedo'] & temperatura_ambiente['muy_frio'],apertura_llave_paso['cerrada'])
regla22 = ctrl.Rule(humedad_suelo['muy_humedo'] & temperatura_ambiente['frio'],apertura_llave_paso['cerrada'])
regla23 = ctrl.Rule(humedad_suelo['muy_humedo'] & temperatura_ambiente['templado'],apertura_llave_paso['cerrada'])
regla24 = ctrl.Rule(humedad_suelo['muy_humedo'] & temperatura_ambiente['calido'],apertura_llave_paso['cerrada'])
regla25 = ctrl.Rule(humedad_suelo['muy_humedo'] & temperatura_ambiente['muy_calido'],apertura_llave_paso['cerrada'])

# Sistema de control.
sistema_control = ctrl.ControlSystem(
    [
    regla1,
    regla2, 
    regla3, 
    regla4, 
    regla5, 
    regla6, 
    regla7, 
    regla8, 
    regla9, 
    regla10,
    regla11,
    regla12, 
    regla13,
    regla14, 
    regla15,
    regla16, 
    regla17, 
    regla18, 
    regla19,
    regla20, 
    regla21, 
    regla22, 
    regla23, 
    regla24, 
    regla25
    ]
    )

# Asocia el sistema de control con las variables de entrada y salida.
riego = ctrl.ControlSystemSimulation(sistema_control)

riego.input['Humedad del Suelo'] = 50
riego.input['Temperatura del Ambiente'] = 25

riego.compute()

print("Apertura de la Llave de Paso:", riego.output['Apertura de la Llave de Paso'])

# Visualización de las funciones de membresía.
temperatura_ambiente.view()
humedad_suelo.view()
apertura_llave_paso.view()
plt.show()