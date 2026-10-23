# Las herramientas de análisis: cuándo sirven y cuándo son relleno

Un FODA de cuatro cuadros con tres viñetas genéricas cada uno no analiza nada, y quien lee el
informe lo sabe. Estas herramientas sirven **cuando se llenan con los datos del informe** y
cuando su resultado cambia lo que se recomienda.

## La prueba de las tres preguntas

Antes de meter cualquier herramienta en el informe:

1. **¿Cada casilla se llena con evidencia de este informe?** Si hay que inventar para llenar
   un cuadro, la herramienta no aplica.
2. **¿El resultado cambia alguna recomendación?** Si el informe diría lo mismo sin ella, se
   quita.
3. **¿La pidieron?** Si los términos de referencia piden un FODA, va, aunque salga flojo. Y
   entonces se llena solo con lo que hay y las casillas vacías se dicen vacías.

Si falla la 1 y la 2 y no se cumple la 3, **fuera**. Es mejor un informe con un análisis bueno
que con cuatro decorativos.

## Cuál usar para qué

| Pregunta que hay que responder | Herramienta |
|---|---|
| ¿Por qué pasa esto? | Ishikawa, cinco por qués, árbol de problemas |
| ¿Dónde se pierde valor en el proceso? | Cadena de valor, mapa de proceso, análisis de cuellos de botella |
| ¿Qué pocas causas explican la mayoría del problema? | Pareto |
| ¿Qué tan atractivo es este sector para entrar? | Cinco fuerzas de Porter |
| ¿Qué de afuera nos va a afectar? | PESTEL |
| ¿Qué hacemos con lo que somos y lo que hay afuera? | FODA, y solo si sale de un análisis previo |
| ¿A quién le vendemos y qué valora? | Segmentación, mapa de valor |
| ¿Cómo estamos frente a los demás? | Comparación con referencias del sector (*benchmark*) |
| ¿Qué puede salir mal? | Matriz de riesgos: probabilidad por impacto |
| ¿Qué hacemos primero? | Matriz de impacto y esfuerzo |

## Las cinco que más se usan, bien hechas

### Ishikawa (espina de pescado)

Para **causas de un problema concreto**, no de «la situación de la empresa». El problema va
en la cabeza, con su cifra. Las espinas clásicas en servicios son personas, proceso, sistemas,
insumos, entorno y medición.

Regla: **cada causa que se pone tiene que tener al lado el dato que la sostiene**, o ir
marcada como hipótesis. Un Ishikawa de veinte causas sin dato es una lluvia de ideas, no un
análisis. Cinco causas con evidencia valen más.

### Cinco por qués

Para un problema con **una cadena causal clara**, sobre todo en un incidente. Se para cuando
se llega a algo que la empresa puede cambiar.

```
Las entregas llegan tarde.
  ¿Por qué? El despacho sale después de las 14:00.
  ¿Por qué? El picking termina a la 13:40.
  ¿Por qué? Las órdenes del sistema se descargan a las 11:00.
  ¿Por qué? La descarga es manual y la hace una sola persona, que atiende mostrador.
  ← Aquí se para: esto se puede cambiar.
```

Si la cadena llega a «porque el mercado es así», la pregunta estaba mal planteada.

### Pareto

Para **priorizar** cuando hay muchas causas o muchos elementos. Exige datos: no se puede decir
que el 20 % de los clientes da el 80 % de las ventas sin la lista de ventas por cliente. El
cálculo va por `trabajar_en_r`, y si los datos no están, el Pareto no entra.

### Cinco fuerzas

Para **entrar a un sector o salir de él**: es de la Fase 3 de un estudio de factibilidad o de
mercado, no de un diagnóstico interno. Cada fuerza se califica y **se dice con qué dato**:
número de competidores, concentración, costo de cambiar de proveedor, existencia de
sustitutos. Cinco fuerzas sin un dato de mercado es un ensayo.

No sirve para: un informe de gestión, un incidente, un informe técnico.

### FODA

El más usado y el peor usado. Tres reglas:

- **Va al final del análisis, no al principio.** Sus casillas se llenan con los hallazgos que
  ya están en el informe, cada uno con su cifra. Si el FODA trae algo que no está en el
  informe, o el FODA está mal o falta una sección.
- **Fortaleza y debilidad son de la empresa; oportunidad y amenaza son de afuera.** «Falta de
  capacitación» es debilidad, no amenaza.
- **Termina en cruces**, que es lo único que produce decisiones: qué fortaleza aprovecha qué
  oportunidad, y qué debilidad hay que cerrar frente a qué amenaza. Un FODA sin cruces no
  llega a ninguna recomendación.

| Mal (genérico) | Bien (con evidencia) |
|---|---|
| Debilidad: «falta de tecnología» | Debilidad: «el inventario se lleva en hoja de cálculo; la última toma física fue en 2024» |
| Amenaza: «competencia creciente» | Amenaza: «dos operadores nuevos en la ruta Lima-Trujillo desde 2025, con tarifas 8 % menores [AR…]» |

## Matriz de riesgos

Para la Fase 4, cuando se recomienda algo. Probabilidad (alta, media, baja) por impacto
(alto, medio, bajo), y **cada riesgo con su mitigación y su responsable**. Un riesgo sin
mitigación es una advertencia, no un análisis.

## Cómo va en el Word

Estas herramientas salen como **tabla**, no como dibujo, salvo que él tenga la imagen hecha y
la vaya a pegar. Un Ishikawa se puede presentar como tabla de causa y evidencia por categoría,
y se entiende igual.

Si tiene el diagrama hecho, va como figura con su marca:

```
**Figura 3**
*Diagrama de causas del retraso en el despacho*
[Insertar aquí la Figura 3: ishikawa-despacho.png]
*Nota.* Elaboración propia con los registros de despacho de enero a marzo de 2026.
```

## Lo que no se hace

- **No se aplican dos herramientas a lo mismo** para llenar páginas. Si el Ishikawa ya explicó
  las causas, el árbol de problemas sobra.
- **No se inventa el contenido de una casilla** porque el cuadro quede desparejo. Se dice:
  «no se identificaron amenazas relevantes con la información disponible».
- **No se usa una herramienta que él no pueda defender.** Si no sabe qué es una cadena de
  valor y quien lo lee le va a preguntar, se elige otra o se le explica antes.
