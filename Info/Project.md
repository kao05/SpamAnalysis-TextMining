# Minería de Texto · Problemas del Segundo Parcial

## R1-2. Filtro de spam en SMS: Bayes ingenuo frente a máxima entropía

| Tópico | Clasificación probabilística binaria con clases desbalanceadas. |
| :--- | :--- |
| **Conceptos de las Notas** | Inferencia bayesiana; regresión logística; principio de máxima entropía; BOW y TF-IDF. |
| **Corpus** | SMS Spam Collection (UCI; 5,574 mensajes en inglés, ≈13 % spam): [https://archive.ics.uci.edu/dataset/228/sms+spam+collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). |

### Objetivo

Comparar un modelo generativo (Bayes ingenuo) con uno discriminativo (regresión logística, equivalente a un modelo de máxima entropía) en un problema desbalanceado, y decidir el umbral de clasificación en función del costo de los errores.

---

### Trabajo en clase (en papel)

1. **Bayes ingenuo a mano.** Con $P(\text{spam}) = P(\text{ham}) = 1/2$ y los conteos spam: gratis 3, premio 2, hola 1, mañana 0; ham: gratis 0, premio 0, hola 3, mañana 3, calcular con suavizado de Laplace $P(\text{spam} \mid \text{«gratis hola premio»})$.
2. **Bayes ingenuo es un clasificador lineal.** Escribir $\log[P(\text{spam} \mid m)/P(\text{ham} \mid m)]$ como $w \cdot x + b$, donde $x$ es el vector de conteos del mensaje. Obtener los pesos $w$ a partir de los conteos del ejercicio anterior y compararlos con la forma de la regresión logística.
3. **Umbral y costos.** Si clasificar como spam un mensaje legítimo cuesta 10 veces más que dejar pasar un spam, deducir el umbral sobre $P(\text{spam} \mid m)$ que minimiza el costo esperado.
4. **Métricas en un problema desbalanceado.** Construir una matriz de confusión hipotética para 1,000 mensajes, de los cuales 130 son spam, para dos clasificadores: uno que declara todos los mensajes legítimos y otro con valores plausibles elegidos por el equipo. Calcular para ambos la exactitud y la precisión, exhaustividad y F1 de la clase spam, y explicar por qué la exactitud es engañosa en este problema.

---

### Trabajo experimental (programación en Colab)

* **Etapa 1 · Análisis, representación y baseline.** Explorar el corpus (longitudes, desbalance, vocabulario característico), tokenizar y separar Train, Dev y Test de forma estratificada. Baseline: bolsa de palabras + Bayes ingenuo multinomial.
* **Etapa 2 · Primera aproximación.** TF-IDF + regresión logística con regularización L2; comparar ambos modelos y estudiar el efecto del umbral de decisión.
* **Etapa 3 · Mejora.** Añadir atributos (longitud, número de dígitos, URLs, proporción de mayúsculas) y ajustar el umbral según el análisis de costos hecho en clase.
* **Experimento control.** Las palabras con mayor log-razón $P(w \mid \text{spam})/P(w \mid \text{ham})$ deben ser interpretables; al entrenar con las etiquetas permutadas al azar, el desempeño debe caer al nivel del azar.
* **Métricas.** F1 de la clase spam, precisión, exhaustividad y AUC-ROC.

---

### Estrategia de trabajo en equipo

* **Debate generativo vs. discriminativo.** Antes de programar la Etapa 2, dos integrantes preparan el argumento a favor de cada modelo y el tercero actúa como moderador y redacta la conclusión. En la Etapa 3 los papeles rotan.
* **Revisión cruzada del código.** Quien implementa un modelo no es quien lo revisa: el revisor debe poder explicar cada línea del cuaderno al equipo antes de que se acepte.
* **Puente papel–código.** Quien resolvió a mano el ejercicio de los pesos lineales verifica, junto con otro integrante, que los coeficientes que produce el código para un vocabulario de juguete coinciden con los calculados en papel.