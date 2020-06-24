CREATE
#Control sur
(p1:Policia {name: 'Departamento De UPC)'}),
(p2:Policia {name: 'Policia UPC el Salado'}),
(p3:Policia {name: 'Policia Narcoticos'}),


#Centro
(p4:Policia {name: 'CENTRO DE SALUD N°24 POLICIA NACIONAL'}),
(p5:Policia {name: 'Policía Nacional'}),
(p6:Policia {name: 'Cooperativa Policía Nacional Agencia Cuenca'}),
(p7:Policia {name: 'Policía Nacional Zona6'}),
(p8:Policia {name: 'UPC Unidad De Policia Comunitaria'}),
(p9:Policia {name: 'Intendencia General De Policía del Azuay'}),
(p10:Policia {name: 'UPC BELLAVISTA'}),

#Vecino
(p11:Policia {name: 'Subzona De Policia Azuay No.1'}),
(p12:Policia {name: 'Upc Miraflores'}),
(p13:Policia {name: 'Policia Judicial Del Azuay'}),
(p14:Policia {name: 'UPC TOTORACOCHA'}),



#Paraiso
(p15:Policia {name: 'UPC EL PARAÍSO'}),
(p16:Policia {name: 'Unidad de Policía Comunitaria'}),


#Americas
(p17:Policia {name: 'UPC Cayambe'}),
(p18:Policia {name: 'UPC Av. de las Americas'})


 (p1)-[:FRIENDS]->(p4),
 (p1)-[:FRIENDS]->(p2),
 (p2)-[:WORKS_WITH]->(p5),
 (p2)-[:FRIENDS]->(p3),
 (p3)-[:WORKS_WITH]->(p5),
 (p4)-[:FRIENDS]->(p5)


#No vale
 MATCH (p1:Policia  {name: 'Policia Narcoticos'})
 MATCH (p2:Policia  {name: 'Policía Nacional'})
 RETURN gds.alpha.linkprediction.commonNeighpors(p1, p2,{relationshipQuery: "FRIENDS"}) as nivel_Cercania