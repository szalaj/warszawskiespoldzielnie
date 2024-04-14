

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
    console.log('d')
    console.log 
    //count of keys in dane
    let c = dane.size;

    //intermap length


    console.log('c')
    console.log(c)


    const y_s = 60;
    const x_s = 140;

    const marg = 25;
    const height = c * marg-20;


    // const dzielnie = d3.group(dane, (d) => d.dzielnica);
    let cz = d3.create('svg')
    .attr('width', 460)
    .attr('height', 500)
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
