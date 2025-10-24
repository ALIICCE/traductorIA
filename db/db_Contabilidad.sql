CREATE DATABASE db_contabilidad;

\c db_contabilidad;

-- Crear tabla de palabras clave
CREATE TABLE palabras_contabilidad (
    id SERIAL PRIMARY KEY,
    palabra TEXT NOT NULL,
    porcentaje_identidad NUMERIC(4,2),
    sinonimos TEXT
);

-- Insertar datos en la tabla palabras_contabilidad
INSERT INTO palabras_contabilidad (palabra, porcentaje_identidad, sinonimos) VALUES
('Activo', 0.95, 'bien, recurso, propiedad'),
('Pasivo', 0.93, 'deuda, obligación, compromiso'),
('Capital', 0.90, 'patrimonio, fondos, inversión'),
('Balance', 0.92, 'estado financiero, resumen contable'),
('Ingreso', 0.88, 'ganancia, entrada, utilidad'),
('Egreso', 0.87, 'gasto, salida, desembolso'),
('Factura', 0.85, 'recibo, comprobante, nota de venta'),
('Asiento', 0.84, 'registro, anotación, entrada'),
('Libro diario', 0.80, 'registro diario, libro contable'),
('Inventario', 0.86, 'existencias, mercancías, stock'),
('Depreciación', 0.83, 'pérdida de valor, amortización'),
('Costo', 0.89, 'precio, gasto, inversión'),
('Beneficio', 0.91, 'ganancia, utilidad, provecho'),
('Auditoría', 0.88, 'revisión, inspección, verificación'),
('Contabilidad', 1.00, 'registro financiero, sistema contable');
