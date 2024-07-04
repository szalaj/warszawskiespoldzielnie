# Mapy 

https://overpass-turbo.eu/

## Export działki

[out:json][timeout:25];
area["name"="Kraków"]->.searchArea;
(
  node["landuse"="allotments"](area.searchArea);
  way["landuse"="allotments"](area.searchArea);
  relation["landuse"="allotments"](area.searchArea);
);
out body;
>;
out skel qt;


## Export roads


[out:xml][timeout:25];
// Definiowanie obszaru Ursusa
area["name"="Mokotów"]->.searchArea;
// Wyszukiwanie wszystkich kategorii dróg w Ursusie
(
  way["highway"="motorway"](area.searchArea);
  way["highway"="trunk"](area.searchArea);
  way["highway"="primary"](area.searchArea);
  way["highway"="secondary"](area.searchArea);
  way["highway"="tertiary"](area.searchArea);

  way["highway"="residential"](area.searchArea);

  relation["highway"="motorway"](area.searchArea);
  relation["highway"="trunk"](area.searchArea);
  relation["highway"="primary"](area.searchArea);
  relation["highway"="secondary"](area.searchArea);
  relation["highway"="tertiary"](area.searchArea);

  relation["highway"="residential"](area.searchArea);

);
// Wyświetlenie wyników
out body;
>;
out skel qt;


## Mapshaper

https://mapshaper.org/