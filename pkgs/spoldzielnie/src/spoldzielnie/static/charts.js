

export function wykres_spoldzielni(name) {
    // Select the body of the document
    let cz = d3.create('svg');
    cz.append('circle')
        .attr('cx', 50)
        .attr('cy', 50)
        .attr('r', 50)
        .style('fill', 'red');

    cz.append('circle')
        .attr('cx', 50)
        .attr('cy', 50)
        .attr('r', 40)
        .style('fill', 'yellow');
    // Append an SVG element to the body
    return cz.node();
}

export function pogrupuj(dane) {
    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    const dzielnie = d3.rollup(dane, (D) => d3.sum(D, d => d.bilans), (d) => d.dzielnica);
    //sort dzielnie
    const sorted = new Map([...dzielnie.entries()].sort((a, b) => b[1] - a[1]));
    return sorted;
}

export function pogrupuj2(dane) {
    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    const dzielnie = d3.rollup(dane, (D) => D.length, (d) => d.dzielnica);
    //sort dzielnie
    const sorted = new Map([...dzielnie.entries()].sort((a, b) => b[1] - a[1]));
    return sorted;
}

export function daj_mi_wykres(dane, caption) {

    //count of keys in dane
    let c = dane.size;

    //intermap length



    const y_s = 60;
    const x_s = 140;

    const marg = 25;
    const height = c * marg-20;


    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    let cz = d3.create('svg')
    .attr('width', 460)
    .attr('height', 500)
    .attr('class', 'cell')
    .style("background","#fffaaf");


    cz.append('text')
    .attr('x', 15)
    .attr('y', 20)
    .text(caption)
    .style('font-size', '13px')
    .style('fill', 'blue')
    .style('font-family', 'Arial')
    .style('font-weight', 'bold');

    
    let xscale = d3.scaleLinear()
        .domain([0, d3.max(dane, d => d[1])])
        .range([0, 300]);

    var formatMoney = function (d) { return d3.format(".0f")(d) + " zł"; }

 
    var xAxis = cz.append("g")
    .attr("class", "xAxis")
    .attr("transform", "translate(" + x_s +"," + height + ")");
      
    xAxis.call(d3.axisBottom(xscale))
        .selectAll("text")
        .attr("transform", "translate(-10,0)rotate(-45)")
        .style("text-anchor", "end")
        .style("font-size", "13px");

        cz.append('g')
        .selectAll('line')
        .data(xscale.ticks())
        .enter().append('line')
        .attr('class', 'gridline')
        .attr('x1', d => x_s + xscale(d))
        .attr('x2', d => x_s + xscale(d))
        .attr('y1', y_s)
        .attr('y2', height)
        .attr('stroke', 'black')

    cz.selectAll('rect')
    .data(dane)
    .enter()
    .append('rect')
    .attr('x', x_s)
    .attr('y', (d, i) => i * 20+y_s)
    .attr('width', (d) => xscale(d[1]))
    .attr('height', 10)
    .style('fill', 'red');

    cz.selectAll('text.dziel')
    .data(dane)
    .enter()
    .append('text')
    .attr('class', 'dziel')
    .attr('text-anchor','end')
    .attr('x', 130)
    .attr('y', (d, i) => i * 20+y_s+10)
    .text((d) => d[0])

    return cz.node();
}

export function wykres_dzielnica(warszawa_dzielnice, dzielnica, spoldzielnie, warszawa_drogi) {

 

    const y_s = 60;
    const x_s = 140;

    const marg = 10;
    const height = 400

    var w = 300;
    var h = 300;

    const margin = { top: 20, right: 20, bottom: 20, left: 20 };
    // Calculate the inner width and height (subtracting margins)
const innerWidth = w - margin.left - margin.right;
const innerHeight = h - margin.top - margin.bottom;

    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    let cz = d3.create('svg')
    .attr('width', w)
    .attr('height', h)
    .style("background","#fffaaf");
    
    const g = cz.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

    const featureDzielnica = warszawa_dzielnice.features.find(feature => feature.properties.name === dzielnica);

    const spoldzielnieDzielnica = spoldzielnie.filter(feature => feature.dzielnica === dzielnica);

    // console.log(spoldzielnieDzielnica);

    const projection = d3.geoMercator()
    .fitSize([innerWidth, innerHeight], featureDzielnica); // Automatically adjust the projection to fit the SVG

    // Create a path generator using the projection
    const path_proj = d3.geoPath()
        .projection(projection);



  // Now, when you draw the "Rembertów" feature, it should fill the SVG dimensions
  g.selectAll("path.continent")
    .data([featureDzielnica]) // Directly use the "Rembertów" feature
    .enter()
    .append("path")
    .attr("class", "continent")
    .attr("d", path_proj);


    let g_drogi = cz.append("g").attr("class", "drogi");

        g_drogi
            .selectAll("path.drogi")
            .data(warszawa_drogi.features)
            .enter().append("path")
            .attr("class", "drogi")
            .attr("d", path_proj)
            .attr("fill", "none")
            .attr("stroke", "white");


    let g_spol = cz.selectAll("g.spoldzielnia")
    .data(spoldzielnieDzielnica)
    .enter()
    .append("g")
    .attr("class", "spoldzielnia")
    .attr("transform", function (d) {
        return "translate(" + projection([d.dlugosc_geo, d.szerokosc_geo]) + ")"
    })

    g_spol
    .append("circle")
    .attr("class", "spoldzielnia")
    .attr("cx", 0)
    .attr("cy", 0)
    .attr("r", function (d) {
        let rr = 0
        // if (d.bilans_rsquare > 0) {
        //    rr = d.bilans_rsquare
        // } 
        // return r_bilans(rr)
        return 4;
    }
    )
    .attr("fill", function (d) {
        return 'rgb(147, 230, 255)'

    })
    .attr("stroke", "black")
    .attr("stroke-width", 1)
    .attr("opacity", 0.7)
    
    return cz.node();
}
