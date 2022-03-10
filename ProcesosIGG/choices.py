Status_Contrato=(
    ('E', 'ELABORADO'),
    ('P', 'PARA FIRMA'),
    ('DOCUM RECIBIDO', 'DOCUM RECIBIDO'),
    ('A', 'ANULADO'),
)

Clase=(
    ('C', 'CONTRATO'),
    ('O', 'OTROS SI'),
)

Tipo=(
    ('E', 'EMPRESA'),
    ('P', 'PERSONAL'),
)

Modelo_ProcesoIGG=(
    ('S', 'SOLO PARTICIPACION'),
    ('OC', 'PARTICIPACION CON OPC COMPRA'),
    ('VP', 'VENTA CON PARTICIPACION'),
    ('V', 'VENTA SIN PARTICIPACION'),
    ('VF', 'VENTA CON CUOTA FIJA'),
    ('A', 'ARRENDAIENTO MENSUAL'),
)

Status_Asignacion=(
    ('A', 'ABIERTA'),
    ('P', 'PRE ASIGNADO'),
    ('AS', 'ASIGNADO'),
    ('A', 'ANULADO'),
)

Status_Retiro=(
    ('S', 'SOLICITUD'),
    ('P', 'POR RETIRAR'),
    ('R', 'RETIRADO'),
    ('U', 'UMS PROCESADO'),
)

Status_Despacho=(
    ('C', 'CODIGOO IGG'),
    ('A', 'ALISTAMIENTO'),
    ('D', 'DESPACHADO'),
)

Status_Instalacion=(
    ('D', 'DESPACHADO'),
    ('P', 'POR INSTALAR'),
    ('E', 'EN OPERACION'),
    ('U', 'UMS PROCESADO'),
)