-- enumera todas las bandas con Glam rock como su estilo principal, clasificadas por su longevidad
SELECCIONA   nombre_banda,
        IFNULL (dividido, 2020 ) - IFNULL (formado, 0 ) COMO vida útil
DE bandas_de_metal
DONDE estilo como  ' %Glam rock% '
ORDEN POR  2  DESC ;
