# UTN Capital

Aplicación de consola en Python para registrar y analizar las compras de acciones de un grupo de usuarios VIP.

> Trabajo realizado como parcial de la Tecnicatura en Programación de la Universidad Tecnológica Nacional (UTN).

## Qué hace

El programa trabaja con 15 usuarios y 3 acciones (Apple, Tesla y NVIDIA). Al iniciar permite:

1. Crear una base de datos nueva y cargar compras desde cero.
2. Cargar compras nuevas sobre una base de datos ya establecida.
3. Usar directamente la base de datos establecida.
4. Salir.

Después de cargar los datos se puede ver la tabla completa (usuario, acción, precio, cantidad y total) y consultar un menú de análisis:

- Cantidad total de acciones adquiridas por usuario.
- Promedio de acciones adquiridas de cada empresa entre todos los usuarios.
- Usuarios ordenados alfabéticamente de la Z a la A, junto con el total invertido.
- Inversión total acumulada de la cartera.
- Empresa en la que cada usuario compró más acciones.
- Acción con mayor inversión en la cartera (en USD).
- Porcentaje de inversión de cada usuario sobre el total.
- Usuarios cuya inversión supera el promedio.
- Usuarios con más acciones de Tesla que el promedio.

Las compras se validan al cargarlas: solo se aceptan usuarios VIP y acciones de la lista, y montos entre 0 y 500.

## Cómo ejecutarlo

Requiere **Python 3.10 o superior** (usa `match`) y no necesita instalar librerías.

```bash
git clone https://github.com/f47ima/UTN-Capital.git
cd UTN-Capital
python main.py
```

## Ejemplo de uso

Eligiendo "Utilizar base de datos establecida", ir directo al menú de opciones y consultar la inversión total:

```
Bienvenido a UTN Capital.
¿Como desea realizar la operacion?
...
> 3
¿Como desea continuar?
...
> 2
Ingrese su preferencia:
> 4
EL total invertido por todos los usuarios es: 96063.0 USD.
```

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `main.py` | Flujo principal y menús |
| `entrada.py` | Carga y validación de datos ingresados por el usuario |
| `output.py` | Funciones para mostrar tablas y resultados |
| `modulo.py` | Operaciones sobre listas y matrices (sumas, promedios, máximos, ordenamientos) |
| `validaciones.py` | Validación de números y manejo de cadenas |

Gran parte de la lógica está implementada a mano, por ejemplo la capitalización de cadenas, los ordenamientos y la búsqueda de máximos.

## Tecnologías

- Python 3
