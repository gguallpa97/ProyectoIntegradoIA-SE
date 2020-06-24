CREATE
(b1:Bombero {name: 'Estación de Bomberos N° 4 Crnl. Jaime Maldonado Ambrosi (Parque Industrial)'}),
(b2:Bombero {name: 'Estación de Bomberos N 1 Cmel. vicente tamarariz valdivieso'}),

(b3:Bombero {name: 'Cuerpo de Bomberos'}),



(b4:Bombero {name: 'Benemérito Cuerpo de Bomberos de Cuenca'}),
(b5:Bombero {name: 'Estación de Bomberos Nro. 2'}),
(b6:Bombero {name: 'Bomberos Cuenca'}),


(b7:Bombero {name: 'Cuerpo De Bomberos Voluntarios De Cuenca'}),
(b8:Bombero {name: 'Estación de bomberos número 3'}),

(b9:Bombero {name: 'Estación 6 Bomberos Cuenca'}),


 (b1)-[:FRIENDS]->(b4),
 (b1)-[:FRIENDS]->(b2),
 (b2)-[:WORKS_WITH]->(b5),
 (b2)-[:FRIENDS]->(b3),
 (b3)-[:WORKS_WITH]->(b5),
 (b4)-[:FRIENDS]->(b5)
 

 
 MATCH (b1:Bombero  {name: 'Cuerpo de Bomberos'})
 MATCH (b2:Bombero  {name: 'Estación de Bomberos Nro. 2'})
  RETURN gds.alpha.linkprediction.commonNeighbors(b1, b2) AS nivel_Cercania