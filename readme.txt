El script está realizado en Python con sqlite embebido, al no tener una referencia
desde donde cargar los datos, desde el script creo una base, agrego una tabla y
la cargo en base a un archivo .csv, luego leo los registros, los cargo en un cursor
y voy haciendo el fetch a un archivo.
Por defecto el script va a listar según las condiciones pedidas de Seller y Site, pero
brinda la oportunidad de cambiarlos en tiempo de ejecución tal lo solicitado en el 
requerimiento.
