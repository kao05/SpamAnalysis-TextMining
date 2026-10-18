# Minería de Texto · Respuestas a dudas[cite: 3, 4]

## 4. «Bayes ingenuo es un clasificador lineal» (R1-2, ejercicio 2)[cite: 3]

> Si se toma el logaritmo del cociente $P(\text{spam} \mid m)/P(\text{ham} \mid m)$, la regla de Bayes ingenuo queda como $w \cdot x + b$: una suma ponderada de los conteos de palabras[cite: 3]. Es la misma forma que la regresión logística[cite: 3]. Lo único que cambia entre los dos modelos es cómo se obtienen los pesos[cite: 3].

**Analogía.** Dos cocineros siguen el mismo formato de receta: «tantos gramos de cada ingrediente»[cite: 3]. Uno decide las cantidades leyendo las de cada ingrediente por separado (Bayes ingenuo cuenta palabras clase por clase); el otro las ajusta probando el platillo completo hasta que sabe bien (la regresión logística optimiza todos los pesos a la vez para predecir la clase)[cite: 3].

### Procedimiento[cite: 3]
Sea $x$ el vector de conteos del mensaje $m$ ($x_j$ = número de veces que aparece la palabra $j$) y $\theta_{j,c} = P(\text{palabra } j \mid \text{clase } c)$[cite: 3]. Por el teorema de Bayes y la hipótesis de independencia:[cite: 3]

$$P(c \mid m) \propto P(c) \cdot \prod_j \theta_{j,c}^{x_j}$$[cite: 3]

Al dividir la expresión de spam entre la de ham, el denominador $P(m)$ se cancela[cite: 3]. Tomando logaritmo natural:[cite: 3]

$$\ln [P(\text{spam} \mid m)/P(\text{ham} \mid m)] = \ln [P(\text{spam})/P(\text{ham})] + \sum_j x_j \cdot \ln (\theta_{j,\text{spam}} / \theta_{j,\text{ham}})$$[cite: 3]

Esto es exactamente $z = w \cdot x + b$, con:[cite: 3]

$$w_j = \ln (\theta_{j,\text{spam}} / \theta_{j,\text{ham}}) \quad \text{y} \quad b = \ln [P(\text{spam})/P(\text{ham})]$$[cite: 3]

Como $P(\text{spam} \mid m) + P(\text{ham} \mid m) = 1$, al despejar se obtiene $P(\text{spam} \mid m) = \sigma(z) = 1/(1 + \exp(-z))$, la misma función sigmoide de la regresión logística[cite: 3]. La frontera de decisión $z = 0$ es un hiperplano en el espacio de los conteos; por eso el clasificador es lineal[cite: 3].

### Con los datos del ejercicio 1[cite: 3]
Con suavizado de Laplace ($V = 4$, total de palabras por clase $= 6$, denominador $6 + 4 = 10$)[cite: 3]:

**Tabla 2.** Pesos de Bayes ingenuo vistos como clasificador lineal[cite: 3].

| Palabra | $\theta$ spam | $\theta$ ham | $w_j = \ln(\theta_{\text{spam}} / \theta_{\text{ham}})$ |
| :--- | :---: | :---: | :---: |
| gratis | 4/10 | 1/10 | $\ln 4 \approx +1.386$ |
| premio | 3/10 | 1/10 | $\ln 3 \approx +1.099$ |
| hola | 2/10 | 4/10 | $\ln 0.5 = -0.693$ |
| mañana | 1/10 | 4/10 | $\ln 0.25 = -1.386$ |

Con priors iguales, $b = \ln 1 = 0$[cite: 3]. Para $m = \text{«gratis hola premio»}$, $x = (1, 1, 1, 0)$ y[cite: 3]:

$$z = 1.386 - 0.693 + 1.099 = 1.792, \quad \sigma(1.792) \approx 0.857$$[cite: 3]

Es el mismo 0.857 que da el ejercicio 1 por el camino directo[cite: 3]. Los pesos se leen fácilmente: las palabras con peso positivo empujan hacia spam y las de peso negativo hacia ham[cite: 3].

**Qué se busca que el equipo concluya.** Bayes ingenuo y regresión logística producen el mismo tipo de frontera[cite: 3]. La diferencia está en cómo se estiman los pesos: Bayes ingenuo los obtiene de conteos por clase, en una sola pasada y sin optimizar, lo que funciona bien con pocos datos[cite: 3]. La regresión logística los obtiene maximizando directamente $P(\text{clase} \mid \text{mensaje})$, lo que suele dar mejores resultados con datos abundantes y atributos correlacionados[cite: 4]. Es la comparación que hace el problema en la Etapa 2[cite: 4].

---

## 5. «Umbral y costos» (R1-2, ejercicio 3)[cite: 4]

> Si mandar a spam un mensaje legítimo cuesta 10 veces más que dejar pasar un spam, conviene marcar como spam sólo cuando $P(\text{spam} \mid m) > 10/11 \approx 0.909$, y no a partir de 0.5 como se hace por defecto[cite: 4].

**Analogía.** En un juicio penal se exige una prueba «más allá de toda duda razonable», no un 51 % de certeza, porque condenar a un inocente se considera mucho más grave que absolver a un culpable[cite: 4]. Aquí el inocente es el mensaje legítimo que termina en la carpeta de spam y nadie lee[cite: 4].

### Procedimiento[cite: 4]
Sea $p = P(\text{spam} \mid m)$[cite: 4]. Hay dos decisiones posibles y cada una tiene un costo esperado[cite: 4]:
* **Marcar como spam:** sólo hay error si el mensaje era legítimo[cite: 4]. Costo esperado $= (1 - p) \cdot 10$[cite: 4].
* **Dejar pasar:** sólo hay error si el mensaje era spam[cite: 4]. Costo esperado $= p \cdot 1$[cite: 4].

Conviene marcar como spam cuando su costo esperado es menor[cite: 4]:

$$10(1 - p) < p \iff p > 10/11 \approx 0.909$$[cite: 4]

En general, con costo $C_{FP}$ por falso positivo y $C_{FN}$ por falso negativo, el umbral óptimo es $t = C_{FP} / (C_{FP} + C_{FN})$[cite: 4]. Con costos iguales, $t = 0.5$[cite: 4]. En términos del puntaje lineal de la respuesta 4, el umbral equivale a $z > \ln 10 \approx 2.303$[cite: 4].

**Consecuencia en el ejemplo.** El mensaje «gratis hola premio» tiene $P(\text{spam} \mid m) \approx 0.857$[cite: 4]. Con el umbral de 0.5 se marca como spam, pero con el umbral de 0.909 **se deja pasar**[cite: 4]. El modelo no cambió; sólo cambió la decisión que se toma con su probabilidad[cite: 4].

En la Etapa 3, el equipo aplica este umbral en lugar de 0.5 y reporta cómo cambian la precisión y la exhaustividad de la clase spam: la precisión debería subir y la exhaustividad bajar[cite: 4].

---

## 6. «Una matriz de confusión inventada por el equipo» (R1-2, ejercicio 4)[cite: 4]

> Se refiere a una matriz **hipotética**, construida por el equipo, con la proporción de spam del corpus (13 %), para razonar sobre las métricas antes de tener resultados reales[cite: 4]. La palabra «inventada» es poco clara; abajo se propone otra redacción[cite: 4].

El ejercicio pide imaginar un clasificador sobre 1,000 mensajes, de los cuales 130 son spam y 870 son legítimos, y llenar las cuatro celdas con valores plausibles[cite: 4]. Con eso se muestra que la exactitud puede ser alta aunque el clasificador sea inútil[cite: 4]. La comparación más ilustrativa es entre dos clasificadores[cite: 4]:

**Tabla 3.** Dos clasificadores hipotéticos sobre 1,000 mensajes con 13 % de spam[cite: 4].

| Métricas / Celdas | Clasificador A: «todo es legítimo» | Clasificador B: razonable |
| :--- | :---: | :---: |
| **VP · FN · FP · VN** | 0 · 130 · 0 · 870 | 100 · 30 · 20 · 850 |
| **Exactitud** | 0.87 | 0.95 |
| **Precisión (spam)** | indefinida (0/0) | 100/120 = 0.83 |
| **Exhaustividad (spam)** | 0 | 100/130 ≈ 0.77 |
| **F1 (spam)** | 0 | 0.80 |

El clasificador A tiene 87 % de exactitud sin detectar un solo spam[cite: 5]. La exactitud premia acertar la clase mayoritaria; la precisión, la exhaustividad y F1 de la clase spam miden lo que realmente interesa[cite: 5].

### Redacción sugerida para el documento de problemas[cite: 5]

| Campo | Contenido |
| :--- | :--- |
| **Problema** | R1-2, ejercicio 4[cite: 5] |
| **Dice** | Dada una matriz de confusión inventada por el equipo con 13 % de spam, calcular...[cite: 5] |
| **Debería decir** | Construir una matriz de confusión hipotética para 1,000 mensajes, de los cuales 130 son spam, para dos clasificadores: uno que declara todos los mensajes legítimos y otro con valores plausibles elegidos por el equipo. Calcular para ambos la exactitud y la precisión, exhaustividad y F1 de la clase spam, y explicar por qué la exactitud es engañosa en este problema.[cite: 5] |