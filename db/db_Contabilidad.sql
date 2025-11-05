CREATE DATABASE db_contabilidad;

\c db_contabilidad;

-- Crear tabla de palabras clave
CREATE TABLE palabras_contabilidad (
    id SERIAL PRIMARY KEY,
    palabra TEXT NOT NULL,
    porcentaje_identidad NUMERIC(5,2),
    sinonimos TEXT
);

-- Insertar datos en la tabla palabras_contabilidad
INSERT INTO palabras_contabilidad (palabra, porcentaje_identidad, sinonimos) VALUES
('Activo', 100.00, 'bien, recurso, propiedad'),
('Pasivo', 90.00, 'deuda, obligacion, compromiso'),
('Capital', 90.00, 'patrimonio, fondos, inversion'),
('Balance', 90.00, 'estado financiero, resumen contable'),
('Ingreso', 80.00, 'ganancia, entrada, utilidad'),
('Egreso', 80.00, 'gasto, salida, desembolso'),
('Factura', 70.00, 'recibo, comprobante, nota de venta'),
('Asiento', 70.00, 'registro, anotacion, entrada'),
('Libro', 60.00, 'registro diario, libro contable'),
('Diario', 60.00, 'registro diario, libro contable'),
('Inventario', 80.00, 'existencias, mercancias, stock'),
('Depreciacion', 70.00, 'perdida de valor, amortizacion'),
('Costo', 80.00, 'precio, gasto, inversion'),
('Beneficio', 90.00, 'ganancia, utilidad, provecho'),
('Auditoria', 80.00, 'revision, inspeccion, verificacion'),
('Contabilidad', 100.00, 'registro financiero, sistema contable');
