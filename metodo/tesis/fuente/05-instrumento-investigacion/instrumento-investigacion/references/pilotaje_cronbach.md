# Pilotaje y alfa de Cronbach

## Importante: frontera con la Skill 7

La Skill 5 (Instrumento) **NO ejecuta el cálculo de alfa de Cronbach** con datos reales. Su trabajo es:

- Describir el procedimiento del pilotaje.
- Generar plantillas (instrucciones, hoja de registro).
- Describir la fórmula y umbrales del Cronbach.
- Indicar software referencial (SPSS, R, JASP).

El cálculo REAL del Cronbach se ejecuta en la **Skill de Análisis de Datos** (Capítulo VII del método), cuando el tesista ya tiene los datos del pilotaje y/o del estudio.

## Qué es el pilotaje

Aplicación previa del instrumento a un grupo pequeño con perfil similar al de la muestra real, antes del trabajo de campo definitivo. Permite detectar problemas que solo aparecen en la práctica.

## Características del pilotaje

| Aspecto | Recomendación |
|---------|---------------|
| Tamaño | 15 a 30 personas |
| Perfil | Similar a la muestra real |
| Origen | NO de la muestra real (esas quedan intactas para el campo) |
| Modalidad | Idéntica a la final (presencial/virtual) |
| Duración registrada | Sí, anotar cuánto tarda cada participante |
| Observaciones | Sí, anotar dudas, ítems en blanco, etc. |

## Instrucciones del pilotaje (plantilla)

> El pilotaje del instrumento se aplicará a un grupo de [15-30] [participantes con perfil similar al de la muestra real, pero no parte de ella]. La modalidad será [presencial/virtual con Google Forms], idéntica a la prevista para el trabajo de campo definitivo. Durante la aplicación se registrará:
>
> - Tiempo total de respuesta de cada participante.
> - Ítems que generaron dudas o solicitud de aclaración.
> - Ítems que el participante dejó en blanco.
> - Comentarios cualitativos sobre la experiencia.
>
> Los datos del pilotaje se utilizarán exclusivamente para calcular la confiabilidad (alfa de Cronbach) y para identificar ítems problemáticos que requieran ajuste. **Los datos del pilotaje no se incluyen en el análisis final de la tesis**.

## Hoja de registro de observaciones (plantilla)

| Participante | Tiempo (min) | Ítems con dudas | Ítems en blanco | Comentarios |
|--------------|--------------|-----------------|------------------|-------------|
| P01 | | | | |
| P02 | | | | |
| ... | | | | |

## Alfa de Cronbach

Coeficiente que mide la consistencia interna de un instrumento con escala Likert. Va de 0 a 1. Propuesto por Cronbach en 1951. En el texto guardado se cita con la clave de esa fuente; si no está en la biblioteca del tesista, se busca con `buscar_fuentes` o se añade con su permiso, y mientras no tenga clave la afirmación va con `[FALTA FUENTE]`.

### Fórmula

```
       k    /         Σ σ²i  \
α = ─────── ·  1  -  ────────
     k - 1   \         σ²t   /
```

Donde:
- k = número de ítems del instrumento (o de la dimensión).
- σ²i = varianza de cada ítem.
- σ²t = varianza total del instrumento (o dimensión).

### Valores de referencia (Hernández-Sampieri y Mendoza, 2018; Ñaupas Paitán et al., 2019)

| Valor de α | Interpretación |
|------------|----------------|
| α ≥ 0.90 | Excelente |
| 0.80 ≤ α < 0.90 | Bueno |
| 0.70 ≤ α < 0.80 | Aceptable (mínimo para pregrado) |
| 0.60 ≤ α < 0.70 | Cuestionable |
| α < 0.60 | Inaceptable |

### Cuándo se calcula

- **En el pilotaje**: con los 15-30 datos del piloto, para validar el instrumento antes del campo grande.
- **En el estudio real**: con los datos finales, para reportar la confiabilidad efectiva del instrumento aplicado.

### Si Cronbach < 0.70

No es señal de catástrofe. Es señal de carpintería. Pasos:

1. Identificar los ítems con menor correlación con el total (item-total correlation).
2. Reformular o eliminar esos ítems.
3. Volver a calcular Cronbach con los ítems restantes.
4. Si sigue bajo, revisar el constructo: puede ser que los ítems estén midiendo más de una dimensión.

### Software referencial

- **SPSS**: módulo de fiabilidad → escala → análisis de fiabilidad.
- **R**: paquete `psych`, función `alpha()`.
- **JASP**: módulo de fiabilidad, gratuito.

## Test-retest

Aplicar el mismo instrumento dos veces a las mismas personas con intervalo de 2-4 semanas. Si correlaciona alto, hay confiabilidad temporal. Más exigente operativamente y poco frecuente en pregrado.

## KR-20 / KR-21

Para instrumentos con respuestas dicotómicas (sí/no, correcto/incorrecto). Funciona como Cronbach pero adaptado a ítems binarios. Rara vez aplica a Likert.

## Cómo lo dice el capítulo

La sub-sección 5.4.3 del capítulo que guarda la Skill 5 incluye lo siguiente (en el texto guardado, las citas van con la clave de cada fuente, no escritas a mano):

> El cálculo del coeficiente alfa de Cronbach con los datos del pilotaje se realizará mediante software estadístico, considerando como opciones SPSS, R con RStudio o JASP. Los valores de referencia para interpretar la confiabilidad, según Hernández-Sampieri y Mendoza [AR…:n] y Ñaupas Paitán et al. [AR…:n], son los siguientes: alfa mayor o igual a 0.90 indica excelente consistencia interna; entre 0.80 y 0.90, buena; entre 0.70 y 0.80, aceptable (mínimo recomendado para pregrado); entre 0.60 y 0.70, cuestionable; y menor a 0.60, inaceptable.
>
> Si el coeficiente alfa de Cronbach obtenido en el pilotaje resulta inferior a 0.70, se procederá a identificar los ítems con menor correlación con el total y a reformularlos o eliminarlos, antes de proceder al trabajo de campo definitivo.
>
> La ejecución detallada del cálculo de confiabilidad con los datos reales del pilotaje se desarrollará en el capítulo de análisis de datos.

`[AR…]` representa la clave real que devuelva `buscar_fuentes` o `mis_fuentes`; nunca se deja así ni se inventa. Como el capítulo del instrumento es de cuadros (ver «Estructura del capítulo» en el SKILL.md), este texto va como nota breve del cuadro de confiabilidad o se usa en el chat, y la mención a la Skill de Análisis se le dice al tesista, no se escribe en el capítulo.
