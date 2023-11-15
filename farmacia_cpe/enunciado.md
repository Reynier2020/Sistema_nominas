# POO Farmacia

Se desea realizar un sistema para gestionar la venta de medicamentos en una farmacia. Se conoce que los medicamentos pueden ser controlados y que en la farmacia hay una lista de medicamentos. De los medicamentos en general se registra su nombre, los miligramos que contiene, la forma de presentación (tabletas, jarabe, etc.), el precio por unidad y la fecha de vencimiento; por otro lado, de los medicamentos controlados se conoce además la especialidad del doctor que lo puede recetar y la máxima cantidad que se puede vender a un paciente (en unidades).

a) Realice el diagrama de clases UML del sistema.

b) Implemente las clases correspondientes al diagrama de clases con sus constructores y los métodos de acceso a sus campos.

c) Implemente la funcionalidad necesaria para determinar el importe de una compra en la farmacia dados el nombre del medicamento y la cantidad de unidades que se van a comprar, teniendo en cuenta que se éste se calcula de la siguiente forma:

- Para los medicamentos en general, se determina a partir del precio del medicamento multiplicado por la cantidad de unidades que se van a comprar más $5.
- Para los medicamentos controlados, se determina como los demás medicamentos, pero agregándole $10 por ser un medicamento controlado.

d) Implemente la funcionalidad necesaria para determinar si se puede comprar un medicamento controlado dado su nombre y la cantidad de unidades que se van a comprar. Se conoce que el medicamento sólo se pueda comprar si no se ha vencido y si la cantidad no excede la permitida. Asuma que la fecha y hora de la PC donde se montará el sistema son correctas.
