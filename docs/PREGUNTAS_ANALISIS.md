# Respuestas a las 12 preguntas de análisis

**Proyecto:** TaskManager — TechSolutions

1. **¿Qué ventajas ofrece utilizar GitHub Projects para organizar un proyecto de software?** Permite visualizar las tareas por estado, asignar responsables, establecer prioridades y conocer los avances del equipo en un solo lugar.
2. **¿Cuál es la diferencia entre Git y GitHub?** Git es la herramienta que guarda versiones del código; GitHub es una plataforma en línea para alojar repositorios y colaborar mediante Issues, Pull Requests y Actions.
3. **¿Por qué es importante utilizar ramas durante el desarrollo?** Porque permiten trabajar en nuevas funciones sin afectar inmediatamente la versión principal y facilitan revisar los cambios antes de integrarlos.
4. **¿Qué función cumple un Pull Request?** Presenta los cambios de una rama para que otras personas los revisen, comenten, prueben y aprueben antes de fusionarlos.
5. **¿Qué problemas permite detectar la integración continua?** Errores de programación, fallas de pruebas, dependencias incorrectas y problemas de integración entre cambios.
6. **¿Cuál es la diferencia entre integración continua y entrega continua?** La integración continua comprueba los cambios automáticamente; la entrega continua deja preparada una versión comprobada para publicarla.
7. **¿Qué diferencia existe entre entrega continua y despliegue continuo?** En la entrega continua la publicación puede requerir una aprobación manual; en el despliegue continuo los cambios aprobados se publican automáticamente.
8. **¿Por qué es importante automatizar las pruebas?** Porque se ejecutan de manera repetible, ahorran tiempo y ayudan a detectar errores antes de que lleguen a los usuarios.
9. **¿Qué sucede si se integra código que contiene errores?** Puede fallar la aplicación, perderse información o romperse funciones existentes; por eso conviene revisar el código y ejecutar pruebas antes de fusionarlo.
10. **¿Por qué DevOps requiere monitorear una aplicación después de publicarla?** Porque pueden aparecer fallos, lentitud o problemas de almacenamiento que no ocurrieron durante el desarrollo.
11. **¿Qué beneficios obtiene una empresa al implementar DevOps?** Mejor colaboración, entregas más rápidas, detección temprana de fallos, mayor trazabilidad y mejor calidad del servicio.
12. **¿Cómo podrían mejorar el proceso de desarrollo en una segunda versión?** Usando una base de datos persistente, aumentando las pruebas de extremo a extremo, agregando filtros de tareas y configurando alertas automáticas ante errores.

## Reflexión del caso
En TaskManager se usaron ramas, Pull Requests, Pytest y GitHub Actions. La aplicación se publicó en Render y se configuró un monitor de salud. Queda por completar la evidencia del tablero, la publicación de la versión y la validación de persistencia.
