# El título definitivo y las palabras clave

Se lee en los Pasos 4 y 7. El título es lo único que leen casi todos los que se
cruzan con el artículo: dice qué se estudió y hace que se encuentre.

## Reglas del título

1. **Refleja lo efectivamente encontrado**, no lo planteado al inicio.
   Si hay mediación, se dice ("el rol mediador de…"). Si una hipótesis se
   rechazó y el título la anunciaba como hallazgo, se corrige: al revisor le
   basta comparar el título con la tabla de resultados.
2. **Nombra la población o el ámbito, no la institución.** "En docentes
   universitarios peruanos", no "en la Universidad Nacional X".
3. **Usa el término que corresponde al diseño** (término unificador de la
   Ficha). *Influencia* o *efecto* solo con modelo direccional declarado;
   *relación* o *asociación* con diseño correlacional.
4. **Sin siglas sin explicar**, salvo las universales del campo.
5. **Sin signos de interrogación, sin dos puntos con frase de efecto**, sin
   juegos de palabras.
6. **Sin palabras vacías al inicio**: "Estudio sobre…", "Análisis de…",
   "Una aproximación a…".
7. **Longitud**: nunca más de `titulo_max_palabras` del perfil (si la guía lo da
   en caracteres, se cuentan caracteres); 12 a 20 palabras suele funcionar.
   Ver cómo titula la revista en su último número: dos puntos, población.
8. **Incluye los términos por los que alguien lo buscaría**, con el nombre
   estándar del constructo en la literatura.

## Estructuras que suelen funcionar

```
[Constructo X] y [constructo Y] en [población]
[Constructo X] y [constructo Y] en [población]: el rol mediador de [M]
```

## Ejemplos

**Débiles y por qué**

- *"Estudio sobre el uso de la inteligencia artificial en estudiantes de la
  Universidad Nacional X, 2026"*: palabra vacía, delimita por institución, no
  dice qué se relaciona con qué. Es un título de tesis.
- *"El impacto de la IA en la educación"*: promete impacto sin diseño causal,
  sin población, demasiado ancho.
- *"¿Influye la IA en el aprendizaje?"*: pregunta, y no dice en quiénes.

**Más sólidos**

- *"Uso de inteligencia artificial generativa y autoeficacia para la escritura
  académica en estudiantes universitarios peruanos"*
- *"Carga laboral y agotamiento emocional en docentes de educación básica: el
  rol mediador del apoyo entre pares"*

(Ejemplos construidos para esta guía; no corresponden a artículos publicados y
no se citan.)

## Cómo trabajarlo con el investigador

Ofrecer **tres versiones** y que elija o ajuste: una centrada en el hallazgo
principal, una que explicite el matiz (mediador, tipo de revisión, periodo) y
una más corta por si la revista limita la longitud. La elegida va con
`--titulo` al armar la `_v7`.

---

# Palabras clave

**Cuántas:** las de `palabras_clave` del perfil (y su tesauro, si lo exige); si
no lo dice, **3 a 5**, en español y en inglés.

- **No repiten palabras del título.** El título ya las indexa; las claves cubren
  lo que no dice: nombre alternativo del constructo, diseño, población, ámbito.
- **Tesauro si el campo lo tiene** (DeCS/MeSH en salud, Tesauro de la UNESCO o
  ERIC en educación). Un descriptor se encuentra; uno inventado, no.
- **Las keywords no son traducción literal**: son los equivalentes que usa la
  literatura en inglés (en salud, el término MeSH).
