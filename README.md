# BBD Behave Python Starter
# Estructura del proyecto
~~~
project/
├── config.ini
├── features/
│   ├── duckduckgo.feature
│   ├── steps/
│   │   └── search_steps.py
│   └── pages/
│       └── duckduckgo_page.py
├── utils/
│   └── driver_utils.py
~~~

# Ejecución
1. Abrir consola y ejecutar:
~~~bash
behave
~~~

# Reportes
1. Tener instalado `allure` en su sistema
2. Abrir consola y ejecutar:

~~~bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
~~~

Lo que hace es ejecutar las pruebas con __Behave__ y luego generar el reporte con __Allure Report__, que luego se abrirá en el navegador.