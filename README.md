# Algoritmo de Segmentación de Imágenes Satelitales para Identificación de Regiones Construidas en Zonas Rurales 🌍

## Descripción del Proyecto 📜

Este proyecto se centra en el desarrollo de un algoritmo que segmenta imágenes satelitales para identificar las regiones construidas en zonas rurales. El objetivo principal es facilitar el diseño e instalación de redes comunitarias, optimizando la localización de las antenas para asegurar una distribución adecuada de la red. Este enfoque contribuye a reducir costos y tiempos de ejecución en futuros proyectos.

## Objetivo 🎯

Desarrollar un algoritmo que permita segmentar imágenes satelitales para identificar de manera eficiente las zonas construidas en áreas rurales, facilitando el diseño e instalación de redes comunitarias.

## Algoritmo 🤖

El algoritmo fue diseñado utilizando bibliotecas de Python como **scikit-image** y **OpenCV** para el procesamiento de imágenes. Se utilizaron imágenes de **Google Earth** con un GSD de 50 cm debido a su alta resolución y accesibilidad.

### Procesamiento de Imágenes 🖼️

El primer paso consiste en aplicar un algoritmo de segmentación de regiones para obtener una imagen con las posibles zonas construidas. Esto permite aplicar un geo-proceso de vectorización que proporciona las coordenadas precisas de las edificaciones.

#### Imagen de Procesamiento de Imágenes
![Imagen de Procesamiento](https://github.com/JHONATAN9A/Imagenes-Satelitales/blob/main/img_c.png)

### Vectorización y Geo-Proceso 🌍

Después de la segmentación, se aplica un proceso de vectorización para obtener las coordenadas de las edificaciones, lo que es esencial para determinar los puntos óptimos para la instalación de antenas.

#### Imagen de Resultados de la Vectorización
![Imagen de Vectorización](https://github.com/JHONATAN9A/Imagenes-Satelitales/blob/main/img_b.png)

### Evaluación del Algoritmo 📊

Para evaluar la precisión del algoritmo, se utilizaron la **matriz de confusión** y el **índice de Kappa**, lo que permite cuantificar la fiabilidad de la identificación de las zonas construidas.

#### Imagen de Evaluación del Algoritmo
![Imagen de Evaluación](https://github.com/JHONATAN9A/Imagenes-Satelitales/blob/main/img_a.png)
